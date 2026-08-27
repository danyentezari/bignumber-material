# Derivation of Divergence

$\displaystyle \operatorname{div}\mathbf{F} = \nabla\cdot\mathbf{F} = \dfrac{\partial F_{x}}{\partial x} + \dfrac{\partial F_{y}}{\partial y} + \dfrac{\partial F_{z}}{\partial z}$

Vector Field. Let

$$
\mathbf{F}
=
F_x\mathbf{i}
+
F_y\mathbf{j}
+
F_z\mathbf{k}
$$

where

- $\mathbf{F}$ is a vector field.
- $F_x$ is the $x$-component of $\mathbf{F}$.
- $F_y$ is the $y$-component of $\mathbf{F}$.
- $F_z$ is the $z$-component of $\mathbf{F}$.
- $\mathbf{i}$ is the unit vector along $x$.
- $\mathbf{j}$ is the unit vector along $y$.
- $\mathbf{k}$ is the unit vector along $z$.

Differential Components. Define

$$
X
=
\frac{\partial F_x}{\partial x}
$$

$$
Y
=
\frac{\partial F_y}{\partial y}
$$

$$
Z
=
\frac{\partial F_z}{\partial z}
$$

where

- $X$ is the differential component along $x$.
- $Y$ is the differential component along $y$.
- $Z$ is the differential component along $z$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\partial$ denotes partial differentiation.

These quantities add as Cartesian scalar contributions. Therefore,

$$
R
=
X
+
Y
+
Z
$$

where

- $R$ is the resulting scalar field.
- $X$, $Y$, $Z$ are its Cartesian contributions.

Substituting the differential components gives

$$
R
=
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}.
$$

Flux Through a Small Box. Consider a rectangular box with side lengths

$$
\Delta x,
\qquad
\Delta y,
\qquad
\Delta z.
$$

Its volume is

$$
\Delta V
=
\Delta x\,\Delta y\,\Delta z.
$$

The two faces perpendicular to the $x$-axis each have area

$$
\Delta A_x
=
\Delta y\,\Delta z.
$$

The outward flux through the face at $x+\Delta x$ is approximately

$$
F_x(x+\Delta x,y,z)
\Delta y\,\Delta z.
$$

The outward normal of the opposite face points in the negative $x$-direction, so its outward flux is approximately

$$
-
F_x(x,y,z)
\Delta y\,\Delta z.
$$

Therefore, the net outward flux through the two $x$-faces is

$$
\begin{aligned}
\Delta\Phi_x
&=
F_x(x+\Delta x,y,z)
\Delta y\,\Delta z
-
F_x(x,y,z)
\Delta y\,\Delta z
\\
&=
\left[
F_x(x+\Delta x,y,z)
-
F_x(x,y,z)
\right]
\Delta y\,\Delta z.
\end{aligned}
$$

By the definition of the partial derivative,

$$
\frac{\partial F_x}{\partial x}
=
\lim_{\Delta x\to0}
\frac{
F_x(x+\Delta x,y,z)
-
F_x(x,y,z)
}{
\Delta x
}.
$$

For small $\Delta x$,

$$
F_x(x+\Delta x,y,z)
-
F_x(x,y,z)
\approx
\frac{\partial F_x}{\partial x}\Delta x.
$$

Substituting gives

$$
\Delta\Phi_x
\approx
\frac{\partial F_x}{\partial x}
\Delta x\,\Delta y\,\Delta z.
$$

Since

$$
\Delta V
=
\Delta x\,\Delta y\,\Delta z,
$$

we obtain

$$
\Delta\Phi_x
\approx
\frac{\partial F_x}{\partial x}
\Delta V.
$$

Similarly,

$$
\Delta\Phi_y
\approx
\frac{\partial F_y}{\partial y}
\Delta V
$$

and

$$
\Delta\Phi_z
\approx
\frac{\partial F_z}{\partial z}
\Delta V.
$$

Total Flux. The total outward flux through the box is

$$
\Delta\Phi
=
\Delta\Phi_x
+
\Delta\Phi_y
+
\Delta\Phi_z.
$$

Substituting the three contributions gives

$$
\Delta\Phi
\approx
\left(
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}
\right)
\Delta V.
$$

Dividing by the volume gives

$$
\frac{\Delta\Phi}{\Delta V}
\approx
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}.
$$

Taking the limit as the box shrinks to a point gives

$$
\lim_{\Delta V\to0}
\frac{\Delta\Phi}{\Delta V}
=
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}.
$$

