# Can LLMs write math papers? — Experiment materials

THIS IS ALL AI-GENERATED, READ AT YOUR OWN RISK.

Companion to [Antoine Levitt's blog post](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/2026-10-llm-writing/).

Four prompts were used to ask GPT-6-Astra, at maximum reasoning effort, to write a paper proving a theorem about graphene conductivity. The experiment varies explicit writing instructions and instructions to iterate with reviewers. These are single runs, conducted on 3 November 2026. A separate GPT-6-Luna run was added on 9 November.

## Manuscripts and prompts

The blind labels are those used in the human comments and AI readability reports. The PDFs, TeX sources, prompts, and comments are unchanged from the experiment workspace.

| Condition | Blind label | Manuscript | Source | Prompt |
| --- | --- | --- | --- | --- |
| Plain | D | [PDF](runs/matrix-2026-11-03/plain/output/graphene_conductivity.pdf) | [TeX](runs/matrix-2026-11-03/plain/output/graphene_conductivity.tex) | [Prompt](prompt) |
| Explicit writing instructions | E | [PDF](runs/matrix-2026-11-03/explicit/output/paper.pdf) | [TeX](runs/matrix-2026-11-03/explicit/output/paper.tex) | [Prompt](prompt_explicit_instruction) |
| Tokenmaxxing | C | [PDF](runs/matrix-2026-11-03/review/output/graphene_conductivity.pdf) | [TeX](runs/matrix-2026-11-03/review/output/graphene_conductivity.tex) | [Prompt](prompt_tokenmaxing) |
| Instructions + tokenmaxxing | A | [PDF](runs/matrix-2026-11-03/explicit_review/output/dirac_conductivity.pdf) | [TeX](runs/matrix-2026-11-03/explicit_review/output/dirac_conductivity.tex) | [Prompt](prompt_explicit_instruction_plus_tokenmaxing) |
| Adapted human baseline | B | [PDF](baseline/comparison-version/main.pdf) | [TeX](baseline/comparison-version/main.tex) | [Adaptation notes](baseline/provenance/comparison-version-NOTES.txt) |
| Luna, plain prompt | — | [PDF](runs/luna-max-2026-11-09/plain/output/graphene_conductivity_paper.pdf) | [TeX](runs/luna-max-2026-11-09/plain/output/graphene_conductivity_paper.tex) | [Prompt](runs/luna-max-2026-11-09/plain/prompt.txt) |

The baseline is an **AI-assisted adaptation**, not the untouched human paper. It combines text from [*Coherent electronic transport in periodic crystals*](https://arxiv.org/abs/2002.01990), by Eric Cancès, Clotilde Fermanian-Kammerer, Antoine Levitt and Sami Siraj-Dine, with arguments from the generated manuscripts. [Provenance and diffs](baseline/provenance/) document the changes; earlier versions are in [old/baseline/](old/baseline/).

## Comments and readability assessments

- [Antoine's comments](COMMENTS_ANTOINE.md), with the original wording and scores.
- [Current AI readability report](runs/matrix-2026-11-03/readability-blind/READABILITY_REVIEW_UPDATED.txt).
- [Original five-way grading prompt](runs/matrix-2026-11-03/readability-blind/grader-prompt.txt), [report](runs/matrix-2026-11-03/readability-blind/READABILITY_REVIEW_BLIND.txt), and [anonymous input bundle](runs/matrix-2026-11-03/readability-blind/anonymous-inputs/).
- [Revised-B grading prompt](runs/matrix-2026-11-03/readability-blind/b-update-2026-11-05/grader-prompt.txt), [report](runs/matrix-2026-11-03/readability-blind/b-update-2026-11-05/READABILITY_REVIEW_BLIND.txt), and [protocol](runs/matrix-2026-11-03/readability-blind/b-update-2026-11-05/PROTOCOL.txt).
- Reviewer-agent feedback used **during writing**: [tokenmaxxing](runs/matrix-2026-11-03/review/output/reviews/) and [instructions + tokenmaxxing](runs/matrix-2026-11-03/explicit_review/output/paper_work/reviews/).

The current AI report combines the original A/C/D/E assessments with a new, standalone assessment of the revised 14-page B manuscript on 5 November. B's earlier 19-page version scored 6/10; the revised version scored 8/10. The other manuscripts were not regraded. This was a readability assessment, not a correctness audit. Historical adaptation notes predate that regrading.

Pierre's scores and discussion are in the blog post; no separate file of his comments was supplied for this archive. Luna has no assigned readability score here.

## Inputs, execution, and costs

The task input is the theorem statement ([PDF](runs/matrix-2026-11-03/inputs/graphene_statement.pdf), [TeX](runs/matrix-2026-11-03/inputs/graphene_statement.tex)). The runs also had local copies of Reed–Simon's *Methods of Modern Mathematical Physics*, volumes I–IV. The books and their extracted text are not redistributed; their file hashes remain in the [input manifest](runs/matrix-2026-11-03/inputs-manifest.json).

- Astra: [protocol](runs/matrix-2026-11-03/PROTOCOL.txt), [configuration](runs/matrix-2026-11-03/common-config.json), [results](runs/matrix-2026-11-03/RESULTS.txt), [CSV](runs/matrix-2026-11-03/results.csv), [API cost calculations](runs/matrix-2026-11-03/api-pricing.json), and [execution/accounting audit](runs/matrix-2026-11-03/INDEPENDENT_AUDIT.txt).
- Luna: [protocol](runs/luna-max-2026-11-09/PROTOCOL.txt) and [results](runs/luna-max-2026-11-09/RESULTS.txt). It used the original Astra runtime instructions to hold the writing guidance constant while changing the model.

Each run directory contains its final response, configuration, timing, token usage, output hashes, an `activity.md` log, and deduplicated `response-usage.jsonl` records. Activity logs contain assistant messages and command/file-change metadata; tool outputs, file diffs, and native reasoning records are omitted. Reviewer reports are linked above.

Wall times include tools and waits. API costs are estimates at the recorded rates, not invoices: the runs used a ChatGPT subscription. Cached-input and reasoning-output counts are subsets of the input and output totals.

## Archive and verification

This is a curated export. Private session databases, raw native traces and startup dumps, credentials, textbook extracts, temporary build files, and software packages are excluded. Historical protocols describe the larger local archive; paths and hashes in those records may refer to files outside this repository. The old five-way mapping still identifies the earlier B; the B-only update records the revised one.

[MANIFEST.json](MANIFEST.json) records the source paths, hashes, and transformations for the exported files. Check the download with:

```sh
sha256sum --check CHECKSUMS.sha256
python3 tools/verify_archive.py
```

The archived launchers preserve how the experiment was run. They depend on the original machine paths, Codex installation, and omitted reference books; this repository is not a self-contained rerun environment. TeX sources are supplied alongside the delivered PDFs.

To refresh this export from the original workspace:

```sh
python3 tools/export_from_workspace.py --source /path/to/blog/src/2026-10-llm-writing
```
