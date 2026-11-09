# Round-one referee review: response, sum rule, and limiting argument

I checked the complete first manuscript, including the analytic appendix, independently against the derivation in `review_response.md`. I also checked the locally extracted Reed–Simon statements X.29, X.38, X.70, XIII.96, and XIII.98. The theorem's sign, normalization, and coefficient are correct. I found no blocking mathematical defect and no need to strengthen the hypotheses. The following revisions would remove several small but real imprecisions and make the argument more publication-ready.

Line numbers below refer to the first complete version of `graphene_conductivity.tex` (899 lines).

## Priority 1: correct two mathematical presentation issues

### 1. The universal basis-invariance assertion is literally false

**Location:** lines 212–215, following `eq:gap-matrix`.

The sentence “All sums in which these quantities occur are invariant under changes of eigenbasis within a degenerate eigenspace” is too strong. The physical sums, with factors depending only on the eigenvalues and with `z`, `Re z`, or `Im z` summed linearly, are invariant. The auxiliary absolute-value sum in `eq:sum-bound`, however, need not be invariant. For a two-dimensional degenerate unoccupied space, choose current-coordinate vectors `(1,0)` and `(0,1)`: the sum of the absolute coordinate products is zero in that basis and one after a forty-five-degree rotation.

**Recommended replacement:** “The response sums below are independent of the eigenbasis within a degenerate eigenspace; the estimates involving absolute values hold for every such choice.” The same clarification applies to the sum-rule expression. There is no defect in any estimate, only in the unrestricted wording.

### 2. Give the absolute-integrability bound needed for Fubini

**Location:** lines 542–543, following `eq:cesaro`.

The stated inequality bounds the already integrated kernel `(1-cos(T Delta))/(T Delta^3)`. Taken by itself, that is not the absolute-integrability bound needed to interchange the time integral with a conditionally signed sine integrand. Earlier estimates in the paper do provide exactly what is needed, so this is easily repaired.

**Recommended replacement:** cite `eq:inverse-gap-integrable` and write

\[
 \frac1T\int_0^T\frac{|\sin(t\Delta)|}{\Delta^2}\,dt
 \leq\frac{T}{2\Delta}.
\]

This explicitly proves absolute integrability in `(t,k,n,m)` before applying Fubini.

## Priority 2: two conspicuous formula typos

**Locations:** `eq:response` (approximately line 423) and `eq:cesaro` (line 539).

Both formulas have a literal comma after `\Ree z_{nm}(k)` where multiplication is intended:

```tex
\Ree z_{nm}(k),
\frac{...}{...}
```

Replace the comma with `\,`. The surrounding equations are otherwise correct.

## Priority 3: short improvements to the analytic explanations

### 3. Spell out why the propagator is unitary after removing damping

**Location:** lines 709–713, proof of `lem:gauge`.

The use of X.70 with `1+iK(t)` and subsequent removal of scalar damping is valid. However, applying the construction in both time directions gives invertibility; unitarity additionally uses norm conservation. Since damping has been removed, the contraction estimate from X.70 alone should not be read as the proof of norm conservation.

**Suggested sentence:** “For initial data in the common domain, self-adjointness of `K(t)` gives `d ||U(t,s)f||^2/dt=0`; density and the backward construction then give unitarity.” This is a concise way to make the implication complete.

### 4. Make the Bloch diagonalization explicit once

**Location:** lines 175–189.

The normalization is derived carefully, but the transform's intertwining identities are left implicit. A short sentence saying that `U H U^{-1}` and `U J_alpha U^{-1}` have fibers `H_k` and `v_alpha(k)`, respectively, would connect the defined transform to the subsequent evolution without relying on a reader to supply this step. XIII.97 is a suitable reference if desired; the identities also follow directly on a core.

### 5. Clarify two harmless uniformity phrases

* **Lines 387–390:** change “the gradient is uniformly bounded away from the punctures” to “the gradient is bounded on the punctured torus, uniformly up to the punctures.” The existing proof establishes the stronger statement, which is what the shrinking-circle argument uses.
* **Lines 766–768:** “whose ranges are uniformly bounded in `H^1`” should mean that `Q(k):L^2→H^1` has a uniform operator bound. The ranges themselves are vector spaces and therefore unbounded. State the operator bound or refer to normalized vectors in the ranges.

