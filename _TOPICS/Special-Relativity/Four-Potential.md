# Four-Potential

A four-vector whose time and space parts are the scalar and vector potentials that is used to package the electromagnetic potentials into one Lorentz-covariant object.

Relativistic unification of the potentials. The electric scalar potential and the magnetic vector potential form one four-vector. A four-vector is a four-component object that transforms as spacetime coordinates do under a Lorentz transformation. This principle is used to treat the potentials as one spacetime quantity.

The four-potential is

$$
A^{\mu} = \left(\dfrac{V}{c},\, \mathbf{A}\right)
$$

where

- $A^{\mu}$ is the four-potential.
- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $c$ is the speed of light.

Local gauge invariance. Adding the spacetime derivative of a scalar function to $A^{\mu}$ leaves $\mathbf{E}$ and $\mathbf{B}$ unchanged. Gauge invariance is that redundancy of the potential. This principle is used to choose the Lorenz gauge $\partial_{\mu}A^{\mu}=0$ and simplify the equations.

Generation of the field tensor. The field tensor is the four-dimensional curl of the four-potential. The electromagnetic field tensor is the antisymmetric $4\times 4$ array of $\mathbf{E}$ and $\mathbf{B}$. This principle is used to obtain Faraday's law and the absence of magnetic monopoles as identities.

The field tensor from the four-potential is

$$
F_{\mu\nu} = \partial_{\mu}A_{\nu} - \partial_{\nu}A_{\mu}
$$

where

- $F_{\mu\nu}$ is the covariant field tensor.
- $\partial_{\mu}$ is the spacetime derivative.

The sourced wave equation. In the Lorenz gauge, the four-potential obeys a wave equation sourced by the four-current. The four-current is the four-vector of charge density and current density. This principle is used to compute radiation from accelerating charges.

The potential wave equation is

$$
\square A^{\mu} = -\mu_{0} J^{\mu}
$$

where

- $\square$ is the d'Alembertian.
- $\mu_{0}$ is the permeability of free space.
- $J^{\mu}$ is the four-current.

Note: Also called the potential $4$-vector. Also called the $4$-vector potential.

## References

1. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — potential $4$-vector $A^{\alpha}=\left(\dfrac{V}{c},\mathbf{A}\right)$; gauge invariance; $F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu}$.
2. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — $A^{\mu}=\left(\dfrac{V}{c},A_{x},A_{y},A_{z}\right)$; Lorenz gauge; wave equation.
3. Carroll, S. M. *Spacetime and Geometry*. Cambridge University Press. — four-potential; $F=dA$; gauge transformations.
4. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — four-potential; field tensor from $A^{\mu}$.
