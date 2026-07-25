# Linear Transformation

A linear transformation is a mapping of a vector to another vector in a codomain that is used to represent a change in a scalar value.

Note: Also called linear map.

<i>

**definition [d]** (*Linear Transformation = Linear Map*) From Hubbard and Hubbard Definition 1.3.2: a linear transformation $T: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$ is a mapping such that for all scalars $a$ and all $\mathbf{v}, \mathbf{w} \in \mathbb{R}^{n}$,

- $T(\mathbf{v} + \mathbf{w}) = T(\mathbf{v}) + T(\mathbf{w})$
- $T(a\mathbf{v}) = a\, T(\mathbf{v})$ .

where

- $T$ is the linear transformation.
- $\mathbb{R}^{n}$ is the domain.
- $\mathbb{R}^{m}$ is the codomain.
- $a$ is a scalar.
- $\mathbf{v}, \mathbf{w}$ are vectors in $\mathbb{R}^{n}$.

</i>

## Examples

<i>

**example 1 [d]** (**Linear map $\mathbb{R}^{3}\rightarrow\mathbb{R}^{2}$** — Dummit and Foote) Let $V = \mathbb{R}^{3}$ with the standard basis $B = \{(1,0,0),(0,1,0),(0,0,1)\}$ and let $W = \mathbb{R}^{2}$ with the standard basis $E = \{(1,0),(0,1)}$. Let $\phi$ be the linear transformation

- $\phi(x,y,z) = (x + 2y,\, x + y + z)$ .

Since $\phi(1,0,0) = (1,1)$, $\phi(0,1,0) = (2,1)$, $\phi(0,0,1) = (0,1)$, the matrix $A = M(\phi)$ is

- $A = \begin{bmatrix} 1 & 2 & 0 \\ 1 & 1 & 1 \end{bmatrix}$ .

where

- $\phi$ is the linear transformation.
- $V = \mathbb{R}^{3}$ is the domain.
- $W = \mathbb{R}^{2}$ is the codomain.
- $(x,y,z)$ are coordinates of a vector in $V$.
- $B$ and $E$ are the standard bases of $V$ and $W$.
- $A$ is the matrix of $\phi$ with respect to those bases.

</i>

<i>

**example 2 [d]** (**Rotation by an angle $\theta$** — Hubbard and Hubbard) The transformation $R$ giving rotation by $\theta$ counterclockwise around the origin is linear, and its matrix is

- $[R] = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ .

where

- $R: \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$ is the rotation mapping.
- $\theta$ is the angle of rotation.
- $[R]$ is the matrix of $R$ with respect to the standard basis of $\mathbb{R}^{2}$.

</i>

## Elementary Example
### Simple

A linear transformation maps vectors to vectors and preserves linear combinations.

$$
\phi : \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}
$$

$$
\phi(x,y) = (2x,\ y)
$$

$$
\phi(1,0) = (2,0),\quad \phi(0,1) = (0,1)
$$

where

- $\phi$ is the linear transformation.

### General

Rotation by an angle $\theta$ in the plane is a linear transformation with a $2 \times 2$ matrix.

$$
R_{\theta} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
$$

$$
R_{\theta}(x,y) = (x\cos\theta - y\sin\theta,\ x\sin\theta + y\cos\theta)
$$

where

- $R_{\theta}$ is the rotation matrix.
- $\theta$ is a real angle.


## References

1. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms*, Matrix Editions. — Definition 1.3.2; Example 1.3.9 (rotation by $\theta$).
2. Dummit, D. S., & Foote, R. M. *Abstract Algebra*. Wiley, 2004. — linear map $\phi:\mathbb{R}^{3}\rightarrow\mathbb{R}^{2}$, $\phi(x,y,z)=(x+2y,\,x+y+z)$.
