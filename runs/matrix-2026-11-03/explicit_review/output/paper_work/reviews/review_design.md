# Proof design and verified references

## Recommended narrative

The proof is easiest to understand as transport of the occupied projector.
The electric field translates crystal momentum. At a point Fermi surface the
occupied rank is constant almost everywhere, so its derivative is an ordinary
integrable matrix-valued function, with no surface measure of the type that
would describe an intraband acceleration term. This derivative creates
interband coherence. Time averaging suppresses every transition with a fixed
positive gap; only momenta at distance of order `1/T` from a node remain.
The conical velocity then cancels under rescaling, leaving an angular average.

Suggested main-paper sequence:

1. State the theorem with all hypotheses, conventions, and order of limits.
   Explain why a point Fermi surface need not have zero conductivity, and that
   this is a switch-on / Cesaro response, not a claim about the opposite order
   of limits or interacting graphene.
2. State a finite-time response proposition in terms of interband velocities
   and gaps. Give the transport equation and its linearization in the main
   text, with the analytic justification in an appendix if long.
3. Establish a single semantically coherent result about an isotropic cone:
   local two-band representation, the transverse velocity factor, and the
   integrable derivative of its occupied projector. The eigenvalue hypotheses
   alone force the required matrix geometry.
4. Prove the theorem by averaging, discarding uniformly gapped pairs, and
   rescaling the cone disks. This is the main climax and should be short.
5. An appendix supplies rough-potential operator setup, local trace identity,
   and the rigorous finite-time derivative without interrupting the mechanism.

Avoid splitting regularity estimates into individually numbered ad-hoc lemmas.
Avoid a diamagnetic term followed by a separate cancellation if transport gives
the formula directly. Avoid choosing analytic eigenvectors for all occupied
bands: the occupied projector and the isolated two-band cluster suffice, even
when lower or higher bands cross each other.

## Occupied-projector regularity

Let `P(k)` be the rank-`N` occupied projector away from the node set `D`, and
let `A=1-Delta_per`. On any fixed bounded set of reciprocal momenta,

```
||A P(k)||_1 <= C,
||A partial_beta P(k)||_1 <= C (1 + dist(k,D)^(-1)).
```

Consequently `P` is locally `W^{1,1}` in the Banach norm `||A X||_1`; globally
it is a covariant `W^{1,1}` Bloch field. Its weak derivative has no point masses.
This is the natural statement to support transport and pairing with the
unbounded current, because `v_alpha(k) A^{-1}` is uniformly bounded and
common-domain propagators are bounded in the `A` graph norm.

Proof details:

* A fixed-contour Riesz projection is analytic as a map from `L²` into `H²`.
  This follows directly from analytic resolvents in the common graph norm.
* Near a node, the lower separated cluster `P_<(k)` is analytic, as is the
  rank-two crossing cluster `Q(k)`. Choose an isometry `E_0:C² -> Ran Q(k_i)`.
  The local frame
  `E(k)=Q(k)E_0 [E_0^* Q(k) E_0]^(-1/2)`
  is analytic into `H²` and isometric for real `k`.
* Write `h(k)=E(k)^*H_kE(k)=a(k)I+d(k).sigma`. The eigenvalue assumptions give
  `|d(k_i+q)| >= c|q|`, while analyticity gives bounded first derivatives of
  `d`. Thus `p_-(k)=(I-d(k).sigma/|d(k)|)/2` obeys
  `||partial p_-|| <= C/|q|` and
  `P=P_<+E p_- E^*` gives the claimed operator and trace-norm estimates.
  Finite rank converts the graph operator bounds to trace norm.
* To identify the weak derivative, integrate by parts outside disks of radius
  `rho`. The graph trace norm of `P` is bounded, so each boundary term is
  `O(rho)`. It vanishes, and `1/|q|` is integrable in two dimensions.

The frame also makes the velocity statement transparent. For
`B_alpha=E^*(partial_alpha H)E`, differentiation gives

```
partial_alpha h = B_alpha + [h, E^* partial_alpha E].
```

The commutator is `O(|q|)`, so physical velocity matrices agree to leading
order with derivatives of the reduced cone. At the node `h=mu I`, hence
`B_alpha(0)=partial_alpha h(0)` exactly. This is enough; no Berry connection
needs to be introduced as separate notation in the paper.

## Exact response and summability

In periodic-gauge Bloch coordinates, `x_beta=i partial_beta`, so the density
equation is

```
partial_t rho_epsilon + epsilon partial_beta rho_epsilon
    = -i [H_k,rho_epsilon],       rho_epsilon(k,0)=P(k).
```

The exact source equation for `rho_epsilon-P`, followed by the weighted
`W^{1,1}` limit, gives

```
rho_1(k,t) = -int_0^t exp(-is H_k) (partial_beta P(k)) exp(is H_k) ds.
```

For `n<=N<m`, with `Delta=lambda_m-lambda_n>0`,
`(partial_beta P)_{nm}=-(v_beta)_{nm}/Delta`. The diagonal blocks vanish.
Time reversal (`V` real) pairs `k` and `-k`, annihilating the imaginary
interband coefficient. The real response is therefore

```
L_alpha_beta(t) = 2/(2pi)^2 int_B sum_{n<=N<m}
   Re[(v_alpha)_{mn}(v_beta)_{nm}] sin(t Delta)/Delta^2 dk.
```

