# Linear Algebra

Linear algebra is the study of vector spaces and the linear maps between them.

A vector space is a structured set that is used to add and scale its elements, where an element is called a vector and a scaling number is called a scalar.

Here are the ideas that are fundamental to the study of linear algebra.

Linear combination and span. A linear combination is a vector: the result of scaling given vectors and adding them. The span is a set: every linear combination of a chosen list of vectors.

Basis and dimension. A basis is a list of linearly independent vectors that spans the space. Linear independence is a property: no vector in the list is a combination of the others. Dimension is a number: the length of any basis.

Linear transformations. A linear transformation is a map between vector spaces that preserves addition and scaling. Preservation means the image of a sum is the sum of the images.

<i>

**definition [d]**

A **vector space** over a field of scalars is a nonempty set $V$ of vectors with addition and scalar multiplication such that for all $u,v,w \in V$ and all scalars $c,d$:

1. $u+v = v+u$
2. $(u+v)+w = u+(v+w)$
3. there is a zero vector $0$ with $u+0 = u$
4. each $u$ has an additive inverse $-u$ with $u+(-u) = 0$
5. $c(du) = (cd)u$
6. $c(u+v) = cu+cv$
7. $(c+d)u = cu+du$
8. $1u = u$

*where*

- $V$ is the set of vectors
- $c,d$ are scalars
- $u,v,w$ are vectors in $V$

**Note:**

- The two operations are vector addition and scalar multiplication.
- The same axioms define a vector space for any field of scalars.

</i>

## Elementary Example
### Simple

Linear algebra studies vectors and linear maps. Here three vectors in a plane.

$$
V = \{ e_{1},\ e_{2},\ v \}
$$

$$
e_{1} = (1,0),\quad e_{2} = (0,1),\quad v = (2,3)
$$

where

- $V$ is a set of sample vectors.
- $e_{1}, e_{2}$ form the standard basis of $\mathbb{R}^{2}$.

### General

Matrices represent linear maps. A $3 \times 3$ matrix acts on $\mathbb{R}^{3}$.

$$
A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}
$$

$$
A(x_{1},x_{2},x_{3}) = (x_{1},\ 2 x_{2},\ 3 x_{3})
$$

where

- $A$ is a linear transformation written as a matrix.

## References

1. Axler, S. *Linear Algebra Done Right*. Springer, 2015. — vector spaces and the linear maps between them; linear combinations and span.
2. Shilov, G. E. *Linear Algebra*. Dover, 1977. — basis and dimension.
3. Shifrin, T., & Adams, M. *Linear Algebra: A Geometric Approach*. — linear transformations as maps that preserve addition and scaling.
4. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1978. — the axioms of a vector space.