One can also say “for almost every `k`” when beginning the differentiation lemma, to maintain the already correct convention that the rank at the exact node fibers is irrelevant. This is optional, since lines 197–200 have already declared that convention.

## Checks that passed

### Signs and matrix-element conventions

The gauge has the correct sign: `e^{-itH_epsilon}=e^{+i epsilon t x_beta}U_epsilon`, so the current contains the positive scalar term `epsilon t alpha·beta`. With scalar products linear in their second argument, the commutator trace is exactly

\[
 \sum(z e^{-ir\Delta}-\bar z e^{ir\Delta}),
\]

and multiplication by `-i` yields the raw response printed in `eq:raw-response`, including the positive imaginary term. The current expansion in the appendix is also consistent with the declared scalar-product convention.

The integrated sum rule cancels the complete `t` term. The remaining response is symmetric after time reversal: `Delta(-k)=Delta(k)` and `z(-k)=conj z(k)`. The manuscript correctly avoids assuming each individual `z` is real.

### Trace normalization and trace class

The transform with measure `dk/|B|` is unitary. The local Hilbert–Schmidt identity gives `1/|B|`, and division by `|Omega|` gives exactly `(2pi)^{-2}`. The factorization of the localized current as a product of two Hilbert–Schmidt operators is valid even though `J Q` is not self-adjoint. The fiber trace norms are integrable, which justifies exchanging the cell-basis sum and the Bloch integral.

### Fixed-time differentiation

The common-domain Duhamel formula gives an `L^2` derivative, and the uniform `H^2` bound plus interpolation gives the `H^1` control needed for the quadratic current remainder. The `O(epsilon^{3/2})` estimate is correct and supplies a uniform majorant in `k`. The range of `[v_beta,P]` is indeed in `H^1`: `v_beta P` has that range because `P` maps into `H^2`, while `P v_beta` has its finite-dimensional range in `H^2`. Autonomous evolution preserves the form domain, so the trace in the commutator response is well defined.

The gauge identification through weak solutions correctly avoids assuming any position moment of the initial state. The Faris–Lavine application uses the full theorem, rather than its unsuitable globally `L^p` corollary, and both hypotheses are verified.

### Occupied degeneracies and conical punctures

The Riesz projection remains smooth through all degeneracies internal to the occupied spectrum. Differentiating `[H,P]=0` produces only occupied-to-unoccupied denominators. The inverse-gap sum has an integrable `1/r` bound at each cone, and `Tr(Pv_beta)` supplies a uniform gradient bound independently of any differentiated eigenvalue remainder. The boundary integrals on circles of radius `rho` are `O(rho)`, so no point-supported term is lost. This is a complete and economical justification of the sum rule.

### Cone reduction and long-time coefficient

The analytic frame is valid into the common domain; the connection identity `partial h=B+[h,A]` has the correct sign. Since `h(0)=mu I`, the connection affects the physical velocity only at order `r`. The Pauli trace identity gives exactly the claimed angular factor, with no missing factor of two.

In the Cesàro scaling `s=Tr`, the Jacobian and powers of `T` cancel correctly. The limiting integrand has coefficient `f/(4v)`, the scalar integral is `pi v`, and the angular integral is `pi alpha·beta`. Multiplication by `(2pi)^{-2}` gives `alpha·beta/16` per crossing. The majorant `C min(1,s^{-2})` is valid uniformly in angle and time. All other infinitely many transitions are `O(T^{-1})` because their gaps are uniformly positive and their current products are absolutely summable.

The Tonelli/Laplace-transform evaluation of the scalar integral is particularly clean and completely self-contained.

## Expository assessment

The main argument is well organized. Separating the raw response, the two cancellations, the cone matrix element, and the scaling calculation makes each logical dependency visible. The appendix is long enough to be credible but does not interrupt the main proof. The treatment of complex matrix elements, node fibers, and internal degeneracies prevents the most common hidden assumptions.

I would keep the present architecture and make the targeted corrections above rather than expand the main proof. An optional one-sentence physical explanation is that Cesàro averaging suppresses every uniformly gapped transition, leaving only momenta within distance of order `T^{-1}` of the conical crossings. The actual scaling computation already shows this precisely. No claim about an ordinary long-time limit, exchange of limits, or finite-field conductivity should be added.

