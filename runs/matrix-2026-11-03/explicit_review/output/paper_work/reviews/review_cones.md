# Conical reduction and the universal coefficient

This note records an independent derivation for the manuscript. No online sources were used.

## 1. The response formula to aim for

Let `v_a(k)=(-i∇+k)·a`, let `u_m(k)` be an orthonormal eigenbasis, and write

\[
\Delta_{mn}(k)=\lambda_n(k)-\lambda_m(k),\qquad
Z_{mn}^{ab}(k)=\langle u_m,v_a u_n\rangle\langle u_n,v_bu_m\rangle,
\quad m\leq N<n.
\]

The real-potential, step-field response should be

\[
\sigma_{ab}(t)=\frac{2}{(2\pi)^2}\int_{\mathcal B}
\sum_{m\leq N<n}\Re Z_{mn}^{ab}(k)
\frac{\sin(t\Delta_{mn}(k))}{\Delta_{mn}(k)^2}\,dk.
\tag{1}
\]

The sign here is positive for longitudinal response. Before time-reversal cancellation, the additional summand is
`2 Im Z (1−cos(tΔ))/Δ²`. Indeed, `∂_b P` has unoccupied–occupied matrix element `−(v_b)_{nm}/Δ`, and the response is `−∫_0^t tr(v_a e^{-isH} ∂_bP e^{isH}) ds`.

Complex conjugation relates `k` to `−k`: it reverses each velocity, while the product of the two matrix elements becomes the complex conjugate of `Z`. Thus the imaginary summand integrates to zero on the reciprocal torus. Degeneracies within the occupied or empty sectors do not obstruct this argument: sums over the corresponding eigenspaces are basis independent. No Berry-curvature assumption is needed.

The Cesàro mean of (1) is

\[
\overline\sigma_{ab}(T)=\frac{2}{(2\pi)^2}\int_{\mathcal B}
\sum_{m\leq N<n}\Re Z_{mn}^{ab}(k)
\frac{1-\cos(T\Delta_{mn}(k))}{T\Delta_{mn}(k)^3}\,dk.
\tag{2}
\]

For a diagonal response this kernel is nonnegative. It makes clear that only transitions with gaps of order `T^{-1}` can survive.

## 2. A natural local lemma: geometry of an isotropic crossing

Fix a node `k_*`, put `q=k−k_*`, `r=|q|`, `n=q/r`, and let `v` be its Fermi velocity. The isolated two-band cluster has an analytic rank-two projection `Q(q)`. Choose a local analytic orthonormal frame `U(q): C²→Ran Q(q)` and set

\[
h(q)=U(q)^*H_{k_*+q}U(q)
=\mu_F I+A(q)+O(r^2),\qquad A(q)=q_1A_1+q_2A_2.
\]

All remainders here are uniform in angle. The eigenvalue assumptions imply that `A(q)` has eigenvalues `±v|q|`, for every `q`. Consequently

\[
\operatorname{tr}A_j=0,\qquad A_j^2=v^2I,\qquad
A_1A_2+A_2A_1=0.
\tag{3}
\]

Equivalently, `A(q)` is a massless isotropic two-dimensional Dirac matrix, up to a fixed unitary basis change. This conclusion uses only the stated eigenvalue asymptotics; no assumptions on eigenvectors are missing.

Let `π_±(q)` be the two eigenprojections of `h(q)`, and `Π_±=Uπ_±U*` the actual band projections. Then

\[
\pi_\pm(q)=\tfrac12(I\pm S(n))+O(r),\qquad
S(n)=A(n)/v,\qquad S(n)^2=I.
\tag{4}
\]

Also `∂π_±=O(r^{-1})`, and hence `∂Π_±=O(r^{-1})`. One can see both statements directly by writing a two-by-two Hermitian matrix as its scalar part plus its traceless part and dividing the latter by its positive eigenvalue. Analyticity makes its numerator `A(q)+O(r²)` with bounded first derivative; the denominator is `vr+O(r²)`.

The velocity compressed to the cluster satisfies

\[
W_a(q):=U(q)^*v_a(k_*+q)U(q)=A(a)+O(r).
\tag{5}
\]

The moving frame creates no leading-order correction. In detail, with `C_a=U*∂_aU`,
`∂_ah=W_a+[h,C_a]`; the commutator vanishes at `q=0` because `h(0)=μ_F I`. Continuity/analyticity then gives (5). This avoids the false identity `W_a=∂_ah` away from the node.

Combining (3)–(5), the conical transition weight obeys

\[
\begin{split}
\Delta(q)&=2vr+O(r^2),\\
Z^{ab}(q)&:=\operatorname{tr}\bigl(\Pi_-(q)v_a\Pi_+(q)v_b\bigr)\\
&=v^2\bigl[a\cdot b-(a\cdot n)(b\cdot n)\bigr]+O(r).
\end{split}
\tag{6}
\]

In particular, the leading coefficient is real; `Im Z=O(r)`.

A short proof of the trace identity avoids introducing Pauli notation. From (3),
`tr A(a)A(b)=2v² a·b`, `tr S A(b)=2v n·b`, and
`S A(a) S=2v(a·n)S−A(a)`. Traces of products of three matrices in the two-dimensional span of `A_1,A_2` vanish. Expanding
`(1/4)tr[(I−S)A(a)(I+S)A(b)]` therefore gives the leading expression in (6).

The frame can, if desired, be constructed without appealing to a separate analytic-frame theorem: for a fixed isometry `U_0` onto `Ran Q(0)`, use
`U(q)=Q(q)U_0[U_0*Q(q)U_0]^{-1/2}`. The Riesz projection is analytic into the common operator domain, so (5) is also valid for the unbounded original velocity.

