# Hilbert Space

A complete inner product space that is used to expand vectors in a basis and to represent bounded linear functionals, where an inner product space is a vector space with an inner product, and where completeness is the property that every Cauchy sequence has a limit in the space.

Note: Also written $H$. Also written $\mathcal{H}$. Also called a complete pre-Hilbert space.

Inner product. An inner product is a scalar attached to each ordered pair of vectors. The pairing is linear in the first argument, conjugate-symmetric, and positive-definite. A conjugate-symmetric pairing swaps the arguments and takes the complex conjugate. A positive-definite pairing gives a positive length to every nonzero vector. This principle is used to measure angle and length.

The inner product axioms are

$$
\begin{aligned}
\langle x+y,z\rangle
&=
\langle x,z\rangle+\langle y,z\rangle
\\
\langle \alpha x,y\rangle
&=
\alpha\langle x,y\rangle
\\
\langle x,y\rangle
&=
\overline{\langle y,x\rangle}
\\
\langle x,x\rangle
&\ge
0
\end{aligned}
$$

where

- $x$, $y$, $z$ are vectors.
- $\alpha$ is a scalar.
- $\langle x,y\rangle$ is the inner product of $x$ and $y$.
- $\overline{\langle y,x\rangle}$ is the complex conjugate of $\langle y,x\rangle$.
- $\langle x,x\rangle=0$ if and only if $x=0$.

Induced norm. The inner product defines a length by taking the square root of the inner product of a vector with itself. This principle is used to turn inner-product geometry into a normed space.

The induced norm is

$$
\lVert x\rVert
=
\langle x,x\rangle^{\dfrac{1}{2}}
$$

where

- $\lVert x\rVert$ is the length of $x$.

Induced metric. The distance between two vectors is the norm of their difference. This principle is used to define Cauchy sequences and completeness.

The induced metric is

$$
d(x,y)
=
\lVert x-y\rVert
$$

where

- $d(x,y)$ is the distance from $x$ to $y$.

Completeness. Every Cauchy sequence of vectors has a limit in the space. A Cauchy sequence is a sequence whose terms become arbitrarily close. This principle is used to keep limits of approximations inside the Hilbert space.

Schwarz inequality. The absolute value of an inner product is at most the product of the two norms. Equality holds when the two vectors are linearly dependent. This principle is used to bound inner products.

The Schwarz inequality is

$$
\bigl|\langle x,y\rangle\bigr|
\le
\lVert x\rVert\,\lVert y\rVert
$$

where

- $\bigl|\langle x,y\rangle\bigr|$ is the absolute value of the inner product.

Triangle inequality. The norm of a sum is at most the sum of the norms. This principle is used to control distances after addition.

The triangle inequality is

$$
\lVert x+y\rVert
\le
\lVert x\rVert+\lVert y\rVert
$$

Parallelogram equality. The sum of the squared lengths of the two diagonals of a parallelogram equals twice the sum of the squared side lengths. This principle is used to recover the inner product from the norm.

The parallelogram equality is

$$
\lVert x+y\rVert^{2}+\lVert x-y\rVert^{2}
=
2\bigl(\lVert x\rVert^{2}+\lVert y\rVert^{2}\bigr)
$$

Orthogonal projection. If $Y$ is a closed subspace of $H$, then $H$ is the direct sum of $Y$ and its orthogonal complement. A closed subspace contains its limit points. The orthogonal complement is the set of vectors orthogonal to every vector of $Y$. This principle is used to split a vector into a part in $Y$ and a part orthogonal to $Y$.

The direct sum theorem is

$$
H
=
Y\oplus Y^{\perp}
$$

where

- $H$ is the Hilbert space.
- $Y$ is a closed subspace of $H$.
- $Y^{\perp}$ is the orthogonal complement of $Y$.
- $\oplus$ is the direct sum of subspaces.

Bessel inequality. For an orthonormal sequence, the sum of the squared moduli of the Fourier coefficients of a vector is at most the squared norm of the vector. An orthonormal sequence is a sequence of unit vectors that are pairwise orthogonal. This principle is used to bound Fourier coefficients.

The Bessel inequality is

$$
\sum_{k}
\bigl|\langle x,e_{k}\rangle\bigr|^{2}
\le
\lVert x\rVert^{2}
$$

where

- $(e_{k})$ is an orthonormal sequence.
- $\langle x,e_{k}\rangle$ is the Fourier coefficient of $x$ along $e_{k}$.

