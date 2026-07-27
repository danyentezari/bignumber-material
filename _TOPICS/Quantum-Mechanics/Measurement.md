# Measurement

A process that yields an eigenvalue of an observable and updates the state that is used to connect a quantum state to a definite laboratory outcome.

Note: Also called the collapse of the wave function when the post-measurement state is emphasized.

<i>

**definition [d]** (*Measurement*) From Hall: suppose a quantum system is initially in a state $\psi$ and that a measurement of an observable $f$ is performed. If the result of the measurement is the number $\lambda \in \mathbb{R}$, then immediately after the measurement, the system will be in a state $\psi'$ that satisfies

- $\hat{f}\psi' = \lambda\psi'$ .

The passage from $\psi$ to $\psi'$ is called the collapse of the wave function. Here $\hat{f}$ is the self-adjoint operator associated with $f$.

where

- $\psi$ is the state before measurement.
- $f$ is the observable being measured.
- $\lambda$ is the measured value.
- $\psi'$ is the state immediately after measurement.
- $\hat{f}$ is the self-adjoint operator for $f$.

</i>

<i>

**definition [d]** (*Measurement*) From Sakurai: when the measurement causes $|\alpha\rangle$ to change into $|a'\rangle$, it is said that $A$ is measured to be $a'$. It is in this sense that the result of a measurement yields one of the eigenvalues of the observable being measured.

where

- $|\alpha\rangle$ is the state before measurement.
- $|a'\rangle$ is an eigenket of the observable $A$.
- $a'$ is the corresponding eigenvalue.

</i>

## Elementary Example

### Simple

Measuring $S_{z}$ on a spin-up eigenstate $|+\rangle$ yields $+\hbar/2$ and leaves the state $|+\rangle$.

$$
\hat{S}_{z}|+\rangle = \dfrac{\hbar}{2}|+\rangle
$$

where

- the post-measurement state is already an eigenstate.

### General

If $|\psi\rangle = c_{+}|+\rangle + c_{-}|-\rangle$, a measurement of $S_{z}$ yields $+\hbar/2$ or $-\hbar/2$ and collapses to $|+\rangle$ or $|-\rangle$ accordingly.

$$
P(+) = |c_{+}|^{2},\quad P(-) = |c_{-}|^{2}
$$

where

- $c_{\pm}$ are the expansion coefficients.

## References

1. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — Axiom 4: measurement result $\lambda$ and collapse to an eigenstate of $\hat{f}$.
2. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — measurement yields an eigenvalue of the observable.
