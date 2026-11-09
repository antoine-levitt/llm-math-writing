#!/usr/bin/env python3
"""Summarize Codex 0.166 native usage without exposing conversation content.

Use after the CLI and all reviewers have finished. The caller still needs to
record launch-to-exit wall time; summed agent durations can overlap.
"""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re


TOKEN_FIELDS = (
    "input_tokens", "cached_input_tokens", "cache_write_input_tokens",
    "output_tokens", "reasoning_output_tokens", "total_tokens",
)
UUID_SUFFIX = re.compile(r"([0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12})\.jsonl$")


def add_usage(rows):
    rows = list(rows)
    return {key: sum(row.get(key, 0) for row in rows) for key in TOKEN_FIELDS}


def summarize(state_dir, root_id):
    state_dir = Path(state_dir)
    files = []
    for dirname in ("sessions", "archived_sessions"):
        path = state_dir / dirname
        if path.exists():
            files.extend(path.rglob("*.jsonl"))
    # Also allow a directory containing only an archived sessions tree.
    if not files:
        files = list(state_dir.rglob("rollout-*.jsonl"))

    warnings = []
    traces = defaultdict(list)
    metadata = {}
    paths = defaultdict(list)
    for path in sorted(set(files)):
        match = UUID_SUFFIX.search(path.name)
        if not match:
            continue
        file_id = match.group(1)
        paths[file_id].append(str(path))
        for line_number, line in enumerate(path.open(), 1):
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                warnings.append(f"Unparsed JSON at {path}:{line_number}")
                continue
            traces[file_id].append(row)
            payload = row.get("payload", {})
            if row.get("type") == "session_meta" and payload.get("id") == file_id:
                metadata[file_id] = payload

    if root_id not in traces:
        raise ValueError(f"No native trace found for root thread {root_id}")

    relevant = {root_id}
    while True:
        expanded = relevant | {
            thread_id for thread_id, meta in metadata.items()
            if meta.get("parent_thread_id") in relevant
        }
        if expanded == relevant:
            break
        relevant = expanded

    # Copied history can contain duplicate records. Attribute to the payload's
    # thread, not to the enclosing filename; deduplicate by upstream response ID.
    response_records = {}
    duplicate_records = 0
    for rows in traces.values():
        for row in rows:
            if row.get("type") != "token_usage_record":
                continue
            p = row.get("payload", {})
            if p.get("thread_id") not in relevant:
                continue
            response_id = p.get("response_id")
            if not response_id:
                warnings.append("A token_usage_record has no response_id")
                continue
            old = response_records.get(response_id)
            if old:
                duplicate_records += 1
                for key in ("thread_id", "usage"):
                    if old["payload"].get(key) != p.get(key):
                        warnings.append(f"Conflicting {key} for response {response_id}")
                if old.get("timestamp", "") > row.get("timestamp", ""):
                    continue
            response_records[response_id] = row

    by_thread = defaultdict(list)
    for row in response_records.values():
        by_thread[row["payload"]["thread_id"]].append(row)

    summaries = []
    for thread_id in sorted(relevant):
        meta = metadata.get(thread_id, {})
        boundary = meta.get("subagent_history_start_ordinal")
        own_rows = [
            row for row in traces[thread_id]
            if boundary is None or row.get("ordinal", boundary) >= boundary
        ]
        usages = sorted(by_thread[thread_id], key=lambda row: row.get("timestamp", ""))
        own_turn_ids = {row["payload"].get("turn_id") for row in usages}
        for row in own_rows:
            p = row.get("payload", {})
            if row.get("type") == "event_msg" and p.get("type") == "task_started":
                if p.get("turn_id"):
                    own_turn_ids.add(p["turn_id"])

        settings = set()
        completions = {}
        aborted = set()
        item_types = Counter()
        fallback_token_count = None
        for row in own_rows:
            p = row.get("payload", {})
            if row.get("type") == "turn_context" and p.get("turn_id") in own_turn_ids:
                settings.add((p.get("model"), p.get("effort", p.get("reasoning_effort"))))
            if row.get("type") == "response_item":
                item_types[p.get("type", "unknown")] += 1
            if row.get("type") != "event_msg":
                continue
            if p.get("type") == "token_count" and p.get("info"):
                fallback_token_count = p["info"].get("total_token_usage")
            if p.get("turn_id") not in own_turn_ids:
                continue
            if p.get("type") == "task_complete":
                completions[p["turn_id"]] = {
                    key: p.get(key) for key in (
                        "turn_id", "started_at", "completed_at", "duration_ms",
                        "time_to_first_token_ms",
                    )
                }
            if p.get("type") == "turn_aborted":
                aborted.add(p["turn_id"])

        usage = add_usage(row["payload"].get("usage", {}) for row in usages)
        last_thread_counter = usages[-1]["payload"].get("thread_token_usage") if usages else None
        if last_thread_counter and any(
            last_thread_counter.get(key, 0) != usage[key] for key in TOKEN_FIELDS
        ):
            warnings.append(f"Response sum differs from last thread counter: {thread_id}")
        if not usages and own_turn_ids:
            warnings.append(f"No response-level usage records for active thread {thread_id}")

        source = meta.get("source", {})
        subagent_source = source.get("subagent", {}) if isinstance(source, dict) else {}
        kind = "root" if thread_id == root_id else "subagent"
        if subagent_source.get("other") == "guardian":
            kind = "guardian"
        summaries.append({
            "thread_id": thread_id,
            "parent_thread_id": meta.get("parent_thread_id"),
            "agent_path": meta.get("agent_path"),
            "kind": kind,
            "history_mode": meta.get("history_mode"),
            "history_start_ordinal": boundary,
            "trace_files": paths[thread_id],
            "model_effort_pairs": [list(pair) for pair in sorted(settings, key=str)],
            "responses": len(usages),
            "usage": usage if usages else None,
            "last_thread_usage_counter": last_thread_counter,
            "token_count_snapshot_for_comparison_only": fallback_token_count,
            "completed_turns": list(completions.values()),
            "summed_turn_duration_ms": sum(c.get("duration_ms") or 0 for c in completions.values()),
            "aborted_turn_ids": sorted(aborted),
            "own_response_item_types": dict(item_types),
        })

    return {
        "root_thread_id": root_id,
        "method": "Sum token_usage_record.payload.usage once per unique upstream response_id; attribute by payload.thread_id.",
        "duplicate_response_records_ignored": duplicate_records,
        "total_usage": add_usage(row["payload"].get("usage", {}) for row in response_records.values()),
        "reviewer_thread_count": sum(s["kind"] == "subagent" and s["responses"] > 0 for s in summaries),
        "threads": summaries,
        "warnings": sorted(set(warnings)),
        "timing_note": "Agent turn durations include tools/waits and can overlap. Measure launch-to-exit wall time separately; these records do not expose GPU compute time.",
        "token_note": "Cached input is part of input_tokens; reasoning output is part of output_tokens. Do not add either subset to its total again.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state_directory", type=Path)
    parser.add_argument("--root-thread", required=True)
    args = parser.parse_args()
    print(json.dumps(summarize(args.state_directory, args.root_thread), indent=2))
