# Round-one review: operator foundations

I reviewed the complete manuscript, with special attention to Appendix A and every use of its lemmas. I found no substantive mathematical gap, no incorrect operator-domain assertion, and no need to strengthen (V\in H^1_{\rm per}). The weak temporal-gauge argument, Hilbert–Schmidt localization, and (L^2)-derivative/interpolation argument are all sound. The main proof does not rely on (H^3) propagation or differentiability of (V).

The changes below would improve precision. Line numbers refer to the first manuscript at approximately 11:13 on 3 November.

## Ranked actionable items

### 1. Narrow the eigenbasis-invariance assertion (minor mathematical wording correction)

**Lines 212–215**, immediately after `eq:gap-matrix`, say that *all sums* involving the matrix elements are invariant under changing a basis inside a degenerate eigenspace. The response sums are invariant, but the absolute-value majorant (\sum|z_{nm}|) in `eq:sum-bound` generally is not invariant under a unitary change of a degenerate basis.

Replace with: “The response sums below are invariant under changes of eigenbasis within a degenerate eigenspace, since their weights depend only on the eigenvalues.” Alternatively, make the exact statement about sums of (z_{nm}) over full eigenspaces. All absolute-value estimates remain valid in every basis, so no proof changes are needed.

### 2. Align the shifted resolvents with the chosen evolution generator (clarification, not a gap)

**Lines 707–715**, Lemma `lem:gauge`. The use of (A(t)=1+iK(t)) in Theorem X.70 is correct. Reed–Simon call (A) the generator of (e^{-sA}), and therefore use accretive, rather than dissipative, generators. This is explicit in II, Theorem X.48 and its proof, and in the signs in the proof of X.70. Do not change (1+iK) to (1-iK).

However,

\[
 (1+iK)^{-1}=-i(K-i)^{-1},
\]

while the manuscript displays estimates with (K+i). Those estimates imply the needed ones because ((K+i)(K-i)^{-1}) is unitary, so there is no error. For immediate readability, change the two displayed shifted resolvents in this proof to (K(s)-i), or state the estimates for both signs. It is also useful to write (e^{-r(1+iK)}=e^{-r}e^{-irK}), making the damping and sign transparent in one short clause.

### 3. Give the short resolvent argument for joint graph-norm analyticity (recommended strengthening of exposition)

**Lines 447–452**, Lemma `lem:cone`. The claimed real analyticity of the Riesz projection as a map (\mathscr H\to\mathscr D) is correct. Section XII.2 of RS IV is the right reference, but it mostly formulates one-parameter analyticity with values in bounded operators on the original Hilbert space. A two-line argument would directly establish the slightly stronger, joint two-parameter graph-norm assertion used here.

For (R_0(z)=(H_{k_i}-z)^{-1}\in\mathcal B(\mathscr H,\mathscr D)), write

\[
 (H_{k_i+q}-z)^{-1}
 =R_0(z)\bigl[I+(H_{k_i+q}-H_{k_i})R_0(z)\bigr]^{-1}.
\]

For (z) on a fixed contour around the isolated pair, the inverse exists by a uniform Neumann series for small complex (q). Contour integration proves joint analyticity of (Q(q)) with the asserted target space. The explicit frame `eq:analytic-frame` then proves everything else. This also avoids relying on any one-variable-to-several-variable implication left implicit in the citation.

### 4. State measurability of the fiber propagators (optional completion)

**Lines 689–691 and 717–719**, Lemma `lem:gauge`. The direct integral is legitimate, but its measurability is not explicitly recorded. One sentence suffices: the stepwise propagator construction in X.70 consists of products of measurable fiber groups, and its strong limit is measurable in (k). Its reciprocal-lattice covariance follows from that of (H_k). This is automatic from the construction; no new theorem is needed.

### 5. Remove two accidental commas used as multiplication signs (typesetting)

**`eq:response` and `eq:cesaro`**, approximately lines 422 and 539, contain `\Ree z_{nm}(k),` immediately before the kernel. Replace the comma with `\,` or remove it. The comma does not affect the mathematics but is visibly distracting in the two central formulas.

## Detailed audit results

### Domains and self-adjointness: passed

* Periodicity plus (L^2(\Omega)) gives uniformly local (L^2), exactly the hypothesis of XIII.96 in dimension two.
* Kato–Rellich gives the stated domains and uniform graph equivalence; compact resolvent follows from the compact domain embedding.
* The form estimate is a standard localized two-dimensional (L^4) Sobolev interpolation estimate, valid for (L^2\) potentials. Its use to identify the form domain (H^1) is justified.
* The Faris–Lavine argument checks both hypotheses of X.38, including the comparison core via X.29. It correctly avoids applying the more restrictive global-(L^p) corollary to a periodic potential.
* All initial occupied projectors are uniformly bounded from (L^2) to (H^2). The finitely many enlarged-rank fibers at the Fermi points do not affect the argument.

