#!/usr/bin/env python3
"""Audit saved execution evidence; never modify a model's paper."""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import subprocess

from summarize_traces import summarize

HERE = Path(__file__).resolve().parent


def read_json(path):
    return json.loads(Path(path).read_text())


def jsonl(path):
    for number, line in enumerate(Path(path).read_text().splitlines(), 1):
        try:
            yield number, json.loads(line)
        except json.JSONDecodeError:
            yield number, {"type": "audit_unparsed_line"}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tool_failures(value):
    """Extract explicit failure indicators, retaining them for human review."""
    found = []
    if isinstance(value, dict):
        if value.get("exit_code") not in [0, None]:
            found.append({"exit_code": value["exit_code"],
                          "output_tail": str(value.get("output", ""))[-1800:]})
        if value.get("isError") or value.get("error"):
            found.append({"error": str(value.get("error", value))[:1800]})
        for key, item in value.items():
            if key not in ["error", "isError"]:
                found.extend(tool_failures(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(tool_failures(item))
    elif isinstance(value, str):
        try:
            decoded = json.loads(value)
        except (ValueError, TypeError):
            decoded = None
        if isinstance(decoded, (dict, list)):
            found.extend(tool_failures(decoded))
        elif re.search(r"(?:^Error(?: executing|:)|^Script failed|apply_patch verification failed)", value, re.M):
            found.append({"error_text": value[:1800]})
    return found


def audit_case(case, condition):
    root = HERE / case
    timing = read_json(root / "timing.json")
    artifacts = read_json(root / "artifact-manifest.json")
    root_id = artifacts["root_thread_ids"][0]
    usage = summarize(root / "native", root_id)
    (root / "usage.json").write_text(json.dumps(usage, indent=2) + "\n")
    warnings = list(usage["warnings"])
    if timing["exit_code"]:
        warnings.append("CLI exited unsuccessfully")
    if not all(artifacts["inputs_unchanged"].values()):
        warnings.append("At least one input was changed")
    if sha(root / "prompt.txt") != condition["prompt_sha256"]:
        warnings.append("Recorded prompt hash changed")
    for thread in usage["threads"]:
        if thread["responses"] and thread["kind"] != "guardian":
            if thread["model_effort_pairs"] != [["gpt-6-astra", "max"]]:
                warnings.append("Unexpected model/effort: " + thread["thread_id"])
        if thread["aborted_turn_ids"]:
            warnings.append("Aborted turns: " + thread["thread_id"])
    if condition["review_instruction"] and usage["reviewer_thread_count"] < 2:
        warnings.append("Review condition used fewer than two responding subagents")

    rows = [x for _, x in jsonl(root / "events.jsonl")]
    failed_commands, errors = [], []
    for event in rows:
        item = event.get("item", {})
        if event.get("type") in ["error", "turn.failed", "audit_unparsed_line"]:
            errors.append(event)
        if event.get("type") == "item.completed" and item.get("type") == "command_execution":
            if item.get("exit_code") not in [0, None]:
                failed_commands.append({"command": item.get("command"),
                    "exit_code": item.get("exit_code"),
                    "output_tail": item.get("aggregated_output", "")[-1800:]})
    if errors:
        warnings.append("CLI error events recorded; inspect whether recovered")
    if not any(x.get("type") == "turn.completed" for x in rows):
        warnings.append("No completed root turn in CLI events")

    # Collect calls once across copied parent histories; inspect actual calls,
    # not URLs quoted in book text or written into a bibliography.
    calls, outputs, own_starts, own_finishes = {}, {}, {}, {}
    root_user_texts = []
    relevant = {t["thread_id"] for t in usage["threads"]}
    for trace in (root / "native").rglob("rollout-*.jsonl"):
        match = re.search(r"([0-9a-f-]{36})\.jsonl$", trace.name)
        if not match or match.group(1) not in relevant:
            continue
        file_id = match.group(1)
        data = [x for _, x in jsonl(trace)]
        metadata = next((x["payload"] for x in data if x.get("type") == "session_meta"
                         and x["payload"].get("id") == file_id), {})
        boundary = metadata.get("subagent_history_start_ordinal")
        for row in data:
            p = row.get("payload", {})
            if boundary is not None and row.get("ordinal", boundary) < boundary:
                continue
            if row.get("type") == "response_item":
                kind, call_id = p.get("type"), p.get("call_id")
                if file_id == root_id and kind == "message" and p.get("role") == "user":
                    root_user_texts.extend(c.get("text", "") for c in p.get("content", [])
                                           if isinstance(c, dict))
                if kind in ["function_call", "custom_tool_call"] and call_id:
                    calls[call_id] = {"name": p.get("name"),
                        "thread_id": file_id, "timestamp": row.get("timestamp"),
                        "arguments": p.get("arguments", p.get("input", ""))}
                if kind in ["function_call_output", "custom_tool_call_output"] and call_id:
                    outputs[call_id] = p.get("output", "")
            if row.get("type") == "event_msg" and p.get("turn_id"):
                key = (file_id, p["turn_id"])
                if p.get("type") == "task_started": own_starts[key] = p
                if p.get("type") in ["task_complete", "turn_aborted"]: own_finishes[key] = p
    unfinished = [{"thread_id": a, "turn_id": b}
                  for a, b in sorted(set(own_starts) - set(own_finishes))]
    if unfinished:
        warnings.append("Started agent turns lack a completion/abort in the saved traces")
    exact_prompt_in_trace = (root / "prompt.txt").read_text() in root_user_texts
    if not exact_prompt_in_trace:
        warnings.append("Exact saved prompt not found in the root trace")
    network_candidates = []
    delegation_calls = []
    for call_id, call in calls.items():
        name, args = call["name"] or "", call["arguments"]
        if not isinstance(args, str): args = json.dumps(args)
        if re.search(r"(?:web__run|web\.run|search_query|\bcurl\s|\bwget\s|requests\.(?:get|post)\(|urllib\.request)", name + " " + args):
            network_candidates.append({"call_id": call_id, **call,
                                       "output": outputs.get(call_id)})
        if any(token in name for token in ["spawn_agent", "followup_task", "send_message", "interrupt_agent"]):
            delegation_calls.append({"call_id": call_id, **call,
                                     "output": outputs.get(call_id)})
    if network_candidates:
        warnings.append("Potential online-access calls require manual inspection")

    failure_candidates = []
    for call_id, output in outputs.items():
        failures = tool_failures(output)
        if failures:
            failure_candidates.append({"call_id": call_id, **calls.get(call_id, {}),
                                       "failures": failures})
    stderr = (root / "stderr.log").read_text()
    stderr_errors = [line for line in stderr.splitlines()
                     if re.search(r"\b(?:ERROR|WARN)\b", line)]

    pdfs = []
    for pdf in sorted((root / "output").rglob("*.pdf")):
        result = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                                text=True, timeout=10)
        pages = re.search(r"^Pages:\s+(\d+)", result.stdout, re.M)
        pdfs.append({"file": str(pdf.relative_to(root)),
                     "pages": int(pages.group(1)) if pages else None,
                     "pdfinfo_exit_code": result.returncode})
    tex_logs = []
    for log in sorted((root / "output").rglob("*.log")):
        lines = log.read_text(errors="replace").splitlines()
        if not any("TeX" in line for line in lines[:8]):
            continue
        findings = [line for line in lines if re.search(
            r"(?:^!|Warning|Overfull|Underfull|Output written on|Fatal error)", line)]
        tex_logs.append({"file": str(log.relative_to(root)), "findings": findings})
    database_checks, runtime_log_issues, memory_rows = {}, [], {}
    for database in sorted((root / "native").rglob("*.sqlite")):
        relative = str(database.relative_to(root))
        with sqlite3.connect(f"file:{database}?mode=ro", uri=True) as db:
            check = [row[0] for row in db.execute("PRAGMA quick_check")]
            database_checks[relative] = check
            if check != ["ok"]:
                warnings.append("SQLite consistency check failed: " + relative)
            if database.name.startswith("logs_"):
                runtime_log_issues.extend({"file": relative, "timestamp": ts,
                    "level": level, "target": target, "body": body}
                    for ts, level, target, body in db.execute(
                        "SELECT ts,level,target,feedback_log_body FROM logs "
                        "WHERE upper(level) IN ('WARN','WARNING','ERROR') ORDER BY id"))
            if database.name.startswith("memories_"):
                memory_rows[relative] = db.execute("SELECT count(*) FROM stage1_outputs").fetchone()[0]
    reference_keys = {}
    for tex in sorted((root / "output").glob("*.tex")):
        source = tex.read_text()
        groups = re.findall(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", source)
        reference_keys[str(tex.relative_to(root))] = sorted({
            key.strip() for group in groups for key in group.split(",")})
    result = {"condition": case, "timing": timing,
        "usage": usage["total_usage"], "reviewer_count": usage["reviewer_thread_count"],
        "models": [{"path": t["agent_path"], "kind": t["kind"],
                    "model_effort_pairs": t["model_effort_pairs"], "responses": t["responses"]}
                   for t in usage["threads"]],
        "inputs_unchanged": all(artifacts["inputs_unchanged"].values()),
        "pdfs": pdfs, "cli_errors": errors, "nonzero_root_commands": failed_commands,
        "unfinished_turns": unfinished, "tool_call_counts": dict(Counter(c["name"] for c in calls.values())),
        "potential_online_access": network_candidates, "delegation_calls": delegation_calls,
        "tool_failure_candidates": failure_candidates, "stderr_error_lines": stderr_errors,
        "tex_logs": tex_logs,
        "database_checks": database_checks, "runtime_log_issues": runtime_log_issues,
        "generated_memory_rows": memory_rows, "manuscript_citation_keys": reference_keys,
        "exact_prompt_in_root_trace": exact_prompt_in_trace,
        "warnings": sorted(set(warnings)),
        "scope": "Execution, isolation, provenance, usage and artifacts. This is not a mathematical correctness score."}
    (root / "audit.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    return result


def main():
    exp = read_json(HERE / "experiment.json")
    results = []
    for case, condition in exp["conditions"].items():
        if not (HERE / case / "timing.json").exists():
            raise SystemExit("Run not finished: " + case)
        results.append(audit_case(case, condition))
    fields = ["condition", "explicit_instruction", "review_instruction", "elapsed_seconds",
              "reviewers", "input_tokens", "cached_input_tokens", "uncached_input_tokens",
              "output_tokens", "reasoning_output_tokens", "total_tokens", "exit_code"]
    with (HERE / "results.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for result in results:
            c, usage, timing = result["condition"], result["usage"], result["timing"]
            writer.writerow({"condition": c,
                "explicit_instruction": exp["conditions"][c]["explicit_instruction"],
                "review_instruction": exp["conditions"][c]["review_instruction"],
                "elapsed_seconds": round(timing["elapsed_wall_seconds"], 3),
                "reviewers": result["reviewer_count"],
                **{k: usage.get(k, 0) for k in fields if k.endswith("tokens") and k != "uncached_input_tokens"},
                "uncached_input_tokens": usage["input_tokens"] - usage["cached_input_tokens"],
                "exit_code": timing["exit_code"]})
    (HERE / "audit-summary.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
    for result in results:
        print(result["condition"], "minutes", round(result["timing"]["elapsed_wall_seconds"] / 60, 2),
              "reviewers", result["reviewer_count"], "usage", result["usage"],
              "warnings", result["warnings"])


if __name__ == "__main__":
    main()
