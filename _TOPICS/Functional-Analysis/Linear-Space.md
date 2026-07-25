# Linear Space

A set of vectors together with addition of vectors and multiplication by scalars that is used to build domains for functions and for linear transformations.

Note: Also called vector space.

<i>

**definition [d]** (*Linear Space = Vector Space*) From Kreyszig Definition 2.1-1: a vector space over a field $K$ is a nonempty set $X$ of elements $x, y, \ldots$ called vectors together with two algebraic operations called vector addition and multiplication of vectors by scalars, that is, by elements of $K$.

Vector addition associates with every ordered pair $(x,y)$ of vectors a vector $x+y$ such that vector addition is commutative and associative. Multiplication by scalars satisfies

- $\alpha(\beta x) = (\alpha\beta)x$
- $1x = x$

and the distributive laws

- $\alpha(x+y) = \alpha x + \alpha y$
- $(\alpha+\beta)x = \alpha x + \beta x$ .

Vector addition is a mapping $X \times X \rightarrow X$, and multiplication by scalars is a mapping $K \times X \rightarrow X$.

where

- $X$ is the set of vectors.
- $K$ is the scalar field.
- $X$ is a real vector space if $K = \mathbb{R}$.
- $X$ is a complex vector space if $K = \mathbb{C}$.

</i>

## Elementary Example
### Simple

A linear space has vector addition and scalar multiplication. On three labeled vectors in $\mathbb{R}$, addition is ordinary.

$$
X = \{ 0,\ 1,\ -1 \}
$$

$$
1 + (-1) = 0,\quad 2 \cdot 1 = 2\ \text{in }\mathbb{R}
$$

where

- $X$ illustrates elements of a real vector space.
- the ambient operations are those of $\mathbb{R}$ as a vector space over itself.

### General

The space $\mathbb{R}^{3}$ is a linear space: add componentwise and multiply by scalars.

$$
X = \mathbb{R}^{3}
$$

$$
(1,0,0) + (0,2,0) = (1,2,0),\quad 3(0,1,0) = (0,3,0)
$$

where

- $X$ is the set of vectors.
- the scalar field is $K = \mathbb{R}$.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 2.1-1 (Vector space).