### Common-domain evolution: passed

* The family (K(t)) is (C^1(\mathscr D,\mathscr H)), with uniformly equivalent graph norms on every compact ((k,t,\varepsilon)) set. Its derivative times the resolvent is uniformly norm continuous.
* These hypotheses imply the two quotient conditions of X.70; the theorem's proof provides the graph-norm bounds claimed in `eq:propagator-graph`.
* Forward and backward construction, followed by uniqueness, yields a unitary propagator after removing damping.
* The direct-integral graph bounds identify the full-space evolution on (H^2(\mathbb R^2)).

### Weak temporal gauge: passed

* The transformed compactly supported test vector is differentiable in (H^2), so there is no hidden position-moment hypothesis.
* The sign in `eq:weak-stark` and the plus sign in the accelerated momentum are correct for the scalar potential (-\varepsilon x\cdot e_\beta).
* Essential self-adjointness extends the integrated weak identity to the full Stark domain. The backward-orbit uniqueness argument is valid; choosing data in (D(H_\varepsilon^2)) gives the requisite graph differentiability.

### Local trace: passed

* The cell-basis proof of `eq:hs-localization` is valid. A basis multiplied by (e^{-ik\cdot x}) is still an orthonormal basis of the fiber (L^2(\Omega)); no boundary condition on a generic (L^2) basis is needed.
* Applying the localization identity to (A^*) proves the equality of left and right localized Hilbert–Schmidt norms.
* The factorization of the localized current is correct because (Q^2=Q), and it establishes trace class before the trace is used.
* Fiber trace norms are uniformly bounded by the rank and the (H^1) bounds, so the trace/sum/integral exchanges are justified.
* The factor ((2\pi)^{-2}) is correct. One obtains (1/(|\Omega||\mathcal B|)), and (|\Omega||\mathcal B|=(2\pi)^2).
* Conjugation by the temporal gauge preserves periodicity and local trace class, and contributes exactly (+\varepsilon t(e_\alpha\cdot e_\beta)) to the current.

### Differentiation of the current: passed

* Duhamel on (H^2) gives a uniform (O(\varepsilon)) difference in (L^2), while common-domain propagation gives a uniform (H^2) bound.
* Interpolation yields an (O(|\varepsilon|^{1/2})) bound in (H^1). The current's quadratic remainder is consequently (O(|\varepsilon|^{3/2})), so the (L^2) derivative suffices.
* The finite number of occupied states and the uniform (H^2) bound give the claimed majorant for differentiating under the Brillouin integral.
* The commutator ([v_\beta,P]) extends to a bounded finite-rank operator with range in (H^1): (v_\beta P) maps into (H^1), and the bounded extension of (Pv_\beta) maps into (\operatorname{Ran}P\subset H^2).
* (e^{-irH_k}) preserves (H^1=D((H_k+c)^{1/2})), so the left current factor in `eq:commutator-response` really is defined. The subsequent absolutely convergent spectral expansion is legitimate.

### Use in the main proof: passed

* The sum estimates control all remote bands without a spectral cutoff.
* Smoothness of the occupied cluster away from the Fermi points is unaffected by internal degeneracies.
* The band-energy Hessian identity uses only the off-diagonal derivative of the Riesz projection; its inverse-gap singularity is integrable.
* Boundedness of the first derivative makes the small-circle boundary terms vanish. No unaccounted distribution concentrated at a crossing remains.
* The rank-two reduction and its frame derivatives take values in (H^2), so all compressed velocity products are well defined. The connection term is of order (|q|), exactly as claimed.

## Citation verification

Every citation in the manuscript is to a real, relevant result in the provided books:

| Manuscript citation | Verified location and content |
|---|---|
| RS I, VI.22(h) | p. 210: trace class if and only if a product of two Hilbert–Schmidt operators |
| RS II, X.12 | pp. 162–163: Kato–Rellich, including preservation of cores |
| RS II, X.29 | pp. 185–186: essential self-adjointness for a nonnegative locally (L^2) part plus a small relative perturbation |
| RS II, X.38 | pp. 198–199: Faris–Lavine with the two hypotheses verified in the manuscript |
| RS II, X.70 | statement pp. 285–286; proof pp. 286–289: common-domain evolution and graph-norm control |
| RS IV, XII.2 | pp. 10–24: regular perturbation theory, resolvent analytic families, Riesz projections and finite-dimensional reduction |
| RS IV, XIII.96 | pp. 302–303: uniformly locally (L^2) potentials in dimension two are infinitesimally (-\Delta)-bounded |
| RS IV, XIII.98 | pp. 304–305: complete measurable Bloch eigenfunction expansion |

The bibliography has the correct book titles, editions and years. My earlier preliminary foundation memo understated the length of the proof of X.70; it continues through p. 289, not p. 287. The manuscript itself gives only the theorem number, so it is unaffected.

