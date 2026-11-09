#!/usr/bin/env python3
"""Verify file integrity, input/output identity, and response-level token totals."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(relative):
    return json.loads((ROOT / relative).read_text())


def sha(relative):
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def main():
    manifest = load("MANIFEST.json")
    for entry in manifest["files"]:
        assert sha(entry["path"]) == entry["sha256"], entry["path"]
        if entry.get("transformation") == "none":
            assert entry["sha256"] == entry["source_sha256"], entry["path"]
    expected = {entry["path"] for entry in manifest["files"]} | {"MANIFEST.json", "CHECKSUMS.sha256"}
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
              if p.is_file() and ".git" not in p.relative_to(ROOT).parts}
    assert actual == expected, {"extra": sorted(actual - expected), "missing": sorted(expected - actual)}
    for line in (ROOT / "CHECKSUMS.sha256").read_text().splitlines():
        expected_hash, relative = line.split("  ", 1)
        assert sha(relative) == expected_hash, relative

    matrix = Path("runs/matrix-2026-11-03")
    experiment = load(matrix / "experiment.json")
    for condition, settings in experiment["conditions"].items():
        assert sha(settings["prompt_file"]) == settings["prompt_sha256"], condition
        assert sha(matrix / condition / "prompt.txt") == settings["prompt_sha256"], condition
    for filename in ("graphene_statement.tex", "graphene_statement.pdf"):
        assert sha(matrix / "inputs" / filename) == experiment["inputs"][filename], filename
        assert sha(Path("runs/luna-max-2026-11-09/inputs") / filename) == experiment["inputs"][filename], filename
    assert sha("runs/luna-max-2026-11-09/plain/prompt.txt") == sha("prompt")

    grading = matrix / "readability-blind"
    mapping = load(grading / "private-mapping.json")["mapping"]
    manuscripts = {"A": "explicit_review/output/dirac_conductivity.pdf",
                   "C": "review/output/graphene_conductivity.pdf",
                   "D": "plain/output/graphene_conductivity.pdf", "E": "explicit/output/paper.pdf"}
    for label, filename in manuscripts.items():
        assert sha(matrix / filename) == mapping[label]["sha256"], label
        assert sha(grading / "anonymous-inputs" / f"Manuscript_{label}.pdf") == mapping[label]["sha256"], label
    assert sha("old/baseline/statement-version/main.pdf") == mapping["B"]["sha256"]
    assert sha(grading / "anonymous-inputs/Manuscript_B.pdf") == mapping["B"]["sha256"]
    update = grading / "b-update-2026-11-05"
    revised_b = load(update / "private-mapping.json")["B"]["sha256"]
    assert sha("baseline/comparison-version/main.pdf") == revised_b
    assert sha(update / "anonymous-inputs/Manuscript_B.pdf") == revised_b

    run_count = response_count = 0
    for path in sorted((ROOT / "runs").rglob("response-usage.jsonl")):
        records = [json.loads(line) for line in path.read_text().splitlines()]
        assert len(records) == len({row["response_id"] for row in records}), path
        expected_usage = json.loads((path.parent / "usage.json").read_text())["total_usage"]
        actual_usage = {key: sum(row["usage"].get(key, 0) for row in records) for key in expected_usage}
        assert actual_usage == expected_usage, path
        run_count += 1
        response_count += len(records)
    assert run_count == 7, run_count
    print(f"Verified {len(manifest['files'])} files, manuscript mappings, exact prompts/inputs, "
          f"and {response_count} unique responses across {run_count} runs.")


if __name__ == "__main__":
    main()
