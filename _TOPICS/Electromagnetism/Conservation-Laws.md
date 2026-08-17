# Conservation Laws

A set of local balance laws that is used to track charge, energy, and momentum of particles and electromagnetic fields, where a local balance law is an equation that relates the change of a density inside a volume to flow through the surface.

1\. Electric charge is never created and never destroyed. If charge inside a volume falls, the same charge must flow out as current. This principle is used as the local statement of charge conservation and as a consistency condition on Maxwell's equations.

The continuity equation is

$$
\nabla\cdot\mathbf{J} = -\dfrac{\partial\rho}{\partial t}
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{J}$ is the volume current density.
- $\rho$ is the volume charge density.
- $t$ is time.

2\. The work done by electromagnetic fields on charges in a volume equals the loss of field energy in that volume minus the energy that leaves through the surface. Energy density is field energy per unit volume. This principle is used to track how field energy becomes mechanical energy or heat.

Poynting's theorem is

$$
\dfrac{dW}{dt} = -\dfrac{d}{dt}\displaystyle\int_{V}u\,d\tau - \oint_{\partial V}\mathbf{S}\cdot d\mathbf{a}
$$

where

- $W$ is the work done on the charges.
- $u$ is the electromagnetic energy density.
- $V$ is the volume.
- $d\tau$ is the volume element.
- $\mathbf{S}$ is the Poynting vector.
- $d\mathbf{a}$ is an outward area element of the boundary.

3\. In an isolated system the sum of mechanical energy and field energy is constant. An isolated system is a system with no electromagnetic energy flux through its boundary. This principle is used to treat field energy as a real contribution to the energy balance.

The electromagnetic energy density is

$$
u = \dfrac{1}{2}\Bigl(\epsilon_{0}E^{2} + \dfrac{1}{\mu_{0}}B^{2}\Bigr)
$$

where

- $u$ is the electromagnetic energy density.
- $E$ is the magnitude of the electric field.
- $B$ is the magnitude of the magnetic field.
- $\epsilon_{0}$ is the permittivity of free space.
- $\mu_{0}$ is the permeability of free space.

4\. The total linear momentum of a closed system is conserved. If the mechanical momentum of the charges changes, the momentum stored in the fields changes by the opposite amount. This principle is used to restore momentum balance when field momentum is included.

The field momentum is

$$
\mathbf{p}_{\mathrm{field}} = \epsilon_{0}\displaystyle\int_{V}\bigl(\mathbf{E}\times\mathbf{B}\bigr)\,d\tau
$$

where

- $\mathbf{p}_{\mathrm{field}}$ is the momentum stored in the fields.
- $\epsilon_{0}$ is the permittivity of free space.
- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.
- $V$ is the volume.
- $d\tau$ is the volume element.

5\. The electromagnetic force on charges in a volume can be written as the flux of a stress tensor through the boundary. A stress tensor is a matrix of force per unit area. This principle is used to compute net electromagnetic force from the fields on a surrounding surface.

The Maxwell stress tensor is

$$
T_{ij} = \epsilon_{0}\Bigl(E_{i}E_{j} - \dfrac{1}{2}\delta_{ij}E^{2}\Bigr) + \dfrac{1}{\mu_{0}}\Bigl(B_{i}B_{j} - \dfrac{1}{2}\delta_{ij}B^{2}\Bigr)
$$

where

- $T_{ij}$ is a component of the Maxwell stress tensor.
- $E_{i}$ and $E_{j}$ are components of the electric field.
- $B_{i}$ and $B_{j}$ are components of the magnetic field.
- $\delta_{ij}$ is the Kronecker delta.
- $\epsilon_{0}$ is the permittivity of free space.
- $\mu_{0}$ is the permeability of free space.

6\. The total angular momentum of a closed system is conserved when the angular momentum stored in the fields is included. Angular momentum density is rotational momentum of the fields per unit volume. This principle is used to resolve electromagnetic rotation paradoxes.

The field angular momentum is

$$
\mathbf{L}_{\mathrm{field}} = \epsilon_{0}\displaystyle\int_{V}\bigl[\mathbf{r}\times(\mathbf{E}\times\mathbf{B})\bigr]\,d\tau
$$

where

- $\mathbf{L}_{\mathrm{field}}$ is the angular momentum stored in the fields.
- $\epsilon_{0}$ is the permittivity of free space.
- $\mathbf{r}$ is the position relative to the origin.
- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.
- $V$ is the volume.
- $d\tau$ is the volume element.

Note: These principles are conservation of electric charge, Poynting's theorem, conservation of electromagnetic energy, conservation of electromagnetic momentum, the Maxwell stress tensor, and conservation of electromagnetic angular momentum.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §8.1–8.2 — continuity, Poynting's theorem, field momentum, Maxwell stress tensor, and field angular momentum.
