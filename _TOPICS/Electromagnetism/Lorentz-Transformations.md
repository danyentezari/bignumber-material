# Lorentz Transformations

A change of inertial frame that is used to convert electromagnetic fields from one observer to another moving at constant relative velocity, where an inertial frame is a frame in which free particles move at constant velocity.

Invariance of the parallel fields. Under a boost, the components of $\mathbf{E}$ and $\mathbf{B}$ parallel to the relative velocity are unchanged. A boost is a Lorentz transformation between frames that differ by a constant velocity. This principle is used to keep the longitudinal fields the same for both observers.

The parallel field transformations are

$$
\bar{E}_{\parallel} = E_{\parallel},\qquad \bar{B}_{\parallel} = B_{\parallel}
$$

where

- $E_{\parallel}$ and $B_{\parallel}$ are the field components along the boost.
- bars mark the fields in the moving frame.

Mixing of the transverse fields. The transverse fields mix. A field that is purely electric in one frame has a magnetic part in a frame in relative motion. This principle is used to transform the fields perpendicular to the boost.

The field transformation for a boost along $x$ is

$$
\bar{E}_{y} = \gamma(E_{y} - v B_{z}),\qquad \bar{E}_{z} = \gamma(E_{z} + v B_{y})
$$

$$
\bar{B}_{y} = \gamma\Bigl(B_{y} + \dfrac{v}{c^{2}}E_{z}\Bigr),\qquad \bar{B}_{z} = \gamma\Bigl(B_{z} - \dfrac{v}{c^{2}}E_{y}\Bigr)
$$

where

- $\mathbf{E}$ and $\mathbf{B}$ are the fields in the original frame.
- $\bar{\mathbf{E}}$ and $\bar{\mathbf{B}}$ are the fields in the boosted frame.
- $v$ is the relative speed along $x$.
- $\gamma$ is the Lorentz factor.
- $c$ is the speed of light.

The tensor transformation of $F^{\mu\nu}$. The same mixing is the tensor transformation of $F^{\mu\nu}$. This principle is used to obtain the field transformations from the Lorentz transformation of a second-rank tensor.

The Lorentz transformation of the field tensor is

$$
\bar{F}^{\mu\nu} = \Lambda^{\mu}{}_{\alpha}\Lambda^{\nu}{}_{\beta}F^{\alpha\beta}
$$

where

- $F^{\mu\nu}$ is the electromagnetic field tensor.
- $\Lambda^{\mu}{}_{\alpha}$ is the Lorentz transformation matrix.

Note: Also called a Lorentz boost of the electromagnetic field.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §12.3.2 — Lorentz transformation of electromagnetic fields.
