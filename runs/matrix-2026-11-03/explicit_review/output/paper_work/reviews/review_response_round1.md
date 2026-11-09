# Mathematical review of Section 2 and Appendix A

## Verdict

The finite-time response proof is complete at the usual research-paper level. I found no missing hypothesis, wrong sign, normalization error, unjustified interchange of limits, or substantive gap in the unbounded-current argument. The revised transport approach is materially clearer and shorter than a proof that separately introduces and cancels a diamagnetic term.

There are two literal precision issues worth correcting, followed by a few small additions that would make the most delicate passages easier to audit. None requires changing the argument or adding another lemma.

Line numbers below refer to the draft reviewed before further edits.

## Corrections worth making

### 1. Restrict the blanket covariance claim (line 689)

“The same covariance holds for all the operator fields used above” is too broad: the fixed auxiliary weight \(\Lambda=1-\Delta_{\mathrm{per}}\) does not satisfy that covariance, and neither does \(\Lambda P(k)\Lambda\) with precisely the same conjugating unitary. The physical fields \(P,v_\alpha,U_\varepsilon\) do satisfy it.

Suggested replacement:

> The projections, velocities, and characteristic propagators obey the same covariance. Multiplication by \(e^{-iK\cdot x}\) preserves \(H^2_{\mathrm{per}}\), so the weighted estimates remain valid on every bounded enlargement of a cell. We use this covariant extension when translating momentum across a cell boundary.

This also cleanly explains why the fixed-weight translation assertion in (A.8) is legitimate. It is not necessary to pretend that the fixed-weight field is literally periodic in a single global trivialization.

### 2. Qualify uniformity of the occupied range (line 721)

“The occupied projection has uniformly bounded range in \(H^2\)” is intended on bounded momentum sets. It is false if read uniformly for all \(k\in\mathbb R^2\), because reciprocal translations conjugate by growing plane-wave frequencies.

Suggested replacement:

> On every bounded momentum set, the occupied projection has uniformly bounded range in \(H^2\).

For any fixed \(\varepsilon\) and finite time interval, the characteristic momenta lie in such a bounded set, so the subsequent assertion remains correct exactly as intended.

## Small additions that improve auditability

### 3. Expose the cancellation behind the exact source identity (lines 307–315)

The existing derivation is mathematically adequate, but the cancellation is central enough to deserve one displayed differentiation. Put \(k_s=k-\varepsilon(t-s)e_\beta\), suppress the propagator arguments for that line, and write

\[
\frac{d}{ds}\bigl(U_\varepsilon(t,s;k)P(k_s)U_\varepsilon(t,s;k)^*\bigr)
=U_\varepsilon(t,s;k)
 \bigl(\varepsilon\partial_\beta P(k_s)+i[H_{k_s},P(k_s)]\bigr)
 U_\varepsilon(t,s;k)^*
=\varepsilon U_\varepsilon(t,s;k)(\partial_\beta P)(k_s)U_\varepsilon(t,s;k)^*.
\]

The current text can be replaced by this rather than supplemented with a paragraph. It immediately verifies the minus sign in the integrated identity and makes the mechanism visible.

If this is too wide, state the commutator cancellation in prose and display only the first and last expressions. The identity initially holds in trace norm; the weighted estimates make its right side admissible for the current. No further regularity of the field-evolved density is being presumed.

### 4. Add one sentence about the Stark unitary group (lines 707–716)

The group assertion is correct. A reader may nevertheless wonder why a time-dependent fiber propagator produces a group. Suggested addition:

> Concatenating the momentum characteristics gives the group law, and strong continuity follows from that of the propagators and momentum translations.

Then say that differentiating at \(t=0\) on the transformed core yields \(-iH_k-\varepsilon\partial_\beta\), so its self-adjoint generator extends \(H_k-i\varepsilon\partial_\beta\). This is slightly more precise than saying that the generator “is” that expression before its domain is identified. Essential self-adjointness then gives the claimed identification.

One can implicitly extend the characteristic construction to negative times here, or explicitly add “for \(t\in\mathbb R\).” The common-domain theorem applies on every bounded time interval, so there is no obstacle.

### 5. Eigenbasis measurability (lines 336–337)

“Choose a measurable orthonormal eigenbasis; no smooth choice is needed” is a slightly safer formulation than “at each momentum ... no smooth or global choice is needed.” Measurable eigenbases exist for this compact-resolvent family, as also discussed in Reed–Simon IV, Theorem XIII.98 and its proof. Alternatively, the present basis-independent sums are measurable through spectral projections, so this is a precision improvement, not a gap.

### 6. Optional qualification of the main Bloch trace statement (line 195)

Appendix A correctly states and proves the trace identity for a **bounded** periodic operator with integrable fiber trace norm, which is exactly what is used. Add “bounded” to its first statement in Section 2 for perfect agreement. A more general unbounded version can be phrased through forms, but the paper needs no such extension.

## Checks performed

