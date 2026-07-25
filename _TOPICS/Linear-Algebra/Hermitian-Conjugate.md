# Hermitian Conjugate

A matrix obtained from another matrix by taking the transpose and then the complex conjugate of each entry that is used to define adjoints and to form norms of complex vectors.

<i>

**definition [d]** (*Hermitian Conjugate = Adjoint = Conjugate Transpose = Hermitian Transpose*) The matrix $A^{\dagger}$ obtained from $A$ by transposition together with complex conjugation:

- (Matrix) $(A^{\dagger})_{ij} = \overline{a_{ji}}$ .
- (Operator) $\langle A\mathbf{a},\, \mathbf{b} \rangle = \langle \mathbf{a},\, A^{\dagger}\mathbf{b} \rangle$ for all $\mathbf{a}, \mathbf{b}$.

where

- $A$ is a matrix on a complex Hilbert space.
- $A^{\dagger}$ is the Hermitian conjugate of $A$.
- $a_{ij}$ are the entries of $A$.
- $\overline{\,\cdot\,}$ denotes the complex conjugate.
- $\langle \cdot,\, \cdot \rangle$ is the inner product.
- $\mathbf{a}, \mathbf{b}$ are vectors in the Hilbert space.

Note:

- the same definition applies when $A$ is a linear operator.
- $A^{\dagger}$ is also written $A^{*}$.
- $A^{\dagger}$ is also written $A^{H}$.

</i>

## Elementary Example
### Simple

The Hermitian conjugate is the conjugate transpose of a matrix.

$$
A = \begin{pmatrix} 1 & 2+i \\ 0 & 3 \end{pmatrix}
$$

$$
A^{\dagger} = \begin{pmatrix} 1 & 0 \\ 2-i & 3 \end{pmatrix}
$$

where

- $A^{\dagger}$ is the Hermitian conjugate of $A$.
- $(A^{\dagger})_{ij} = \overline{a_{ji}}$.

### General

For a $3 \times 3$ complex matrix, transpose and then conjugate every entry.

$$
A = \begin{pmatrix} 1 & i & 0 \\ 2 & 0 & 1+i \\ 0 & 3 & -i \end{pmatrix}
$$

$$
A^{\dagger} = \begin{pmatrix} 1 & 2 & 0 \\ -i & 0 & 3 \\ 0 & 1-i & i \end{pmatrix}
$$

where

- $A^{\dagger}$ is also written $A^{*}$ or $A^{H}$.


## References

1. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — matrix condition (2.53); operator adjoint (§5.3).
2. Schwichtenberg, J. *Physics from Symmetry*. Springer, 2018. — dagger notation ($U^{\dagger} = U^{T*}$, transpose plus complex conjugation).
3. McWeeny, R., & Jones, H. *Symmetry: An Introduction to Group Theory and Its Applications*. 1963. — names "Hermitian transpose", "adjoint", "associate".
