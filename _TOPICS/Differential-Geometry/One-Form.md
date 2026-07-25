# One-Form

A linear functional on a vector space that is used as the integrand of a line integral.

<i>

**definition** (*1-form = linear functional = covector = covariant vector*) A linear, real-valued function of a single vector input, $\boldsymbol{\omega}: \mathbf{V} \rightarrow \mathbb{R}$, which satisfies the following conditions for all vectors and scalars:

- (Additivity) $\boldsymbol{\omega}(\mathbf{u} + \mathbf{v}) = \boldsymbol{\omega}(\mathbf{u}) + \boldsymbol{\omega}(\mathbf{v})$.
- (Homogeneity) $\boldsymbol{\omega}(k\mathbf{v}) = k \cdot \boldsymbol{\omega}(\mathbf{v})$.

where

- $\mathbf{V}$ is a real vector space.
- $\mathbb{R}$ is the set of real numbers.
- $\boldsymbol{\omega}$ is a 1-form.
- $\mathbf{u}, \mathbf{v}$ are vectors in $\mathbf{V}$.
- $k$ is a scalar.

</i>

## Elementary Example
### Simple

A one-form is a linear functional on vectors.

$$
\omega : V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
\omega(e_{1}) = 3,\quad \omega(e_{2}) = -1,\quad \omega(e_{3}) = 4
$$

where

- $\omega$ is the one-form.
- $e_{i}$ are basis vectors.

### General

On $\mathbb{R}^{3}$, $\omega$ is a row of components acting by contraction on a column of vector components.

$$
\omega(v) = \omega_{1} v^{1} + \omega_{2} v^{2} + \omega_{3} v^{3}
$$

$$
(\omega_{1},\omega_{2},\omega_{3}) = (3,-1,4)
$$

where

- $\omega_{i}$ are the components of the one-form.
