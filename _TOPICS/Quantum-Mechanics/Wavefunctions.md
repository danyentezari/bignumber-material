# Wavefunctions

A complex-valued function that is used to describe the physical state of a quantum system, where the absolute square of the function is the probability density of finding the particle.

1\. The state of a particle in one dimension is a wavefunction $\Psi(x,t)$. This principle is used to replace a classical trajectory by a function of position and time.

2\. The probability of finding the particle in an interval is the integral of $|\Psi|^{2}$ over that interval. This principle is used to compute all position probabilities from one function.

The Born rule is

$$
P(a\leq x\leq b) = \displaystyle\int_{a}^{b}\lvert\Psi(x,t)\rvert^{2}\,dx
$$

where

- $P$ is the finding probability.
- $\Psi$ is the wavefunction.

3\. The wavefunction must be normalizable so that the total probability is one. This principle is used to discard solutions that grow at infinity.

The normalization condition is

$$
\displaystyle\int_{-\infty}^{\infty}\lvert\Psi(x,t)\rvert^{2}\,dx = 1
$$

where

- $\Psi$ is the wavefunction.

4\. The wavefunction evolves according to the Schrödinger equation. This principle is used to compute $\Psi$ at a later time.

5\. A global phase factor $e^{i\alpha}$ does not change any probability. This principle is used to treat wavefunctions that differ by a constant phase as the same physical state.

Note: These principles are the wavefunction as the state, the Born rule, normalization, Schrödinger evolution, and irrelevance of a global phase.

## References

1. Griffiths, D. J. *Introduction to Quantum Mechanics*. Cambridge University Press, 2018. §1.2–1.4 — wavefunctions and the statistical interpretation.
2. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — position-space wavefunction.
