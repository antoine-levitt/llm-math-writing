# Independent review: conical reduction and the universal constant

The theorem in graphene_statement.tex is consistent. Its eigenvalue
assumptions imply the leading interband matrix elements needed for \(M/16\);
a separate Bloch eigenvector hypothesis is unnecessary. The real-valuedness
of \(V\) cancels the imaginary, antisymmetric response. No online sources
were used.

## 1. Analytic two-band frame

Fix one node, put \(q=k-k_i\), \(r=|q|\), and write \(v=v_i\). A fixed contour
around \(\mu_{\mathrm F}\), enclosing only the double eigenvalue at \(q=0\),
defines the analytic rank-two Riesz projection \(Q(q)\) for all small \(q\).
It is analytic as an operator into \(H^2_{\rm per}\), since the fibers have
a common domain and depend polynomially on \(q\). Choose an isometry
\(U_0:\mathbb C^2\to\operatorname{Ran}Q(0)\), and set

\[
 U(q)=Q(q)U_0\bigl(U_0^*Q(q)U_0\bigr)^{-1/2}.
\]

The inverse square root exists near zero and is real analytic. Thus \(U(q)\)
is an analytic orthonormal frame for \(\operatorname{Ran}Q(q)\), with values
in \(H^2_{\rm per}\). Its reduced Hamiltonian is the Hermitian matrix

\[
 h(q)=U(q)^*H_{k_i+q}U(q)=a(q)I+d(q)\cdot\sigma,
 \qquad d(q)\in\mathbb R^3.
\]

Its eigenvalues are \(a(q)\pm|d(q)|\). The hypotheses imply

\[
 a(q)=\mu_{\mathrm F}+O(r^2),\qquad
 d(q)=Lq+O(r^2),\qquad L^*L=v^2I_{\mathbb R^2}.
\]

Indeed, the first assertion follows by adding the eigenvalue expansions.
Analyticity gives \(d=Lq+O(r^2)\); comparison along each ray with
\(|d(q)|=vr+O(r^2)\) gives \(|L\omega|=v\) for every unit \(\omega\).
This is exactly \(L^*L=v^2I\). Derivative estimates for the remainders now
follow from analyticity, without differentiating the original eigenvalue
remainder.

## 2. Physical velocities and a basis-independent matrix element

For a direction \(e\), write

\[
 B_e(q)=U(q)^*(\partial_eH_{k_i+q})U(q),\qquad
 A_e(q)=U(q)^*\partial_eU(q).
\]

Differentiation of \(h=U^*HU\), using \(HU=Uh\), gives

\[
 \partial_e h=B_e+[h,A_e],\qquad
 B_e(q)=(Le)\cdot\sigma+O(r).
\]

The connection term is \(O(r)\) because \(h(0)=\mu_{\mathrm F}I\).
Physical velocities are therefore not literally derivatives of the
reduced matrix in a moving frame, but their leading terms coincide.

Let \(n(q)=d(q)/|d(q)|\), and \(\pi_\pm(q)=(I\pm n(q)\cdot\sigma)/2\).
The active physical spectral projectors are \(P_\pm=U\pi_\pm U^*\). The
following trace is independent of all choices of eigenvectors and frame:

\[
 z_{\alpha\beta}(q)
   =\operatorname{Tr}\bigl(P_-(q)(\partial_\alpha H)
       P_+(q)(\partial_\beta H)\bigr)
   =\operatorname{tr}_{\mathbb C^2}
       \bigl(\pi_-B_\alpha\pi_+B_\beta\bigr).
\]

The Pauli identity, for \(a,b,n\in\mathbb R^3\) with \(|n|=1\), is

\[
 \operatorname{tr}\bigl(\pi_-(a\cdot\sigma)
             \pi_+(b\cdot\sigma)\bigr)
 =a\cdot b-(a\cdot n)(b\cdot n)-i\,n\cdot(a\times b).
\]

Consequently, uniformly for \(q=r\omega\),

\[
 \begin{split}
 \operatorname{Re}z_{\alpha\beta}(r\omega)
 &=v^2f_{\alpha\beta}(\omega)+O(r),\\
 \operatorname{Im}z_{\alpha\beta}(r\omega)&=O(r),\\
 f_{\alpha\beta}(\omega)
 &=e_\alpha\cdot e_\beta
       -(e_\alpha\cdot\omega)(e_\beta\cdot\omega).
 \end{split}
\]

