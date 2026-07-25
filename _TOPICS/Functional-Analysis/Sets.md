# Sets 

A collection of mathematical objects such as numbers or vectors that is used as the basic building block for other constructions.

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

A set is a collection of elements. Here a three-element set of numbers.

$$
A = \{ 1,\ 2,\ 3 \}
$$

where

- $A$ is the set.
- $1, 2, 3$ are its elements.

### General

Sets of vectors are the building blocks of linear spaces. Here a basis set in $\mathbb{R}^{3}$.

$$
B = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
e_{1} = (1,0,0),\quad e_{2} = (0,1,0),\quad e_{3} = (0,0,1)
$$

where

- $B$ is a set of vectors.

