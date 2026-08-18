# Expectation Values

A weighted average of an observable in a quantum state that is used to predict the mean outcome of many measurements of that observable, where an observable is a measurable quantity represented by a Hermitian operator.

1\. The expectation value of an operator $A$ in a normalized state is the sandwich $\langle\psi|A|\psi\rangle$. This principle is used to compute the mean of many repeated measurements.

The expectation value is

$$
\langle A\rangle = \langle\psi|A|\psi\rangle
$$

where

- $A$ is an observable operator.
- $|\psi\rangle$ is the normalized state.
- $\langle A\rangle$ is the expectation value.

2\. The expectation value of position is the first moment of the probability density. This principle is used to compute the mean position from $\Psi(x)$.

The expectation value of position is

$$
\langle x\rangle = \displaystyle\int x\,\lvert\psi(x)\rvert^{2}\,dx
$$

where

- $\langle x\rangle$ is the mean position.
- $\psi(x)$ is the wavefunction.

3\. The uncertainty of an observable is the root-mean-square deviation from the expectation value. This principle is used to compute $\Delta A$ for the uncertainty principle.

The uncertainty is

$$
\Delta A = \sqrt{\langle A^{2}\rangle - \langle A\rangle^{2}}
$$

where

- $\Delta A$ is the uncertainty of $A$.
- $\langle A\rangle$ is the expectation value of $A$.

Note: These principles are the Dirac sandwich, the position mean, and the definition of uncertainty. Also called the mean value.

## References

1. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — $\langle A\rangle=\langle\alpha|A|\alpha\rangle$.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — $E(x)=\int x|\psi|^{2}dx$ and $\langle X\rangle_{\psi}=\langle\psi,X\psi\rangle$.
3. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — $\langle x\rangle=\int P(x)x\,dx$.
