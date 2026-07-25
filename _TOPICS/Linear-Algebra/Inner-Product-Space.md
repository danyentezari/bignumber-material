# Inner Product Space

A set of vectors equipped with an inner product that is used to define distance and length of vectors from that inner product.

<i>

**definition [D]** (*Inner Product Space*) A vector space equipped with an inner product that associates a complex scalar with every ordered pair of vectors, where the following conditions apply:

- The mapping satisfies conjugate symmetry: $\langle \alpha | \beta \rangle = \langle \beta | \alpha \rangle^*$.
- The mapping is linear in the second factor: $\langle \alpha | a\beta + b\gamma \rangle = a\langle \alpha | \beta \rangle + b\langle \alpha | \gamma \rangle$.
- The mapping is positive definite: $\langle \alpha | \alpha \rangle \ge 0$, vanishing only if $\alpha = 0$.

where

- $V$ is a vector space over a field $K$.
- $\langle \alpha | \beta \rangle$ is the inner product of vectors $\alpha$ and $\beta$.
- $K$ is the scalar field.
- $\|\alpha\| = \sqrt{\langle \alpha | \alpha \rangle}$ is the norm.

Note:

- a vector space is also called a linear space.
- the inner product is also called the scalar product.
- $K$ is typically $\mathbb{R}$.
- $K$ is also typically $\mathbb{C}$.
- the norm generalizes the concept of length.

</i>

## Elementary Example
### Simple

An inner product space is a vector space with an inner product. Take $\mathbb{R}^{2}$ with the dot product.

$$
V = \mathbb{R}^{2}
$$

$$
\langle u,v \rangle = u_{1} v_{1} + u_{2} v_{2}
$$

$$
\lVert u \rVert = \sqrt{\langle u,u \rangle}
$$

where

- $V$ is the inner product space.
- $\lVert u \rVert$ is the induced norm.

### General

The space $\mathbb{C}^{3}$ with the Hermitian inner product is an inner product space.

$$
V = \mathbb{C}^{3}
$$

$$
\langle u,v \rangle = \sum_{j=1}^{3} u_{j} \overline{v_{j}}
$$

where

- distance is defined by $d(u,v) = \lVert u - v \rVert$.

