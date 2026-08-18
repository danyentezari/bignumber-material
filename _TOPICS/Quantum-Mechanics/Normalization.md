# Normalization

A condition that the integral of $|\psi|^{2}$ equals one that is used to make the total probability of finding the particle somewhere equal to unity.

1\. The particle has to be somewhere, so all position probabilities add to one. This principle is used to fix the overall scale of the wavefunction.

The normalization condition is

$$
\displaystyle\int_{-\infty}^{\infty}\lvert\psi(x)\rvert^{2}\,dx = 1
$$

where

- $\psi(x)$ is the wavefunction.

2\. In Dirac notation the same statement is that the state ket has unit norm. This principle is used to normalize abstract states as well as wavefunctions.

The ket normalization is

$$
\langle\alpha|\alpha\rangle = 1
$$

where

- $|\alpha\rangle$ is the state ket.

3\. If a wavefunction is not yet normalized, dividing by the square root of its squared norm produces a normalized wavefunction. This principle is used to convert any square-integrable solution into a physical state.

The normalized wavefunction is

$$
\psi_{\mathrm{norm}} = \dfrac{\psi}{\sqrt{N}},\qquad N = \displaystyle\int\lvert\psi\rvert^{2}\,dx
$$

where

- $N$ is the squared $L^{2}$ norm of $\psi$.

Note: These principles are the integral normalization condition, ket normalization, and rescaling to unit norm. Also called the normalization condition.

## References

1. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — $\int|\psi|^{2}dx=1$.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — unit vectors in $L^{2}(\mathbb{R})$.
3. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — $\langle\alpha|\alpha\rangle=1$ implies normalized position probability.