### Occupied-space regularity

The frame formula is correct: \((QW_0)^*(QW_0)=W_0^*QW_0\), and the inverse square root is real analytic near the identity. Riesz projections are analytic from \(L^2\) into the common \(H^2\) domain. Consequently the frame columns and their derivatives are genuinely \(H^2\)-valued, as required for the bilateral weight.

The estimate \(\partial_\beta\pi_-=O(|q|^{-1})\) follows from analytic \(b\), \(b(0)=0\), and \(d\asymp|q|\); the conical assumptions are enough. The bounded weighted projection and the \(O(\rho)\) puncture boundaries establish the weak derivative without any point mass. Internal degeneracies below the Fermi energy cause no issue because the whole occupied cluster is projected at once.

### Exact transport and differentiation

The Bloch transform sends \(x\cdot e_\beta\) to \(i\partial_\beta\), hence the transport sign is positive. The characteristic starts at \(k-\varepsilon te_\beta\), and differentiating backward propagator endpoints gives the source formula with its stated negative sign.

Weighted \(W^{1,1}\) gives absolute continuity on almost every line in the field direction. The derivative of the conjugated finite-rank projection is legitimate in trace norm because all its factors lie in the common operator domain. Its commutator cancels before integration.

The approximation estimates in Appendix A.3 are sufficient and correctly ordered. Duhamel provides \(O(\varepsilon)\) as \(H^2\to L^2\); graph bounds and interpolation provide \(O(\sqrt\varepsilon)\) as \(H^2\to H^1\). Factoring \(A=\Lambda^{-1}B\Lambda^{-1}\) controls both sides of the unbounded-current expression. In the second factor, the adjoint of the Duhamel estimate gives \(\|\Lambda^{-1}(U_\varepsilon^*-U_0^*)\|=O(\varepsilon)\), so the displayed trace-norm estimate follows. This avoids the common but invalid inference that ordinary trace-norm convergence alone controls an unbounded velocity.

The momentum translation convergence is in the correct bilateral weighted norm. Applying it to shifts with length at most \(\varepsilon t\) is uniform in the time integration variable by ordinary \(L^1\) translation continuity.

### Local trace class and normalization

The zero-extension computation is correct and is cleaner than a polar-decomposition proof. The integral is a trace-class Bochner integral; its prefactor is \(|\mathcal B|^{-1}\). Dividing by \(|\Omega|\) gives exactly \((2\pi)^{-2}\).

The same argument also controls cross-cell compressions: they differ by a scalar Bloch phase. A bounded spatial set meets finitely many standard lattice cells, so finite sums prove local trace class. The final use concerns a bounded periodic current operator; uniform finite-rank \(H^2\) bounds indeed give boundedness and uniformly bounded fiber trace norms.

### Response, symmetry, and infinite sums

The matrix element of \(\partial_\beta P\) has the displayed minus sign. With the stated conjugate-linear-first inner product, the imaginary term in the unsymmetrized response has **plus** sign, exactly as written. The real response has the factor \(2/(2\pi)^2\).

Time reversal conjugates the product of the two velocity matrix elements and leaves the gap unchanged. The integrated imaginary term therefore vanishes; the same symmetry gives zero equilibrium current. Degenerate eigenspaces cause no ambiguity after summation.

The Cauchy–Schwarz estimate is correct even with infinitely many empty bands and uses only the finitely many occupied velocity norms. The \(t/\Delta\) bound is locally integrable because the smallest gap is linear in the distance to a cone in two dimensions. The imaginary term is bounded by \(t^2/2\). These estimates justify spectral expansion, the time integral, symmetry cancellation, and later averaging over each bounded time interval.

### Self-adjointness and citations

I checked Reed–Simon IV, Theorems XIII.96, XIII.97, and XIII.99 in the local extracted volume. XIII.96 is exactly the uniformly local \(L^2\), relative-bound-zero statement used here in dimension two. The two Bloch references are appropriate after the elementary fixed-domain gauge change displayed in the paper. Section XII.2 is a suitable reference for analytic perturbation.

The Kato–Rellich, Faris–Lavine, and common-domain evolution references in volume II are correctly numbered and correctly applied. The proof checks the oscillator core hypothesis for Faris–Lavine rather than misapplying its global-\(L^p\) corollary to a periodic potential. The field-transport group construction avoids unjustified differentiation of a position-dependent gauge on states without known position moments.

## Exposition

The structure is effective: regularity of the occupied space, transport, then spectral transitions. The appendix carries the right technical burden, and its interpolation estimate explains why the spatial weights were needed. There is little unnecessary repetition.

The only central mechanism currently compressed into a phrase is the commutator cancellation in the exact source identity. Recommendation 3 would improve both readability and mathematical transparency. The broad covariance sentence is the only wording that risks an actual incorrect reading. Beyond those adjustments, I would not expand Section 2 or the appendix further: more elementary detail would obscure the proof's scale separation.
