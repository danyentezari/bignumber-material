# Operator

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

**example [d]** (**Matrix multiplication** — Shifrin & Adams) The operator $T(\mathbf{x}) = A\mathbf{x}$ with

- $A = \begin{pmatrix} 1 & 3 \\ 2 & -1 \\ 1 & 1 \end{pmatrix}$, \quad $\mathbf{x} = \begin{pmatrix} 4 \\ -1 \end{pmatrix}$ .

acts as

- $A\mathbf{x} = \begin{pmatrix} 1 \\ 9 \\ 3 \end{pmatrix}$ .

</i>

<i>

**example [d]** (**Matrix multiplication** — Kreyszig) The operator $T(\mathbf{x}) = A\mathbf{x}$ with

- $A = \begin{pmatrix} 4 & 2 \\ 1 & 8 \end{pmatrix}$, \quad $\mathbf{x} = \begin{pmatrix} 3 \\ 5 \end{pmatrix}$ .

acts as

- $A\mathbf{x} = \begin{pmatrix} 22 \\ 43 \end{pmatrix}$ .

</i>

<i>

**example [d]** (**Differentiation** — Aleksandrov et al.) The operator $D = \dfrac{d}{dx}$ with

- input $y = x^{2}$ .

acts as

- $Dy = 2x$ .

</i>

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — linear operator axioms; matrix example $A=\begin{pmatrix}4&2\\1&8\end{pmatrix}$, $\mathbf{x}=\begin{pmatrix}3\\5\end{pmatrix}$.
2. Hassani, S. *Mathematical Physics: A Modern Introduction to Its Foundations*. Springer, 2013. — linear transformation / linear map.
3. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — linear operator / linear transformation.
4. Shifrin, T., & Adams, M. *Linear Algebra: A Geometric Approach*. W. H. Freeman, 2010. — matrix example $A=\begin{pmatrix}1&3\\2&-1\\1&1\end{pmatrix}$, $\mathbf{x}=\begin{pmatrix}4\\-1\end{pmatrix}$.
5. Aleksandrov, A. D., Kolmogorov, A. N., & Lavrent'ev, M. A. *Mathematics: Its Content, Methods and Meaning*. Dover, 1999. — differentiation example $y=x^{2}\mapsto 2x$.
6. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — matrix multiplication as a linear transformation.
7. Cahill, K. *Physical Mathematics*. Cambridge University Press, 2019. — matrix multiplication as a linear transformation.
