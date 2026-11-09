# Editorial and consistency review: first complete draft

I read the full source and compiled it twice into
`paper_work/design_review_build/dirac_conductivity.pdf` (10 pages). The
architecture is sound: the reader sees the mechanism before the machinery,
the results have coherent meanings, and the decisive scaling step is visibly
the climax. I found no mathematical obstruction to the theorem in this draft.
The remaining work is targeted editing and two small analytic clarifications,
not another structural rewrite.

## Changes to make

1. **Fix cross-reference types.** The compiled PDF calls Proposition 2.1
   “theorem 2.1,” Proposition 2.2 “theorem 2.2,” and Lemma 3.1 “theorem 3.1.”
   Shared theorem counters confuse the current cleveref setup. Explicit
   label types (`\label[proposition]{...}`, `\label[lemma]{...}`) or aliascnt
   fix this. Appendix references should say “Appendix A” / “Appendix A.2,”
   not “section A” / “section A.2.” Capitalized reference names would read
   more naturally throughout this manuscript.

2. **Improve the first conceptual sentence.** A Fermi curve in an ordinary
   two-dimensional metal also has zero area, so the opening emphasis on zero
   area does not identify the special issue. Suggested replacement:

   > A two-dimensional semimetal can have a Fermi surface consisting of
   > finitely many points, where occupied and empty bands meet in cones.
   > Transitions across arbitrarily small gaps can nevertheless leave a
   > finite contribution after a long time average.

   The rest of the opening can stay. This introduces the point Fermi surface,
   which is the feature actually used by the projector argument.

3. **Remove the orphan notation in the reciprocal-lattice display.** Instead
   of “Its reciprocal lattice and a reciprocal cell are denoted by [display
   ending in a bare `B`],” write “Its reciprocal lattice is [definition]. Let
   `B` be a fundamental cell of `R*`, so that ...”. This reads like a
   mathematical definition rather than a notational list.

4. **Define both directional velocities and derivatives together.** The
   first display of Section 2 defines only `v_alpha` and `partial_beta`,
   although `v_beta` and `partial_alpha` are subsequently used. Write the
   definitions with `nu in {alpha,beta}`. The meanings are inferable now, but
   an explicit joint definition costs essentially nothing.

5. **Say “Sobolev weights,” not “spatial weights.”** `Lambda=1-Delta_per`
   controls derivatives; “spatial weights” usually means multiplication by
   a function of position. Keep the weighted conclusion in Proposition 2.1.
   It occupies only a few lines, follows in the same proof, and makes the
   result complete. Moving it entirely to the appendix would create the
   user's disliked pattern of an important fact being added later. The
   weighted Banach-space formalism and current estimates correctly remain
   in Appendix A.3.

6. **Correct “periodic fibers.”** In Section 2.2, the density is periodic in
   physical space, while its Bloch field is covariant under reciprocal
   translations. Say “The evolved density has Bloch fibers `rho_epsilon`” or
   “The evolved density is periodic in space and has Bloch fibers ...”.

7. **Simplify the characteristic regularity justification.** Replace the
   invocation of Banach-valued Sobolev absolute continuity by the immediate
   geometric fact: “For almost every final momentum `k`, the characteristic
   avoids the crossings, so `P` is smooth along it.” For fixed finite `t` the
   exceptional set is a finite union of line segments on the torus. This
   proves the exact source identity without importing an abstract ACL
   theorem. The weighted `W^{1,1}` property is still used for the subsequent
   integral limit. State the source identity for `epsilon>0`.

8. **Clarify the transition interpretation.** The radial/tangential
   discussion after Lemma 3.1 is excellent, but qualify it with “For the
   linearized cone,” since at nonzero `q` the exact curved bands have `O(r)`
   corrections. The distinction matters for an insight paragraph that the
   reader might remember literally.

9. **Avoid `C(q)` next to generic constants `C`.** Section 4.2 uses `C(q)`
   for the transition weight, then `Cr` for a gap bound and `C min{...}` for
   the dominator. Rename the weight to `w(q)` or `F(q)`; this is the only
   appreciable notation collision in the manuscript.

10. **Make the local trace-class extension explicit.** After (A.6), local
    trace class on an arbitrary bounded set requires the off-diagonal
    blocks between different cells as well as each same-cell compression.
    State that the block between `Omega+R` and `Omega+S` has the same
    trace-class Bochner integral with the additional scalar phase
    `exp(ik.(R-S))`. A bounded set meets only finitely many cells, so all
    blocks are trace class. The present “same argument ... intersections”
    hides this short but relevant point.

