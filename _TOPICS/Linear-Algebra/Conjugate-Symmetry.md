# Conjugate Symmetry

A property of an inner product under which swapping the two vector inputs replaces the scalar value by its complex conjugate that is used to keep the norm of a vector a real number.

<i>

**definition [d]** (*Conjugate Symmetry = Hermitian Symmetry*) A property of a complex inner product $\langle \cdot, \cdot \rangle$ on a vector space $\mathbf{V}$ that satisfies the following condition for all vectors:

- $\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$ .

where

- $\mathbf{V}$ is a complex vector space.
- $\mathbf{u}, \mathbf{v} \in \mathbf{V}$.
- $\overline{\,\cdot\,}$ denotes the complex conjugate.

</i>

## Elementary Example
### Simple

Conjugate symmetry says swapping the two inputs conjugates the inner-product value.

$$
\langle u,v \rangle = \overline{\langle v,u \rangle}
$$

$$
u = (1,0),\quad v = (i,0),\quad \langle u,v \rangle = -i,\quad \langle v,u \rangle = i
$$

where

- $\langle \cdot,\cdot \rangle$ is the inner product.
- $\overline{\,\cdot\,}$ is complex conjugation.

### General

On $\mathbb{C}^{3}$ with the standard Hermitian inner product, the same identity holds for every pair.

$$
\langle u,v \rangle = u_{1}\overline{v_{1}} + u_{2}\overline{v_{2}} + u_{3}\overline{v_{3}}
$$

$$
\langle u,v \rangle = \overline{\langle v,u \rangle}
$$

where

- $u = (u_{1},u_{2},u_{3})$ and $v = (v_{1},v_{2},v_{3})$ are vectors in $\mathbb{C}^{3}$.


## References

1. Griffel, D. H. *Applied Functional Analysis*. Ellis Horwood, 1981. — inner-product axiom (b) (conjugation under order reversal).
2. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — Hilbert-space inner product (order reversal = complex conjugation).
