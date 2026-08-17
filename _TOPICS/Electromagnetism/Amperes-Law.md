# Ampere's Law

A relation that is used to relate the magnetic field around a closed loop to the current through the enclosed surface, where a closed loop is a path that returns to its starting point.

1\. The line integral of $\mathbf{B}$ around a closed path equals $\mu_{0}$ times the enclosed current. This principle is used to compute $\mathbf{B}$ when symmetry makes the field constant on the path.

Ampère's law in integral form is

$$
\oint\mathbf{B}\cdot d\mathbf{l} = \mu_{0}I_{\mathrm{enc}}
$$

where

- $\mathbf{B}$ is the magnetic field.
- $d\mathbf{l}$ is a displacement along the loop.
- $I_{\mathrm{enc}}$ is the current through any surface bounded by the loop.
- $\mu_{0}$ is the permeability of free space.

2\. In differential form the curl of $\mathbf{B}$ is proportional to the local current density. This principle is used to write the local magnetostatic Maxwell equation.

Ampère's law in differential form is

$$
\nabla\times\mathbf{B} = \mu_{0}\mathbf{J}
$$

where

- $\nabla\times$ is the curl.
- $\mathbf{B}$ is the magnetic field.
- $\mathbf{J}$ is the volume current density.
- $\mu_{0}$ is the permeability of free space.

3\. In time-dependent problems the enclosed current is completed by the displacement current. Displacement current is the term $\epsilon_{0}\dfrac{\partial\mathbf{E}}{\partial t}$ that restores charge conservation. This principle is used to apply Ampère's law to charging capacitors and electromagnetic waves.

The Ampère–Maxwell law is

$$
\oint\mathbf{B}\cdot d\mathbf{l} = \mu_{0}I_{\mathrm{enc}} + \mu_{0}\epsilon_{0}\dfrac{d\Phi_{E}}{dt}
$$

where

- $\Phi_{E}$ is the electric flux through the surface bounded by the loop.
- $\epsilon_{0}$ is the permittivity of free space.
- $t$ is time.

Note: These principles are Ampère's law in integral and differential form and the Ampère–Maxwell correction.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §5.3, §7.3 — Ampère's law and the displacement current.
