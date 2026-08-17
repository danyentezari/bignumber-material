# Maxwell's Equations

A set of four field equations that is used to describe how electric and magnetic fields arise from charges and currents and how the fields generate each other, where a field equation is a differential equation that relates a field to its sources.

1\. Electric charge produces electric field that spreads from the charge. Charge density is charge per unit volume. Divergence is a measure of how much a vector field spreads from a point. This principle is used to find the electric field of a given charge distribution.

Gauss's law is

$$
\nabla\cdot\mathbf{E} = \dfrac{\rho}{\epsilon_{0}}
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{E}$ is the electric field.
- $\rho$ is the volume charge density.
- $\epsilon_{0}$ is the permittivity of free space.

2\. Magnetic field lines form closed loops with no beginning and no end. A magnetic monopole is an isolated single magnetic pole. No magnetic monopole has been observed. This principle is used to constrain magnetic fields so they never diverge from a point source.

Gauss's law for magnetism is

$$
\nabla\cdot\mathbf{B} = 0
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{B}$ is the magnetic field.

3\. A magnetic field that changes in time produces a swirling electric field around the changing magnetic field. Curl is a measure of the local swirl of a vector field. Electromagnetic induction is the generation of electric field by a changing magnetic field. This principle is used to design generators, transformers, and inductors.

Faraday's law is

$$
\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}
$$

where

- $\nabla\times$ is the curl.
- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.
- $t$ is time.

4\. Magnetic fields are produced by electric current and by electric fields that change in time. Current density is charge flow per unit area. The displacement current is Maxwell's addition: a changing electric field that sources magnetic field as a current does. This principle is used to compute fields of electromagnets and to show that electromagnetic waves travel in empty space.

The Ampère-Maxwell law is

$$
\nabla\times\mathbf{B} = \mu_{0}\mathbf{J} + \mu_{0}\epsilon_{0}\dfrac{\partial\mathbf{E}}{\partial t}
$$

where

- $\nabla\times$ is the curl.
- $\mathbf{B}$ is the magnetic field.
- $\mu_{0}$ is the permeability of free space.
- $\mathbf{J}$ is the volume current density.
- $\epsilon_{0}$ is the permittivity of free space.
- $\mathbf{E}$ is the electric field.
- $t$ is time.

5\. Electric charge is never created and never destroyed: if charge inside a volume falls, the same charge must flow out through the surface. Local conservation is the requirement that a conserved quantity move continuously through space. This principle is used to tie charge density to current density as a consistency condition.

The continuity equation is

$$
\nabla\cdot\mathbf{J} = -\dfrac{\partial\rho}{\partial t}
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{J}$ is the volume current density.
- $\rho$ is the volume charge density.
- $t$ is time.

Note: These principles are Gauss's law, Gauss's law for magnetism, Faraday's law of induction, the Ampère-Maxwell law, and the continuity equation. Gauss's law for magnetism is also called the no-monopole law. The Ampère-Maxwell law is also called Ampère's law with Maxwell's correction. The continuity equation is also called local charge conservation.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §2.2.4, §5.1.3, §5.3.2, §7.2.1, §7.3.1, §7.3.3, §8.1.1 — Maxwell equations and continuity.
