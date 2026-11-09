# Round 2 referee report: mathematics, prose, and PDF

I reread the complete revised source and checked the eleven-page PDF's
page boundaries and extracted text. I also visually inspected rendered
pages 6, 7, 10, and 11, which contain the cone proof, the Cesaro argument,
the local trace proof, and the final differentiation argument.

## Verdict

The mathematical issues identified in round 1 have been resolved. I find
no remaining gap in the cone reduction, integrated band-energy identity,
time-reversal cancellation, or Cesaro limit. The theorem still states
the result in the notes with its original assumptions and order of
limits. The analytical appendix is coherent with the main argument.
Subject to the small wording fixes below and the independent final
operator review, I consider the manuscript ready.

## Small corrections

1. **Remove a duplicated phrase in the introduction.**

   Current:

   > We first derive the fixed-time response formula for the response of
   > the full Hamiltonian.

   Suggested:

   > We first derive the fixed-time response formula for the full
   > Hamiltonian.

2. **State the gauge/translation relation accurately.**

   In the local current trace proof, change

   > its commutator with each lattice translation is a scalar phase

   to

   > it commutes with each lattice translation up to a scalar phase.

   The current wording is valid for a multiplicative group commutator,
   but throughout the manuscript “commutator” has its usual additive
   meaning. The proposed wording expresses the intended relation
   unambiguously.

3. **Optional precision in the differentiation proof.**

   Change “Since \(\operatorname{Ran}P(k)\) has a uniformly bounded
   \(H^2\) norm” to “Since unit vectors in \(\operatorname{Ran}P(k)\)
   have uniformly bounded \(H^2\) norms.” The context already makes the
   intended meaning clear, but a linear subspace itself is not bounded.

## Layout

* The title metadata is now present and correct. The PDF has eleven
  pages and the TeX log contains no overfull/underfull warnings.
* References to lemmas, propositions, and the appendix now have the
  correct names.
* The important main-text lemma/proof boundary issues from round 1 are
  gone. Section 3 occupies page 5 coherently; the cone lemma and its
  proof start together on page 6.
* The cone proof crosses from page 6 to page 7 at a natural paragraph
  boundary. Section 5 begins on page 7 with enough content below its
  heading. Display widths, equation numbers, the Pauli matrices, and
  the boxed response formula fit comfortably.
* The sole remaining avoidable boundary is Appendix A.4: its heading
  and short lemma statement are at the bottom of page 10, and the proof
  starts on page 11. Moving the heading and statement to page 11 should
  fit: the current last page has room above its footer for that block.
  A page break or an appropriate needspace before subsection A.4 is
  worth testing. Do not introduce a twelfth page solely for this.
* The bibliography is now integrated into the final page rather than
  occupying an otherwise empty page. It looks balanced.

## Checks of the revision

* The Fubini estimate now bounds
  \(T^{-1}\int_0^T|\sin(t\Delta)|/\Delta^2\,dt\), exactly the quantity
  required for the interchange.
* The basis-invariance caveat correctly distinguishes physical signed
  sums from basis-dependent absolute-value estimates.
* The gradient is explicitly uniformly bounded all the way to the
  punctures; the small-circle argument is consequently complete.
* Reciprocal covariance is stated with the correct unitary and sign:
  \(\tau_K=e^{-iK\cdot x}\) gives
  \(H_{k+K}=\tau_KH_k\tau_K^*\).
* The added Neumann-series identity has the correct order of factors,
  proves analyticity into the graph domain, and avoids any unjustified
  assertion that individual conical eigenvalues are analytic.
* The frame connection, leading velocity, Pauli trace, dominated
  convergence majorant, angular factor, and coefficient are unchanged
  and remain correct.
* Nothing added to the exposition claims a proof that all graphene or
  honeycomb potentials have the assumed band structure. The motivating
  graphene sentence is suitably limited.
* The appended operator statements cover the prerequisites actually
  used in the main text; no claimed pointwise long-time limit or rate
  has been added.

The argument is appropriately focused. I recommend no additional
extensions, rates, physical discussion, or sections.
