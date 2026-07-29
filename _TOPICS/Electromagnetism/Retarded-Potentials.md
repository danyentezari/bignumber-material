# Retarded Potentials

Potentials evaluated at the retarded time that is used to express the electromagnetic response of sources at the earlier time when signals left them.

Note: Also called retarded potentials for $V$ and $\mathbf{A}$.

<i>

**definition [d]** (*Retarded Potentials*) From Griffiths: the retarded potentials are

- $V(\mathbf{r}, t) = \dfrac{1}{4\pi\epsilon_{0}}\displaystyle\int\dfrac{\rho(\mathbf{r}', t_{r})}{|\mathbf{r}-\mathbf{r}'|}\,d\tau'$ ,
- $\mathbf{A}(\mathbf{r}, t) = \dfrac{\mu_{0}}{4\pi}\displaystyle\int\dfrac{\mathbf{J}(\mathbf{r}', t_{r})}{|\mathbf{r}-\mathbf{r}'|}\,d\tau'$ ,

where the retarded time is $t_{r} = t - |\mathbf{r}-\mathbf{r}'|/c$.

where

- $\rho$ and $\mathbf{J}$ are evaluated at $t_{r}$.
- $c$ is the speed of light.

</i>

<i>

**definition [d]** (*Retarded Time*) From Griffiths: the retarded time is the time at which a signal traveling at speed $c$ from the source point must have left in order to arrive at the field point at time $t$.

where

- $t_{r} = t - R/c$ with $R = |\mathbf{r}-\mathbf{r}'|$.

</i>

<i>

**definition [d]** (*Retarded Potentials*) From Knight: electromagnetic influences propagate at the speed of light, so potentials at a point depend on the sources at earlier retarded times.

where

- causality is built into the retarded solution.

</i>

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