The equilibrium current also vanishes by time reversal. The trace-per-volume
normalization is `(2pi)^(-2) int_B tr_fiber`, not the normalized Brillouin-zone
average alone.

At each `k`, Cauchy--Schwarz and completeness give

```
sum_{n<=N<m} |(v_alpha)_{mn}(v_beta)_{nm}|
  <= sum_{n<=N} ||v_alpha u_n|| ||v_beta u_n|| <= C.
```

All occupied energies are uniformly bounded; the common graph estimate
controls their `H¹` norms. This single estimate handles every infinite sum,
including all degeneracies away from the crossing pair. After time averaging
the multiplier is `(1-cos(T Delta))/(T Delta^3)`, so every uniformly gapped
collection contributes `O(1/T)` without any oscillatory-integral theorem.

## The clean conical limit

Use direct dilation `q=p/T`. No radial gap-coordinate change or quantitative
phase-error estimate is needed. The averaged integrand, including the
Jacobian, becomes

```
2 Re z(p/T) [1-cos(T Delta(p/T))]/[T Delta(p/T)]^3.
```

It is dominated on the expanding disk by
`C min(|p|²,1)/|p|³`, an integrable function on `R²`. Pointwise convergence
uses `T Delta(p/T)->2v|p|` and the leading transverse velocity factor.
Dominated convergence therefore proves that only the linear cone matters.

For a cone of slope `v`, the numerator is
`v²[e_alpha.e_beta-(e_alpha.n)(e_beta.n)]`. Its angular integral is
`pi v² e_alpha.e_beta`. The radial integral uses
`int_0^infty (1-cos s)/s² ds=pi/2`. Accounting for the leading `2`,
the gap `2vr`, and `(2pi)^(-2)` gives `1/16` per node.

## Verified Reed--Simon locations

The local DjVu files contain searchable text. Extracted copies are
`paper_work/reed_simon_II.txt` and `paper_work/reed_simon_IV.txt`.

* **II, Theorem X.12, p.162:** Kato--Rellich; a symmetric perturbation with
  relative bound `<1` preserves self-adjointness on the original domain and
  essential self-adjointness on any core.
* **IV, Theorem XIII.96, pp.302--303:** uniformly locally `L²` potentials in
  dimension `n<=3` are `-Delta`-bounded with relative bound zero. This covers a
  rough periodic potential on the whole plane directly.
* **IV, Theorem XIII.97, pp.303--304:** the position-space Bloch decomposition
  for periodic potentials in the appropriate cell `L^p` class.
* **IV, Theorem XIII.99, pp.305--307:** the reciprocal-space Bloch decomposition;
  the paragraph immediately afterward explicitly treats `H(k)` as an entire
  analytic family of type (A) in multiple momentum parameters.
* **IV, Section XII.2, pp.16--24:** analytic common-domain perturbation and Riesz
  projections. Theorem XII.9 establishes analytic resolvents for type-(A)
  families. Theorem XII.12, p.22, gives an analytic unitary identification of
  analytic finite-rank projections, but its statement uses one complex
  parameter. The explicit local frame above handles two parameters without
  an imprecise citation.
* **II, Theorem X.70, pp.285--289:** common-domain time-dependent generator
  theorem. The conditions are satisfied for `i H_{k+epsilon t e_beta}`
  after a harmless scalar resolvent shift; its proof supplies uniform graph
  bounds for the propagator. Theorem X.71 is a narrower `L²+L∞` potential
  application in `R³`, so cite X.70 here.
* **II, Theorem X.37, pp.197--198:** operator commutator theorem, requiring a
  comparison operator `N>=1`, a common core, `||Au||<=C||Nu||`, and the
  quadratic commutator bound.
* **II, Theorem X.38, pp.198--199:** Faris--Lavine. It allows
  `-Delta+V_1+W` when `V_1>=-c|x|²-d`, `-aDelta+W` is bounded below for some
  `a<1`, and the corresponding operator with `2c|x|²` added is essentially
  self-adjoint on an invariant dense core. Apply to twice the Stark operator,
  with `V_1=-2epsilon x.e_beta`, `W=2V`, and `C_c^infty` as core. The confining
  auxiliary operator is covered by Kato--Rellich relative to the harmonic
  oscillator, using XIII.96 and its graph bound for `-Delta`. The first
  corollary of X.38 assumes a global `L^p` remainder and therefore does not
  directly cover a rough periodic potential.

## Pitfalls to avoid

* Do not infer analytic individual eigenvectors through arbitrary band
  crossings or globally across a cone.
* The rank-`N+1` convention at an isolated node does not affect any direct
  integral or integral. Say this once; define the rank-`N` field almost
  everywhere and do not carry the exceptional convention throughout.
* A reciprocal cell need not be invariant under `k -> -k`. Use periodicity/
  covariance or work intrinsically on the reciprocal torus when invoking
  time reversal.
* The current is a particle current under the sign convention of the notes;
  no extra electron charge or spin/valley multiplicity should be inserted.
  `M` already counts all inequivalent nodes.
* Arbitrary `e_alpha,e_beta` need not be unit vectors. Keep directional
  derivatives and the dot product throughout.
* Do not claim an ordinary long-time limit from a Cesaro argument. The theorem
  asks for fixed-time linear response first, followed by time averaging.

