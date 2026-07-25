# Orthonormal

A property of a set of vectors of unit norm whose pairwise inner products vanish when the vectors differ that is used to build a convenient basis.

<i>

**definition [D]** (*Orthonormal*) A collection of mutually orthogonal normalized vectors in an inner product space. The set must satisfy the following conditions:

- Each vector in the set has unit length.
- Any two distinct vectors in the set are orthogonal, meaning their inner product is zero.

where

- $\langle \alpha_i | \alpha_j \rangle$ is the inner product of two vectors in the set.
- $\delta_{ij}$ is the Kronecker delta, which is 1 if $i = j$ and 0 otherwise.
- $\|\alpha\|$ is the norm of a vector, defined as the square root of the inner product of the vector with itself.
- $V$ is an inner product space.

Note:

- unit length means $\|\alpha\| = 1$.
- the norm is also called the length.
- $V$ may be regarded as a vector space with an inner product.

</i>

## Elementary Example
### Simple

An orthonormal set has unit vectors that are pairwise orthogonal.

$$
B = \{ e_{1},\ e_{2} \}
$$

$$
e_{1} = (1,0),\quad e_{2} = (0,1)
$$

$$
\langle e_{i}, e_{j} \rangle = \delta_{ij}
$$

where

- $\langle e_{i}, e_{i} \rangle = 1$.
- $\langle e_{1}, e_{2} \rangle = 0$.
- $\delta_{ij}$ is the Kronecker delta.

### General

The standard basis of $\mathbb{R}^{3}$ is orthonormal.

$$
B = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
\langle e_{i}, e_{j} \rangle = \delta_{ij},\quad i,j \in \{1,2,3\}
$$

where

- each $\lVert e_{i} \rVert = 1$.

