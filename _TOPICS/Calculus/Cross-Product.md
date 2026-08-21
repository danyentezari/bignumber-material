# Cross Product

A vector formed from two vectors in three-dimensional space that is used to produce a direction perpendicular to both.

Determinant formula. The Cartesian cross product is the symbolic determinant whose first row is the unit vectors and whose remaining rows are the components of the two factors. This principle is used to compute the product from coordinates.

The determinant formula is

$$
\mathbf{a}\times\mathbf{b}
=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_{1} & a_{2} & a_{3} \\
b_{1} & b_{2} & b_{3}
\end{vmatrix}
$$

which equals

$$
\mathbf{a}\times\mathbf{b}
=
(a_{2}b_{3}-a_{3}b_{2})\mathbf{i}
+
(a_{3}b_{1}-a_{1}b_{3})\mathbf{j}
+
(a_{1}b_{2}-a_{2}b_{1})\mathbf{k}
$$

where

- $\mathbf{a}$ is the first vector.
- $\mathbf{b}$ is the second vector.
- $a_{1}$, $a_{2}$, $a_{3}$ are the Cartesian components of $\mathbf{a}$.
- $b_{1}$, $b_{2}$, $b_{3}$ are the Cartesian components of $\mathbf{b}$.
- $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$ are the Cartesian unit vectors.

Magnitude formula. The length of the cross product equals the product of the two lengths times the sine of the included angle. An included angle is the angle between the two directions. This principle is used to compute the area of the parallelogram they span.

The magnitude formula is

$$
\lvert\mathbf{a}\times\mathbf{b}\rvert
=
\lvert\mathbf{a}\rvert\,\lvert\mathbf{b}\rvert\sin\theta
$$

where

- $\lvert\mathbf{a}\times\mathbf{b}\rvert$ is the length of the cross product.
- $\lvert\mathbf{a}\rvert$ is the length of $\mathbf{a}$.
- $\lvert\mathbf{b}\rvert$ is the length of $\mathbf{b}$.
- $\theta$ is the included angle.

Right-hand rule. If the fingers of the right hand curl from the first vector toward the second through the included angle, the thumb points along the cross product. This principle is used to fix the sense of the perpendicular.

Orthogonality. The cross product is orthogonal to both factors. Orthogonal means the dot product with each factor vanishes. This principle is used to construct a normal to a plane.

The orthogonality identities are

$$
\mathbf{a}\cdot(\mathbf{a}\times\mathbf{b})
=
0
$$

$$
\mathbf{b}\cdot(\mathbf{a}\times\mathbf{b})
=
0
$$

where

- $\mathbf{a}$ is the first vector.
- $\mathbf{b}$ is the second vector.

Anticommutativity. Reversing the order of the factors reverses the direction of the product. This principle is used to track orientation when the factors are swapped.

The anticommutativity identity is

$$
\mathbf{a}\times\mathbf{b}
=
-(\mathbf{b}\times\mathbf{a})
$$

where

- $\mathbf{a}$ is the first vector.
- $\mathbf{b}$ is the second vector.

Note: Also called the vector product. Also denoted $\mathbf{a}\times\mathbf{b}$.

## References

1. Stewart, J., Clegg, D., & Watson, S. *Calculus: Early Transcendentals*. Section 12.4 — determinant formula; $\lvert\mathbf{a}\times\mathbf{b}\rvert=\lvert\mathbf{a}\rvert\lvert\mathbf{b}\rvert\sin\theta$; right-hand rule; orthogonality to both factors.
2. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. Section 9.3 — vector product; right-handed triple; perpendicular direction.
3. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. Section 1.4 — determinant formula; parallelogram area; orthogonality.
4. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*. 7th ed. Academic Press, 2013. Section 3.2 — component formula; right-handed system; $A\cdot C=B\cdot C=0$.
5. Boas, M. L. *Mathematical Methods in the Physical Sciences*. 3rd ed. Wiley, 2005. Chapter 3, Section 4 — determinant formula.
