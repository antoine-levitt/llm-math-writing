# Operator-foundation review

The stated regularity is sufficient. I found no obstruction to the theorem in the operator-theoretic setup. The most delicate points are the Stark core, the use of an unbounded current in linear response, and trace normalization. All can be handled without strengthening the assumptions or importing results beyond Reed–Simon and elementary Sobolev estimates.

## Verified Reed–Simon references

All references below were checked in the locally supplied volumes (OCR in `reference_text`).

* II, Theorem X.12, pp. 162–163: Kato–Rellich, including preservation of cores and lower boundedness.
* II, Theorem X.29, pp. 185–186: if (V_1\geq0), (V_1\in L^2_{\rm loc}), and (V_2) is relatively (-\Delta)-bounded with bound below one, then (-\Delta+V_1+V_2) is essentially self-adjoint on (C_c^\infty).
* II, Theorem X.38, pp. 198–199: Faris–Lavine; see the concrete verification below. Do not cite its subsequent corollary alone: that corollary assumes a globally (L^p) singular part, whereas an unbounded periodic potential is not globally (L^p).
* II, Theorem X.70, pp. 285–286 (proof continues to p. 287): common-domain nonautonomous evolution. The theorem and proof provide invariance of the common operator domain and uniform graph-norm bounds on compact time intervals.
* IV, Theorem XIII.96, pp. 302–303: a uniformly locally (L^2) multiplication potential in dimension two is infinitesimally (-\Delta)-bounded.
* IV, Theorems XIII.97–98, pp. 303–305: Bloch decomposition and measurable band eigenfunctions for periodic potentials with the required local integrability. The book uses quasiperiodic boundary conditions; multiplication by (e^{-ik\cdot x}) gives the fixed periodic-domain convention of the notes.
* I, Theorem VI.22(h), p. 210: a product of two Hilbert–Schmidt operators is trace class. VI.23, pp. 210–211 gives the kernel criterion.

## 1. Self-adjointness and graph norms

Periodic (V\in H^1(\Omega)\subset L^2(\Omega)) is uniformly locally (L^2). Thus, on \(\mathbb R^2\),

\[
 \|Vu\|_2\leq \eta\|\Delta u\|_2+C_\eta\|u\|_2,
 \qquad u\in H^2,\quad \eta>0.
\]

The same estimate holds on the torus, either by the same local proof or by the compact-domain Sobolev inequality. Uniformly for (k) in any compact set, (H_k) is self-adjoint on (H^2_{\rm per}), bounded below uniformly, and

\[
 C^{-1}\|u\|_{H^2}\leq \|(H_k+c)u\|_2\leq C\|u\|_{H^2}
\]

after increasing (c) so (H_k+c\geq1). The resolvent is compact. The family is polynomial, hence analytic as a map from (H^2_{\rm per}) to (L^2_{\rm per}). All these conclusions also hold on the full space except compactness of the resolvent.

For the Stark operator, apply Faris–Lavine to

\[
 2H_\varepsilon=-\Delta+U+W,
 \qquad U=-2\varepsilon x\cdot e_\beta,
 \qquad W=2V.
\]

Choose (c>0,d) so (U\geq-c|x|^2-d), and (D=C_c^\infty(\mathbb R^2)). This (D) is invariant under (x_j) and (-i\partial_j). The comparison operator

\[
 -\Delta+U+W+2c|x|^2
\]

is essentially self-adjoint on (D): add a scalar to make (U+2c|x|^2\geq0), then invoke X.29 with the infinitesimally (-\Delta)-bounded part (W). For any fixed (0<a<1), (-a\Delta+W) is bounded below by X.12. These are exactly X.38(i)–(ii). Hence (H_\varepsilon|_D) has the unique self-adjoint closure used in the notes. This argument avoids derivatives of (V).

## 2. Temporal gauge and its rigorous identification

Let (p=-i\nabla), (b=e_\beta), and let 

\[
 i\partial_t U_\varepsilon(t,s)
   =\bigl(\tfrac12(p+\varepsilon t b)^2+V\bigr)U_\varepsilon(t,s),
 \qquad U_\varepsilon(s,s)=1.
\]

The Hamiltonians have common domain (H^2) and are continuously differentiable in (\mathcal B(H^2,L^2)). Their graph norms are uniformly equivalent on compact time and parameter intervals. The hypotheses of X.70 follow because

\[
 \partial_t H(t)\,(H(t)+c)^{-1}
 =\varepsilon b\cdot(p+\varepsilon t b)(H(t)+c)^{-1}
\]

is bounded and norm continuous. This gives a unitary propagator preserving (H^2), with

