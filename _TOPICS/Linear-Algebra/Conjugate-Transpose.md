# Conjugate Transpose

A matrix obtained by interchanging rows and columns and then taking the complex conjugate of each entry that is used to form adjoints of complex matrices.

Note: Also called Hermitian conjugate. Also called Hermitian transpose. Also called adjoint of a matrix.

<i>

**definition [d]** (*Conjugate Transpose*) From Axler: the conjugate transpose of an $m$-by-$n$ matrix $A$ is the $n$-by-$m$ matrix $A^{*}$ obtained by interchanging the rows and columns and then taking the complex conjugate of each entry. In other words, if $j \in \{1,\ldots,n\}$ and $k \in \{1,\ldots,m\}$, then

- $(A^{*})_{j,k} = \overline{A_{k,j}}$ .

where

- $A$ is an $m$-by-$n$ matrix with complex entries.
- $A^{*}$ is the conjugate transpose of $A$.
- $\overline{\,\cdot\,}$ denotes the complex conjugate.

</i>

<i>

**definition [d]** (*Hermitian Transpose*) From Cohen: the Hermitian transpose, often called simply the Hermitian, is a conjugate-and-transpose operation. It is indicated with a superscripted $H$ instead of a $T$.

where

- $A^{H}$ denotes the Hermitian transpose of a matrix $A$.
- $v^{H}$ denotes the Hermitian transpose of a vector $v$.

</i>

<i>

**definition [d]** (*Adjoint of a Matrix*) From Arfken: the adjoint of a matrix $A$, denoted $A^{\dagger}$, is obtained by both complex conjugating and transposing it. Thus

- $(A^{\dagger})_{ij} = a_{ji}^{*}$ .

where

- $A$ is a matrix.
- $A^{\dagger}$ is the adjoint of $A$ in the matrix sense.
- $a_{ji}^{*}$ is the complex conjugate of the entry $a_{ji}$.

</i>

## Elementary Example

### Simple

Interchange rows and columns, then conjugate each entry.

$$
A = \begin{pmatrix} 1 & 2+i \\ 0 & 3 \end{pmatrix}
$$

$$
A^{*} = \begin{pmatrix} 1 & 0 \\ 2-i & 3 \end{pmatrix}
$$

where

- $A^{*}$ is the conjugate transpose of $A$.
- $(A^{*})_{j,k} = \overline{A_{k,j}}$.

### General

For a $3 \times 2$ matrix, the conjugate transpose is $2 \times 3$.

$$
A = \begin{pmatrix} 1 & i \\ 2 & 0 \\ 1+i & -i \end{pmatrix}
$$

$$
A^{*} = \begin{pmatrix} 1 & 2 & 1-i \\ -i & 0 & i \end{pmatrix}
$$

where

- $A^{*}$ is also written $A^{H}$ or $A^{\dagger}$.

## References

1. Axler, S. *Linear Algebra Done Right*. Springer, 2024. — Definition 7.7: conjugate transpose $A^{*}$, $(A^{*})_{j,k} = \overline{A_{k,j}}$.
2. Cohen, M. X. *Linear Algebra: Theory, Intuition, Code*. Sincxpress BV, 2021. — Hermitian transpose $A^{H}$.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — $(A^{\dagger})_{ij} = a_{ji}^{*}$.
