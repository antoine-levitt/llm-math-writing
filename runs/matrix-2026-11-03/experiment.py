#!/usr/bin/env python3
"""Run the four unchanged prompts with a common isolated Codex configuration."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import random
import re
import resource
import shutil
import sqlite3
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
SOURCE = PROJECT.parent / "2026-10-graphene"
CLI = Path("/home/antoine/.local/bin/codex").resolve()
AUTH = Path("/home/antoine/.codex/auth.json")
CASES = {
    "plain": "prompt",
    "explicit": "prompt_explicit_instruction",
    "review": "prompt_tokenmaxing",
    "explicit_review": "prompt_explicit_instruction_plus_tokenmaxing",
}


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path = Path(path)
    pending = path.with_suffix(path.suffix + ".tmp")
    pending.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    pending.replace(path)


def read_json(path):
    return json.loads(Path(path).read_text())


def toml(value):
    if isinstance(value, dict):
        return "{" + ", ".join(json.dumps(k) + " = " + toml(v)
                               for k, v in value.items()) + "}"
    if isinstance(value, list):
        return "[" + ", ".join(map(toml, value)) + "]"
    return json.dumps(value)


def records(case):
    return HERE / case


def runtime(case):
    return read_json(records(case) / "runtime.json")


def base_args(case):
    rt = runtime(case)
    args = [str(CLI), "--no-daemon", "-C", rt["workspace"]]
    for key, value in read_json(records(case) / "config.json").items():
        args += ["-c", key + "=" + toml(value)]
    return args


def environment(case):
    rt = runtime(case)
    # Exclude parent thread/tool identifiers and initialize a separate genuine
    # Codex state directory for this subprocess. Do not change the parent env.
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(("CODEX_", "MCP_"))}
    env.update({"CODEX_HOME": rt["codex_state"], "TMPDIR": rt["temporary"],
                "PATH": "/usr/bin:/usr/local/bin:/bin"})
    return env


def prepare():
    if (HERE / "experiment.json").exists():
        raise SystemExit("Experiment already prepared; refusing to overwrite it.")
    catalog = read_json("/home/antoine/.codex/models_cache.json")
    write_json(HERE / "model-catalog.json", {"models": catalog["models"]})
    tool_root = Path(tempfile.mkdtemp(prefix="graphene-tools-"))
    shutil.copytree("/tmp/graphene-2a0699g8/tools/usr/bin", tool_root / "usr/bin")
    input_files = [SOURCE / "graphene_statement.tex", SOURCE / "graphene_statement.pdf"]
    input_files += sorted((SOURCE / "Reed_simon").glob("*.djvu"))
    input_hashes = {str(p.relative_to(SOURCE)): digest(p) for p in input_files}
    common = {
        "model": "gpt-6-astra", "model_reasoning_effort": "max",
        "agents.default_subagent_model": "gpt-6-astra",
        "agents.default_subagent_reasoning_effort": "max",
        "agents.max_concurrent_threads_per_session": 3,
        "approval_policy": "never", "project_doc_max_bytes": 0,
        "memories.use_memories": False, "memories.generate_memories": False,
        "features.memories": False, "features.apps": False,
        "features.plugins": False, "features.browser_use": False,
        "features.browser_use_external": False, "features.in_app_browser": False,
        "features.computer_use": False, "features.hooks": False,
        "features.multi_agent": True, "features.skip_host_skill_discovery": True,
        "skills.include_instructions": False, "skills.bundled.enabled": False,
        "web_search": "disabled", "notify": [],
        "suppress_unstable_features_warning": True, "allow_login_shell": False,
        "default_permissions": "graphene",
        "permissions.graphene.network.enabled": False,
        "shell_environment_policy.inherit": "core",
    }
    write_json(HERE / "common-config.json", common)
    seed = int.from_bytes(os.urandom(8), "big")
    order = list(CASES)
    random.Random(seed).shuffle(order)
    exp = {"prepared_at": utc(), "model": "gpt-6-astra", "reasoning_effort": "max",
           "cli": str(CLI), "cli_sha256": digest(CLI), "cli_version": "0.166.0",
           "catalog_sha256": digest(HERE / "model-catalog.json"),
           "execution": "sequential", "order_seed": seed, "order": order,
           "input_source": str(SOURCE), "inputs": input_hashes,
           "shared_tools": str(tool_root), "conditions": {}}
    for case, prompt_name in CASES.items():
        record = records(case)
        record.mkdir()
        scratch = Path(tempfile.mkdtemp(prefix="graphene-run-"))
        work = scratch / "work"
        state = scratch / "codex-state"
        temp = scratch / "tmp"
        for folder in [work, state, temp, scratch / "state", scratch / "log"]:
            folder.mkdir(mode=0o700)
        for src in input_files:
            dst = work / src.relative_to(SOURCE)
            dst.parent.mkdir(exist_ok=True)
            shutil.copy2(src, dst)
        shutil.copy2(PROJECT / prompt_name, record / "prompt.txt")
        shutil.copy2(HERE / "model-catalog.json", state / "model-catalog.json")
        rt = {"scratch": str(scratch), "workspace": str(work),
              "codex_state": str(state), "temporary": str(temp),
              "database": str(scratch / "state"), "log": str(scratch / "log"),
              "shared_tools": str(tool_root)}
        write_json(record / "runtime.json", rt)
        cfg = dict(common)
        cfg.update({
            "sqlite_home": rt["database"], "log_dir": rt["log"],
            "model_catalog_json": str(state / "model-catalog.json"),
            "permissions.graphene.filesystem": {
                ":minimal": "read", ":workspace_roots": "write",
                str(temp): "write", str(tool_root): "read",
                str(CLI.parent.parent): "read", "/var/lib/texmf": "read",
                "/var/cache/fontconfig": "read",
            },
            "shell_environment_policy.set": {
                "PATH": str(tool_root / "usr/bin") + ":/usr/bin:/usr/local/bin:/bin",
                "TMPDIR": str(temp),
            },
        })
        write_json(record / "config.json", cfg)
        exp["conditions"][case] = {"prompt_file": prompt_name,
            "prompt_sha256": digest(record / "prompt.txt"),
            "explicit_instruction": case in ["explicit", "explicit_review"],
            "review_instruction": case in ["review", "explicit_review"],
            "workspace": str(work)}
    write_json(HERE / "experiment.json", exp)
    print("Prepared:", ", ".join(order), flush=True)


def supply_auth(case):
    target = Path(runtime(case)["codex_state"]) / "auth.json"
    shutil.copyfile(AUTH, target)
    target.chmod(0o600)


def normalize(value, case):
    rt = runtime(case)
    if isinstance(value, dict):
        return {k: normalize(v, case) for k, v in value.items()
                if k not in ("id", "internal_chat_message_metadata_passthrough")}
    if isinstance(value, list):
        return [normalize(v, case) for v in value]
    if isinstance(value, str):
        value = value.replace(rt["scratch"], "<RUN>")
        value = value.replace(rt["shared_tools"], "<TOOLS>")
        value = re.sub(r"codex-arg0[A-Za-z0-9]+", "codex-arg0<ID>", value)
        return value
    return value


def preflight(case):
    record, rt = records(case), runtime(case)
    supply_auth(case)
    args = base_args(case)
    prompt = (record / "prompt.txt").read_text()
    validation = subprocess.run(args + ["app-server", "--strict-config", "--print-startup-config"],
                                env=environment(case), cwd=rt["workspace"],
                                capture_output=True, text=True, timeout=50)
    (record / "config-validation.json").write_text(validation.stdout)
    (record / "config-validation.stderr").write_text(validation.stderr)
    if validation.returncode:
        raise RuntimeError(validation.stderr)
    result = subprocess.run(args + ["debug", "prompt-input", prompt],
                            env=environment(case), cwd=rt["workspace"],
                            capture_output=True, text=True, timeout=50)
    (record / "startup-context.json").write_text(result.stdout)
    (record / "preflight.stderr").write_text(result.stderr)
    if result.returncode:
        raise RuntimeError(result.stderr)
    context = json.loads(result.stdout)
    users = [x for x in context if x.get("type") == "message" and x.get("role") == "user"]
    assert len(users) == 2, "Unexpected injected user context"
    assert users[-1]["content"][0]["text"] == prompt, "Prompt mismatch"
    nonprompt = [x for x in context if x is not users[-1]]
    rendered = json.dumps(nonprompt, ensure_ascii=False)
    for banned in ["AGENTS.md instructions", "Antoine Levitt", "llm-writing",
                   "<memory", "grill-me", "prompt_tokenmaxing"]:
        assert banned.lower() not in rendered.lower(), "Context leak: " + banned
    assert '"name": "spawn_agent"' in rendered, "Subagent tool missing"
    normalized = normalize(nonprompt, case)
    write_json(record / "startup-normalized.json", normalized)
    # Test the exact sandbox before a model request, including the TeX cache
    # and isolation from every other condition and the source paper.
    denied = [str(PROJECT / "prompt"), str(AUTH),
              "/home/antoine/Nextcloud/blog/AGENTS.md",
              "/home/antoine/Nextcloud/recherche/2018-quantum-transport/revision/paper.tex",
              str(Path(rt["codex_state"]) / "auth.json")]
    for other in CASES:
        if other != case:
            denied.append(str(Path(runtime(other)["workspace"]) / "graphene_statement.tex"))
    probe = '''from pathlib import Path
import subprocess, tempfile
p=Path('graphene_statement.tex')
assert p.read_text()
q=Path('.preflight.tmp'); q.write_text('check'); q.unlink()
for name in DENIED:
    try: Path(name).read_bytes()
    except (PermissionError,FileNotFoundError): pass
    else: raise RuntimeError('Readable forbidden path: '+name)
book=next(Path('Reed_simon').glob('*.djvu'))
r=subprocess.run(['djvutxt','-page=1',str(book)],capture_output=True,timeout=10)
assert r.returncode==0 and r.stdout.strip()
for item in ['article.cls','pdflatex.fmt','pdftex.map']:
    r=subprocess.run(['kpsewhich','-engine=pdftex','-progname=pdflatex',item],capture_output=True,text=True,timeout=10)
    assert r.returncode==0 and r.stdout.strip(),item
print('PASS: inputs, writes, DjVu, TeX resources, and cross-run isolation.')
'''.replace("DENIED", repr(denied))
    result = subprocess.run(args + ["sandbox", "--", "/usr/bin/python3", "-c", probe],
                            env=environment(case), cwd=rt["workspace"],
                            capture_output=True, text=True, timeout=45)
    (record / "sandbox-check.txt").write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    write_json(record / "preflight.json", {"passed_at": utc(),
        "normalized_context_sha256": digest(record / "startup-normalized.json"),
        "config_sha256": digest(record / "config.json"),
        "prompt_sha256": digest(record / "prompt.txt")})
    print("Preflight passed:", case, flush=True)


def preflight_all():
    for case in CASES:
        preflight(case)
    hashes = {digest(records(c) / "startup-normalized.json") for c in CASES}
    assert len(hashes) == 1, "Startup context differs beyond prompt and isolated paths"
    write_json(HERE / "preflight.json", {"passed_at": utc(),
        "normalized_context_sha256": hashes.pop(), "cases": list(CASES)})
    print("All four startup contexts match after removing prompt and neutral run paths.")


def archive(case):
    record, rt = records(case), runtime(case)
    exp = read_json(HERE / "experiment.json")
    state = Path(rt["codex_state"])
    evidence = record / "native"
    evidence.mkdir(exist_ok=True)
    for name in ["sessions", "archived_sessions"]:
        if (state / name).exists():
            shutil.copytree(state / name, evidence / name, dirs_exist_ok=True)
    if Path(rt["log"]).exists():
        shutil.copytree(rt["log"], evidence / "log", dirs_exist_ok=True)
    for db in Path(rt["database"]).glob("*.sqlite"):
        with sqlite3.connect(f"file:{db}?mode=ro", uri=True) as src:
            with sqlite3.connect(evidence / db.name) as dst:
                src.backup(dst)
    inputs_unchanged = {name: digest(Path(rt["workspace"]) / name) == sha
                        for name, sha in exp["inputs"].items()}
    output = record / "output"
    output.mkdir(exist_ok=True)
    output_hashes = {}
    for src in Path(rt["workspace"]).rglob("*"):
        if not src.is_file() or src.is_symlink():
            continue
        relative = str(src.relative_to(rt["workspace"]))
        if relative in exp["inputs"]:
            continue
        dst = output / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        output_hashes[relative] = digest(dst)
    # Preserve temporary draft/reviewer/build files too, excluding tool-server
    # sockets. Their contents are not fed to any later condition.
    temp_out = record / "temporary-artifacts"
    for src in Path(rt["temporary"]).rglob("*"):
        if not src.is_file() or src.is_symlink():
            continue
        relative = src.relative_to(rt["temporary"])
        if any(part.startswith("codex-") for part in relative.parts):
            continue
        dst = temp_out / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    rows = []
    for line in (record / "events.jsonl").read_text().splitlines():
        try: rows.append(json.loads(line))
        except json.JSONDecodeError: pass
    messages = [x["item"]["text"] for x in rows if x.get("type") == "item.completed"
                and x.get("item", {}).get("type") == "agent_message"]
    if messages:
        (record / "final-response.txt").write_text(messages[-1] + "\n")
    usage = [x.get("usage") for x in rows if x.get("type") == "turn.completed"]
    threads = [x["thread_id"] for x in rows if x.get("type") == "thread.started"]
    write_json(record / "artifact-manifest.json", {"archived_at": utc(),
        "inputs_unchanged": inputs_unchanged, "output_hashes": output_hashes,
        "root_thread_ids": threads, "cli_turn_usage": usage,
        "parent_edited_output": False})
    (state / "auth.json").unlink(missing_ok=True)


def launch(case):
    record, rt = records(case), runtime(case)
    if (record / "timing.json").exists():
        raise RuntimeError("Refusing to overwrite a previous attempt: " + case)
    assert (HERE / "preflight.json").exists(), "Preflight not complete"
    check = read_json(record / "preflight.json")
    assert digest(record / "config.json") == check["config_sha256"]
    assert digest(record / "prompt.txt") == check["prompt_sha256"]
    supply_auth(case)
    args = base_args(case) + ["exec", "--strict-config", "--ignore-user-config", "--ignore-rules",
                             "--skip-git-repo-check", "--json", "--color", "never", "-"]
    write_json(record / "argv.json", args)
    started = utc()
    clock = time.monotonic()
    cpu_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    write_json(record / "status.json", {"status": "running", "started_at": started})
    print("Starting", case, started, flush=True)
    with (record / "prompt.txt").open("rb") as prompt, \
         (record / "events.jsonl").open("wb") as events, \
         (record / "events-timed.jsonl").open("w", buffering=1) as timed, \
         (record / "stderr.log").open("wb") as stderr:
        proc = subprocess.Popen(args, env=environment(case), cwd=rt["workspace"],
                                stdin=prompt, stdout=subprocess.PIPE, stderr=stderr)
        write_json(record / "process.json", {"pid": proc.pid, "started_at": started})
        for line in proc.stdout:
            events.write(line)
            events.flush()
            try: item = json.loads(line)
            except json.JSONDecodeError: item = {"unparsed": line.decode(errors="replace")}
            timed.write(json.dumps({"received_at": utc(),
                "elapsed_seconds": time.monotonic() - clock, "event": item}) + "\n")
        code = proc.wait()
    ended, elapsed = utc(), time.monotonic() - clock
    cpu_end = resource.getrusage(resource.RUSAGE_CHILDREN)
    write_json(record / "timing.json", {"started_at": started, "ended_at": ended,
        "elapsed_wall_seconds": elapsed, "exit_code": code,
        "local_child_user_cpu_seconds": cpu_end.ru_utime - cpu_start.ru_utime,
        "local_child_system_cpu_seconds": cpu_end.ru_stime - cpu_start.ru_stime,
        "server_compute_seconds": None,
        "note": "Wall time covers CLI launch through process exit, excluding setup and archival. Provider GPU/compute time is not exposed."})
    archive(case)
    write_json(record / "status.json", {"status": "completed" if code == 0 else "failed",
                                       "ended_at": ended, "exit_code": code})
    print("Finished", case, "exit", code, "elapsed seconds", round(elapsed, 1), flush=True)
    if code:
        raise SystemExit(code)


def run_all():
    exp = read_json(HERE / "experiment.json")
    for case in exp["order"]:
        if (records(case) / "timing.json").exists():
            existing = read_json(records(case) / "timing.json")
            if existing["exit_code"]:
                raise SystemExit("A previous condition failed; inspect before continuing.")
            continue
        launch(case)
    write_json(HERE / "finished.json", {"finished_at": utc(), "order": exp["order"]})


def status():
    exp = read_json(HERE / "experiment.json")
    for case in exp["order"]:
        r = records(case)
        state = read_json(r / "status.json") if (r / "status.json").exists() else {"status": "pending"}
        print(case, state)
        if (r / "events.jsonl").exists():
            lines = (r / "events.jsonl").read_text().splitlines()
            print("  event lines:", len(lines))
            for line in reversed(lines):
                try: x = json.loads(line)
                except json.JSONDecodeError: continue
                i = x.get("item", {})
                if i.get("type") == "agent_message":
                    print("  latest message:", i.get("text", "")[:650])
                    break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "preflight", "run", "status", "archive"])
    parser.add_argument("--case", choices=list(CASES))
    a = parser.parse_args()
    if a.action == "prepare": prepare()
    elif a.action == "preflight": preflight(a.case) if a.case else preflight_all()
    elif a.action == "run": launch(a.case) if a.case else run_all()
    elif a.action == "status": status()
    elif a.action == "archive": archive(a.case)
