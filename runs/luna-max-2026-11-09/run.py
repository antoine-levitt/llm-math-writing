#!/usr/bin/env python3
"""Repeat the original plain condition with GPT-6-Luna/max.

Reuse the original launch, archive and accounting code. Never edit a model's
manuscript or overwrite an existing attempt.
"""
from __future__ import annotations

import argparse
import difflib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
ORIGINAL = HERE.parent / "matrix-2026-11-03"
CASE = "plain"
MODEL = "gpt-6-luna"


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


runner = module("original_experiment", ORIGINAL / "experiment.py")
runner.HERE = HERE
runner.CASES = {CASE: "prompt"}
metadata = runner.read_json(ORIGINAL / "experiment.json")
runner.CLI = Path(metadata["cli"])


def prepare():
    if (HERE / "experiment.json").exists() or (HERE / CASE).exists():
        raise SystemExit("Already prepared; refusing to overwrite an attempt.")
    assert runner.digest(runner.CLI) == metadata["cli_sha256"]
    assert runner.digest(PROJECT / "prompt") == metadata["conditions"][CASE]["prompt_sha256"]
    catalog = runner.read_json(ORIGINAL / "model-catalog.json")
    model = next(m for m in catalog["models"] if m["slug"] == MODEL)
    assert "max" in [level["effort"] for level in model["supported_reasoning_levels"]]
    package = HERE / "support/djvulibre-bin_3.5.29-1_amd64.deb"
    assert runner.digest(package) == "877174dd762401862dc91dd40ef790f31d3df6130e17628403cde25331fa3705"
    tool_root = Path(tempfile.mkdtemp(prefix="graphene-tools-"))
    subprocess.run(["dpkg-deb", "-x", str(package), str(tool_root)], check=True, timeout=30)
    # The original experiment exposed the package's executables, not its docs.
    for child in tool_root.iterdir():
        if child.name != "usr":
            raise RuntimeError("Unexpected package layout: " + str(child))
    for child in (tool_root / "usr").iterdir():
        if child.name != "bin":
            shutil.rmtree(child)
    for name, digest in metadata["inputs"].items():
        assert runner.digest(ORIGINAL / "inputs" / name) == digest, name
    shutil.copytree(ORIGINAL / "inputs", HERE / "inputs")
    shutil.copy2(ORIGINAL / "model-catalog.json", HERE / "model-catalog.json")
    shutil.copy2(ORIGINAL / "inputs-manifest.json", HERE / "inputs-manifest.json")
    record = HERE / CASE
    record.mkdir()
    scratch = Path(tempfile.mkdtemp(prefix="graphene-run-"))
    rt = {"scratch": str(scratch), "workspace": str(scratch / "work"),
          "codex_state": str(scratch / "codex-state"),
          "temporary": str(scratch / "tmp"), "database": str(scratch / "state"),
          "log": str(scratch / "log"), "shared_tools": str(tool_root)}
    for key in ["workspace", "codex_state", "temporary", "database", "log"]:
        Path(rt[key]).mkdir(mode=0o700)
    shutil.copytree(HERE / "inputs", rt["workspace"], dirs_exist_ok=True)
    shutil.copy2(HERE / "model-catalog.json", Path(rt["codex_state"]) / "model-catalog.json")
    shutil.copy2(PROJECT / "prompt", record / "prompt.txt")
    runner.write_json(record / "runtime.json", rt)
    old_rt = runner.read_json(ORIGINAL / CASE / "runtime.json")
    original_config = (ORIGINAL / CASE / "config.json").read_text()
    config_text = original_config.replace(old_rt["scratch"], rt["scratch"])
    config_text = config_text.replace(old_rt["shared_tools"], rt["shared_tools"])
    config = json.loads(config_text)
    config["model"] = MODEL
    config["agents.default_subagent_model"] = MODEL
    context = runner.read_json(ORIGINAL / CASE / "startup-context.json")
    instructions = next(x for x in context if x.get("type") == "message"
                        and x.get("role") == "developer")["content"][0]["text"]
    instruction_file = Path(rt["codex_state"]) / "model-instructions.txt"
    instruction_file.write_text(instructions)
    (record / "model-instructions.txt").write_text(instructions)
    config["model_instructions_file"] = str(instruction_file)
    runner.write_json(record / "config.json", config)
    common = runner.read_json(ORIGINAL / "common-config.json")
    common["model"] = MODEL
    common["agents.default_subagent_model"] = MODEL
    runner.write_json(HERE / "common-config.json", common)
    runner.write_json(HERE / "experiment.json", {
        "prepared_at": runner.utc(), "model": MODEL, "reasoning_effort": "max",
        "cli": str(runner.CLI), "cli_sha256": runner.digest(runner.CLI),
        "cli_version": metadata["cli_version"],
        "catalog_sha256": runner.digest(HERE / "model-catalog.json"),
        "execution": "single additional condition", "order": [CASE],
        "input_source": str(ORIGINAL / "inputs"), "inputs": metadata["inputs"],
        "shared_tools": str(tool_root),
        "conditions": {CASE: {**metadata["conditions"][CASE], "workspace": rt["workspace"]}},
        "protocol_source": str(ORIGINAL / "PROTOCOL.txt"),
        "original_experiment_sha256": runner.digest(ORIGINAL / "experiment.json"),
        "launcher_sha256": runner.digest(Path(__file__)),
        "reused_launcher_sha256": runner.digest(ORIGINAL / "experiment.py"),
        "usage_parser_sha256": runner.digest(ORIGINAL / "summarize_traces.py"),
        "intentional_config_changes": {"model": MODEL, "agents.default_subagent_model": MODEL,
            "model_instructions_file": "Original Astra runtime instructions held constant."},
        "model_instructions_sha256": runner.digest(instruction_file),
        "tool_package": {"file": str(package.relative_to(HERE)),
                         "sha256": runner.digest(package), "version": "3.5.29-1",
                         "note": "Restored missing /tmp tools from Ubuntu package; historical binaries were not retained."},
        "tool_hashes": {str(p.relative_to(tool_root)): runner.digest(p)
                        for p in sorted(tool_root.rglob("*")) if p.is_file()},
    })
    print("Prepared Luna/max with the unchanged basic prompt and frozen inputs.", flush=True)


