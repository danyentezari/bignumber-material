# Basis

A set of vectors that spans a vector space and represents every vector by unique scalar values that is used to write vectors in coordinates relative to that set.

<i>

**definition [d]** (*Basis = Ordered Basis*) An ordered set of linearly independent vectors that span a vector space $V$.

where

- $V$ is a vector space.
- the ordered set is the basis of $V$.

Note:

- two bases are considered different if one is a rearrangement of the other.
- this ordered notion is sometimes called an ordered basis.

</i>

<i>

**definition [d]** (**Basis**) A set $B$ of linearly independent vectors that spans all of a vector space $V$.

where

- $V$ is a vector space.
- $B$ is the basis of $V$.

Note:

- every vector in $V$ is a unique linear combination of the vectors in $B$.
- the coefficients in that expansion are the components relative to $B$.

</i>

<i>

**definition [d]** (**Basis**) A set of vectors that both spans a vector space and is linearly independent: every vector is a linear combination of the basis vectors, and no basis vector is a linear combination of the others.

where

- the spanning condition means every vector is a linear combination of the basis vectors.
- the linear-independence condition means no basis vector is a linear combination of the remaining basis vectors.

Note:

- this formulation is the geometric one used in spacetime treatments of tangent spaces.

</i>

## Elementary Example
### Simple

A basis is a linearly independent spanning set. The standard basis of $\mathbb{R}^{2}$ has two vectors.

$$
B = \{ e_{1},\ e_{2} \}
$$

$$
e_{1} = (1,0),\quad e_{2} = (0,1)
$$

$$
v = v^{1} e_{1} + v^{2} e_{2}
$$

where

- $B$ is the basis.
- $v^{1}, v^{2}$ are the unique coordinates of $v$.

### General

In $\mathbb{R}^{3}$, three independent vectors form a basis and give unique coordinates.

$$
B = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
e_{1}=(1,0,0),\ e_{2}=(0,1,0),\ e_{3}=(0,0,1)
$$

$$
v = v^{1} e_{1} + v^{2} e_{2} + v^{3} e_{3}
$$

where

- every vector in $\mathbb{R}^{3}$ has a unique expansion in $B$.


## References

1. Dummit, D. S., & Foote, R. M. *Abstract Algebra*. Wiley, 2004. — ordered basis as ordered linearly independent spanning set.
2. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — basis as linearly independent spanning set; unique components.
3. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — basis as spanning and linearly independent.
