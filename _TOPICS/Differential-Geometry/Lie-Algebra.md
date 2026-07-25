# Lie Algebra

A set of vectors with a mapping that combines two vectors into a third vector that is used to calculate the change of a vector value.

<i>

**definition [d]** (*Lie Algebra*) From Hall Definition 16.10: a Lie algebra over a field $F$ is a vector space $\mathfrak{g}$ over $F$, together with a bracket map $[\cdot,\cdot]: \mathfrak{g} \times \mathfrak{g} \rightarrow \mathfrak{g}$ having the following properties:

1. $[\cdot,\cdot]$ is bilinear.
2. $[Y,X] = -[X,Y]$ for all $X,Y \in \mathfrak{g}$.
3. $[X,X] = 0$ for all $X \in \mathfrak{g}$.
4. For all $X,Y,Z \in \mathfrak{g}$ the Jacobi identity holds:

- $[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0$ .

where

- $\mathfrak{g}$ is the Lie algebra.
- $F$ is the field of scalars.
- $[\cdot,\cdot]$ is the Lie bracket.

</i>

<i>

**definition [d]** (*Lie Algebra*) From Hassani Definition 29.2.1: a finite-dimensional vector space $V$ over $\mathbb{R}$ or $\mathbb{C}$ is called a Lie algebra over $\mathbb{R}$ or $\mathbb{C}$ if there is a binary operation, called Lie multiplication, $[\cdot,\cdot]: V \times V \rightarrow V$ on $V$, satisfying

- $[X,Y] = -[Y,X]$ for all $X,Y \in V$ (antisymmetry).
- $[\alpha X + \beta Y, Z] = \alpha[X,Z] + \beta[Y,Z]$ for $\alpha,\beta$ scalars (linearity).
- $[X,[Y,Z]] + [Z,[X,Y]] + [Y,[Z,X]] = 0$ (Jacobi identity).

where

- $V$ is the Lie algebra.
- $[\cdot,\cdot]$ is Lie multiplication.

</i>


## Elementary Example
### Simple

A Lie algebra is a vector space with a bracket $[\ ,\ ]$. On three elements the bracket closes in the set.

$$
\mathfrak{g} = \{ X,\ Y,\ Z \}
$$

$$
[X,Y] = Z,\quad [Y,Z] = X,\quad [Z,X] = Y,\quad [X,X] = 0
$$

where

- $\mathfrak{g}$ is the Lie algebra.
- $[X,Y]$ is the Lie bracket of $X$ and $Y$.

### General

Matrix commutators give a concrete bracket: $[A,B] = AB - BA$ on $2 \times 2$ matrices.

$$
A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix},\quad
B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}
$$

$$
[A,B] = AB - BA = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

where

- $A, B$ are matrices in the Lie algebra.
- $AB - BA$ is the commutator bracket.

## References

1. Hall, B. C. *Quantum Theory for Mathematicians*. Springer. — Definition 16.10 (Lie algebra).
2. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — Definition 29.2.1 (Lie algebra).
