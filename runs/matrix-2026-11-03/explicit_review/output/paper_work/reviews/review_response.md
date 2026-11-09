# Finite-time response and operator foundations

The transport proof is sound and is preferable to an acceleration-gauge proof with an explicit diamagnetic term. It packages the cancellation correctly and avoids a separate effective-mass sum rule. The essential facts and all signs/constants are below.

## 1. Bloch normalization and the local current

Use

\[
(\mathcal U f)(k,x)=\sum_{R\in\mathcal R}e^{-ik\cdot(x+R)}f(x+R),
\quad x\in\Omega,
\]

with direct-integral measure \(dk/|\mathcal B|\). Then \(H\) has fibers \(H_k\), momentum has fibers \(v_\alpha(k)=(-i\nabla+k)\cdot e_\alpha\), and multiplication by \(x\cdot e_\beta\) becomes \(i\partial_\beta\). The boundary identification is
\(A(k+K)=e^{-iKx}A(k)e^{iKx}\).

For a periodic operator with \(\int_\mathcal B\|A(k)\|_1\,dk<\infty\), its cell localization is trace class and

\[
\underline{\operatorname{Tr}}A
=\frac1{(2\pi)^2}\int_\mathcal B\operatorname{Tr}A(k)\,dk.
\]

This deserves a short proof or an explicit statement. For positive \(A\), extend an orthonormal basis of \(L^2(\Omega)\) by zero to the plane and apply Parseval; multiplication by \(e^{-ikx}\) takes that basis to another orthonormal basis. For general \(A\), use its periodic polar decomposition and factor the localization into two Hilbert--Schmidt operators. Thus integrable fiber trace norm suffices, and the factor is \((|\Omega||\mathcal B|)^{-1}=(2\pi)^{-2}\).

This applies to current fibers \(v_\alpha\rho\): the density has rank \(N\) a.e., its range has uniformly bounded \(H^2\) norm on finite time intervals, and
\(\|v_\alpha\rho\|_1\le\sqrt N(\operatorname{Tr}\rho v_\alpha^2\rho)^{1/2}\).

## 2. The occupied projection has exactly the Sobolev regularity needed

Write \(P(k)=\mathbf1_{(-\infty,\mu_F]}(H_k)\), with arbitrary values at the finitely many touching points. Its rank is \(N\) almost everywhere; the extra state selected by the closed interval at a touching point is immaterial to the direct integral.

Let \(Q=1-\Delta\) on the periodic cell. Analytic finite-band frames in \(H^2\) give, locally on the Brillouin torus,

\[
\|QP(k)Q\|_1\le C,
\qquad
\|Q(\partial_\beta P)(k)Q\|_1
\le C\bigl(1+\sum_i|k-k_i|^{-1}\bigr).
\]

Near a touching, split off the smooth projection onto bands below the two-band cluster, choose a smooth orthonormal frame of that cluster, and use the lower spectral projection of its two-by-two matrix. Its gap is bounded below by \(c|k-k_i|\), hence its first derivatives are \(O(1/|k-k_i|)\). All frame vectors and their derivatives have bounded \(H^2\) norm. This proves the displayed estimate in the bilateral weight, not just operator norm.

The right side is integrable in dimension two. Integration by parts on the torus with radius-\(r\) disks deleted produces boundary terms bounded by \(Cr\), so there is no point-supported part in the weak derivative. Thus \(P\) is \(W^{1,1}\) in this weighted trace norm. The usual reciprocal-lattice covariance is harmless: use finitely many Bloch charts or a bounded enlargement of one cell. In particular, translations of \(Q(\partial_\beta P)Q\) are continuous in \(L^1\), with the covariance understood at cell boundaries.

## 3. Evolution along characteristics

Fix final \((t,k)\). Let \(W_\varepsilon(t,s;k)\) be the propagator from time \(s\) to \(t\) for

\[
r\longmapsto H_{k-\varepsilon(t-r)e_\beta}.
\]

The physical density has fibers

\[
\rho_\varepsilon(k,t)
=W_\varepsilon(t,0;k)P(k-\varepsilon te_\beta)
 W_\varepsilon(t,0;k)^*.
\]

Equivalently, it solves \(\partial_t\rho+\varepsilon\partial_\beta\rho=-i[H_k,\rho]\). This is why the transport sign is positive: \(H_\varepsilon\) transforms to \(H_k-i\varepsilon\partial_\beta\).

For almost every characteristic, \(s\mapsto P(k-\varepsilon(t-s)e_\beta)\) is absolutely continuous. Differentiate its conjugation by \(W_\varepsilon(t,s;k)\). The commutator vanishes because the instantaneous projection commutes with the instantaneous Hamiltonian. Integration gives the **exact** identity

