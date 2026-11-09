# Independent review: linear response and Cesàro limit

The theorem has the expected coefficient and sign under the stated hypotheses. The two indispensable structural steps are the integrated sum rule (which cancels the term linear in time) and time reversal (which cancels the imaginary, antisymmetric response). Isotropic eigenvalue expansions suffice for the matrix-element asymptotics; eigenvectors need not be assumed separately.

Throughout, use the physical normalization

\[
 c_{\mathrm B}=(2\pi)^{-2},\qquad
 \underline{\operatorname{Tr}} A=c_{\mathrm B}\int_{\mathcal B}\operatorname{Tr} A(k)\,dk.
\]

Let \(P(k)=\mathbf1_{(-\infty,\mu_F]}(H_k)\), with its value at the finitely many nodes ignored. It has rank \(N\) almost everywhere. Write \(v_\eta(k)=(p+k)\cdot e_\eta\). For eigenvectors \(u_n(k)\), set

\[
 \Delta_{mn}=\lambda_m-\lambda_n>0,\qquad
 a_{nm}^{\alpha\beta}=\langle u_n,v_\alpha u_m\rangle
 \langle u_m,v_\beta u_n\rangle,\qquad n\leq N<m.
\]

All expressions summed over a degenerate eigenspace are independent of the eigenbasis. In particular, crossings internal to the occupied or unoccupied spectrum cause no difficulty.

## 1. Uniform summability

Uniform graph bounds for the occupied eigenfunctions give

\[
 \sup_k\sum_{n\leq N}\|v_\eta(k)u_n(k)\|^2<\infty,
 \qquad \sup_k\sum_{n\leq N<m}|a_{nm}^{\alpha\beta}(k)|<\infty.
\]

The second assertion is Cauchy–Schwarz and Parseval, with the sum over \(m>N\) bounded by the sum over all \(m\). On the complement of small node disks all interband gaps are bounded below. In a node disk the only small gap is \(n=N,m=N+1\), and it is comparable to the distance \(r\) from the node. All other gaps admit a common positive lower bound. Consequently

\[
 \sum_{n\leq N<m}\frac{|a_{nm}|}{\Delta_{mn}}
 \leq C(1+r^{-1})
\]

near a node, hence is integrable in two dimensions. This bound justifies the sum rule and fixed-time response manipulations below.

## 2. Acceleration gauge and the sign of the response

Set \(\psi(t)=e^{i\varepsilon t x\cdot e_\beta}u(t)\). Then

\[
 i\partial_tu=\left[\tfrac12(p+\varepsilon t e_\beta)^2+V\right]u.
\]

The fiber propagator \(U_k^\varepsilon(t)\) therefore solves

\[
 i\partial_tU_k^\varepsilon(t)=H_{k+\varepsilon t e_\beta}U_k^\varepsilon(t),
 \qquad U_k^\varepsilon(0)=I.
\]

The physical current is

\[
 j_\varepsilon(t)=c_{\mathrm B}\int_{\mathcal B}
 \operatorname{Tr}\!\left[(v_\alpha(k)+\varepsilon t e_\alpha\cdot e_\beta)
 U_k^\varepsilon(t)P(k)U_k^\varepsilon(t)^*\right]dk.
\]

Time reversal, or integration of the band-energy gradient, gives \(j_0(t)=0\).
Differentiating the propagator at fixed \(t\) yields

\[
 \sigma_{\alpha\beta}(t)=c_{\mathrm B}\int_{\mathcal B}\left[
 Nt\,e_\alpha\cdot e_\beta
 -i\int_0^t s\operatorname{Tr}\left(v_\alpha e^{-i(t-s)H_k}
 [v_\beta,P]e^{i(t-s)H_k}\right)ds\right]dk.
\]

This sign corresponds to the potential \(-\varepsilon x\cdot e_\beta\) and the current \(+p\cdot e_\alpha\) in the notes.
The commutator trace has the absolutely convergent expansion

\[
 \sum_{n\leq N<m}\left(a_{nm}e^{-iu\Delta_{mn}}
 -\overline{a_{nm}}e^{iu\Delta_{mn}}\right)
 =2i\sum_{n\leq N<m}\left(\operatorname{Im}a_{nm}\cos(u\Delta_{mn})
 -\operatorname{Re}a_{nm}\sin(u\Delta_{mn})\right),
 \quad u=t-s.
\]

Since

\[
 \int_0^t(t-u)\sin(u\Delta)du=\frac t\Delta-\frac{\sin(t\Delta)}{\Delta^2},
 \qquad
 \int_0^t(t-u)\cos(u\Delta)du=\frac{1-\cos(t\Delta)}{\Delta^2},
\]

