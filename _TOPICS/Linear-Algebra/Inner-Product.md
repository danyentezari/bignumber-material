# Inner Product

A mapping that assigns a scalar to each ordered pair of vectors that is used to define length through a norm and to compare vectors.

<i>

**definition [d]** (*Inner Product = Scalar Product = Dot Product*) A map $(\cdot,\, \cdot) : V \times V \rightarrow K$ associating a scalar with every ordered pair of vectors, satisfying for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and scalars $\alpha, \beta$:

- (Conjugate symmetry) $(\mathbf{u},\, \mathbf{v}) = \overline{(\mathbf{v},\, \mathbf{u})}$ .
- (Linearity in the first argument) $(\alpha\mathbf{u} + \beta\mathbf{v},\, \mathbf{w}) = \alpha(\mathbf{u},\, \mathbf{w}) + \beta(\mathbf{v},\, \mathbf{w})$ .
- (Positive-definiteness) $(\mathbf{u},\, \mathbf{u}) \geq 0$, and $(\mathbf{u},\, \mathbf{u}) = 0 \iff \mathbf{u} = 0$ .

where

- $V$ is a vector space over a field $K$.
- $\overline{\,\cdot\,}$ denotes the complex conjugate.

Note:

- $K$ is typically $\mathbb{R}$.
- $K$ is also typically $\mathbb{C}$.
- the complex conjugate is redundant if $K = \mathbb{R}$.

</i>

<i>

**definition [d]** (*Inner Product = Scalar Product = Dot Product*) A map $\langle \cdot,\, \cdot \rangle : V \times V \rightarrow K$ associating a scalar with every ordered pair of vectors, satisfying for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and scalars $\alpha, \beta$:

- (Conjugate symmetry) $\langle \mathbf{u},\, \mathbf{v} \rangle = \overline{\langle \mathbf{v},\, \mathbf{u} \rangle}$ .
- (Linearity in the second argument) $\langle \mathbf{u},\, \alpha\mathbf{v} + \beta\mathbf{w} \rangle = \alpha\langle \mathbf{u},\, \mathbf{v} \rangle + \beta\langle \mathbf{u},\, \mathbf{w} \rangle$ .
- (Positive-definiteness) $\langle \mathbf{u},\, \mathbf{u} \rangle \geq 0$, and $\langle \mathbf{u},\, \mathbf{u} \rangle = 0 \iff \mathbf{u} = 0$ .

where

- $V$ is a vector space over a field $K$.
- $\overline{\,\cdot\,}$ denotes the complex conjugate.

Note:

- $K$ is typically $\mathbb{R}$.
- $K$ is also typically $\mathbb{C}$.
- the complex conjugate is redundant if $K = \mathbb{R}$.

</i>

## Elementary Example
### Simple

An inner product assigns a scalar to each ordered pair of vectors. On $\mathbb{R}^{2}$ use the dot product.

$$
\langle u,v \rangle = u_{1} v_{1} + u_{2} v_{2}
$$

$$
u = (1,2),\quad v = (3,4),\quad \langle u,v \rangle = 11
$$

where

- $\langle \cdot,\cdot \rangle$ is the inner product.
- $u, v$ are vectors.

### General

On $\mathbb{C}^{3}$, the standard Hermitian inner product conjugates the second factor.

$$
\langle u,v \rangle = u_{1}\overline{v_{1}} + u_{2}\overline{v_{2}} + u_{3}\overline{v_{3}}
$$

$$
\langle u,u \rangle \ge 0,\quad \langle u,u \rangle = 0 \iff u = 0
$$

where

- $\overline{v_{j}}$ is the complex conjugate of the component $v_{j}$.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — inner-product axioms (linearity in the first argument).
2. Griffel, D. H. *Applied Functional Analysis*. Ellis Horwood, 1981. — inner-product axioms.
3. Hassani, S. *Mathematical Physics: A Modern Introduction to Its Foundations*. Springer, 2013. — physics convention (linearity in the second argument).
4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — scalar product / dot product.