\[
\frac{\rho_\varepsilon(k,t)-P(k)}{\varepsilon}
=-\int_0^t W_\varepsilon(t,s;k)
 (\partial_\beta P)(k-\varepsilon(t-s)e_\beta)
 W_\varepsilon(t,s;k)^*\,ds.
\tag{A}
\]

It is enough to derive this first in ordinary trace norm. The right side has integrable bilateral weighted trace norm, so the identity also legitimizes the current trace.

For bounded \(k,t\), common-domain evolution gives

\[
\|QW_\varepsilon(t,s;k)Q^{-1}\|\le C_t.
\]

Duhamel's formula, using \(H_{k+h}-H_k=h\cdot(-i\nabla+k)+|h|^2/2\), gives

\[
\|(W_\varepsilon(t,s;k)-e^{-i(t-s)H_k})Q^{-1}\|
\le C_t\varepsilon.
\]

Interpolation between \(L^2\) and \(H^2\) gives the stronger estimate needed for an unbounded current:

\[
\|v_\alpha(k)(W_\varepsilon(t,s;k)-e^{-i(t-s)H_k})Q^{-1}\|
\le C_t\sqrt\varepsilon.
\]

These estimates, plus weighted \(L^1\) translation continuity from Section 2, justify taking the current trace and sending \(\varepsilon\downarrow0\) in (A). Concretely, for \(A=Q^{-1}BQ^{-1}\), current traces of propagated \(A\) are bounded by \(C_t\|B\|_1\); changing the propagator changes the trace by \(C_t\sqrt\varepsilon\|B\|_1\). This is a clean way to avoid an unsupported claim that trace-norm convergence alone controls an unbounded velocity.

Consequently

\[
\sigma_{\alpha\beta}(t)
=-\frac1{(2\pi)^2}\int_\mathcal B\int_0^t
\operatorname{Tr}\bigl(v_\alpha(k)e^{-isH_k}(\partial_\beta P)(k)e^{isH_k}\bigr)
\,ds\,dk.
\tag{B}
\]

This is the derivative of \(j_\varepsilon(t)-j_0\). Real \(V\) gives \(j_0=0\), so it is exactly the limit in the problem.

## 4. Exact interband formula, including its imaginary part

Choose an orthonormal eigenbasis at almost every \(k\). For \(n\le N<m\), put

\[
\omega_{mn}=\lambda_m-\lambda_n>0,
\qquad
c_{nm}=\langle u_n,v_\alpha u_m\rangle
          \langle u_m,v_\beta u_n\rangle.
\]

Differentiating \(P^2=P\) and \([H,P]=0\) yields

\[
\langle u_m,(\partial_\beta P)u_n\rangle
=-\frac{\langle u_m,v_\beta u_n\rangle}{\omega_{mn}},
\]

and no occupied--occupied or empty--empty block. Inserting this in (B) gives

\[
\sigma_{\alpha\beta}(t)
=\frac{2}{(2\pi)^2}\int_\mathcal B
\sum_{n\le N<m}
\frac{\operatorname{Re}c_{nm}\sin(t\omega_{mn})
 +\operatorname{Im}c_{nm}[1-\cos(t\omega_{mn})]}{\omega_{mn}^2}\,dk.
\tag{C}
\]

The sign of the imaginary term is **plus** with this definition of \(c\). Its sign will not affect the final theorem because it cancels under time reversal, but it should still be correct.

Complex conjugation gives \(CH_kC=H_{-k}\), \(Cv_\alpha(k)C=-v_\alpha(-k)\). Thus energies are even, \(c(-k)=\overline{c(k)}\) after paired eigenbasis choices, and the sum of imaginary terms integrates to zero. This is basis independent even at internal band degeneracies because one sums entire eigenspaces. The same symmetry gives \(j_0=0\). Therefore

\[
\boxed{\displaystyle
\sigma_{\alpha\beta}(t)
=\frac{2}{(2\pi)^2}\int_\mathcal B
\sum_{n\le N<m}\operatorname{Re}c_{nm}
\frac{\sin(t\omega_{mn})}{\omega_{mn}^2}\,dk.}
\tag{D}
\]

The finite-time expression includes the usual diamagnetic cancellation automatically. No separate effective-mass identity is needed.

## 5. Absolute convergence and the gapped transitions

Uniform \(H^2\) control of occupied states and Cauchy--Schwarz give

