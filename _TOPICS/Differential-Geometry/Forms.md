# Forms

Forms are functions that take vectors as input and return scalars. A 1-form takes a single vector as input, a 2-form takes two vectors as input, and so on.

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
