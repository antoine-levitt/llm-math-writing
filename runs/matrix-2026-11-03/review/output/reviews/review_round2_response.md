# Second-round mathematical referee review

I reread the revised `graphene_conductivity.tex` in full, including the new Bloch covariance identities, graph-norm resolvent argument, time-dependent propagator construction, and weak uniqueness calculation. I also inspected the complete extracted PDF text in `build/manuscript_layout.txt` and checked the compilation log for warnings, undefined references, and overfull or underfull boxes; none were reported by that check.

**Assessment: mathematically ready.** All substantive points raised in my first review have been resolved. I found no remaining gap in the proof of the stated theorem and no error introduced by the revisions. The proof retains the exact assumptions and order of limits from the notes.

## Verification of the revisions

1. The basis-independence claim now applies precisely to the response and sum-rule formulas; the absolute-value estimates are correctly asserted for every basis choice.
2. The Cesàro step now states the absolute time-integral estimate needed for Fubini. This closes the small logical imprecision in the first version.
3. The two product-formula commas are gone.
4. The common-domain propagator argument now uses the matching shifted resolvent `(K(s)-i)^{-1}` and explicitly proves norm conservation before concluding unitarity.
5. Reciprocal-lattice covariance has the correct sign with `tau_K=e^{-iK·x}`. Its use in the torus integrals and time-reversal cancellation is sound.
6. The Neumann-series resolvent identity proves analyticity into `B(H,D)`, not merely into `B(H)`. The order of the two factors in the inverse formula is correct, and the frame and compressed Hamiltonian are therefore justified at the required regularity.
7. The explicit weak uniqueness argument has the correct backward test orbit and scalar-product signs. Taking the terminal test vector in `D(H_epsilon^2)` permits differentiation in the graph norm and justifies the time-dependent testing step.

## Remaining optional copy edits

These are wording improvements, not obstacles to the theorem or to readiness.

* **Lines 181–182:** “We first derive the fixed-time response formula for the response of the full Hamiltonian” repeats “response.” Use “We first derive the fixed-time response of the full Hamiltonian” or “We first derive a fixed-time response formula for the full Hamiltonian.”
* **Lines 843–845:** “its commutator with each lattice translation is a scalar phase” is technically ambiguous because the paper uses ordinary additive commutators elsewhere. The intended fact is that `G_epsilon(t)` **commutes with each lattice translation up to a scalar phase**. Replacing the phrase by those words avoids confusing a multiplicative commutator with an additive one. The periodicity conclusion is correct.
* **Lines 836–837 and 877:** the phrases “uniformly bounded H^2 ranges” and “Ran P(k) has a uniformly bounded H^2 norm” can be made precise with “uniformly bounded as maps from H to H^2” and “occupied unit vectors have uniformly bounded H^2 norms,” respectively. Their intended meaning is already clear from the neighboring estimates and the fixed unit vector in the differentiation proof.

## Independent checks of the complete argument

The trace normalization remains `(2pi)^{-2}`. The local Hilbert–Schmidt factorization gives actual local trace class for the unbounded-current product rather than merely a formal fiber trace. Finite-time differentiation is controlled uniformly in momentum by the `L^2` Duhamel estimate and the interpolated `H^1` remainder. No differentiability of the Fermi projector at a node is used in this step.

The band-energy calculation uses a smooth occupied Riesz projection off the finite set of nodes, so internal band degeneracies do not create additional denominators. Its gradient is uniformly bounded up to the nodes; the Hessian has an integrable inverse-distance bound. The small-circle boundary integrals therefore vanish, proving the integrated sum rule with no hidden distributional contribution.

The raw response has the correct diamagnetic sign and the correct signs of its real and imaginary matrix-element terms. Time reversal cancels the imaginary contribution only after integration over the torus, exactly as stated. The real formula is absolutely integrable at each finite time.

The analytic two-band reduction extracts all necessary eigenvector information from the eigenvalue hypotheses. The connection correction in the physical velocities is of order `|q|`, since the reduced Hamiltonian at the node is scalar. The Pauli identity, angular integral, and factor of two in the interband response combine consistently.

The Cesàro kernel suppresses every transition with a uniformly positive gap. Uniform current-norm bounds control the infinite unoccupied-band sum. For the active cone pair, `q=s omega/T` gives a majorant `C min(1,s^{-2})`; the exact resulting coefficient is `1/16` per crossing. The proof makes no claim about an ordinary long-time limit or an interchange of the time and field limits.

## Readiness recommendation

Keep the present structure and make only the small copy edits above if desired. The manuscript is concise enough to read as a paper, while the appendix supplies the analytic details needed to turn the response calculation into a proof. Further expansion of the main argument is unlikely to improve it.

