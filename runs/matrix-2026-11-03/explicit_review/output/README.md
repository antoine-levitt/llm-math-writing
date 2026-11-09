# Residual conductivity at isotropic Dirac points

- [Read the paper](dirac_conductivity.pdf).
- [LaTeX source](dirac_conductivity.tex).

The ten-page manuscript states and proves the theorem in
`graphene_statement.tex`, including the existence of the fixed-time linear
response and the subsequent time-averaged limit. The main text explains
the transport of the occupied subspace, the geometry forced by an
isotropic crossing, and the cancellation of the cone velocity. An
appendix supplies the operator and trace estimates.

Only the supplied notes and the local Reed–Simon volumes were consulted;
no online sources were used. Three subagents developed independent checks
and completed two rounds of mathematical and editorial review. Their
reports are in [paper_work/reviews](paper_work/reviews).

To rebuild with a standard TeX Live installation, run twice:

```sh
pdflatex -interaction=nonstopmode -halt-on-error dirac_conductivity.tex
```

The source is self-contained and has no external figures or bibliography
files. The final build has no unresolved references or LaTeX warnings.