The leading imaginary part vanishes because \(L\omega,Le_\alpha,Le_\beta\)
all belong to the same plane in \(\mathbb R^3\). In particular,

\[
 \int_0^{2\pi}f_{\alpha\beta}(\omega(\theta))\,d\theta
   =\pi e_\alpha\cdot e_\beta.
\]

## 3. Short dominated-convergence proof of the cone limit

Set \(\Delta(q)=\lambda_{N+1}(k_i+q)-\lambda_N(k_i+q)=2|d(q)|\).
For small fixed \(\delta>0\), \(c r\leq\Delta(r\omega)\leq Cr\).
Consider the symmetric Cesaro contribution

\[
 I_T=\frac1{(2\pi)^2}\int_{|q|<\delta}
 \frac{2\operatorname{Re}z_{\alpha\beta}(q)}{T\Delta(q)^3}
 \bigl(1-\cos(T\Delta(q))\bigr)\,dq .
\]

Make the exact substitution \(r=s/T\), and define
\(D_T(s,\omega)=T\Delta((s/T)\omega)\). Then

\[
 I_T=\frac1{(2\pi)^2}\int_0^{2\pi}\int_0^\infty
 {\bf1}_{s<\delta T}\,
 \frac{2\operatorname{Re}z_{\alpha\beta}((s/T)\omega)\,s}
      {D_T(s,\omega)^3}
       (1-\cos D_T(s,\omega))\,ds\,d\theta .
\]

Since \(cs\leq D_T\leq Cs\), the absolute value of this integrand is at
most \(C\min(1,s^{-2})\), an integrable majorant independent of \(T,\theta\).
For every \(s>0\), it converges to

\[
 \frac{f_{\alpha\beta}(\omega)}{4v}
       \frac{1-\cos(2vs)}{s^2}.
\]

Dominated convergence, the angular identity above, and
\(\int_0^\infty(1-\cos s)s^{-2}\,ds=\pi/2\) give

\[
 \lim_{T\to\infty}I_T
 =\frac1{(2\pi)^2}\frac\pi4
         \int_0^{2\pi}f_{\alpha\beta}(\omega)\,d\theta
 =\frac1{16}e_\alpha\cdot e_\beta .
\]

A short self-contained proof of the scalar integral uses
\(s^{-2}=\int_0^\infty y e^{-ys}\,dy\). Tonelli, applied to the nonnegative
integrand, gives

\[
 \int_0^\infty\frac{1-\cos s}{s^2}\,ds
 =\int_0^\infty y\left(\frac1y-\frac{y}{y^2+1}\right)\,dy
 =\int_0^\infty\frac{dy}{1+y^2}=\frac\pi2.
\]

This scaling proof neither differentiates the gap nor replaces an
oscillatory phase by an asymptotic expansion at fixed \(r\).

## 4. Other transitions and antisymmetric response

Outside the active pair in sufficiently small node disks, all occupied to
unoccupied gaps have a uniform positive lower bound. The sum over all
unoccupied states is absolutely controlled by

\[
 \sum_{n\le N,m>N}|z_{nm}^{\alpha\beta}(k)|
 \le\left(\sum_{n\le N}\|v_\alpha(k)u_n(k)\|^2\right)^{1/2}
      \left(\sum_{n\le N}\|v_\beta(k)u_n(k)\|^2\right)^{1/2}.
\]

The right side is uniformly finite on a compact Brillouin zone. Thus the
remaining symmetric Cesaro contribution is \(O(T^{-1})\). No stationary
phase theorem, regularity of remote individual bands, or restriction on
critical energies is required.

For imaginary terms, real-\(V\) time reversal gives an exact cancellation:
complex conjugation maps \(H_k\) to \(H_{-k}\) and \(v_\alpha(k)\) to
\(-v_\alpha(-k)\). Transition gaps are even and the corresponding summed
imaginary matrix elements are odd. Their Brillouin-zone integrals vanish.
The active static quantity \(\operatorname{Im}z/\Delta^2=O(1/r)\) is locally
integrable, so even a formula separated into static and oscillatory
imaginary terms remains legitimate. For finite times one can cancel
before separation, using the bounded cosine kernel.

