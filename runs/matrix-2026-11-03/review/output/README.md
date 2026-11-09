The completed paper is [Residual conductivity at isotropic conical band crossings](graphene_conductivity.pdf). Its editable source is [graphene_conductivity.tex](graphene_conductivity.tex).

The paper states and proves the theorem in `graphene_statement.tex`, including the analytic justification of the Stark evolution and current. The original notes are unchanged. Only the supplied files and existing mathematical knowledge were used; no online sources were consulted. Reed–Simon citations were checked in the supplied volumes.

Three subagents developed independent proof checks and then reviewed the manuscript through two rounds of revision. Their reports and the revision record are in [reviews/README.md](reviews/README.md).

To rebuild the self-contained LaTeX source:

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build graphene_conductivity.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build graphene_conductivity.tex
```

The resulting PDF is `build/graphene_conductivity.pdf`. The delivered copy at the workspace root is the same final PDF.
