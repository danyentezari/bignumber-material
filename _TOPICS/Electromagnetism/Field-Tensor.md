# Field Tensor

An antisymmetric spacetime tensor that is used to package the electric and magnetic fields into one Lorentz-covariant object, where an antisymmetric tensor is a two-index object that changes sign when its indices are swapped.

1\. The six independent components of $F^{\mu\nu}$ are the three electric and three magnetic field components. This principle is used to treat $\mathbf{E}$ and $\mathbf{B}$ as parts of one spacetime field.

The electromagnetic field tensor is

$$
F^{\mu\nu} =
\begin{pmatrix}
0 & -E_{x}/c & -E_{y}/c & -E_{z}/c \\
E_{x}/c & 0 & -B_{z} & B_{y} \\
E_{y}/c & B_{z} & 0 & -B_{x} \\
E_{z}/c & -B_{y} & B_{x} & 0
\end{pmatrix}
$$

where

- $F^{\mu\nu}$ is the electromagnetic field tensor.
- $E_{x}$, $E_{y}$, $E_{z}$ are the electric-field components.
- $B_{x}$, $B_{y}$, $B_{z}$ are the magnetic-field components.
- $c$ is the speed of light.

2\. The field tensor is the curl of the four-potential. This principle is used to obtain $F^{\mu\nu}$ from $A^{\mu}$.

The field tensor from the four-potential is

$$
F_{\mu\nu} = \partial_{\mu}A_{\nu} - \partial_{\nu}A_{\mu}
$$

where

- $F_{\mu\nu}$ is the covariant field tensor.
- $A_{\mu}$ is the four-potential.
- $\partial_{\mu}$ is the spacetime derivative.

3\. Maxwell's equations are two tensor equations for $F^{\mu\nu}$. This principle is used to write electrodynamics in every inertial frame at once.

The inhomogeneous Maxwell equation is

$$
\dfrac{\partial F^{\mu\nu}}{\partial x^{\nu}} = \mu_{0}J^{\mu}
$$

The homogeneous Maxwell equation is

$$
\dfrac{\partial F_{\mu\nu}}{\partial x^{\lambda}} + \dfrac{\partial F_{\nu\lambda}}{\partial x^{\mu}} + \dfrac{\partial F_{\lambda\mu}}{\partial x^{\nu}} = 0
$$

where

- $F^{\mu\nu}$ is the electromagnetic field tensor.
- $J^{\mu}$ is the four-current.
- $\mu_{0}$ is the permeability of free space.
- $x^{\nu}$ are the spacetime coordinates.

Note: These principles are the component identification of $F^{\mu\nu}$, the potential formula $F=dA$, and the covariant Maxwell equations. Also called the Faraday tensor. Also called the electromagnetic field tensor.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §12.3.3 — electromagnetic field tensor.
