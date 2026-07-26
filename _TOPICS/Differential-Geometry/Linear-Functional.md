# Linear Functional

A linear mapping from a vector space to scalars that is used to define the dual space.

<i>

**definition** (*Linear Functional*) A linear transformation from a vector space $V$ to its associated field of scalars $K$, The mapping $f: V \rightarrow K$ must satisfy the following linearity condition:

- $f(ax + by) = af(x) + bf(y)$ 

where

- $x, y \in V$ are vectors
- $a, b \in K$ are scalars
- $V$ is a vector space
- $K$ is the field of scalars.

</i>

## Elementary Example
### Simple

A linear functional maps each vector to a scalar.

$$
f : V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
f(e_{1}) = 1,\quad f(e_{2}) = -2,\quad f(e_{3}) = 0
$$

where

- $f$ is the linear functional.
- $V$ is the set of basis vectors used as inputs.

### General

On $\mathbb{R}^{3}$, $f$ is given by a row of components $\omega_{i}$ via the dot product with those components.

$$
f(v) = \omega_{1} v^{1} + \omega_{2} v^{2} + \omega_{3} v^{3}
$$

$$
(\omega_{1},\omega_{2},\omega_{3}) = (1,-2,0)
$$

where

- $\omega_{i}$ are the components of $f$ in the dual basis.
- $v^{i}$ are the components of $v$.
