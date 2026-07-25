# Complete Set

A set of vectors whose linear combinations can approximate every vector in a larger set that is used as a basis-like tool to represent other vectors.

<i>

**definition** (*Complete Set*) A subset of a normed space whose span is dense in that space, meaning any element in the space can be represented by a linear combination of the set's members. The set must satisfy the following condition:

- The only vector in the space that is orthogonal to every element in the set is the zero vector.

where

- $M$ is the set of vectors being tested for completeness.
- $H$ is the Hilbert space containing the set.
- $\text{span } M$ is the set of all finite linear combinations of elements in $M$.
- $\delta(x - x')$ is the Dirac delta function.
- $1 = \sum |e_n\rangle\langle e_n|$ is the completeness relation for a discrete orthonormal basis.

Note:

- the same notion applies in an inner product space.
- $M$ may be a set of functions.
- an element may be approximated rather than exactly represented by a linear combination.
- $\delta(x - x')$ is used to express the completeness relation for sets with continuous indices.
- the completeness relation is also called the resolution of the identity.

</i>

## Elementary Example
### Simple

A complete set spans a dense subspace. In $\mathbb{R}^{2}$, the two standard basis vectors form a complete set.

$$
M = \{ e_{1},\ e_{2} \}
$$

$$
e_{1} = (1,0),\quad e_{2} = (0,1)
$$

$$
\operatorname{span} M = \mathbb{R}^{2}
$$

where

- $M$ is the set being tested for completeness.
- $\operatorname{span} M$ is the set of finite linear combinations of members of $M$.

### General

In $\mathbb{R}^{3}$, the three standard basis vectors form a complete set: only the zero vector is orthogonal to all three.

$$
M = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
\operatorname{span} M = \mathbb{R}^{3}
$$

where

- if $\langle v, e_{i} \rangle = 0$ for $i = 1,2,3$, then $v = 0$.