the response before cancellation is

\[
 \sigma_{\alpha\beta}(t)=c_{\mathrm B}\int_{\mathcal B}\left[
 Nt\,e_\alpha\cdot e_\beta
 -2\sum_{n\leq N<m}\operatorname{Re}a_{nm}
 \left(\frac t{\Delta_{mn}}-\frac{\sin(t\Delta_{mn})}{\Delta_{mn}^2}\right)
 +2\sum_{n\leq N<m}\operatorname{Im}a_{nm}
 \frac{1-\cos(t\Delta_{mn})}{\Delta_{mn}^2}\right]dk.
\]

For analytic foundations, it is sufficient to differentiate \(U_k^\varepsilon(t)u_n\) in \(L^2\), uniformly in \(k,n\leq N\), and to have uniform \(H^2\) bounds for these vectors. Interpolation then gives \(\|U^\varepsilon u_n-U^0u_n\|_{H^1}=O(\sqrt\varepsilon)\), and

\[
 \langle\psi_\varepsilon,v_\alpha\psi_\varepsilon\rangle
 -\langle\psi_0,v_\alpha\psi_0\rangle
 =2\operatorname{Re}\langle v_\alpha\psi_0,\psi_\varepsilon-\psi_0\rangle
 +\langle\psi_\varepsilon-\psi_0,v_\alpha(\psi_\varepsilon-\psi_0)\rangle.
\]

The last term is \(O(\varepsilon^{3/2})\). Thus differentiability in the full graph norm is not necessary, and no derivative of the singular Fermi projector in \(k\) is needed for fixed-time linear response.

## 3. Integrated sum rule, including conical singularities

On the punctured Brillouin torus let

\[
 E(k)=\operatorname{Tr}(H_kP(k))=\sum_{n=1}^N\lambda_n(k).
\]

Although individual occupied bands can cross, \(E\) and \(P\) are smooth wherever the Fermi gap is open. Riesz projection differentiation gives

\[
 \partial_\alpha\partial_\beta E
 =N e_\alpha\cdot e_\beta
 -2\sum_{n\leq N<m}\frac{\operatorname{Re}a_{nm}^{\alpha\beta}}{\Delta_{mn}}.
\]

The first derivative \(\partial_\beta E=\operatorname{Tr}(Pv_\beta)\) is uniformly bounded. The displayed Hessian is integrable, by the gap bounds in Section 1. Integrate over the torus minus disks of radius \(\rho\); the only boundary integrals are bounded by \(C\rho\), so vanish as \(\rho\downarrow0\). Hence

\[
 N|\mathcal B| e_\alpha\cdot e_\beta
 =2\int_{\mathcal B}\sum_{n\leq N<m}
 \frac{\operatorname{Re}a_{nm}^{\alpha\beta}}{\Delta_{mn}}\,dk.
\]

There is no point-supported term in this second derivative: bounded first derivatives and a vanishing boundary length exclude it. Substitution cancels the entire secular term.

## 4. Time reversal is essential for the clean symmetric formula

Complex conjugation \(C\) obeys

\[
 CH_kC=H_{-k},\qquad Cv_\eta(k)C=-v_\eta(-k).
\]

Thus, choosing paired eigenbases, \(\Delta_{mn}(-k)=\Delta_{mn}(k)\) and
\(a_{nm}^{\alpha\beta}(-k)=\overline{a_{nm}^{\alpha\beta}(k)}\). Reciprocal-lattice covariance makes this an involution of the torus. The imaginary contribution integrates to zero for every fixed \(t\); its absolute integrability at fixed \(t\) follows already from \(1-\cos(t\Delta)\leq t^2\Delta^2/2\), so no stronger local estimate is required at this step. Therefore

\[
 \boxed{\displaystyle
 \sigma_{\alpha\beta}(t)=\frac2{(2\pi)^2}\int_{\mathcal B}
 \sum_{n\leq N<m}\operatorname{Re}a_{nm}^{\alpha\beta}(k)
 \frac{\sin(t\Delta_{mn}(k))}{\Delta_{mn}(k)^2}\,dk.}
\]

If the manuscript writes this real formula before invoking time reversal, it should explicitly state the omitted imaginary term and its cancellation. Individual \(a_{nm}\) are not generally real.

## 5. Local cone matrix elements

An analytic frame for the isolated rank-two spectral cluster gives a Hermitian matrix

\[
 h(q)=\mu_FI+q_1A_1+q_2A_2+O(|q|^2).
\]

