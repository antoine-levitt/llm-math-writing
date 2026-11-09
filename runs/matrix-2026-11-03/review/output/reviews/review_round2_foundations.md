# Round-two review: operator foundations

**Readiness verdict: mathematically ready.** I re-read the full appendix, the revised Bloch conventions, the occupied-band estimates, the band-energy identity, the two-band reduction, and the uses of these facts in the limit argument. I found no unresolved mathematical gap and no new mistake introduced by the revisions. The theorem follows under the regularity and band assumptions stated in the notes.

## Revisions checked

1. **Evolution generator and resolvents.** The proof now consistently pairs (1+iK(t)) with (K(s)-i). This is the correct sign in Reed–Simon’s accretive-generator convention. Removing the scalar damping yields the stated Schrödinger equation. The added norm-conservation argument, density, and backward construction establish unitarity without presuming it.

2. **Hypotheses of X.70.** The norm-(C^1) family from the fixed graph domain to (L^2), together with uniform graph-norm equivalence, supplies all of X.70’s quotient and diagonal-continuity hypotheses. There is no missing second derivative or stronger regularity requirement. The compact parameter bounds are uniform in (k,t,\varepsilon), exactly as needed for `eq:propagator-graph`.

3. **Measurability and covariance.** The added stepwise-propagator argument legitimizes the direct integral. The reciprocal-lattice identities have the correct sign for (\tau_K=e^{-iK\cdot x}), and covariance passes to the strong limit.

4. **Weak gauge uniqueness.** The explicit orbit (\phi_s=e^{-i(s-t)H_\varepsilon}\phi) has the correct sign. For (\phi\in D(H_\varepsilon^2)), it is differentiable in the graph domain, so the extended weak identity gives the stated constant scalar product. The endpoint identity and density prove the gauge formula. No position moments are assumed at any point.

5. **Riesz projection in the graph norm.** The new Neumann formula has the correct operator order. Its rightmost inverse is analytic on the fiber Hilbert space, while (R_0(z)) takes values in (H^2). Uniformity on the compact contour proves the precise joint analyticity needed for the frame and the compressed velocities. The real-analytic inverse square root in `eq:analytic-frame` is legitimate because its matrix argument is positive and close to the identity for real (q).

6. **Local traces.** The hypothesis on (Q(k):\mathscr H\to H^1_{\rm per}) is now explicit. The Hilbert–Schmidt factorization, cell-basis calculation, and normalized trace formula remain correct. The subsequent gauge conjugation establishes the current trace for arbitrary fixed finite field and time.

7. **Current differentiation.** The (L^2) Duhamel derivative, uniform (H^2) bounds, interpolation, and (O(|\varepsilon|^{3/2})) quadratic remainder still close the argument. The proof explicitly excludes the finitely many enlarged-rank fibers when choosing occupied vectors. All domination claims used for the Brillouin integral are valid.

8. **Eigenbasis invariance.** The revised sentence correctly separates invariant response/sum-rule formulas from basis-dependent absolute-value majorants. The estimates hold for every measurable eigenbasis, which is all the proof needs.

9. **Main-proof dependencies.** The sum-rule proof only uses smoothness of an isolated occupied cluster, not of individual possibly degenerate occupied bands. Its boundary terms vanish by the uniform gradient bound. The response series and its time average have the stated integrable majorants. The rescaled conical integral is justified by dominated convergence and gives the coefficient (1/16) with the displayed normalization.

## Citation check

The citations verified in round one remain accurate. The newly added use of RS IV, Theorem XIII.97, for the periodic direct-integral decomposition is correct. The current-fiber identity also follows directly by differentiating the Bloch transform on a core, as the manuscript says. No new external result has been introduced without adequate justification.

## Two optional wording refinements

These do not affect mathematical readiness and do not call for another proof revision.

* **Around lines 843–845:** replace “its commutator with each lattice translation is a scalar phase” with “it commutes with each lattice translation up to a scalar phase.” The existing phrase is naturally understood as a group commutator; the replacement avoids confusion with the additive operator commutator used elsewhere in the paper.
* **Around line 877:** replace “Since (\operatorname{Ran}P(k)) has a uniformly bounded (H^2) norm” with “Since the occupied unit vectors under consideration have uniformly bounded (H^2) norms.” This makes the already valid estimate literal; an entire nonzero linear range is of course unbounded.

No further operator-theoretic changes are needed.

