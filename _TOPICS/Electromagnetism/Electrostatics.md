# Electrostatics

A branch of electromagnetism that is used to describe fields and forces of electric charges that are at rest, where a stationary charge is a charge whose position does not change in time.

Coulomb's law. The force between two stationary point charges is proportional to the product of the charges and falls as the inverse square of their separation. A point charge is a charge treated as concentrated at a single location. This principle is used to compute the mechanical force between two isolated charges at rest.

Coulomb's law is

$$
\mathbf{F} = \dfrac{1}{4\pi\epsilon_{0}}\dfrac{qQ}{r^{2}}\hat{\mathbf{r}}
$$

where

- $\mathbf{F}$ is the electrostatic force on the test charge $Q$.
- $q$ is the source charge.
- $Q$ is the test charge.
- $r$ is the separation of the two charges.
- $\hat{\mathbf{r}}$ is the unit vector from $q$ toward $Q$.
- $\epsilon_{0}$ is the permittivity of free space.

Superposition. The net electric field of many stationary charges is the vector sum of the fields that each charge would produce alone. A vector sum is an addition that accounts for both magnitude and direction. This principle is used to build the field of a complicated charge collection from simpler pieces.

The superposition of electric fields is

$$
\mathbf{E}(\mathbf{r}) = \sum_{i=1}^{n}\mathbf{E}_{i}(\mathbf{r})
$$

where

- $\mathbf{E}(\mathbf{r})$ is the net electric field at position $\mathbf{r}$.
- $\mathbf{E}_{i}$ is the electric field of source charge $i$.
- $n$ is the number of source charges.

The electric field. A stationary charge distribution produces a vector field throughout space that exerts a local force on any other charge. A vector field is an assignment of a vector to each point in space. This principle is used to map electrostatic force without treating action at a distance.

The electric field of a charge distribution is

$$
\mathbf{E}(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}}\displaystyle\int\dfrac{\rho(\mathbf{r}')}{r^{2}}\hat{\mathbf{r}}\,d\tau'
$$

where

- $\mathbf{E}(\mathbf{r})$ is the electric field at the field point.
- $\rho$ is the volume charge density.
- $\mathbf{r}'$ is the source position.
- $r$ is the distance from the source element to the field point.
- $\hat{\mathbf{r}}$ is the unit vector from the source element to the field point.
- $d\tau'$ is the volume element.
- $\epsilon_{0}$ is the permittivity of free space.

Gauss's law. The net outward flux of the electric field through a closed surface is proportional to the charge enclosed by that surface. Flux is the amount of a vector field that crosses a surface. This principle is used to find electric fields of highly symmetric charge distributions.

The integral form of Gauss's law is

$$
\oint\mathbf{E}\cdot d\mathbf{a} = \dfrac{Q_{\mathrm{enc}}}{\epsilon_{0}}
$$

The differential form of Gauss's law is

$$
\nabla\cdot\mathbf{E} = \dfrac{\rho}{\epsilon_{0}}
$$

where

- $\mathbf{E}$ is the electric field.
- $d\mathbf{a}$ is an outward area element of the closed surface.
- $Q_{\mathrm{enc}}$ is the enclosed charge.
- $\nabla\cdot$ is the divergence.
- $\rho$ is the volume charge density.
- $\epsilon_{0}$ is the permittivity of free space.

The electrostatic potential. A static electric field is conservative, so it is minus the gradient of a scalar potential. A conservative field is a field for which the work around every closed path vanishes. This principle is used to replace a three-component field problem by a single scalar function.

The electrostatic potential difference is

$$
V(\mathbf{b}) - V(\mathbf{a}) = -\displaystyle\int_{\mathbf{a}}^{\mathbf{b}}\mathbf{E}\cdot d\mathbf{l}
$$

The electric field from the potential is

$$
\mathbf{E} = -\nabla V
$$

where

- $V$ is the electric potential.
- $\mathbf{E}$ is the electric field.
- $d\mathbf{l}$ is a displacement along the path.
- $\nabla$ is the gradient.

Electrostatic potential energy. The electrostatic potential energy of a static charge collection is the work required to assemble those charges from infinite separation. This principle is used to compute the energy stored in a charge distribution and in its field.

The electrostatic energy of discrete charges is

$$
W = \dfrac{1}{2}\sum_{i=1}^{n}q_{i}V(\mathbf{r}_{i})
$$

The electrostatic energy of the field is

$$
W = \dfrac{\epsilon_{0}}{2}\displaystyle\int E^{2}\,d\tau
$$

where

- $W$ is the electrostatic potential energy.
- $q_{i}$ is charge $i$.
- $V(\mathbf{r}_{i})$ is the potential at charge $i$ due to the other charges.
- $E$ is the magnitude of the electric field.
- $d\tau$ is the volume element.
- $\epsilon_{0}$ is the permittivity of free space.

The electrostatic properties of conductors. In a conductor at electrostatic equilibrium the interior electric field vanishes, excess charge resides on the surface, and the potential is constant throughout the conductor. A conductor is a material whose charges are free to move. This principle is used to design electrostatic shielding and to set boundary values on conducting surfaces.

The conductor conditions are

$$
\mathbf{E}_{\mathrm{inside}} = 0,\qquad \rho_{\mathrm{inside}} = 0,\qquad V = \mathrm{constant}
$$

where

- $\mathbf{E}_{\mathrm{inside}}$ is the electric field in the bulk of the conductor.
- $\rho_{\mathrm{inside}}$ is the volume charge density in the bulk of the conductor.
- $V$ is the electric potential.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §2.1–2.5 — Coulomb's law, superposition, electric field, Gauss's law, potential, energy, and conductors.
