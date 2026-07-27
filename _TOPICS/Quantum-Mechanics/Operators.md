# Operators

A linear mapping on a Hilbert space that is used to represent a physical observable acting on quantum states.

Note: Also called quantum operators. Observables of interest are represented by Hermitian operators.

<i>

**definition [d]** (*Operators*) From Hall: to each real-valued function $f$ on the classical phase space there is associated a self-adjoint operator $\hat{f}$ on the quantum Hilbert space.

where

- $f$ is a classical observable as a real-valued function on phase space.
- $\hat{f}$ is the corresponding self-adjoint operator.
- the quantum Hilbert space is the space of states.

</i>

<i>

**definition [d]** (*Operators*) From Sakurai: observables like momentum and spin components are to be represented by operators that can act on kets. We can consider a more general class of operators that act on kets; they will be denoted by $X$, $Y$, and so forth, while $A$, $B$, and so on will be used for a restrictive class of operators that correspond to observables. Let us consider the eigenkets and eigenvalues of a Hermitian operator $A$. We use the symbol $A$, reserved earlier for an observable, because in quantum mechanics Hermitian operators of interest quite often turn out to be the operators representing some physical observables. We expect on physical grounds that an observable has real eigenvalues. The theorem just proved guarantees the reality of eigenvalues whenever the operator is Hermitian. That is why we talk about Hermitian observables in quantum mechanics.

where

- an operator acts on kets.
- $A$ denotes an operator corresponding to an observable.
- a Hermitian operator has real eigenvalues.

</i>

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
