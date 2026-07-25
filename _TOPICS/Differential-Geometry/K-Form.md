# k-form

An alternating multilinear function of k vectors that is used to measure oriented size of a k-dimensional subspace.

<i>

**definition** (*k-form*) A multilinear, completely antisymmetric, real-valued function of $k$ vector inputs, $\boldsymbol{\omega}: \mathbf{V}^k \rightarrow \mathbb{R}$, which satisfies the following conditions for all vectors and scalars:

- (k-Linearity) $\boldsymbol{\omega}(\mathbf{v}_1, \dots, a\mathbf{v}_i + b\mathbf{v}_i', \dots, \mathbf{v}_k) = a \cdot \boldsymbol{\omega}(\mathbf{v}_1, \dots, \mathbf{v}_i, \dots, \mathbf{v}_k) + b \cdot \boldsymbol{\omega}(\mathbf{v}_1, \dots, \mathbf{v}_i', \dots, \mathbf{v}_k)$ for each argument $i$ where

* $1 \leq i \leq k$.
- (Complete Antisymmetry) Swapping any two vector inputs reverses the sign of the output: $\boldsymbol{\omega}(\dots, \mathbf{u}, \dots, \mathbf{v}, \dots) = -\boldsymbol{\omega}(\dots, \mathbf{v}, \dots, \mathbf{u}, \dots)$.

where

- $\mathbf{V}$ is a real vector space.
- $\mathbf{V}^k$ is the $k$-fold Cartesian product of $\mathbf{V}$.
- $\mathbb{R}$ is the set of real numbers.
- $\boldsymbol{\omega}$ is a $k$-form.
- $\mathbf{v}_1, \dots, \mathbf{v}_k, \mathbf{v}_i', \mathbf{u}, \mathbf{v}$ are vectors in $\mathbf{V}$.
- $k$ is a positive integer representing the degree of the form.
- $a, b$ are scalars.

</i>

## Elementary Example
### Simple

A $2$-form is an alternating bilinear function of two vectors.

$$
\omega : V \times V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
\omega(e_{1},e_{2}) = 2,\quad \omega(e_{2},e_{1}) = -2,\quad \omega(e_{1},e_{1}) = 0
$$

where

- $\omega$ is a $k$-form with $k = 2$.

### General

On $\mathbb{R}^{3}$, a $2$-form has a skew $3 \times 3$ component matrix.

$$
(\omega_{ij}) = \begin{pmatrix} 0 & 2 & 0 \\ -2 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}
$$

$$
\omega(u,v) = \sum_{i,j} \omega_{ij}\, u^{i}\, v^{j}
$$

where

- $\omega_{ij}$ are the components of the $2$-form $\omega$.
