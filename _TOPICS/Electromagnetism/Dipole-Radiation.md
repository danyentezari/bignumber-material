# Dipole Radiation

Electromagnetic radiation from an oscillating electric dipole that is used as the leading radiating multipole for many small sources.

1\. Radiation is energy that leaves the source forever. That requires the outward energy flux, measured by the Poynting vector, to fall no faster than $1/r^{2}$ at large $r$. This principle is used to tell true radiating fields apart from near fields that keep energy near the charges.

The radiated power is

$$
P_{\mathrm{rad}}(t) = \lim_{r\to\infty}\oint\mathbf{S}\cdot d\mathbf{a}
$$

where

- $P_{\mathrm{rad}}$ is the radiated power.
- $\mathbf{S}$ is the Poynting vector.
- $d\mathbf{a}$ is the outward vector area element.
- $r$ is the distance from the source.

2\. In the radiation zone, distances much larger than both the source size and the wavelength, the $1/r^{3}$ and $1/r^{2}$ near fields die away and only the $1/r$ wave fields remain. This principle is used to replace the full near-zone fields by simple wave fields at large distance.

3\. In that zone the electric and magnetic fields are transverse to the travel direction, perpendicular to each other, in phase, and related by $E/B = c$. Retarded time is the emission time at the source. This principle is used to find the fields that a distant receiver measures.

The radiation-zone dipole fields are

$$
\mathbf{E}(r,\theta,t) \approx \dfrac{\mu_{0}}{4\pi}\dfrac{\sin\theta}{r}\,\dfrac{d^{2}p}{dt^{2}}(t_{r})\,\hat{\boldsymbol{\theta}}
$$

$$
\mathbf{B}(r,\theta,t) \approx \dfrac{\mu_{0}}{4\pi c}\dfrac{\sin\theta}{r}\,\dfrac{d^{2}p}{dt^{2}}(t_{r})\,\hat{\boldsymbol{\phi}}
$$

where

- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.
- $p$ is the electric dipole moment along the $z$ axis.
- $t_{r} = t - r/c$ is the retarded time.
- $\theta$ is the polar angle from the dipole axis.
- $r$ is the distance from the source.
- $\mu_{0}$ is the permeability of free space.
- $c$ is the speed of light.

4\. An oscillating dipole radiates no power along its axis and maximum power in the equatorial plane, so the intensity pattern is donut-shaped. Intensity is the time-averaged energy flux. This principle is used to aim antennas so power goes where receivers sit.

The time-averaged Poynting vector is

$$
\langle\mathbf{S}\rangle = \dfrac{\mu_{0}p_{0}^{2}\omega^{4}}{32\pi^{2}c}\dfrac{\sin^{2}\theta}{r^{2}}\,\hat{\mathbf{r}}
$$

where

- $\langle\mathbf{S}\rangle$ is the time-averaged Poynting vector.
- $p_{0}$ is the amplitude of the oscillating dipole.
- $\omega$ is the angular frequency.
- $\theta$ is the polar angle from the dipole axis.
- $r$ is the distance from the source.

5\. The total average power of a sinusoidally oscillating dipole scales as $\omega^{4}$. Angular frequency is the oscillation rate in radians per second. This principle is used to explain why high-frequency sources radiate far more efficiently than low-frequency ones.

The average dipole power is

$$
\langle P\rangle = \dfrac{\mu_{0}p_{0}^{2}\omega^{4}}{12\pi c}
$$

where

- $\langle P\rangle$ is the time-averaged radiated power.
- $p_{0}$ is the dipole amplitude.
- $\omega$ is the angular frequency.

6\. A charge at rest does not radiate, and a charge in uniform motion does not radiate; acceleration does, with power proportional to the square of the acceleration. This principle is used to compute radiative energy loss of accelerating charges.

The Larmor formula is

$$
P = \dfrac{\mu_{0}q^{2}a^{2}}{6\pi c}
$$

where

- $P$ is the radiated power.
- $q$ is the charge.
- $a$ is the magnitude of the acceleration.

7\. For a source small compared with the wavelength, electric dipole radiation dominates; magnetic dipole and electric quadrupole terms are suppressed by powers of size over wavelength. A multipole expansion ranks those radiator terms. This principle is used to treat small antennas and molecules as electric dipoles first.

Note: These principles are the radiation criterion, the radiation-zone approximation, the radiation-zone field equations, the dipole radiation pattern, the $\omega^{4}$ dipole power law, the Larmor formula, and electric-dipole dominance in the multipole expansion. Also called electric dipole radiation.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §11.1.1–11.1.4, §11.2.1 — radiation criterion, radiation zone, dipole fields and power, Larmor formula.
2. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — accelerating charges radiate.
