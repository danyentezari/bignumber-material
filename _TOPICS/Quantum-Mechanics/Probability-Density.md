# Probability Density

A nonnegative function built from a wavefunction that is used to give the probability of finding a particle in a region of space.

Note: Also called the position probability density.

<i>

**definition [d]** (*Probability Density*) From Sakurai: the quantity $\rho(x', t)$ defined by

- $\rho(x', t) = |\psi(x', t)|^{2} = |\langle x'|\alpha, t_{0}; t\rangle|^{2}$

is therefore regarded as the probability density in wave mechanics. Specifically, when we use a detector that ascertains the presence of the particle within a small volume element $d^{3}x'$ around $x'$, the probability of recording a positive result at time $t$ is given by $\rho(x', t)\, d^{3}x'$.

where

- $\psi(x', t)$ is the wavefunction in the position representation.
- $\rho(x', t)$ is the probability density.
- $d^{3}x'$ is a small volume element about $x'$.

</i>

<i>

**definition [d]** (*Probability Density*) From Hall: the function $|\psi(x)|^{2}$ is supposed to be the probability density for the position of the particle. This means that the probability that the position of the particle belongs to some set $E \subset \mathbb{R}$ is

- $\displaystyle\int_{E} |\psi(x)|^{2}\, dx$ .

where

- $\psi : \mathbb{R} \rightarrow \mathbb{C}$ is the wave function.
- $E$ is a subset of the real line.

</i>

<i>

**definition [d]** (*Probability Density*) From Shankar: we introduce the notion of a probability density $P(x)$ defined as follows:

- $|\psi(x)|^{2}\, dx \equiv P(x)\, dx =$ the probability the particle is found between $x$ and $x + dx$ .

where

- $\psi(x)$ is the wavefunction.
- $P(x) = |\psi(x)|^{2}$ is the probability density.
- $dx$ is an infinitesimal interval.

</i>

## Elementary Example

### Simple

For a normalized wavefunction constant on $[0,2]$ and zero elsewhere,

$$
\psi(x) = \dfrac{1}{\sqrt{2}},\quad x \in [0,2]
$$

$$
P(x) = |\psi(x)|^{2} = \dfrac{1}{2}
$$

where

- $P(x)$ is the probability density on that interval.

### General

The probability that the particle lies in $[0,1]$ is

$$
\int_{0}^{1} P(x)\, dx = \dfrac{1}{2}
$$

where

- the integral of $P$ over a set is the finding probability.

## References

1. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — $\rho=|\psi|^{2}$ as probability density.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — $|\psi(x)|^{2}$ as position probability density.
3. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — $P(x)dx=|\psi(x)|^{2}dx$.
