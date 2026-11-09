# Round 1 referee report: cone analysis and exposition

I read the complete current manuscript, graphene_conductivity.tex, including
the appendix, and checked the cone calculation independently against the
displayed formulas. I also inspected the extracted PDF text. I did not edit
the manuscript.

The local reduction and the Cesaro limit are mathematically sound. In
particular, the moving-frame commutator has the correct sign, the Pauli
trace matches the stated convention for the scalar product, the rescaling
contains the correct powers of \(T\), and the final constant is \(1/16\).
The theorem faithfully retains the hypotheses and order of limits in the
notes. I found the following actionable issues.

## Required corrections

1. **Correct the mathematical punctuation in the two central formulas.**
   In eq:response and eq:cesaro (approximately source lines 422 and 539),
   a literal comma follows \(\operatorname{Re}z_{nm}(k)\). It should be
   multiplication spacing, i.e. a LaTeX thin-space command. The comma is
   especially conspicuous because the response formula is boxed.

2. **The Fubini justification should bound the absolute time integral.**
   The sentence immediately following eq:cesaro currently bounds the
   already-integrated signed kernel
   \((1-\cos(T\Delta))/(T\Delta^3)\). That proves integrability of the final
   expression, but by itself it does not justify exchanging the time
   integral with the signed band/momentum integrals. Replace the displayed
   bound in that sentence by
   \[
     \frac1T\int_0^T
        \frac{|\sin(t\Delta)|}{\Delta^2}\,dt
       \leq \frac{T}{2\Delta}.
   \]
   Together with eq:inverse-gap-integrable this directly proves Fubini's
   hypothesis. The earlier uniform fixed-time estimates already contain
   this argument, so this is a local repair rather than a proof problem.

3. **Narrow the claim of eigenbasis invariance.**
   The sentence following eq:gap-matrix says that all sums involving the
   quantities are invariant under changes of basis in a degenerate
   eigenspace. This is false for the absolute-value sums in
   eq:sum-bound and eq:inverse-gap-integrable. For instance, two vectors
   \(a=(1,0)\), \(b=(0,1)\) have
   \(\sum_m|a_m b_m|=0\), whereas a \(45^\circ\) simultaneous basis
   rotation makes the sum equal to \(1\).

   The physically used signed sums, with a weight depending only on the
   transition energies, are invariant. Suggested replacement:

   > The response formulas below are independent of the choice of basis
   > within a degenerate eigenspace; the estimates hold for every such
   > choice.

## Recommended clarifications

4. **Make the gradient bound at the punctures unambiguous.**
   In the sum-rule proof, “\(\nabla_k E\) is uniformly bounded away from
   the punctures” can mean merely bounded on subsets separated from the
   nodes, which is not enough for the shrinking-circle argument. The
   cited occupied-state estimate proves the stronger statement actually
   needed. Write “\(\nabla_k E\) is uniformly bounded on the punctured
   torus, including as \(k\) approaches a crossing.” This makes the
   \(O(\rho)\) boundary estimate immediate.

5. **Give reciprocal covariance explicitly once.**
   Periodicity of band energies and invariant traces is used in the
   sum rule and the time-reversal cancellation. Although standard, one
   displayed identity would make those uses self-contained:
   \[
     H_{k+K}=\tau_K H_k\tau_K^*,\qquad
     v_\eta(k+K)=\tau_K v_\eta(k)\tau_K^*,\qquad
     \tau_Ku(x)=e^{-iK\cdot x}u(x).
   \]
   It would fit naturally after the Bloch transform or the definition of
   the fiber velocities. This is optional if brevity is preferred, but
   it would substantiate the later reference to covariance.

## Editorial refinements worth considering

6. **Connect the motivating model to the title/intro.**
   The word “graphene” does not occur anywhere in the manuscript. The
   general theorem justifies the general title, and the two-crossing
   sentence already gives the relevant normalization. A brief addition
   there could explain the motivation without asserting that an
   unspecified honeycomb potential satisfies the hypotheses:

   > The two-crossing case is the spinless graphene band structure
   > motivating the result.

   This is optional; do not add claims of existence or universality for
   all graphene potentials, which the paper does not establish.

7. **The proof roadmap slightly obscures its own order.**
   The introduction says first “derive a convergent interband formula,”
   then cancel linear growth. That can mean either the raw formula or
   the boxed final formula. Calling the first object “the fixed-time
   response formula” would remove the ambiguity.

8. **Keep the current level of detail in the cone proof.**
   The explicit frame and the connection term are useful and should not
   be shortened to an unsupported assertion that velocities are
   derivatives of \(h\). Conversely, no quantitative convergence rate,
   Berry-curvature digression, or anisotropic extension is needed for
   this manuscript. The existing short DCT proof is the right length.

## Details checked successfully

* From \(h=aI+d\cdot\sigma\), the energy hypotheses imply
  \(a=\mu_{\rm F}+O(r^2)\), \(d=Lq+O(r^2)\), and \(L^*L=v^2I\).
  Differentiation of these remainders is justified by the analytic
  functions \(a,d\), not by differentiating the original band estimates.
* The frame identity is
  \(\partial_\eta h=B_\eta+[h,A_\eta]\), so
  \(B_\eta=(Le_\eta)\cdot\sigma+O(r)\). The scalar leading term vanishes
  because the specified cones have no linear tilt.
* The trace in eq:matrix-trace is the product defining \(z_{N,N+1}\)
  with the correct order of \(\alpha,\beta\).
* \(n(r\omega)=L\omega/v+O(r)\) is uniform in \(\omega\), so the cone
  matrix-element estimate is uniform and follows without an additional
  eigenvector assumption.
* After \(r=s/T\), the factor in eq:scaled-integral is exactly
  \(2b_i((s/T)\omega)s(1-\cos D_T)/D_T^3\).
* For \(s\leq1\), use \(1-\cos D_T\leq D_T^2/2\) and \(D_T\geq cs\);
  for \(s\geq1\), use \(1-\cos D_T\leq2\). This proves the asserted
  uniform majorant \(C\min(1,s^{-2})\).
* The radial integral is \(\pi v_i\), the angular integral is
  \(\pi e_\alpha\cdot e_\beta\), and the Bloch factor is
  \((2\pi)^{-2}\). The result is exactly \(1/16\) per crossing.
* Remote transitions contribute \(O(T^{-1})\) by their positive gap and
  the absolute band-sum bound; no stationary-phase assumptions enter.
* The sum-rule proof is not circular: bounded velocity expectations and
  the already established inverse-gap integrability suffice before the
  conical eigenvector lemma is proved.
* Time reversal is invoked before separating any potentially singular
  static antisymmetric term, so no extra local imaginary-part estimate
  is required.

After corrections 1–3, and preferably clarification 4, the sections I
audited would be ready for a second-round check. The analytic appendix
should also receive the independent operator-theoretic review already
planned.