11. **Keep the proof's conclusion with its computation.** In the current PDF,
    page 7 ends with the displayed `1/16`, while page 8 begins with the lone
    “Adding the M disks ... proves (1.7)” followed by the closing paragraph
    and Appendix A. The last line of the proof should travel with the last
    displayed computation. Prefer light editing before forced page breaks:
    Section 4.1's final paragraph and the sentence about avoiding phase
    difference estimates can be shortened, recovering several lines.
    Ultimately inspect the rebuilt PDF after all edits, since the current
    page break will change.

## Optional refinements

* Consider calling the cone matrix-element result a **Proposition**, giving
  it equal visual status with the response formula and projector regularity.
  It is one of the paper's two main conceptual inputs; its current title and
  proof are already semantically strong, so this is emphasis rather than a
  mathematical issue.
* In Section 4.1, combine the final two sentences into “Only the touching pair
  in each disk remains.” Internal degeneracies are already handled by the
  basis-invariant sums and need not be mentioned again here.
* After (4.6), “Thus quadratic corrections to the cone do not affect the
  limit” is enough. The sentence about not estimating differences of rapidly
  oscillating phases describes the proof-writing process rather than the
  phenomenon and can be dropped.
* The manuscript ends its main argument well. If trimming is needed, the
  closing paragraph can become: “Isotropy fixes the leading interband
  transition strength, and time averaging selects the linear part of each
  cone. The cone slopes may differ: each contributes the same tensor.”
  This reinforces precisely what is universal without repeating the entire
  introduction.

## What should stay

* The abstract is informative and proportionate. It states the order of
  limits, the multiplicity convention, and the eigenvalue-to-eigenvector
  insight without overselling.
* The theorem statement is self-contained with respect to the preceding
  assumptions and includes well-definedness of the current.
* The transport argument successfully avoids an artificial collection of
  cancellation lemmas. The source identity is motivated before it is used.
* The local frame is explicit, and the second use of it in Section 3 is
  short enough that the reader need not retain its detailed formula.
* The Clifford-identity argument is better here than introducing Pauli
  matrices, three-vector coefficients, rotations, and gauge notation.
* The one-cone rescaling visibly displays both velocity cancellation and a
  single integrable dominator. This is the right amount of detail.
* The elementary Laplace evaluation of the radial integral is short and
  avoids an unexplained citation to the Dirichlet integral.
* Appendix A is about the right length. The stronger weighted norm is
  technically convenient and keeps its continuity estimates elementary.

## Figure recommendation

Do **not** add a generic cone illustration. The existing argument is short,
and such a picture would mostly repeat the word “cone.” A meaningful figure
would need two panels: tangential velocity coupling and concentration of the
averaged radial kernel at radius `1/T`. That would occupy substantial space
and introduce plotting choices while adding little beyond (3.1) and (4.4).
The formulas and the explanatory paragraphs already provide the needed
geometric visualization. A figure is not a prerequisite for this paper's
readability.

## Mathematics and citations checked

* All signs and normalization factors in the real response and conical limit
  are consistent. With the stated definition of `Z`, the imaginary term in
  (2.15) has the displayed plus sign.
* The double-sided weighted bounds follow from the finite-rank `H²` frame;
  they do not require `H⁴` eigenfunctions.
* The scalar gap assumptions force the traceless linear cone matrix and its
  anticommutator identity. The moving-frame derivative terms vanish at the
  scalar degeneracy, so the physical velocity has the asserted leading
  matrix. This subtle point is handled correctly.
* Cauchy--Schwarz controls the entire infinite sum using only occupied
  eigenfunctions. The uniformly gapped remainder is indeed `O(1/T)`.
* The interpolation estimate in Appendix A.3 is sufficient for the current;
  no unjustified strong `H²` convergence is assumed.
* Reed--Simon II Theorems X.12, X.38, X.70 and IV Theorems XIII.96, XIII.97,
  XIII.99, together with Section XII.2, are correctly cited for the results
  used. In particular the manuscript applies X.38 itself to the periodic
  potential, avoiding its inapplicable global-`L^p` corollary.
* The bibliography titles, volumes, and years are correct.

