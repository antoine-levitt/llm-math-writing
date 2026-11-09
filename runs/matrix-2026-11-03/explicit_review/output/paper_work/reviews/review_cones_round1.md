# Review of `dirac_conductivity.tex`, first full draft

## Verdict

The conical reduction and the long-time limit are correct, including all constants. I found no counterexample under the stated hypotheses and no missing eigenvector, symmetry, or nondegeneracy assumption. The finite-time formula has the correct sign and the correct factor of two. The manuscript is already coherent and readable: its major steps correspond to genuine mathematical mechanisms, and the universal coefficient receives the emphasis it deserves.

I recommend acceptance after a small editing pass. There is no major mathematical revision to request from my review.

## Detailed mathematical checks

1. **Assumptions match the notes.** The band gap, isolation of the touching pair, isotropic first-order splitting, real potential, and order of limits are all retained. The statement that the `O(|q|²)` remainder is uniform in direction merely spells out the usual meaning of the original multivariable asymptotic; it does not add an assumption. The choice `N≥1` is implicit in the original band setting.

2. **No hidden choice of eigenvectors.** The local rank-two Riesz projection is isolated by the external gaps. The displayed frame is well defined and analytic into `H²`, since its Gram matrix is positive and invertible near the crossing. Formula (3.3) for the limiting rank-one projections follows from the exact two-by-two spectral-projection formula already proved in Section 2. Individual eigenvectors are used only inside basis-invariant sums.

3. **Eigenvalues really determine the needed matrix algebra.** For fixed direction `ω`, `(h(rω)−μI)/r→A(ω)` in matrix norm, so its eigenvalues converge to `±v`. Hence `tr A=0` and `A(q)²=v²|q|²I`; polarization gives the Clifford relation. There is no unnoticed tilt term. The argument works for an arbitrary fixed embedding of the two linear matrices in the traceless Hermitian two-by-two matrices; no spatial rotation or special Pauli basis is assumed.

4. **The moving frame is handled correctly.** The physical velocity is generally not exactly `∂h`, but the frame-derivative terms vanish at the scalar matrix `h(0)=μI`. The proof differentiates only at that point and then invokes analyticity. Thus (3.4) is valid and includes the possible connection correction in its `O(r)` error.

5. **The trace calculation is sound.** In the convention of the paper, `tr(P_- v_α P_+ v_β)` is precisely `Z_{N,N+1}`. The real part of `tr(RA(a)A(b))` is `v² a·b` by the anticommutator, and rank one gives `tr(RA(a)RA(b))=tr(RA(a))tr(RA(b))`. The resulting tangential weight and sign are correct.

6. **Uniformly gapped transitions vanish collectively.** The one Cauchy–Schwarz/Parseval bound controls the entire infinite unoccupied-band sum. External isolation gives a common positive lower bound on all nonconical occupied–empty gaps near a node, and compactness provides the bound away from nodes. Their total is therefore genuinely `O(T^{-1})`; this is not merely termwise convergence.

7. **The rescaling and domination are exact.** With `s=2vTr`, the factor is `1/(8π²v²)`, as printed. The numerator is bounded by both `D_T²/2` and `2`; using `D_T∼s` gives `C min(1,s^{-2})`. Extending by zero causes no problem for pointwise convergence. The majorant is integrable uniformly in angle, so dominated convergence is justified without differentiating the band remainder or estimating oscillatory phase errors.

8. **The constant is correct.** The angular integral is `π e_α·e_β`, the radial integral is `π/2`, and `(8π²)^{-1}×π×π/2=1/16`. The Laplace/Tonelli evaluation is valid because the underlying integrand is nonnegative. The absence of a spin factor and the interpretation of `M` are stated accurately.

9. **The response/time-reversal reduction is consistent.** With conjugate-linear-first inner products, the response before time reversal contains `Re Z sin(tΔ)+Im Z(1−cos(tΔ))`, exactly as printed. Complex conjugation reverses each velocity and conjugates their product, so the imaginary contribution cancels on the reciprocal torus without choosing a symmetric cell.

10. **The weak derivative across each point is legitimate.** The punctured derivative is `O(r^{-1})` and the integration-by-parts boundary term is `O(r)`, also in the weighted trace norm. Thus there is no omitted node-supported derivative or corresponding extra response term.

I also checked the stated uses of Reed–Simon X.38 and X.70 against the locally extracted texts. The Faris–Lavine hypotheses described in the appendix match the actual theorem (including its auxiliary-operator hypothesis), and the common-domain evolution citation supports the graph-norm propagation used here.

## Minor changes recommended

1. **Avoid using `C` simultaneously as a named transition-weight function and as a generic constant.** In Section 4.2, `C(q)=Re Z` is introduced immediately before `cr≤Δ≤Cr`, and `C` then appears as the generic domination constant. This is a small but unnecessary working-memory cost. Rename the transition weight to `F(q)` throughout that subsection, retaining `C` for bounds.

2. **Qualify the radial/tangential interpretation.** At the end of Section 3, write “To leading order, the radial velocity shifts the energy within a band, while the tangential velocity couples the two bands.” The present sentence is correct for the limiting Dirac matrix but could be read as an exact statement about the full Bloch Hamiltonian.

3. **Match the scope of the trace criterion to its proof.** Before (2.2), say “a bounded periodic operator with integrable fiber trace norm.” The appendix proves exactly that assertion, and all operators to which the paper applies it are bounded. This avoids raising a domain question about an arbitrary unbounded direct-integral operator whose fibers merely have integrable trace norms.

4. **Remove a slightly defensive aside if tightening prose.** After (4.7), the sentence “no estimate of differences of rapidly oscillating phases is needed” explains a rejected proof method more than the result. The preceding statement that quadratic corrections do not contribute is the useful mathematical content. A tighter replacement is: “Thus only the linearized cone contributes to the limit.” This is optional; the present version is not misleading.

5. **Optional precision in the abstract.** “Momenta of size `1/T`” is correct up to a node-dependent fixed constant, but “momenta on the inverse-time scale around each crossing” reads more naturally without suppressing the velocity in a dimensional-looking formula. The detailed introduction already gives the precise scale `(v_iT)^{-1}`.

## Readability assessment

The manuscript avoids the user's principal failure modes. The regularity proposition has a coherent semantic purpose and supplies both the integrable singularity and the absence of a point term. The conical lemma addresses the exact conceptual gap between eigenvalue hypotheses and current matrix elements. The proof strategy is announced before the details, and the final scaling calculation is not hidden among estimates.

The two-by-two trace computation is especially effective: it is short, basis independent, and avoids adding Pauli-matrix notation solely for one calculation. The main proof and appendix are appropriately separated. I would not undertake a large reorganization at this stage; it would risk losing the current logical flow without a clear gain.
