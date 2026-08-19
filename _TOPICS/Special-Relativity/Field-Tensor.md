# Field Tensor

The antisymmetric spacetime tensor that packages electric and magnetic field components into one covariant object in relativistic electrodynamics.

Unified geometrical representation of $\mathbf{E}$ and $\mathbf{B}$. Electric and magnetic fields form one antisymmetric second-rank tensor in spacetime. An antisymmetric tensor is a two-index object that changes sign when its indices are swapped. This principle is used to treat $\mathbf{E}$ and $\mathbf{B}$ as frame-dependent parts of one field.

The electromagnetic field tensor is

$$
F^{\mu\nu} =
\begin{pmatrix}
0 & \dfrac{E_{x}}{c} & \dfrac{E_{y}}{c} & \dfrac{E_{z}}{c} \\
-\dfrac{E_{x}}{c} & 0 & B_{z} & -B_{y} \\
-\dfrac{E_{y}}{c} & -B_{z} & 0 & B_{x} \\
-\dfrac{E_{z}}{c} & B_{y} & -B_{x} & 0
\end{pmatrix}
$$

where

- $F^{\mu\nu}$ is the electromagnetic field tensor.
- $E_{x}$, $E_{y}$, $E_{z}$ are the electric-field components.
- $B_{x}$, $B_{y}$, $B_{z}$ are the magnetic-field components.
- $c$ is the speed of light.

Definition from the four-potential. The field tensor is the four-dimensional curl of the four-potential. The four-potential is the four-vector $\left(\dfrac{V}{c},\,\mathbf{A}\right)$. This principle is used to obtain $\mathbf{E}$ and $\mathbf{B}$ from derivatives of $A^{\mu}$.

The field tensor from the four-potential is

$$
F_{\mu\nu} = \partial_{\mu}A_{\nu} - \partial_{\nu}A_{\mu}
$$

where

- $F_{\mu\nu}$ is the covariant field tensor.
- $A_{\mu}$ is the four-potential.
- $\partial_{\mu}$ is the spacetime derivative.

Covariant Maxwell equations. Maxwell's four vector equations reduce to two tensor equations. Manifest covariance is the property that an equation written in tensors keeps its form under Lorentz transformations. The four-current is the four-vector $(c\rho,\,\mathbf{J})$. This principle is used to write electrodynamics so that it holds in every inertial frame.

The inhomogeneous Maxwell equation is

$$
\partial_{\mu}F^{\mu\nu} = \mu_{0}J^{\nu}
$$

The homogeneous Maxwell equation is

$$
\partial_{\lambda}F_{\mu\nu} + \partial_{\mu}F_{\nu\lambda} + \partial_{\nu}F_{\lambda\mu} = 0
$$

where

- $J^{\nu}$ is the four-current.
- $\mu_{0}$ is the permeability of free space.

The relativistic Lorentz force. The four-force on a charge is the contraction of the field tensor with the four-velocity. Four-velocity is the rate of change of spacetime position with proper time. This principle is used to write electric and magnetic forces as one equation.

The Minkowski force is

$$
f^{\mu} = q F^{\mu}{}_{\nu} U^{\nu}
$$

where

- $f^{\mu}$ is the four-force.
- $q$ is the charge.
- $U^{\nu}$ is the four-velocity.

Frame-invariant field scalars. Some combinations of $\mathbf{E}$ and $\mathbf{B}$ built from the field tensor are the same in every inertial frame. A spacetime invariant is a scalar unchanged by a Lorentz transformation. This principle is used to recognize a radiation field as a field with $E^{2}-c^{2}B^{2}=0$ in every frame.

The field invariant is

$$
F_{\mu\nu}F^{\mu\nu} = 2\left(B^{2} - \dfrac{E^{2}}{c^{2}}\right)
$$

Note: Also called the Faraday tensor. Also called the electromagnetic field tensor.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. — source for the heading explanation.
2. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — $F^{\mu\nu}$ matrix; $F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu}$; covariant Maxwell equations; $f^{\mu}=qF^{\mu}{}_{\nu}U^{\nu}$.
3. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — field-tensor components; four-potential.
4. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — $F_{\mu\nu}$; Maxwell tensor equations; field invariants.
5. Carroll, S. M. *Spacetime and Geometry*. Cambridge University Press. — Faraday tensor; $f^{\mu}=qF^{\mu}{}_{\nu}U^{\nu}$; $F_{\mu\nu}F^{\mu\nu}$.