Divergence. This scalar is the divergence of $\mathbf{F}$:

$$
\operatorname{div}\mathbf{F}
=
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}
$$

where

- $\operatorname{div}\mathbf{F}$ is the divergence of $\mathbf{F}$.
- Each term is a Cartesian differential contribution.

Thus,

$$
\operatorname{div}\mathbf{F}
=
X
+
Y
+
Z.
$$

Dot Product. For

$$
\mathbf{a}
=
a_1\mathbf{i}
+
a_2\mathbf{j}
+
a_3\mathbf{k}
$$

and

$$
\mathbf{b}
=
b_1\mathbf{i}
+
b_2\mathbf{j}
+
b_3\mathbf{k}
$$

where

- $\mathbf{a}$ is the first vector.
- $\mathbf{b}$ is the second vector.
- $a_1$, $a_2$, $a_3$ are components of $\mathbf{a}$.
- $b_1$, $b_2$, $b_3$ are components of $\mathbf{b}$.

The dot product is

$$
\mathbf{a}\cdot\mathbf{b}
=
a_1b_1
+
a_2b_2
+
a_3b_3
$$

where

- $\mathbf{a}\cdot\mathbf{b}$ is the dot product.
- Each term is a Cartesian contribution.

Differential Operator. Define

$$
\nabla
=
\mathbf{i}\frac{\partial}{\partial x}
+
\mathbf{j}\frac{\partial}{\partial y}
+
\mathbf{k}\frac{\partial}{\partial z}
$$

where

- $\nabla$ is the vector differential operator.
- $\dfrac{\partial}{\partial x}$ differentiates with respect to $x$.
- $\dfrac{\partial}{\partial y}$ differentiates with respect to $y$.
- $\dfrac{\partial}{\partial z}$ differentiates with respect to $z$.

Set

$$
\mathbf{a}=\nabla
$$

and

$$
\mathbf{b}=\mathbf{F}.
$$

The dot-product rule gives

$$
\nabla\cdot\mathbf{F}
=
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}
$$

where

- $\nabla$ supplies the differential operators.
- $\mathbf{F}$ supplies the field components.
- $\cdot$ applies the dot-product rule.

Comparing with the component form,

$$
\operatorname{div}\mathbf{F}
=
\nabla\cdot\mathbf{F}.
$$

Trace Form. The ordinary gradient matrix may be written

$$
\operatorname{grad}\mathbf{F}
=
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x}
&
\dfrac{\partial F_x}{\partial y}
&
\dfrac{\partial F_x}{\partial z}
\\
\dfrac{\partial F_y}{\partial x}
&
\dfrac{\partial F_y}{\partial y}
&
\dfrac{\partial F_y}{\partial z}
\\
\dfrac{\partial F_z}{\partial x}
&
\dfrac{\partial F_z}{\partial y}
&
\dfrac{\partial F_z}{\partial z}
\end{pmatrix}
$$

where

- Each row contains partial derivatives of one field component.
- Each column contains partial derivatives along one coordinate.

The trace of this matrix is

$$
\operatorname{tr}
\left(
\operatorname{grad}\mathbf{F}
\right)
=
\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}
$$

where

- $\operatorname{tr}$ denotes the trace of a matrix.
- The trace is the sum of the diagonal entries.

Comparing with the component form,

$$
\operatorname{div}\mathbf{F}
=
\operatorname{tr}
\left(
\operatorname{grad}\mathbf{F}
\right).
$$

Hence,

$\displaystyle \operatorname{div}\mathbf{F} = \nabla\cdot\mathbf{F} = \dfrac{\partial F_{x}}{\partial x} + \dfrac{\partial F_{y}}{\partial y} + \dfrac{\partial F_{z}}{\partial z}$

## References

1. Kreyszig, E. *Advanced Engineering Mathematics*. 10th ed. Wiley, 2011. §9.8 — divergence of a vector field and its Cartesian representation.

2. Kreyszig, E. *Advanced Engineering Mathematics*. 10th ed. Wiley, 2011. §10.7 — Gauss's divergence theorem and the relation between divergence and outward flux.

3. Griffiths, D. J. *Introduction to Electrodynamics*. 4th ed. Pearson, 2013. Chapter 1 — divergence, flux, and the divergence theorem.

4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. 3rd ed. Cambridge University Press, 2006. Chapters 10–11 — vector differential operators and surface and volume integrals.

5. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists: A Comprehensive Guide*. 7th ed. Academic Press, 2012. Chapter 3 — vector analysis, differential vector operators, surface integrals, and integral theorems.
