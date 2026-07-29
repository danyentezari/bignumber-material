# Multipole Expansion

A series expansion of the potential or field of a localized charge distribution that is used to organize contributions by monopole, dipole, quadrupole, and higher moments.

Note: Also called the multipole expansion of the potential.

<i>

**definition [d]** (*Multipole Expansion*) From Griffiths: for a localized charge distribution, the potential far away can be expanded as

- $V(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}}\sum_{n=0}^{\infty}\dfrac{1}{r^{n+1}}\int (r')^{n}P_{n}(\cos\alpha)\,\rho(\mathbf{r}')\,d\tau'$ ,

which begins with the monopole term, then dipole, quadrupole, and so on.

where

- $r$ is the distance to the field point.
- $\rho$ is the charge density.
- $P_{n}$ are Legendre polynomials.

</i>

<i>

**definition [d]** (*Dipole Term*) From Griffiths: the leading correction after the total charge is the dipole term involving

- $\mathbf{p} = \displaystyle\int\mathbf{r}'\rho(\mathbf{r}')\,d\tau'$ .

where

- $\mathbf{p}$ is the electric dipole moment.

</i>

<i>

**definition [d]** (*Multipole Expansion*) From Knight: a compact charge distribution looks, from far away, like a point charge plus dipole and higher corrections whose importance falls with distance.

where

- distant observers see the lowest nonvanishing multipole first.

</i>

## Elementary Example

### Simple

A pure point charge $Q$ has only the monopole term

$$
V(r) = \dfrac{1}{4\pi\epsilon_{0}}\dfrac{Q}{r}
$$

where

- all higher multipoles vanish.

### General

A neutral dipole with moment $\mathbf{p}$ has

$$
V(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}}\dfrac{\mathbf{p}\cdot\hat{\mathbf{r}}}{r^{2}}
$$

where

- the monopole term is absent.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — multipole expansion of $V$.
2. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — dipole moment $\mathbf{p}$.
3. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — far-field multipole viewpoint.
