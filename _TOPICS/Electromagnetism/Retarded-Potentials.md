# Retarded Potentials

Potentials evaluated at the retarded time that are used to express the electromagnetic response of sources at the earlier time when signals left them, where retarded time is the emission time at a source point.

1\. Electromagnetic influences propagate at the speed of light, so the potentials at a field point depend on the sources at earlier times. This principle is used to build causality into the solution of Maxwell's equations.

The retarded time is

$$
t_{r} = t - \dfrac{|\mathbf{r}-\mathbf{r}'|}{c}
$$

where

- $t_{r}$ is the retarded time.
- $t$ is the observation time.
- $\mathbf{r}$ is the field point.
- $\mathbf{r}'$ is the source point.
- $c$ is the speed of light.

2\. The retarded scalar potential is the Coulomb integral of the charge density at the retarded time. This principle is used to compute $V$ of a time-dependent charge distribution.

The retarded scalar potential is

$$
V(\mathbf{r}, t) = \dfrac{1}{4\pi\epsilon_{0}}\displaystyle\int\dfrac{\rho(\mathbf{r}', t_{r})}{|\mathbf{r}-\mathbf{r}'|}\,d\tau'
$$

where

- $V$ is the scalar potential.
- $\rho$ is the charge density evaluated at $t_{r}$.
- $\epsilon_{0}$ is the permittivity of free space.
- $d\tau'$ is the volume element.

3\. The retarded vector potential is the corresponding integral of the current density. This principle is used to compute $\mathbf{A}$ of a time-dependent current.

The retarded vector potential is

$$
\mathbf{A}(\mathbf{r}, t) = \dfrac{\mu_{0}}{4\pi}\displaystyle\int\dfrac{\mathbf{J}(\mathbf{r}', t_{r})}{|\mathbf{r}-\mathbf{r}'|}\,d\tau'
$$

where

- $\mathbf{A}$ is the vector potential.
- $\mathbf{J}$ is the current density evaluated at $t_{r}$.
- $\mu_{0}$ is the permeability of free space.

Note: These principles are retarded time, the retarded scalar potential, and the retarded vector potential. Also called retarded potentials for $V$ and $\mathbf{A}$.

## Elementary Example

### Simple

For a static point charge, $t_{r}$ dependence drops out and

$$
V = \dfrac{1}{4\pi\epsilon_{0}}\dfrac{q}{r}
$$

where

- the Coulomb potential is recovered.

### General

For time-dependent $\rho$ and $\mathbf{J}$, both integrals use

$$
t_{r} = t - \dfrac{|\mathbf{r}-\mathbf{r}'|}{c}
$$

where

- each source point has its own retarded time.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — retarded $V$ and $\mathbf{A}$.
2. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — retarded time $t_{r}$.
3. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — finite propagation speed of electromagnetic influences.