Parseval relation. An orthonormal set is total if and only if the Parseval relation holds for every vector. A total orthonormal set is an orthonormal set whose span is dense. This principle is used to expand every vector as a Fourier series in the orthonormal set.

The Parseval relation is

$$
\lVert x\rVert^{2}
=
\sum_{k}
\bigl|\langle x,e_{k}\rangle\bigr|^{2}
$$

where

- the sum runs over the nonzero Fourier coefficients of $x$.

Riesz representation. Every bounded linear functional on a Hilbert space is the inner product against a unique vector, and that vector has the same norm as the functional. A bounded linear functional is a continuous linear map from the space into the scalars. This principle is used to identify dual elements with vectors in the space.

The Riesz representation is

$$
f(x)
=
\langle x,z\rangle
$$

where

- $f$ is a bounded linear functional on $H$.
- $z$ is the unique vector determined by $f$.
- $\lVert z\rVert=\lVert f\rVert$.

## Elementary Example

### Simple

The plane with the ordinary dot product is a Hilbert space.

$$
H=\mathbb{R}^{2}
$$

$$
\langle (x_{1},x_{2}),(y_{1},y_{2})\rangle
=
x_{1}y_{1}+x_{2}y_{2}
$$

where

- $H$ is the Hilbert space.
- $(x_{1},x_{2})$ and $(y_{1},y_{2})$ are vectors in the plane.

### General

Euclidean $n$-space with the standard inner product is a Hilbert space.

$$
\langle x,y\rangle
=
\sum_{j=1}^{n} \xi_{j}\eta_{j}
$$

$$
d(x,y)
=
\Biggl(\sum_{j=1}^{n}(\xi_{j}-\eta_{j})^{2}\Biggr)^{\dfrac{1}{2}}
$$

where

- $x=(\xi_{1},\ldots,\xi_{n})$ and $y=(\eta_{1},\ldots,\eta_{n})$ are vectors in $\mathbb{R}^{n}$.
- $d(x,y)$ is the Euclidean metric.

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. §3.1-1 — inner product space and Hilbert space; §3.1-3, p. 131 — Euclidean space $\mathbb{R}^{n}$; §3.2-1, p. 136 — Schwarz inequality and triangle inequality; §3.3-4, p. 146 — direct sum; §3.4-6, p. 157 — Bessel inequality; §3.6-3, p. 168 — totality and Parseval; §3.8-1, p. 188 — Riesz representation.

2. Szekeres, P. *A Course in Modern Mathematical Physics: Groups, Hilbert Space and Differential Geometry*. Cambridge University Press, 2004. §5.2, Example 5.4, p. 134 — finite-dimensional inner product space.

<!--
Hilbert space. A Hilbert space is a complete inner product space, so every Cauchy sequence converges within the space. This principle is used to combine completeness with the geometry of inner products.

Cauchy-Schwarz inequality. Every Hilbert space satisfies $|\langle x,y\rangle|\leq\|x\|\|y\|$. This principle is used to bound inner products and establish fundamental norm inequalities.

Orthogonality. Vectors $x$ and $y$ are orthogonal when $\langle x,y\rangle=0$. This principle is used to decompose vectors into mutually orthogonal components.

Projection theorem. Every vector has a unique orthogonal projection onto a closed subspace. This principle is used to obtain nearest points and best approximations within closed subspaces.

Orthonormal expansion. A complete orthonormal system represents vectors through convergent expansions in orthogonal components. This principle is used to express vectors through their inner product coefficients.

Riesz representation theorem. Every bounded linear functional on a Hilbert space has the form $f(x)=\langle x,y\rangle$ for a unique $y$. This principle is used to represent continuous linear functionals by vectors.

## Problems

- Establish $|\langle x,y\rangle|\leq\|x\|\|y\|$.
- Obtain $\|x+y\|^2=\|x\|^2+\|y\|^2$ when $\langle x,y\rangle=0$.
- Establish existence and uniqueness of the orthogonal projection $P_M x$ onto a closed subspace $M$.
- Show that $x-P_M x\in M^\perp$.
- Obtain the decomposition $H=M\oplus M^\perp$ for a closed subspace $M$.
- Establish Bessel's inequality for an orthonormal sequence.
- Establish Parseval's identity for a complete orthonormal system.
- Show that every bounded linear functional has a unique representation $f(x)=\langle x,y\rangle$.
- Show that every Cauchy sequence in a Hilbert space converges to an element of the space.
-->
