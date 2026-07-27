# Normalization

A condition that the integral of $|\psi|^{2}$ equals one that is used to make the total probability of finding the particle somewhere equal to unity.

Note: Also called the normalization condition.

<i>

**definition [d]** (*Normalization*) From Shankar: the statement that the particle has to be somewhere, namely, that all the probabilities add up to $1$, becomes the normalization condition

- $\displaystyle\int_{-\infty}^{\infty} |\psi(x)|^{2}\, dx = \displaystyle\int_{-\infty}^{\infty} P(x)\, dx = 1$ .

Of this family of physically equivalent functions, we are now going to pick one that is normalized, i.e., obeys

- $\displaystyle\int_{-\infty}^{\infty} |\psi(x)|^{2}\, dx = 1$ .

where

- $\psi(x)$ is the wavefunction.
- $P(x) = |\psi(x)|^{2}$ is the probability density.

</i>

<i>

**definition [d]** (*Normalization*) From Hall: for any unit vector $\psi \in L^{2}(\mathbb{R})$,

- $\displaystyle\int_{-\infty}^{\infty} |\psi(x)|^{2}\, dx = 1$ .

where

- $\psi$ is a square-integrable wave function of unit norm.

</i>

<i>

**definition [d]** (*Normalization*) From Sakurai: the probability of recording the particle somewhere between $-\infty$ and $\infty$ is normalized to unity if $|\alpha\rangle$ is normalized:

- $\langle\alpha|\alpha\rangle = 1 \implies \displaystyle\int_{-\infty}^{\infty} dx'\, |\langle x'|\alpha\rangle|^{2} = 1$ .

where

- $|\alpha\rangle$ is a normalized state ket.
- $\langle x'|\alpha\rangle$ is the position-space wavefunction.

</i>

## Elementary Example

### Simple

For $\psi(x) = A$ on $[0,L]$ and zero elsewhere, normalization requires

$$
\int_{0}^{L} |A|^{2}\, dx = 1 \implies |A| = \dfrac{1}{\sqrt{L}}
$$

where

- $A$ is the constant amplitude.
- $L$ is the length of the interval.

### General

If $\psi$ is not normalized but $\displaystyle\int |\psi|^{2} = N > 0$, the normalized wavefunction is

$$
\psi_{\mathrm{norm}} = \dfrac{\psi}{\sqrt{N}}
$$

where

- $N$ is the squared $L^{2}$ norm of $\psi$.

## References

1. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — $\int|\psi|^{2}dx=1$.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — unit vectors in $L^{2}(\mathbb{R})$.
3. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — $\langle\alpha|\alpha\rangle=1$ implies normalized position probability.