\[
 \sup_{|t|,|s|\leq L,\,|\varepsilon|\leq1}
 \|U_\varepsilon(t,s)\|_{H^2\to H^2}<\infty.
\]

The same bound holds uniformly for fiber propagators (U_{\varepsilon,k}), whose Hamiltonians are (H_{k+\varepsilon tb}), with (k) in a fixed Brillouin cell. A useful explicit version is the graph estimate

\[
 \|(H(t)+c)U(t,s)(H(s)+c)^{-1}\|
 \leq \exp\!\left(\int_s^t
       \|\partial_r H(r)(H(r)+c)^{-1}\|\,dr\right),
\]

obtained through the piecewise-constant propagators in the proof of X.70 (or its standard graph-norm argument).

The correct gauge identity is

\[
 e^{-itH_\varepsilon}=e^{i\varepsilon t x\cdot b}U_\varepsilon(t,0).
\]

One must not differentiate the right-hand side in (L^2) for arbitrary (H^2) data, since no (x)-moment is assumed. Instead, for (f\in H^2), set (v(t)=e^{i\varepsilon t x\cdot b}U_\varepsilon(t,0)f), and test against (\phi\in C_c^\infty). The transformed test (e^{-i\varepsilon t x\cdot b}\phi) remains in (C_c^\infty) and is differentiable in (H^2). Product differentiation therefore gives, with the scalar product linear in its second argument,

\[
 \frac{d}{dt}\langle\phi,v(t)\rangle
   =-i\langle H_\varepsilon\phi,v(t)\rangle.
\]

The integrated identity extends from (C_c^\infty) to (D(H_\varepsilon)) by graph density. Continuous (L^2) weak solutions of this equation are unique: test against the backward orbit (e^{-i(s-t)H_\varepsilon}\phi), first for (\phi\in D(H_\varepsilon^2)), and then use density. Thus (v(t)=e^{-itH_\varepsilon}f). Density extends the identity to all initial data in (L^2).

No propagation of position moments or differentiability of the potential is needed.

## 3. Local trace class and normalization

Use the Bloch transform

\[
 (\mathcal U f)(k,x)=\sum_{R\in\mathcal R}
   e^{-ik\cdot(x+R)}f(x+R),\quad x\in\Omega,
\]

with direct-integral measure (dk/|\mathcal B|). This is unitary by lattice Parseval. The fiber Hilbert space uses the ordinary (L^2(\Omega,dx)) norm, not a normalized cell measure.

If (A) is a bounded periodic operator with Hilbert–Schmidt fibers and integrable squared fiber norms, lattice Parseval for its kernel gives

\[
 \|\mathbf1_\Omega A\|_{\mathfrak S_2}^2
 =\frac1{|\mathcal B|}\int_\mathcal B
       \|A_k\|_{\mathfrak S_2}^2\,dk.
\]

In particular, if (Q) is a periodic orthogonal projection of finite constant fiber rank and its range has uniformly bounded (H^1) norm, then both (\mathbf1_\Omega J_\alpha Q) and (Q\mathbf1_\Omega) are Hilbert–Schmidt. Consequently

\[
 \mathbf1_\Omega J_\alpha Q\mathbf1_\Omega
  =(\mathbf1_\Omega J_\alpha Q)(Q\mathbf1_\Omega)
\]

is trace class. The Hilbert–Schmidt pairing, followed by Parseval, gives

\[
 \frac1{|\Omega|}\operatorname{Tr}
   (\mathbf1_\Omega J_\alpha Q\mathbf1_\Omega)
 =\frac1{(2\pi)^2}\int_\mathcal B
   \operatorname{Tr}_{L^2(\Omega)}(v_{\alpha,k}Q_k)\,dk,
\]

where (v_{\alpha,k}=(p+k)\cdot e_\alpha), since (|\Omega||\mathcal B|=(2\pi)^2). This derivation also proves local trace class instead of assuming it in the definition of current.

For (P_k=\mathbf1_{(-\infty,\mu_F]}(H_k)), 

\[
 \operatorname{rank}P_k=N,\qquad
 \|P_k\|_{L^2\to H^2}\leq C
\]

almost everywhere. The uniform graph estimate follows from uniformly bounded occupied eigenvalues. Values at the finitely many touching points have no effect on the direct integral. Set (Q_\varepsilon=U_\varepsilon\gamma_0U_\varepsilon^*). Its fibers have rank (N) and uniformly (H^2)-bounded ranges for fixed time. The actual density is (WQ_\varepsilon W^*), with (W=e^{i\varepsilon tx\cdot b}). Conjugation by (W) preserves periodicity because its lattice-translation commutator is a scalar phase. It also preserves (H^2) for fixed time, so the same trace-class conclusion holds.

