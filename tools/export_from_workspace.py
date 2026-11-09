#!/usr/bin/env python3
"""Refresh the explicitly selected companion files from the experiment workspace."""

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


MATRIX = Path("runs/matrix-2026-11-03")
LUNA = Path("runs/luna-max-2026-11-09")
GRADING = MATRIX / "readability-blind"
UPDATE = GRADING / "b-update-2026-11-05"
CONDITIONS = ("plain", "explicit", "review", "explicit_review")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def export(source, destination):
    provenance = {}

    def copy(relative):
        relative = Path(relative)
        original = source / relative
        assert original.is_file() and not original.is_symlink(), original
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
        provenance[relative.as_posix()] = {
            "source": relative.as_posix(),
            "source_sha256": digest(original),
            "transformation": "none",
        }

    def files(directory, names):
        for name in names.split():
            copy(Path(directory) / name)

    def derived(relative, content, sources, transformation):
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        provenance[relative.as_posix()] = {
            "sources": {p.as_posix(): digest(source / p) for p in sources},
            "transformation": transformation,
        }

    files(".", "COMMENTS_ANTOINE.md prompt prompt_explicit_instruction "
          "prompt_tokenmaxing prompt_explicit_instruction_plus_tokenmaxing")
    files("baseline/comparison-version", "main.tex main.pdf refs.bib build.sh")
    for path in sorted((source / "baseline/provenance").iterdir()):
        copy(path.relative_to(source))
    for version in ("statement-version", "prompt-version", "comparison-version-before-fa"):
        files(Path("old/baseline") / version, "main.tex main.pdf refs.bib build.sh")
    files("old/baseline", "statement-version-NOTES.txt prompt-version-NOTES.txt "
          "prompt-version-changes.diff prompt-version-parent-hashes.json "
          "comparison-version-before-fa-NOTES.txt")
    copy("old/manifest-2026-11-05.json")

    for directory in (MATRIX, LUNA):
        files(directory, "PROTOCOL.txt RESULTS.txt results.csv experiment.json "
              "common-config.json inputs-manifest.json audit-summary.json "
              "preflight.json finished.json audit.py")
        files(directory / "inputs", "graphene_statement.tex graphene_statement.pdf")
    files(MATRIX, "api-pricing.json INDEPENDENT_AUDIT.txt TRACE_ACCOUNTING.txt "
          "experiment.py summarize_traces.py")
    files(LUNA, "run.py verification.json")
    files(GRADING, "READABILITY_REVIEW_BLIND.txt READABILITY_REVIEW_UPDATED.txt "
          "RESULTS.txt RESULTS_UPDATED.txt grader-prompt.txt private-mapping.json "
          "verification.json run_isolated.py")
    files(UPDATE, "READABILITY_REVIEW_BLIND.txt PROTOCOL.txt grader-prompt.txt "
          "private-mapping.json verification.json prompt-changes.diff "
          "runner-changes.diff run_isolated.py")
    for directory in (GRADING / "anonymous-inputs", UPDATE / "anonymous-inputs"):
        for path in sorted((source / directory).iterdir()):
            assert path.suffix in (".pdf", ".txt"), path
            copy(path.relative_to(source))

    run_directories = [MATRIX / condition for condition in CONDITIONS]
    run_directories += [LUNA / "plain", GRADING / "isolated", UPDATE / "isolated"]
    for directory in run_directories:
        files(directory, "prompt.txt final-response.txt config.json argv.json "
              "timing.json usage.json artifact-manifest.json")
        if directory in [MATRIX / condition for condition in CONDITIONS] + [LUNA / "plain"]:
            files(directory, "AUDIT.txt audit.json status.json")
        for path in sorted((source / directory / "output").iterdir()):
            if path.is_file() and path.suffix in (".pdf", ".tex", ".bib", ".md", ".txt"):
                copy(path.relative_to(source))
        review_directory = directory / "output" / "reviews"
        if directory.name == "explicit_review":
            review_directory = directory / "output" / "paper_work" / "reviews"
        if (source / review_directory).is_dir():
            for path in sorted((source / review_directory).glob("*.md")):
                copy(path.relative_to(source))

        event_path = directory / "events.jsonl"
        events = [json.loads(line) for line in (source / event_path).read_text().splitlines()]
        activity = ["# Activity log\n", "Extracted from the root CLI event stream. "
                    "Includes completed assistant messages, commands, file-change paths, "
                    "and exit statuses. Tool output (including textbook extracts), file "
                    "diffs, native reasoning records, and private runtime state are omitted. "
                    "Reviewer reports are separate files.\n"]
        for event in events:
            kind = event.get("type")
            if kind == "item.completed":
                item = event["item"]
                if item["type"] == "agent_message":
                    activity.extend(["## Assistant\n", item["text"].rstrip() + "\n"])
                elif item["type"] == "command_execution":
                    command = item["command"]
                    fence = "`" * max(4, max((len(x) for x in re.findall(r'`+', command)), default=0) + 1)
                    activity.extend(["## Command\n", f"{fence}sh\n{command}\n{fence}\n",
                                     f"Status: {item.get('status')}; exit code: {item.get('exit_code')}.\n"])
                elif item["type"] == "file_change":
                    activity.append("## File changes\n")
                    for change in item.get("changes", []):
                        activity.append(f"- {change.get('kind')}: `{change.get('path')}`")
                    activity.append("")
                else:
                    raise ValueError(f"Unreviewed event item type: {item['type']}")
            elif kind not in ("thread.started", "turn.started", "turn.completed", "item.started"):
                raise ValueError(f"Unreviewed event type: {kind}")
        derived(directory / "activity.md", "\n".join(activity), [event_path],
                "Completed assistant messages and command/file-change metadata; tool output and file diffs omitted.")

        records = {}
        trace_paths = sorted((source / directory / "native/sessions").rglob("*.jsonl"))
        assert trace_paths, directory
        for trace in trace_paths:
            for line in trace.read_text().splitlines():
                record = json.loads(line)
                if record.get("type") != "token_usage_record":
                    continue
                payload = record["payload"]
                row = {key: payload[key] for key in ("response_id", "thread_id", "turn_id", "usage")}
                previous = records.setdefault(row["response_id"], row)
                assert previous == row, row["response_id"]
        usage = json.loads((source / directory / "usage.json").read_text())
        actual = {key: sum(row["usage"].get(key, 0) for row in records.values())
                  for key in usage["total_usage"]}
        assert actual == usage["total_usage"], (directory, actual, usage["total_usage"])
        derived(directory / "response-usage.jsonl",
                "".join(json.dumps(row, sort_keys=True) + "\n" for row in records.values()),
                [p.relative_to(source) for p in trace_paths],
                "Response-level token records only; deduplicated by response_id. No conversation content or account identifiers.")

    entries = []
    for path in sorted(destination.rglob("*")):
        if not path.is_file() or ".git" in path.relative_to(destination).parts:
            continue
        relative = path.relative_to(destination).as_posix()
        if relative in ("MANIFEST.json", "CHECKSUMS.sha256"):
            continue
        assert not path.is_symlink(), path
        entries.append({"path": relative, "sha256": digest(path), "bytes": path.stat().st_size,
                        **provenance.get(relative, {"transformation": "Repository documentation or export tooling."})})
    manifest = {"description": "Curated export; source paths are relative to the original blog-post workspace.",
                "files": entries}
    (destination / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    checksum_paths = [entry["path"] for entry in entries] + ["MANIFEST.json"]
    (destination / "CHECKSUMS.sha256").write_text(
        "".join(f"{digest(destination / p)}  {p}\n" for p in sorted(checksum_paths)))
    print(f"Exported {len(entries)} files plus manifest/checksums; "
          f"{sum(entry['bytes'] for entry in entries) / 1024**2:.2f} MiB.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path,
                        help="Original blog-post workspace (contains COMMENTS_ANTOINE.md and runs/).")
    parser.add_argument("--destination", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    assert args.source.resolve() != args.destination.resolve()
    export(args.source.resolve(), args.destination.resolve())