## 3. One scaling argument, with an integrable majorant

There is no need to estimate the difference of two rapidly oscillating cosines or to differentiate the band remainder. Fix a sufficiently small disk `r<δ`, so `c r≤Δ(q)≤C r` and `|Z(q)|≤C`. Its conical contribution to (2) is

\[
I_T=\frac{1}{2\pi^2}\int_0^{2\pi}\int_0^\delta
\Re Z(r,\theta)\frac{1-\cos(T\Delta(r,\theta))}
{T\Delta(r,\theta)^3}\,r\,dr\,d\theta.
\]

Set `s=2vTr`, `b_T(s,θ)=TΔ(s/(2vT),θ)`, and extend the resulting integrand by zero for `s≥2vTδ`. Then

\[
I_T=\frac{1}{8\pi^2v^2}\int_0^{2\pi}\int_0^\infty
\Re Z\bigl(s/(2vT),\theta\bigr)
\frac{s[1-\cos b_T(s,\theta)]}{b_T(s,\theta)^3}
\mathbf1_{s<2vT\delta}\,ds\,d\theta.
\]

For each fixed `s>0`, `b_T→s` and `Z→v²[a·b−(a·n)(b·n)]`. Since `b_T` is uniformly comparable to `s`, the absolute integrand is bounded by

\[
C\min\{1,s^{-2}\},
\]

an integrable function independent of `T` and angle. Dominated convergence yields

\[
\begin{split}
\lim_{T\to\infty}I_T
&=\frac{1}{8\pi^2}
\left(\int_0^{2\pi}[a\cdot b-(a\cdot n)(b\cdot n)]\,d\theta\right)
\left(\int_0^\infty\frac{1-\cos s}{s^2}\,ds\right)\\
&=\frac{1}{8\pi^2}\,(\pi a\cdot b)\,\frac\pi2
=\frac1{16}a\cdot b.
\end{split}
\]

The integral `∫(1−cos s)/s² ds=π/2` has an elementary nonoscillatory evaluation: use `s^{-2}=∫_0^∞t e^{-ts}dt`, Tonelli, and
`∫_0^∞e^{-ts}(1−cos s)ds=1/t−t/(t²+1)`; the result is `∫_0^∞dt/(1+t²)=π/2`. This takes one displayed line and avoids an unnecessary theorem citation or a digression about the Dirichlet integral.

This scaling is a useful centerpiece for the paper. The response probes momenta `r≈(vT)^{-1}`; the two velocity factors and the radial phase-space/energy-gap factors cancel all dependence on `v`.

## 4. Uniform control of all other transitions

Let `P(k)` be the rank-`N` occupied projection away from the nodes. Uniformly on a compact reciprocal cell,

\[
\sum_{m\leq N<n}|Z_{mn}^{ab}(k)|
\leq
\left(\sum_{m\leq N}\|v_a(k)u_m(k)\|^2\right)^{1/2}
\left(\sum_{m\leq N}\|v_b(k)u_m(k)\|^2\right)^{1/2}
\leq C.
\tag{7}
\]

The first inequality is Parseval and Cauchy–Schwarz. The final bound follows from the uniform form bound of the periodic potential and the upper bound `λ_m≤μ_F`; only occupied eigenfunctions are differentiated. Thus there is no need for eigenfunction estimates at high band index or a Weyl-law summation.

Away from fixed small node disks, every occupied–empty gap has a uniform positive lower bound. Within each disk, all transitions except `m=N,n=N+1` have a uniform positive gap, by the external isolation of the rank-two cluster. Hence (7) and `|1−cos|≤2` make the total remainder in (2) `O(T^{-1})`.

This estimate also proves absolute summability of (1) at a fixed time away from the nodes. At a node its only possibly singular summand is bounded by `C_t/r`, since `|sin(tΔ)|≤tΔ`, and is integrable in two dimensions.

## 5. Useful compatibility facts for the response proof

* The occupied projection is `W^{1,p}` locally across every node for `1≤p<2`, since it is bounded and its punctured derivative is `O(r^{-1})`. No distribution supported at the node occurs: the boundary term from a circle of radius `ρ` is `O(ρ)` and tends to zero. This is the exact regularity needed for translation differentiation in `L¹`.
* The sum of the first `N` bands is globally Lipschitz on the reciprocal torus. Its derivative away from nodes is `tr(v_aP)`, so the equilibrium current vanishes after integration. This proof does not require an eigenbasis smooth through internal occupied-band crossings.
* Reciprocal-cell boundaries are best handled by viewing everything on the torus and taking disjoint coordinate disks around nodes. Neither the physical argument nor the constant depends on a symmetric choice of Brillouin cell.
* A rank-two cone at a time-reversal-invariant momentum may be excluded by the real-potential setting, but this fact is unnecessary for the theorem and should not be introduced as an extra assumption or digression.

## 6. Expository recommendation

The main argument can be organized around three semantically complete results: a finite-time interband response formula; the geometry of an isotropic two-band crossing; and the time-averaged concentration calculation. Prove the latter two in the main text, with the response's functional-analytic implementation in an appendix if it is lengthy. Emphasize that (i) time averaging removes uniformly gapped transitions, (ii) the band slopes determine the interband current matrix elements through a two-dimensional Clifford algebra, and (iii) a single scaling integral produces `1/16`. These are the genuine mechanisms; high-band summability is just one Cauchy–Schwarz estimate.
