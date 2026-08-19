# Multipole Expansion

A series expansion of the potential of a localized charge distribution that is used to organize contributions by monopole, dipole, quadrupole, and higher moments, where a localized charge distribution is a charge collection confined to a finite region.

The multipole expansion of the potential. Far from a localized charge distribution the potential can be expanded in inverse powers of distance. This principle is used to replace a complicated source by a sequence of simpler terms that fall off faster and faster.

The multipole expansion of the potential is

$$
V(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}}\sum_{n=0}^{\infty}\dfrac{1}{r^{n+1}}\displaystyle\int (r')^{n}P_{n}(\cos\alpha)\,\rho(\mathbf{r}')\,d\tau'
$$

where

- $V$ is the electric potential.
- $r$ is the distance to the field point.
- $r'$ is the distance of a source element from the origin.
- $P_{n}$ is the $n$th Legendre polynomial.
- $\alpha$ is the angle between $\mathbf{r}$ and $\mathbf{r}'$.
- $\rho$ is the charge density.
- $d\tau'$ is the volume element.
- $\epsilon_{0}$ is the permittivity of free space.

The monopole term. The first term is the monopole potential of the total charge. This principle is used to treat a distant charge collection as a point charge when the net charge is not zero.

The monopole term is

$$
V_{\mathrm{mon}}(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}}\dfrac{Q}{r}
$$

where

- $V_{\mathrm{mon}}$ is the monopole potential.
- $Q$ is the total charge.
- $r$ is the distance to the field point.
- $\epsilon_{0}$ is the permittivity of free space.

The dipole term. The next term is the dipole potential of the dipole moment. This principle is used to describe a neutral charge collection whose opposite charges are slightly separated.

The dipole term is

$$
V_{\mathrm{dip}}(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}}\dfrac{\mathbf{p}\cdot\hat{\mathbf{r}}}{r^{2}}
$$

where

- $V_{\mathrm{dip}}$ is the dipole potential.
- $\mathbf{p}$ is the electric dipole moment.
- $\hat{\mathbf{r}}$ is the unit vector toward the field point.
- $r$ is the distance to the field point.
- $\epsilon_{0}$ is the permittivity of free space.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — multipole expansion of $V$.
2. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — dipole moment $\mathbf{p}$.
3. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — far-field multipole viewpoint.
