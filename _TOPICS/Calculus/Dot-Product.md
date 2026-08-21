# Dot Product

A scalar formed from two vectors that is used to measure how much the vectors align.

Component formula. In Cartesian coordinates the dot product is the sum of products of matching components. This principle is used to compute the scalar from given coordinates.

The component formula is

$$
\mathbf{a}\cdot\mathbf{b}
=
a_{1}b_{1}+a_{2}b_{2}+a_{3}b_{3}
$$

where

- $\mathbf{a}$ is the first vector.
- $\mathbf{b}$ is the second vector.
- $a_{1}$, $a_{2}$, $a_{3}$ are the Cartesian components of $\mathbf{a}$.
- $b_{1}$, $b_{2}$, $b_{3}$ are the Cartesian components of $\mathbf{b}$.

Geometric formula. The dot product equals the product of the two lengths times the cosine of the included angle. An included angle is the angle between the two directions. This principle is used to read alignment from lengths and angle.

The geometric formula is

$$
\mathbf{a}\cdot\mathbf{b}
=
\lvert\mathbf{a}\rvert\,\lvert\mathbf{b}\rvert\cos\theta
$$

where

- $\lvert\mathbf{a}\rvert$ is the length of $\mathbf{a}$.
- $\lvert\mathbf{b}\rvert$ is the length of $\mathbf{b}$.
- $\theta$ is the included angle.

Symmetry. Swapping the two vectors leaves the value unchanged. This principle is used to reverse the order of factors.

The symmetry identity is

$$
\mathbf{a}\cdot\mathbf{b}
=
\mathbf{b}\cdot\mathbf{a}
$$

where

- $\mathbf{a}$ is the first vector.
- $\mathbf{b}$ is the second vector.

Positive definiteness. The dot product of a vector with itself is the square of its length and is zero only for the zero vector. This principle is used to recover length from the dot product.

The self-product is

$$
\mathbf{a}\cdot\mathbf{a}
=
\lvert\mathbf{a}\rvert^{2}
$$

where

- $\mathbf{a}$ is a vector.
- $\lvert\mathbf{a}\rvert$ is the length of $\mathbf{a}$.

Scalar projection. The component of one vector along another is the dot product with a unit vector in that direction. A unit vector is a vector of length one. This principle is used to extract the parallel part.

The scalar projection of $\mathbf{b}$ onto $\mathbf{a}$ is

$$
\operatorname{comp}_{\mathbf{a}}\mathbf{b}
=
\dfrac{\mathbf{a}\cdot\mathbf{b}}{\lvert\mathbf{a}\rvert}
$$

where

- $\mathbf{a}$ is the direction vector.
- $\mathbf{b}$ is the vector being projected.
- $\lvert\mathbf{a}\rvert$ is the length of $\mathbf{a}$.

Note: Also called the inner product. Also called the scalar product. Also denoted $\mathbf{a}\cdot\mathbf{b}$.

## References

1. Stewart, J., Clegg, D., & Watson, S. *Calculus: Early Transcendentals*. Section 12.3 — component formula; geometric formula $\mathbf{a}\cdot\mathbf{b}=\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\cos\theta$; scalar projection.
2. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. Section 9.2 — inner product; geometric formula; work of a force.
3. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. Section 1.4 — dot product in $\mathbb{R}^{n}$; cosine formula in $\mathbb{R}^{2}$ and $\mathbb{R}^{3}$.
4. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*. 7th ed. Academic Press, 2013. Section 1.2 — $A\cdot B=\sum_{i}A_{i}B_{i}$; cosine formula.
5. Boas, M. L. *Mathematical Methods in the Physical Sciences*. 3rd ed. Wiley, 2005. Chapter 3, Section 4 — Cartesian component formula.
