#!/usr/bin/env python3
"""Run one grader with anonymous inputs and genuinely private Codex state."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
MATRIX = HERE.parent.parent
sys.path.insert(0, str(MATRIX))
from experiment import toml
from summarize_traces import summarize


def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc():
    return datetime.now(timezone.utc).isoformat()


def run():
    record = HERE / "isolated"
    record.mkdir()  # Refuse to overwrite a previous attempt.
    scratch = Path(tempfile.mkdtemp(prefix="manuscript-grader-"))
    work, state, temporary = [scratch / p for p in ("work", "codex-state", "tmp")]
    database, log = scratch / "database", scratch / "log"
    for folder in [work, state, temporary, database, log]:
        folder.mkdir(mode=0o700)
    input_hashes = {}
    for src in (HERE / "anonymous-inputs").iterdir():
        shutil.copyfile(src, work / src.name)
        input_hashes[src.name] = sha(src)
    write(record / "input-hashes.json", input_hashes)
    prompt = (HERE / "grader-prompt.txt").read_text().replace(
        "/tmp/manuscripts-fe9zkh8f", str(work))
    (record / "prompt.txt").write_text(prompt)
    metadata = json.loads((MATRIX / "experiment.json").read_text())
    cli = Path(metadata["cli"])
    assert sha(cli) == metadata["cli_sha256"]
    shutil.copyfile(MATRIX / "model-catalog.json", state / "model-catalog.json")
    shutil.copyfile("/home/antoine/.codex/auth.json", state / "auth.json")
    (state / "auth.json").chmod(0o600)
    config = json.loads((MATRIX / "common-config.json").read_text())
    config.pop("permissions.graphene.network.enabled")
    config.update({
        "features.multi_agent": False,
        "default_permissions": "papers",
        "permissions.papers.network.enabled": False,
        "permissions.papers.filesystem": {
            ":minimal": "read", ":workspace_roots": "write",
            str(temporary): "write", str(cli.parent.parent): "read",
            "/var/lib/texmf": "read", "/var/cache/fontconfig": "read",
        },
        "sqlite_home": str(database), "log_dir": str(log),
        "model_catalog_json": str(state / "model-catalog.json"),
        "shell_environment_policy.set": {
            "PATH": "/usr/bin:/usr/local/bin:/bin", "TMPDIR": str(temporary)},
    })
    write(record / "config.json", config)
    write(record / "runtime.json", {"workspace": str(work), "state": str(state),
        "temporary": str(temporary), "database": str(database), "log": str(log)})
    env = {k: v for k, v in os.environ.items() if not k.startswith(("CODEX_", "MCP_"))}
    env.update({"CODEX_HOME": str(state), "TMPDIR": str(temporary),
                "PATH": "/usr/bin:/usr/local/bin:/bin"})
    args = [str(cli), "--no-daemon", "-C", str(work)]
    for key, value in config.items():
        args.extend(["-c", key + "=" + toml(value)])
    validation = subprocess.run(args + ["app-server", "--strict-config", "--print-startup-config"],
        cwd=work, env=env, capture_output=True, text=True, timeout=55)
    (record / "config-validation.json").write_text(validation.stdout)
    (record / "config-validation.stderr").write_text(validation.stderr)
    assert validation.returncode == 0, validation.stderr
    preview = subprocess.run(args + ["debug", "prompt-input", prompt],
        cwd=work, env=env, capture_output=True, text=True, timeout=55)
    (record / "startup-context.json").write_text(preview.stdout)
    assert preview.returncode == 0, preview.stderr
    context = json.loads(preview.stdout)
    users = [x for x in context if x.get("type") == "message" and x.get("role") == "user"]
    assert len(users) == 2
    assert users[-1]["content"][0]["text"] == prompt
    for forbidden in ["AGENTS.md instructions", "Antoine Levitt", "llm-writing",
                      "private-mapping", "explicit_review", "iterative_review"]:
        assert forbidden not in preview.stdout, forbidden
    denied = [str(HERE / "private-mapping.json"),
              str(HERE.parent / "private-mapping.json"),
              str(HERE.parent / "READABILITY_REVIEW_BLIND.txt"),
              str(HERE.parent / "anonymous-inputs/Manuscript_B.pdf"),
              str(MATRIX.parent.parent / "baseline/comparison-version/main.tex"),
              str(state / "auth.json")]
    probe = "from pathlib import Path\nassert Path('Manuscript_B.txt').read_text()\n"
    probe += "for name in " + repr(denied) + ":\n"
    probe += "    try: Path(name).read_bytes()\n    except (PermissionError, FileNotFoundError): pass\n    else: raise RuntimeError('Readable forbidden input: '+name)\n"
    probe += "print('PASS: anonymous inputs readable; mapping, prior review, and credentials blocked.')\n"
    checked = subprocess.run(args + ["sandbox", "--", "/usr/bin/python3", "-c", probe],
        cwd=work, env=env, capture_output=True, text=True, timeout=55)
    (record / "sandbox-check.txt").write_text(checked.stdout + checked.stderr)
    assert checked.returncode == 0, checked.stderr
    write(record / "preflight.json", {"passed_at": utc(), "prompt_sha256": sha(record / "prompt.txt"),
        "startup_sha256": sha(record / "startup-context.json"), "initial_user_messages": len(users)})
    print("Preflight passed: no personal/project context; no access to mapping or previous review.", flush=True)
    command = args + ["exec", "--strict-config", "--ignore-user-config", "--ignore-rules",
                      "--skip-git-repo-check", "--json", "--color", "never", "-"]
    write(record / "argv.json", command)
    start, started = time.monotonic(), utc()
    print("Grader started:", started, flush=True)
    with (record / "prompt.txt").open("rb") as task, (record / "events.jsonl").open("wb") as events, \
         (record / "events-timed.jsonl").open("w", buffering=1) as timed, (record / "stderr.log").open("wb") as stderr:
        proc = subprocess.Popen(command, cwd=work, env=env, stdin=task,
                                stdout=subprocess.PIPE, stderr=stderr)
        write(record / "process.json", {"pid": proc.pid, "started_at": started})
        for line in proc.stdout:
            events.write(line)
            events.flush()
            timed.write(json.dumps({"received_at": utc(), "elapsed_seconds": time.monotonic()-start,
                                    "event": json.loads(line)}) + "\n")
        code = proc.wait()
    write(record / "timing.json", {"started_at": started, "ended_at": utc(),
        "elapsed_wall_seconds": time.monotonic()-start, "exit_code": code})
    native = record / "native"
    native.mkdir()
    for name in ["sessions", "archived_sessions"]:
        if (state / name).exists(): shutil.copytree(state / name, native / name)
    shutil.copytree(log, native / "log")
    for path in database.glob("*.sqlite"):
        with sqlite3.connect(f"file:{path}?mode=ro", uri=True) as src:
            with sqlite3.connect(native / path.name) as dst: src.backup(dst)
    output = record / "output"
    output.mkdir()
    for path in work.rglob("*"):
        if not path.is_file() or path.is_symlink(): continue
        relative = str(path.relative_to(work))
        if relative in input_hashes: continue
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
    unchanged = {name: sha(work / name) == value for name, value in input_hashes.items()}
    rows = [json.loads(line) for line in (record / "events.jsonl").read_text().splitlines()]
    root = next(row["thread_id"] for row in rows if row.get("type") == "thread.started")
    write(record / "usage.json", summarize(native, root))
    messages = [row["item"]["text"] for row in rows if row.get("type") == "item.completed"
                and row.get("item", {}).get("type") == "agent_message"]
    if messages: (record / "final-response.txt").write_text(messages[-1] + "\n")
    write(record / "artifact-manifest.json", {"root_thread_id": root, "inputs_unchanged": unchanged,
        "output_hashes": {str(p.relative_to(output)): sha(p) for p in output.rglob("*") if p.is_file()}})
    (state / "auth.json").unlink(missing_ok=True)
    assert all(unchanged.values())
    print("Finished:", code, "elapsed minutes:", round((time.monotonic()-start)/60, 2), flush=True)
    raise SystemExit(code)


def main():
    try:
        run()
    finally:
        runtime_path = HERE / "isolated/runtime.json"
        if runtime_path.exists():
            state = Path(json.loads(runtime_path.read_text())["state"])
            (state / "auth.json").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
