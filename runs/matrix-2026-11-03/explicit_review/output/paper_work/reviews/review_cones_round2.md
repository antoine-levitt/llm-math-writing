# Final mathematical review

I reread the revised `dirac_conductivity.tex` in full and checked it again against `graphene_statement.tex` and the conical computation. My final verdict is **ready**. I found no mathematical gap, changed hypothesis, or necessary correction.

The revised source identity is especially clear: for each fixed field and time, the exceptional final momenta whose characteristic intersects a node form a null set (a finite union of line segments in any bounded lift). Off that set the displayed differentiation is classical, and the weighted integrability estimates control its integration over momentum. This removes any ambiguity about differentiating through the singular projection.

The Bloch covariance statements now distinguish the operator fields from the Sobolev weights correctly. Multiplication by reciprocal-lattice phases preserves `H²`, with bounded constants on the finite sets of shifts used here; no false invariance of the chosen weighted norm is assumed. The local trace argument includes the off-diagonal cell blocks needed for arbitrary bounded spatial compressions.

I rechecked the response sign, the two conjugate occupied–empty blocks, the time-reversal cancellation, the compression of the physical velocity in the moving frame, and the angular trace identity. Time reversal is understood with time-reversed eigenbases, or equivalently through the basis-independent sums already specified in the text. Internal band degeneracies create no additional assumption.

The long-time argument remains complete: a uniform summability bound removes all uniformly gapped transitions at rate `O(T^{-1})`; the touching pair has the gap and transition-weight asymptotics forced by the stated cone; the scaling `s=2vTr` gives the integrable majorant `C min(1,s^{-2})`; and the two scalar integrals give exactly one sixteenth per cone. The final inline evaluation does not omit any step or obscure the normalization.

The editorial changes resolve my earlier suggestions. In particular, `w(q)` avoids the collision with bounding constants, the radial/tangential interpretation is explicitly restricted to the linearized cone, and the trace criterion has the boundedness qualification used in its proof. The shortened ending now concludes at the mathematical result. Further alterations are not needed for either correctness or readability.
