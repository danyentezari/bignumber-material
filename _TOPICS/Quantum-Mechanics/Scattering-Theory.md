# Scattering Theory

A framework for collisions that is used to relate incoming free-particle states to outgoing amplitudes and cross sections, where a cross section is an effective area that measures the likelihood of a scattering event.

1\. An incident beam interacting with a short-range target produces an outgoing wave. In the far region the wavefunction is an incident plane wave plus a scattered spherical wave. This principle is used to define the scattering amplitude $f$.

The asymptotic scattered wave is

$$
\psi(\mathbf{r}) \sim e^{ikz} + f(\theta,\phi)\dfrac{e^{ikr}}{r}
$$

where

- $f$ is the scattering amplitude.
- $\theta$ and $\phi$ are scattering angles.
- $k$ is the wave number.
- $r$ is the distance from the target.

2\. The differential cross section is the squared modulus of the scattering amplitude. This principle is used to convert $f$ into a measured angular distribution.

The differential cross section is

$$
\dfrac{d\sigma}{d\Omega} = \lvert f(\theta,\phi)\rvert^{2}
$$

where

- $\sigma$ is the cross section.
- $\Omega$ is solid angle.
- $f$ is the scattering amplitude.

3\. In one dimension the same problem is stated as reflection and transmission amplitudes. This principle is used to analyze barriers and wells on the line.

Note: These principles are the incident-plus-scattered wave, the differential cross section, and one-dimensional reflection and transmission. Also called quantum scattering.

## Elementary Example

### Simple

In one dimension, an incident wave $e^{ikx}$ on a barrier yields reflection and transmission amplitudes $R$ and $T$ with

$$
|R|^{2} + |T|^{2} = 1
$$

for a real potential without absorption.

where

- probability is conserved.

### General

In three dimensions,

$$
\dfrac{d\sigma}{d\Omega} = |f(\theta,\phi)|^{2}
$$

where

- the differential cross section is the squared amplitude.

## References

1. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — incident plus scattered wave; amplitude $f$.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — scattering states for short-range potentials.
3. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — $\dfrac{d\sigma}{d\Omega}=|f|^{2}$.