def preflight():
    try:
        runner.preflight(CASE)
        record = HERE / CASE
        rt = runner.runtime(CASE)
        denied = [str(ORIGINAL / CASE / "output/graphene_conductivity.tex"),
                  str(PROJECT / "baseline/comparison-version/main.tex"),
                  str(PROJECT / "main.md"), str(PROJECT.parent / "2026-10-graphene/main.tex")]
        probe = "from pathlib import Path\nimport socket\n"
        probe += "for name in " + repr(denied) + ":\n"
        probe += "    try: Path(name).read_bytes()\n    except (PermissionError,FileNotFoundError): pass\n    else: raise RuntimeError('Readable forbidden input: '+name)\n"
        probe += "try: socket.create_connection(('1.1.1.1',443),timeout=2)\nexcept OSError: pass\nelse: raise RuntimeError('Agent command network is available')\n"
        probe += "print('PASS: earlier manuscripts and baseline inaccessible; command network blocked.')\n"
        result = subprocess.run(runner.base_args(CASE) + ["sandbox", "--", "/usr/bin/python3", "-c", probe],
                                cwd=rt["workspace"], env=runner.environment(CASE),
                                capture_output=True, text=True, timeout=30)
        (record / "additional-sandbox-check.txt").write_text(result.stdout + result.stderr)
        assert result.returncode == 0, result.stderr
        old_rt = runner.read_json(ORIGINAL / CASE / "runtime.json")
        def comparable(value):
            if isinstance(value, dict):
                return {k: comparable(v) for k, v in value.items()}
            if isinstance(value, list):
                return [comparable(v) for v in value]
            if isinstance(value, str):
                # model_instructions_file trims the final newline only.
                return re.sub(r"<current_date>[^<]+", "<current_date><DATE>", value).rstrip()
            return value
        normalized_old = json.dumps(comparable(runner.read_json(ORIGINAL / CASE / "startup-normalized.json")), indent=2)
        normalized_new = json.dumps(comparable(runner.read_json(record / "startup-normalized.json")), indent=2)
        diff = "".join(difflib.unified_diff(normalized_old.splitlines(True), normalized_new.splitlines(True),
                                             fromfile="Astra/plain startup", tofile="Luna/plain startup"))
        (record / "startup-vs-astra.diff").write_text(diff)
        assert not diff, "Startup differs from the original beyond the date and final newline"
        cfg = (record / "config.json").read_text().replace(rt["scratch"], old_rt["scratch"])
        cfg = cfg.replace(rt["shared_tools"], old_rt["shared_tools"])
        comparison = json.loads(cfg)
        comparison["model"] = "gpt-6-astra"
        comparison["agents.default_subagent_model"] = "gpt-6-astra"
        comparison.pop("model_instructions_file")
        assert comparison == runner.read_json(ORIGINAL / CASE / "config.json")
        context = runner.read_json(ORIGINAL / CASE / "startup-context.json")
        instructions = next(x for x in context if x.get("type") == "message"
                            and x.get("role") == "developer")["content"][0]["text"]
        assert (record / "model-instructions.txt").read_text() == instructions
        assert (Path(rt["codex_state"]) / "model-instructions.txt").read_text() == instructions
        runner.write_json(HERE / "preflight.json", {
            "passed_at": runner.utc(), "cases": [CASE],
            "config_matches_original_except_models_neutral_paths_and_instruction_override": True,
            "original_runtime_instructions_preserved": True,
            "startup_matches_original_after_date_and_terminal_whitespace_normalization": not diff,
            "startup_diff": str((record / "startup-vs-astra.diff").relative_to(HERE)),
        })
        print("Preflight passed; startup comparison saved.", flush=True)
    finally:
        (Path(runner.runtime(CASE)["codex_state"]) / "auth.json").unlink(missing_ok=True)


def audit():
    # Retain the original audit, changing only its expected model and location.
    source = (ORIGINAL / "audit.py").read_text()
    assert source.count('[["gpt-6-astra", "max"]]') == 1
    source = source.replace('[["gpt-6-astra", "max"]]', '[["gpt-6-luna", "max"]]')
    target = HERE / "audit.py"
    target.write_text(source)
    sys.path.insert(0, str(ORIGINAL))
    checker = module("luna_audit", target)
    checker.main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["prepare", "preflight", "run", "status", "archive", "audit"])
    args = parser.parse_args()
    if args.action == "prepare": prepare()
    elif args.action == "preflight": preflight()
    elif args.action == "run":
        try:
            runner.launch(CASE)
        finally:
            (Path(runner.runtime(CASE)["codex_state"]) / "auth.json").unlink(missing_ok=True)
    elif args.action == "status": runner.status()
    elif args.action == "archive": runner.archive(CASE)
    elif args.action == "audit": audit()