Since (W) commutes with (\mathbf1_\Omega), and (W^*J_\alpha W=J_\alpha+\varepsilon t(e_\alpha\cdot b)), the exact current formula is

\[
 j_\varepsilon(t)=\frac1{(2\pi)^2}\int_\mathcal B
 \operatorname{Tr}\Bigl[
 (v_{\alpha,k}+\varepsilon t(e_\alpha\cdot b))
 U_{\varepsilon,k}(t,0)P_kU_{\varepsilon,k}(t,0)^*
 \Bigr],dk.
\]

The plus sign in the accelerated momentum is essential.

## 4. Linear response with the unbounded current

Fix (t\geq0), a compact set of (k)'s, and (|\varepsilon|\leq1). For (u\in H^2_{\rm per}), Duhamel gives

\[
 \delta_\varepsilon(t):=
 (U_{\varepsilon,k}(t,0)-e^{-itH_k})u
 =-i\int_0^t U_{\varepsilon,k}(t,s)
       \left(\varepsilon s v_{\beta,k}
          +\tfrac{\varepsilon^2s^2}{2}|b|^2\right)
       e^{-isH_k}u\,ds.
\]

It follows that (\|\delta_\varepsilon(t)\|_2\leq C_t|\varepsilon|\|u\|_{H^2}). The propagators converge strongly to (e^{-i(t-s)H_k}), uniformly in (s\in[0,t]), by this estimate and density. Therefore

\[
 \frac{\delta_\varepsilon(t)}\varepsilon
 \longrightarrow
 -i\int_0^t e^{-i(t-s)H_k}
      s v_{\beta,k}e^{-isH_k}u\,ds
 \quad\hbox{in }L^2.
\]

There is no need to differentiate this convergence in (H^1). Write (\psi_0=e^{-itH_k}u), (\psi_\varepsilon=\psi_0+\delta_\varepsilon). Uniform (H^2) propagation and interpolation imply

\[
 \|\delta_\varepsilon\|_{H^1}
 \leq C\|\delta_\varepsilon\|_2^{1/2}
       \|\delta_\varepsilon\|_{H^2}^{1/2}
 \leq C_t|\varepsilon|^{1/2}\|u\|_{H^2}.
\]

Hence

\[
 \langle\psi_\varepsilon,v_{\alpha,k}\psi_\varepsilon\rangle
 -\langle\psi_0,v_{\alpha,k}\psi_0\rangle
 =2\operatorname{Re}\langle\delta_\varepsilon,
                              v_{\alpha,k}\psi_0\rangle
   +\langle\delta_\varepsilon,
                v_{\alpha,k}\delta_\varepsilon\rangle,
\]

and the last term is (O_t(|\varepsilon|^{3/2}\|u\|_{H^2}^2)). This proves differentiability of the current using only the (L^2) derivative. For occupied normalized eigenvectors the constants are uniform in (k), so the difference quotients admit an integrable, indeed uniform, majorant after summing the (N) occupied states. Dominated convergence gives the macroscopic linear-response formula. No smooth global eigenbasis is needed; measurable bases exist by XIII.98, and all estimates depend only on the occupied projection.

The initial current vanishes by time reversal: complex conjugation intertwines (H_k) with (H_{-k}), takes (P_k) to (P_{-k}), and takes (v_{\alpha,k}) to (-v_{\alpha,-k}). Thus its Brillouin-zone integral is zero. This is necessary because the theorem divides (j_\varepsilon), not (j_\varepsilon-j_0), by (\varepsilon).

## 5. Estimates for later spectral manipulations

For any normalized occupied eigenvector (u_n(k)),

\[
 \sum_{m\geq1}|\langle u_m,v_{a,k}u_n\rangle|^2
 =\|v_{a,k}u_n\|_2^2\leq C|a|^2.
\]

Thus every unweighted interband sum of absolute products is uniformly summable by Cauchy–Schwarz:

\[
 \sum_{n\leq N,m>N}
 |\langle u_n,v_{a,k}u_m\rangle
  \langle u_m,v_{b,k}u_n\rangle|
 \leq C|a||b|.
\]

All transitions except the (N\leftrightarrow N+1) pair near each cone have a uniform strictly positive energy gap. This follows by continuity, compactness, the isolated-double-eigenvalue hypothesis, and monotonicity of ordered eigenvalues. The preceding absolute summability controls all such terms with any inverse power of their gaps. Near a cone the exceptional gap is comparable to (|k-k_i|). Its inverse is integrable in two dimensions, and expressions involving (sin(t\Delta)/\Delta^2) are bounded by (t/\Delta) for fixed (t). These observations justify interchange of fiber traces, time integrals and band sums without requiring a uniform spectral gap.

