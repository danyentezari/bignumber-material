# Differential Form

A local differential statement of Maxwell's equations that is used to relate the fields pointwise to charge and current densities, where a local statement is an equation that holds at each point in space.

1\. The divergence of the electric field at a point is proportional to the charge density at that point. Divergence is a measure of how much a vector field spreads from a point. Charge density is charge per unit volume. This principle is used to find the electric field of a given charge distribution.

The differential form of Gauss's law is

$$
\nabla\cdot\mathbf{E} = \dfrac{\rho}{\epsilon_{0}}
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{E}$ is the electric field.
- $\rho$ is the volume charge density.
- $\epsilon_{0}$ is the permittivity of free space.

2\. The divergence of the magnetic field is zero at every point. This principle is used to constrain magnetic fields so they never begin or end at a point source.

The differential form of Gauss's law for magnetism is

$$
\nabla\cdot\mathbf{B} = 0
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{B}$ is the magnetic field.

3\. The curl of the electric field equals the negative time derivative of the magnetic field. Curl is a measure of the local swirl of a vector field. This principle is used to compute the electric field induced by a changing magnetic field.

The differential form of Faraday's law is

$$
\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}
$$

where

- $\nabla\times$ is the curl.
- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.
- $t$ is time.

4\. The curl of the magnetic field is sourced by current density and by a changing electric field. Current density is charge flow per unit area. This principle is used to compute magnetic fields of currents and of changing electric fields.

The differential form of the Ampère-Maxwell law is

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

Note: These principles are the differential form of Gauss's law, Gauss's law for magnetism, Faraday's law, and the Ampère-Maxwell law. Also called the differential form of Maxwell's equations.

## Elementary Example

### Simple

In empty space with no charges or currents,

$$
\nabla\cdot\mathbf{E} = 0,\quad \nabla\cdot\mathbf{B} = 0
$$

where

- both fields are divergenceless.

### General

With sources $\rho$ and $\mathbf{J}$,

$$
\nabla\cdot\mathbf{E} = \dfrac{\rho}{\epsilon_{0}},\quad \nabla\times\mathbf{B} = \mu_{0}\mathbf{J} + \mu_{0}\epsilon_{0}\dfrac{\partial\mathbf{E}}{\partial t}
$$

where

- the electric field and magnetic field couple to the sources.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §2.2.4, §5.3.2, §7.2.1, §7.3.3 — differential Maxwell equations.
2. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — differential form via divergence and Stokes theorems.
3. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — differential Maxwell equations.
