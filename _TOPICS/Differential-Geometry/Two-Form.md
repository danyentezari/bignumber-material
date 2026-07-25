# Two-Form

An antisymmetric multilinear mapping on ordered pairs of vectors that is used to form integrals over two-dimensional domains.

<i>

**definition** (*2-form*) A bilinear, antisymmetric, real-valued function of two vector inputs, $\boldsymbol{\omega}: \mathbf{V} \times \mathbf{V} \rightarrow \mathbb{R}$, which satisfies the following conditions for all vectors and scalars:

- (Bilinearity) $\boldsymbol{\omega}(a\mathbf{u} + b\mathbf{u}', \mathbf{v}) = a \cdot \boldsymbol{\omega}(\mathbf{u}, \mathbf{v}) + b \cdot \boldsymbol{\omega}(\mathbf{u}', \mathbf{v})$ and $\boldsymbol{\omega}(\mathbf{u}, a\mathbf{v} + b\mathbf{v}') = a \cdot \boldsymbol{\omega}(\mathbf{u}, \mathbf{v}) + b \cdot \boldsymbol{\omega}(\mathbf{u}, \mathbf{v}')$.
- (Antisymmetry) $\boldsymbol{\omega}(\mathbf{u}, \mathbf{v}) = -\boldsymbol{\omega}(\mathbf{v}, \mathbf{u})$.

where

- $\mathbf{V}$ is a real vector space.
- $\mathbb{R}$ is the set of real numbers.
- $\boldsymbol{\omega}$ is a 2-form.
- $\mathbf{u}, \mathbf{u}', \mathbf{v}, \mathbf{v}'$ are vectors in $\mathbf{V}$.
- $a, b$ are scalars.

</i>

## Elementary Example
### Simple

A two-form is antisymmetric on ordered pairs of vectors.

$$
\omega : V \times V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
\omega(e_{1},e_{2}) = 1,\quad \omega(e_{2},e_{1}) = -1,\quad \omega(e_{1},e_{1}) = 0
$$

where

- $\omega$ is the two-form.

### General

On $\mathbb{R}^{3}$, a two-form is a skew-symmetric $3 \times 3$ matrix of components.

$$
(\omega_{ij}) = \begin{pmatrix} 0 & 1 & 2 \\ -1 & 0 & 3 \\ -2 & -3 & 0 \end{pmatrix}
$$

$$
\omega(u,v) = \sum_{i,j} \omega_{ij}\, u^{i}\, v^{j},\quad \omega_{ij} = -\omega_{ji}
$$

where

- $\omega_{ij}$ are the components of $\omega$.