The assumed eigenvalue expansions imply that \(A_1,A_2\) are traceless,
\(A_1^2=A_2^2=v^2I\), and \(A_1A_2+A_2A_1=0\). Up to a fixed unitary they are \(v\sigma_1,v\sigma_2\). The compressed physical velocities are \(A_\eta+O(r)\); the frame connection affects them only at order \(r\), since \(h(0)\) is scalar. For \(\omega=q/r\),

\[
 \Delta(q)=2vr+O(r^2),\qquad
 \operatorname{Re}a_{N,N+1}^{\alpha\beta}(q)
 =v^2\left[e_\alpha\cdot e_\beta
 -(e_\alpha\cdot\omega)(e_\beta\cdot\omega)\right]+O(r).
\]

The estimates are uniform in \(\omega\). The leading imaginary part is zero because both velocity vectors and the Bloch-sphere direction lie in the same plane; indeed \(\operatorname{Im}a=O(r)\). This latter observation is useful but not needed once time reversal has already cancelled the global imaginary response.

## 6. Cesàro scaling: a short dominated-convergence proof

Integrating the boxed formula in time gives

\[
 \overline\sigma_{\alpha\beta}(T)
 =\frac2{(2\pi)^2}\int_{\mathcal B}\sum_{n\leq N<m}
 \operatorname{Re}a_{nm}^{\alpha\beta}
 \frac{1-\cos(T\Delta_{mn})}{T\Delta_{mn}^3}\,dk.
\]

All terms other than the active two-band transitions in node disks are \(O(T^{-1})\), by the uniform summability and the uniform positive gap. In one node disk use \(q=r\omega\) and then \(s=Tr\). The integral becomes

\[
 \frac2{(2\pi)^2}\int_{S^1}\int_0^{T\delta}
 s\,b(s\omega/T)\,
 \frac{1-\cos\bigl(T\Delta(s\omega/T)\bigr)}
 {\bigl(T\Delta(s\omega/T)\bigr)^3}\,ds\,d\omega,
 \quad b=\operatorname{Re}a_{N,N+1}.
\]

Because \(cr\leq\Delta(r\omega)\leq Cr\) and \(|b|\leq C\), its absolute value is bounded by a constant times \(\min\{1,s^{-2}\}\), uniformly in \(T\) and \(\omega\), after extending the integrand by zero past \(T\delta\). Dominated convergence gives

\[
 \frac2{(2\pi)^2}\int_{S^1}v^2 f_{\alpha\beta}(\omega)\,d\omega
 \int_0^\infty\frac{1-\cos(2vs)}{8v^3s^2}\,ds,
 \quad f_{\alpha\beta}=e_\alpha\cdot e_\beta
 -(e_\alpha\cdot\omega)(e_\beta\cdot\omega).
\]

Now

\[
 \int_{S^1}f_{\alpha\beta}\,d\omega=\pi e_\alpha\cdot e_\beta,
 \qquad \int_0^\infty\frac{1-\cos(2vs)}{s^2}\,ds=\pi v.
\]

Their product gives exactly \((e_\alpha\cdot e_\beta)/16\) per node. This argument avoids differentiating the eigenvalue remainder, changing radial variables to the gap, or estimating oscillatory error terms. The limiting kernel has an absolutely integrable majorant because of Cesàro averaging.

The elementary integral follows, for example, by integration by parts and the Dirichlet integral. For a fully self-contained proof of the latter, introduce \(e^{-\eta s}\), differentiate the resulting sine integral with respect to frequency to get \(\arctan(a/\eta)\), then pass \(\eta\downarrow0\). Equivalently, Plancherel applied to the indicator of an interval evaluates the nonnegative cosine integral directly.

## Items a final rigorous manuscript must not hide

1. The trace per unit area has factor \((2\pi)^{-2}\), not merely \(|\mathcal B|^{-1}\).
2. \(P(k_i)\) has rank \(N+1\), but these fibers form a null set and are irrelevant.
3. The acceleration gauge produces \(+\varepsilon t e_\beta\), hence a positive diamagnetic current.
4. The time-dependent propagator needs a domain/energy argument; a formal Duhamel expansion alone is insufficient for the unbounded current.
5. The Hessian sum rule is on a punctured torus, with vanishing small-circle boundary terms.
6. Complex matrix elements can generate an imaginary/Hall term before time reversal is used.
7. All remote-band estimates should sum over infinitely many \(m\), using the uniform current-norm bound.
8. The theorem asserts an iterated, Cesàro limit. No exchange with the weak-field limit or ordinary long-time limit has been justified or is needed.

