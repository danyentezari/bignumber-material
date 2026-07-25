# Operator

A linear transformation from a vector space to itself that is used to transform vectors and to solve equations on that space.

<i>

**definition [d]** (*Operator = Linear Operator = Linear Transformation = Linear Map*) A mapping $T: V \rightarrow W$ between vector spaces over the same field that preserves linear combinations:

- $T(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha\, T(\mathbf{u}) + \beta\, T(\mathbf{v})$ .

where

- $V$ and $W$ are vector spaces over the same scalar field $K$.
- $\mathbf{u}, \mathbf{v} \in V$ and $\alpha, \beta \in K$.

</i>

<i>

**definition [d]** (*Operator = Linear Operator = Linear Transformation = Linear Map*) A mapping $T: V \rightarrow W$ between vector spaces over the same field that satisfies, for all vectors and scalars:

- (Additivity) $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ .
- (Homogeneity) $T(\alpha\mathbf{u}) = \alpha\, T(\mathbf{u})$ .

where

- $V$ and $W$ are vector spaces over the same scalar field $K$.
- $\mathbf{u}, \mathbf{v} \in V$ and $\alpha \in K$.

</i>

## Examples

<i>

**example 1 [d]** (**Matrix multiplication** — Shifrin & Adams) The operator $T(\mathbf{x}) = A\mathbf{x}$ with

- $A = \begin{pmatrix} 1 & 3 \\ 2 & -1 \\ 1 & 1 \end{pmatrix}$, \quad $\mathbf{x} = \begin{pmatrix} 4 \\ -1 \end{pmatrix}$ .

acts as

- $A\mathbf{x} = \begin{pmatrix} 1 \\ 9 \\ 3 \end{pmatrix}$ .

</i>

<i>

**example 2 [d]** (**Matrix multiplication** — Kreyszig) The operator $T(\mathbf{x}) = A\mathbf{x}$ with

- $A = \begin{pmatrix} 4 & 2 \\ 1 & 8 \end{pmatrix}$, \quad $\mathbf{x} = \begin{pmatrix} 3 \\ 5 \end{pmatrix}$ .

acts as

- $A\mathbf{x} = \begin{pmatrix} 22 \\ 43 \end{pmatrix}$ .

</i>

<i>

**example 3 [d]** (**Differentiation** — Aleksandrov et al.) The operator $D = \dfrac{d}{dx}$ with

- input $y = x^{2}$ .

acts as

- $Dy = 2x$ .

</i>

## Elementary Example
### Simple

An operator is a linear map from a space to itself. On $\mathbb{R}^{2}$, matrix multiplication defines an operator.

$$
T(\mathbf{x}) = A\mathbf{x},\quad
A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}
$$

$$
T(1,0) = (1,0),\quad T(0,1) = (1,2)
$$

where

- $T : V \rightarrow V$ is the operator.
- $A$ is the matrix of $T$.

### General

Differentiation on polynomials is an operator on an infinite-dimensional space; on the span of $\{1,x,x^{2}\}$ it acts by

$$
D(1) = 0,\quad D(x) = 1,\quad D(x^{2}) = 2x
$$

$$
D(a + bx + cx^{2}) = b + 2c x
$$

where

- $D = \dfrac{d}{dx}$ is the differentiation operator.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — linear operator axioms; matrix example $A=\begin{pmatrix}4&2\\1&8\end{pmatrix}$, $\mathbf{x}=\begin{pmatrix}3\\5\end{pmatrix}$.
2. Hassani, S. *Mathematical Physics: A Modern Introduction to Its Foundations*. Springer, 2013. — linear transformation / linear map.
3. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — linear operator / linear transformation.
4. Shifrin, T., & Adams, M. *Linear Algebra: A Geometric Approach*. W. H. Freeman, 2010. — matrix example $A=\begin{pmatrix}1&3\\2&-1\\1&1\end{pmatrix}$, $\mathbf{x}=\begin{pmatrix}4\\-1\end{pmatrix}$.
5. Aleksandrov, A. D., Kolmogorov, A. N., & Lavrent'ev, M. A. *Mathematics: Its Content, Methods and Meaning*. Dover, 1999. — differentiation example $y=x^{2}\mapsto 2x$.
6. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — matrix multiplication as a linear transformation.
7. Cahill, K. *Physical Mathematics*. Cambridge University Press, 2019. — matrix multiplication as a linear transformation.