\[
\sum_{n\le N<m}|c_{nm}(k)|
\le
\Big(\sum_{n\le N}\|v_\alpha u_n\|^2\Big)^{1/2}
\Big(\sum_{n\le N}\|v_\beta u_n\|^2\Big)^{1/2}
\le C.
\]

For fixed \(t\), \(|\sin(t\omega)|/\omega^2\le t/\omega\), and the smallest occupied--empty gap is bounded below by \(c|k-k_i|\) near a touching. Thus (D) is absolutely integrable. The full expression (C) is also absolutely integrable, since \((1-\cos(t\omega))/\omega^2\le t^2/2\).

After averaging,

\[
\frac1T\int_0^T\sigma_{\alpha\beta}(t)\,dt
=\frac2{(2\pi)^2}\int_\mathcal B\sum_{n\le N<m}
\operatorname{Re}c_{nm}
\frac{1-\cos(T\omega_{mn})}{T\omega_{mn}^3}\,dk.
\tag{E}
\]

All transitions except the pair \((N,N+1)\) in small touching neighborhoods have a uniform positive gap. The displayed uniform summability shows their contribution is \(O(T^{-1})\), with no need to estimate the high bands individually.

## 6. Self-adjointness and verified Reed--Simon references

I extracted the local volume II to `analysis_text/rs2.txt`; no online sources were used. The following numbers and pages have been checked against that text:

* **RS II, Theorem X.12**, pp. 162--163: Kato--Rellich, including essential self-adjointness on every core of the unperturbed operator.
* **RS II, Theorem X.38**, pp. 198--199: Faris--Lavine. It applies to \(-\Delta+V_1+W\) if \(V_1\ge-c|x|^2-d\), \(V_1\in L^2_{\mathrm{loc}}\), the oscillator-shifted operator is essentially self-adjoint on an invariant core, and \(-a\Delta+W\) is bounded below for some \(a<1\).
* **RS II, Theorem X.70**, pp. 285--289: common-domain nonautonomous evolution. Its hypotheses are easily checked here because \(k\mapsto H_k\) is polynomial as a map \(H^2\to L^2\), its graph norms are uniformly equivalent on compact \(k\)-sets, and after a common scalar shift the inverses are uniformly bounded. The proof supplies bounded propagation in the common graph norm. Use the theorem, rather than the narrower three-dimensional potential statement in X.71.

For completeness: periodic \(V\in H^1_{\rm per}\) is uniformly locally \(L^2\). A fixed-cell Sobolev interpolation inequality, summed over translates, gives

\[
\|Vu\|_2\le\delta\|\Delta u\|_2+C_\delta\|u\|_2,
\qquad
\int|V||u|^2\le\delta\|\nabla u\|_2^2+C_\delta\|u\|_2^2.
\]

These establish the asserted fiber domains and graph norms. They also verify Faris--Lavine for \(2H_\varepsilon=-\Delta+V_1+W\), with \(V_1=-2\varepsilon x\cdot e_\beta\), \(W=2V\), and core \(C_c^\infty\). The oscillator-shifted operator is essentially self-adjoint by Kato--Rellich, since both the linear term and the periodic potential are infinitesimally bounded relative to a harmonic oscillator. The latter assertion follows from the first estimate and the standard identity controlling \(\Delta u\) by \((-\Delta+|x|^2)u\) plus \(\|u\|\).

Do **not** apply the first corollary to X.38 verbatim: it assumes a global \(L^p\) perturbation, whereas a nonzero periodic potential is not globally \(L^p\). Apply the theorem itself with the preceding uniform local estimates.

Finally, identify the characteristic propagator with the given Stark group by applying the Bloch transform to the weak Schrödinger equation on \(C_c^\infty\). The constructed evolution solves that equation, and essential self-adjointness gives uniqueness. Equivalently, the gauge transformation \(e^{i\varepsilon tx\cdot e_\beta}\) yields the common-domain Hamiltonian \(\frac12(p+\varepsilon te_\beta)^2+V\). If differentiating this gauge strongly, one must justify propagation of first moments; using weak equations avoids that extra detour.

## 7. Points to preserve in the final manuscript

1. Explain that the field transports quasimomentum before writing the density equation. This gives a human reason for \(\partial_\beta P\).
2. Put the graph-weighted norm technicality in an appendix or one tightly written justification; it is necessary but not the central mechanism.
3. Keep the exact response formula and the time-reversal cancellation adjacent. An unexplained real part would conceal the Hall term.
4. Explicitly state absolute summability of all interband transitions. It dispatches the infinitely many remote bands in one line.
5. The proof should not suggest the Fermi projection is smooth at a touching. Its integrable derivative, rather than smoothness, is exactly the two-dimensional advantage.
