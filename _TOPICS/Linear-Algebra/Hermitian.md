# Hermitian

A matrix equal to its conjugate transpose that is used to guarantee real eigenvalues.

Note: Also called self-adjoint. Also called Hermitian operator when stated for a linear transformation on an inner product space.

<i>

**definition [d]** (*Hermitian = Hermitian Matrix*) From Arfken: a matrix $H$ must be square, and its elements must satisfy

- $(H^{\dagger})_{ij} = (H)_{ij}$ ,

which means

- $h_{ji}^{*} = h_{ij}$ .

where

- $H$ is a square matrix.
- $H^{\dagger}$ is the Hermitian conjugate of $H$.
- $h_{ij}$ are the entries of $H$.
- $h_{ji}^{*}$ is the complex conjugate of the entry $h_{ji}$.

</i>

<i>

**definition [d]** (*Hermitian = Self-Adjoint Operator*) From Kreyszig: a bounded linear operator $T: H \rightarrow H$ on a Hilbert space $H$ is said to be self-adjoint, written also Hermitian, if

- $T^{*} = T$ .

where

- $H$ is a Hilbert space.
- $T$ is a bounded linear operator on $H$.
- $T^{*}$ is the adjoint of $T$.

Note:

- Hall: what a mathematician calls the adjoint and writes $A^{*}$, a physicist calls the Hermitian conjugate and writes $A^{\dagger}$; physicists call self-adjoint operators Hermitian.

</i>

## Elementary Example

### Simple

A $2 \times 2$ matrix is Hermitian when it equals its conjugate transpose.

$$
H = \begin{pmatrix} 1 & 1+i \\ 1-i & 2 \end{pmatrix}
$$

$$
H^{\dagger} = \begin{pmatrix} 1 & 1+i \\ 1-i & 2 \end{pmatrix} = H
$$

where

- $H$ is the Hermitian matrix.
- $H^{\dagger}$ is the Hermitian conjugate of $H$.
- $i$ is the imaginary unit with $i^{2} = -1$.

### General

A $3 \times 3$ Hermitian matrix has real diagonal entries, and off-diagonal pairs are conjugates of each other.

$$
H = \begin{pmatrix} 2 & 1-i & 0 \\ 1+i & 3 & 4i \\ 0 & -4i & 1 \end{pmatrix}
$$

$$
H^{\dagger} = H
$$

$$
h_{ji}^{*} = h_{ij}
$$

where

- $h_{ij}$ are the entries of $H$.
- $h_{11}, h_{22}, h_{33}$ are real.
- $T^{*} = T$ is the same condition for the operator represented by $H$.

## References

1. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — Hermitian matrix: $(H^{\dagger})_{ij} = (H)_{ij}$, equivalently $h_{ji}^{*} = h_{ij}$.
2. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — self-adjoint or Hermitian operator: $T^{*} = T$.
3. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — adjoint $A^{*}$ versus Hermitian conjugate $A^{\dagger}$; self-adjoint called Hermitian in physics.
