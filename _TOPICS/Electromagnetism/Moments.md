# Moments

Integral quantities of a charge distribution that are used to characterize successive terms in a multipole expansion, where a multipole expansion is a series that organizes a distant potential by inverse powers of distance.

1\. The monopole moment is the total charge of the distribution. This principle is used to write the leading term of the potential when the net charge is not zero.

The monopole moment is

$$
Q = \displaystyle\int\rho(\mathbf{r}')\,d\tau'
$$

where

- $Q$ is the monopole moment.
- $\rho$ is the charge density.
- $d\tau'$ is the volume element.

2\. The dipole moment is the first moment of the charge density. This principle is used to write the leading term of the potential of a neutral charge collection.

The dipole moment is

$$
\mathbf{p} = \displaystyle\int\mathbf{r}'\rho(\mathbf{r}')\,d\tau'
$$

where

- $\mathbf{p}$ is the electric dipole moment.
- $\mathbf{r}'$ is the source-point position.
- $\rho$ is the charge density.
- $d\tau'$ is the volume element.

3\. Higher moments involve higher powers of the source coordinate. This principle is used to continue the expansion when the monopole and dipole both vanish.

The quadrupole and higher moments enter the potential through powers $(r')^{n}$ with $n\geq 2$.

where

- $r'$ is the distance of a source element from the origin.
- $n$ is the order of the multipole.

Note: These principles are the monopole moment, the dipole moment, and the higher multipole moments. Also called multipole moments.

## Elementary Example

### Simple

A single point charge $q$ at the origin has monopole moment

$$
Q = q
$$

and vanishing dipole moment $\mathbf{p} = \mathbf{0}$.

where

- only the monopole survives.

### General

Two charges $+q$ and $-q$ separated by vector $\mathbf{d}$ have

$$
Q = 0,\quad \mathbf{p} = q\mathbf{d}
$$

where

- the monopole vanishes and the dipole is the leading moment.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — multipole moments $Q$, $\mathbf{p}$, and higher.
2. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — far-field multipole moments.
3. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — expansion coefficients for localized sources.