## 5. Local bounds for the f-sum/Drude cancellation

Let \(P(k)={\bf1}_{(-\infty,\mu_{\rm F}]}(H_k)\) away from the nodes and
\(E(k)=\sum_{n\le N}\lambda_n(k)\), extended continuously to the nodes.
Near the chosen node, let \(P_{<}(q)\) be the analytic rank-\(N-1\)
projection onto all lower bands. Then

\[
 P(k_i+q)=P_{<}(q)+U(q)\pi_-(q)U(q)^*,\qquad
 E(k_i+q)=S(q)+a(q)-|d(q)|,
\]

where \(S(q)=\operatorname{Tr}(H_{k_i+q}P_{<}(q))\) is analytic. These
identities hold also for \(N=1\), with \(P_{<}=0\) and \(S=0\).

Because \(d=Lq+O(r^2)\) and \(|d|\geq cr\),

\[
 |\partial_e |d||\leq C,\quad
 |\partial_e\partial_f |d||\leq C/r,\quad
 \|\partial_e n\|\leq C/r,\quad
 \|\partial_e\partial_f n\|\leq C/r^2 .
\]

Therefore, uniformly near the node,

\[
 |\nabla E|\leq C,\qquad |D^2E|\leq C/r,\qquad
 \|\partial_eP\|_{\mathcal B(L^2,H^2)}\leq C/r .
\]

The projector bound follows from the displayed frame formula and bounded
derivatives of \(U\) into \(H^2\). The energy bounds show that \(E\) is
locally Lipschitz and its classical Hessian is integrable on the punctured
disk. To show it is the distributional Hessian, delete radius-\(\eta\)
disks and integrate by parts: boundary terms involving bounded \(\nabla E\)
are \(O(\eta)\) and vanish. Hence \(E\in W^{2,1}\) on the Brillouin torus,
with no point masses in its Hessian, and

\[
 \int_{\mathcal B}\partial_\alpha\partial_\beta E(k)\,dk=0.
\]

On the punctured torus the second derivative identity is

\[
 \partial_\alpha\partial_\beta E
 =N e_\alpha\cdot e_\beta
   -2\sum_{n\le N,m>N}
        \frac{\operatorname{Re}z_{nm}^{\alpha\beta}}
             {\lambda_m-\lambda_n}.
\]

It follows by differentiating
\(\partial_\alpha E=\operatorname{Tr}(P v_\alpha)\):
\(\partial_\beta v_\alpha=e_\alpha\cdot e_\beta\), while the
occupied-unoccupied block of \(\partial_\beta P\) is
\(-\langle u_m,v_\beta u_n\rangle/(\lambda_m-\lambda_n)\).
Internal degeneracies in the occupied cluster do not affect this
projector identity. Its active term is \(O(1/r)\); all others are bounded
after summation. This justifies cancellation of the apparent time-linear
term in the temporal-gauge response.

## 6. Optional quantitative refinement

If a convergence rate is wanted, use the exact variable
\(\rho=\Delta(r\omega)\). Analyticity of \(d\) gives
\(\partial_r\Delta=2v+O(r)>v\); hence

\[
 r=\rho/(2v)+O(\rho^2),\qquad
 r\,\partial_\rho r=\rho/(4v^2)+O(\rho^2).
\]

The transformed amplitude is

\[
 \frac{2\operatorname{Re}z_{\alpha\beta}(r\omega)
                  r\partial_\rho r}{\rho^3}
 =\frac{f_{\alpha\beta}(\omega)}{2\rho^2}
       +O(\rho^{-1}).
\]

The error integrates to \(O((1+\log T)/T)\), and extending the positive
upper limit in the leading term to infinity costs \(O(T^{-1})\). Together
with the other transitions this yields that rate for the Cesaro
conductivity. The simpler dominated-convergence proof is preferable if
the theorem only claims a limit.

## Review conclusions

* No extra Bloch eigenvector hypothesis is required.
* Retain the moving-frame commutator in the velocity identification.
* Direct scaling and a uniform integrable majorant prove universality.
* Prove integrability and the vanishing shrinking-circle boundary terms
  before integrating the occupied energy Hessian.
* Invoke real-\(V\) time reversal explicitly for antisymmetric response.
