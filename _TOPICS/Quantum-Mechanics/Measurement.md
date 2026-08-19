# Measurement

A process that yields an eigenvalue of an observable and updates the state that is used to connect a quantum state to a definite laboratory outcome, where an eigenvalue is an allowed measured value of that observable.

The eigenvalue-outcome rule. A measurement of an observable $A$ yields one of the eigenvalues of $A$. This principle is used to list the possible laboratory outcomes.

Collapse to an eigenstate. If the result is the eigenvalue $a'$, the state immediately afterward is the corresponding eigenstate. This principle is used to update the state after a measurement.

The collapse to an eigenstate is

$$
\hat{A}|\psi'\rangle = a'|\psi'\rangle
$$

where

- $\hat{A}$ is the operator for the observable.
- $a'$ is the measured eigenvalue.
- $|\psi'\rangle$ is the state immediately after the measurement.

The Born probability rule. If the state before measurement is $\sum c_{n}|a_{n}\rangle$, the probability of result $a_{n}$ is $|c_{n}|^{2}$. This principle is used to compute the statistics of repeated measurements.

The Born rule for a discrete spectrum is

$$
P(a_{n}) = \lvert\langle a_{n}|\psi\rangle\rvert^{2}
$$

where

- $P(a_{n})$ is the probability of eigenvalue $a_{n}$.
- $|\psi\rangle$ is the state before measurement.
- $|a_{n}\rangle$ is the corresponding eigenket.

Note: Also called the collapse of the wave function when the post-measurement state is emphasized.

## References

1. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — Axiom 4: measurement result $\lambda$ and collapse to an eigenstate of $\hat{f}$.
2. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — measurement yields an eigenvalue of the observable.
