# Expectation Values

A weighted average of an observable in a quantum state that is used to predict the mean outcome of many measurements of that observable.

Note: Also called the expectation value. Also called the mean value.

<i>

**definition [d]** (*Expectation Value*) From Sakurai: we define the expectation value of $A$ taken with respect to state $|\alpha\rangle$ as

- $\langle A\rangle \equiv \langle\alpha|A|\alpha\rangle$ .

where

- $A$ is an observable operator.
- $|\alpha\rangle$ is the state ket.
- $\langle A\rangle$ is the expectation value.

</i>

<i>

**definition [d]** (*Expectation Value of Position*) From Hall: if $|\psi(x)|^{2}$ is the probability density for the position of a particle, then according to the standard definitions of probability theory, the expectation value of the position will be

- $E(x) = \displaystyle\int_{\mathbb{R}} x\, |\psi(x)|^{2}\, dx$ .

We use the following notation for the expectation value of the operator $X$ in the state $\psi$:

- $\langle X\rangle_{\psi} := \langle\psi, X\psi\rangle$ .

where

- $\psi$ is the wave function.
- $X$ is the position operator.
- $E(x)$ is the mean position.

</i>

<i>

**definition [d]** (*Expectation Value*) From Shankar: in the context of quantum theory $P(x)=|\psi(x)|^{2}$, $\langle x\rangle$ is called the expectation value, with

- $\langle x\rangle = \displaystyle\int P(x)\, x\, dx$ .

where

- $P(x)$ is the probability density.
- $\langle x\rangle$ is the expectation value of position.

</i>

## Elementary Example

### Simple

For $P(x) = \dfrac{1}{2}$ on $[0,2]$,

$$
\langle x\rangle = \int_{0}^{2} x\cdot\dfrac{1}{2}\, dx = 1
$$

where

- $\langle x\rangle$ is the mean position.

### General

For a general observable $A$ in state $|\psi\rangle$,

$$
\langle A\rangle = \langle\psi|A|\psi\rangle
$$

where

- $|\psi\rangle$ is normalized.

## References

1. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — $\langle A\rangle=\langle\alpha|A|\alpha\rangle$.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — $E(x)=\int x|\psi|^{2}dx$ and $\langle X\rangle_{\psi}=\langle\psi,X\psi\rangle$.
3. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — $\langle x\rangle=\int P(x)x\,dx$.
