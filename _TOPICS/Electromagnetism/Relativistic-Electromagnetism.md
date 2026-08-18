# Relativistic Electromagnetism

A formulation of electromagnetism in spacetime that is used to treat electric and magnetic fields as parts of one Lorentz-covariant field, where spacetime is the four-dimensional arena of special relativity, and where a Lorentz-covariant field is a field that transforms so that the same physics holds in every inertial frame.

1\. Under a change of inertial frame, electric and magnetic fields mix. A field that is purely electric in one frame has both electric and magnetic parts in a frame in relative motion. This principle is used to transform fields from one inertial frame to another.

The field transformation for a boost along $x$ is

$$
\bar{E}_{x} = E_{x},\qquad \bar{E}_{y} = \gamma(E_{y} - v B_{z}),\qquad \bar{E}_{z} = \gamma(E_{z} + v B_{y})
$$

$$
\bar{B}_{x} = B_{x},\qquad \bar{B}_{y} = \gamma\Bigl(B_{y} + \dfrac{v}{c^{2}}E_{z}\Bigr),\qquad \bar{B}_{z} = \gamma\Bigl(B_{z} - \dfrac{v}{c^{2}}E_{y}\Bigr)
$$

where

- $\mathbf{E}$ and $\mathbf{B}$ are the fields in the original frame.
- $\bar{\mathbf{E}}$ and $\bar{\mathbf{B}}$ are the fields in the boosted frame.
- $v$ is the relative speed along $x$.
- $\gamma$ is the Lorentz factor.
- $c$ is the speed of light.

2\. The six field components are entries of one antisymmetric second-rank tensor in spacetime. An antisymmetric tensor is a two-index object that changes sign when its indices are swapped. This principle is used to write electrodynamics as a single spacetime field.

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

3\. The scalar potential and the vector potential are the time and space parts of one four-vector. A four-vector is a four-component spacetime quantity that transforms as a displacement in spacetime. This principle is used to solve both potentials together.

The electromagnetic four-potential is

$$
A^{\mu} = \Bigl(\dfrac{V}{c}, A_{x}, A_{y}, A_{z}\Bigr)
$$

where

- $A^{\mu}$ is the four-potential.
- $V$ is the scalar potential.
- $A_{x}$, $A_{y}$, $A_{z}$ are the components of the vector potential.
- $c$ is the speed of light.

4\. Charge density and current density are the time and space parts of one four-vector. This principle is used to write the source of the electromagnetic field in spacetime form.

The electromagnetic four-current is

$$
J^{\mu} = \bigl(c\rho, J_{x}, J_{y}, J_{z}\bigr)
$$

where

- $J^{\mu}$ is the four-current.
- $\rho$ is the volume charge density.
- $J_{x}$, $J_{y}$, $J_{z}$ are the components of the current density.
- $c$ is the speed of light.

5\. The four Maxwell equations become two tensor equations in spacetime. Manifest covariance is the property that both sides of an equation are tensors, so Lorentz invariance is visible. This principle is used to write Maxwell's equations so they hold in every inertial frame.

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

6\. The force on a charge is the contraction of the field tensor with the four-velocity. Proper time is the time read by a clock that travels with the particle. This principle is used to compute the relativistic trajectory of a charged particle.

The covariant Lorentz force law is

$$
\dfrac{dp^{\mu}}{d\tau} = q F^{\mu\nu}\eta_{\nu}
$$

where

- $p^{\mu}$ is the four-momentum of the particle.
- $\tau$ is the proper time.
- $q$ is the electric charge.
- $F^{\mu\nu}$ is the electromagnetic field tensor.
- $\eta_{\nu}$ is the covariant four-velocity.

Note: These principles are the Lorentz transformation of the electromagnetic field, the electromagnetic field tensor, the electromagnetic four-potential, the electromagnetic four-current, the covariant Maxwell equations, and the covariant Lorentz force law. Also called covariant electrodynamics. The field tensor is also called the Faraday tensor.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §12.3 — field transformations, field tensor, four-potential, four-current, and covariant Maxwell and Lorentz laws.
2. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — covariant Maxwell theory.
3. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — electromagnetism as relativistic field theory.
