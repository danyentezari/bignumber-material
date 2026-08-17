# Operators

A linear mapping on a Hilbert space that is used to represent a physical observable acting on quantum states, where a Hilbert space is a complete inner-product space of states.

1\. Each classical real function on phase space is associated with a self-adjoint operator on the quantum Hilbert space. A self-adjoint operator is an operator equal to its adjoint. This principle is used to promote $x$ and $p$ to $\hat{x}$ and $\hat{p}$.

2\. Observables act on kets. A Hermitian operator has real eigenvalues. This principle is used to identify measured values with those eigenvalues.

3\. The expectation value of an operator $A$ in a normalized state is $\langle A\rangle=\langle\alpha|A|\alpha\rangle$. This principle is used to compute the mean of many measurements.

The expectation value is

$$
\langle A\rangle = \langle\alpha|A|\alpha\rangle
$$

where

- $A$ is an observable operator.
- $|\alpha\rangle$ is a normalized state.

4\. In the position representation the position operator multiplies by $x$ and the momentum operator differentiates. This principle is used to write explicit operators on wavefunctions.

The position and momentum operators are

$$
(\hat{x}\psi)(x) = x\psi(x),\qquad (\hat{p}\psi)(x) = -i\hbar\dfrac{d\psi}{dx}
$$

where

- $\psi$ is a wavefunction.
- $\hbar$ is the reduced Planck constant.

Note: These principles are the quantization map to self-adjoint operators, Hermitian observables, expectation values, and the position-representation operators. Also called quantum operators.

## Elementary Example

### Simple

The position operator multiplies by $x$ in the position representation:

$$
(\hat{x}\psi)(x) = x\psi(x)
$$

where

- $\psi$ is a wavefunction.
- $\hat{x}$ is the position operator.

### General

A general observable $A$ acts on a state ket $|\alpha\rangle$ to produce another ket $A|\alpha\rangle$, and its expectation value is

$$
\langle A\rangle = \langle\alpha|A|\alpha\rangle
$$

where

- $|\alpha\rangle$ is a normalized state.

## References

1. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — Axiom 2: classical $f$ associated with self-adjoint $\hat{f}$.
2. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — observables represented by Hermitian operators on kets.
