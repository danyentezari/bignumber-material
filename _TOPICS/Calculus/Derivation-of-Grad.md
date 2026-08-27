# Derivation of Grad

$\displaystyle \operatorname{grad}\mathbf{F} = J_{\mathbf{F}} = \begin{pmatrix} \dfrac{\partial F_{x}}{\partial x} & \dfrac{\partial F_{x}}{\partial y} & \dfrac{\partial F_{x}}{\partial z} \\ \dfrac{\partial F_{y}}{\partial x} & \dfrac{\partial F_{y}}{\partial y} & \dfrac{\partial F_{y}}{\partial z} \\ \dfrac{\partial F_{z}}{\partial x} & \dfrac{\partial F_{z}}{\partial y} & \dfrac{\partial F_{z}}{\partial z} \end{pmatrix}$

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
(\operatorname{grad}\mathbf{F})_{11}
=
\frac{\partial F_x}{\partial x}
$$

$$
(\operatorname{grad}\mathbf{F})_{12}
=
\frac{\partial F_x}{\partial y}
$$

$$
(\operatorname{grad}\mathbf{F})_{13}
=
\frac{\partial F_x}{\partial z}
$$

$$
(\operatorname{grad}\mathbf{F})_{21}
=
\frac{\partial F_y}{\partial x}
$$

$$
(\operatorname{grad}\mathbf{F})_{22}
=
\frac{\partial F_y}{\partial y}
$$

$$
(\operatorname{grad}\mathbf{F})_{23}
=
\frac{\partial F_y}{\partial z}
$$

$$
(\operatorname{grad}\mathbf{F})_{31}
=
\frac{\partial F_z}{\partial x}
$$

$$
(\operatorname{grad}\mathbf{F})_{32}
=
\frac{\partial F_z}{\partial y}
$$

$$
(\operatorname{grad}\mathbf{F})_{33}
=
\frac{\partial F_z}{\partial z}
$$

where

- $(\operatorname{grad}\mathbf{F})_{ij}$ is the differential component in row $i$ and column $j$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\partial$ denotes partial differentiation.

These quantities form a Cartesian matrix of components. Therefore,

$$
\mathbf{R}
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

- $\mathbf{R}$ is the resulting matrix field.
- Each entry is a Cartesian differential component.

Substituting the differential components gives

$$
\mathbf{R}
=
\begin{pmatrix}
(\operatorname{grad}\mathbf{F})_{11}
&
(\operatorname{grad}\mathbf{F})_{12}
&
(\operatorname{grad}\mathbf{F})_{13}
\\
(\operatorname{grad}\mathbf{F})_{21}
&
(\operatorname{grad}\mathbf{F})_{22}
&
(\operatorname{grad}\mathbf{F})_{23}
\\
(\operatorname{grad}\mathbf{F})_{31}
&
(\operatorname{grad}\mathbf{F})_{32}
&
(\operatorname{grad}\mathbf{F})_{33}
\end{pmatrix}.
$$

Position. Let

$$
\mathbf{x}
=
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
$$

and let a small change in position be

$$
\Delta\mathbf{x}
=
\begin{pmatrix}
\Delta x \\
\Delta y \\
\Delta z
\end{pmatrix}.
$$

The corresponding change in the vector field is

$$
\Delta\mathbf{F}
=
\mathbf{F}(\mathbf{x}+\Delta\mathbf{x})
-
\mathbf{F}(\mathbf{x}).
$$

Writing each component,

$$
\Delta\mathbf{F}
=
\begin{pmatrix}
F_x(x+\Delta x,y+\Delta y,z+\Delta z)-F_x(x,y,z)
\\
F_y(x+\Delta x,y+\Delta y,z+\Delta z)-F_y(x,y,z)
\\
F_z(x+\Delta x,y+\Delta y,z+\Delta z)-F_z(x,y,z)
\end{pmatrix}.
$$

First Component. For the $x$-component,

$$
\Delta F_x
=
F_x(x+\Delta x,y+\Delta y,z+\Delta z)
-
F_x(x,y,z).
$$

For small changes, the first-order change is

$$
\Delta F_x
\approx
\frac{\partial F_x}{\partial x}\Delta x
+
\frac{\partial F_x}{\partial y}\Delta y
+
\frac{\partial F_x}{\partial z}\Delta z.
$$

Second Component. Similarly,

$$
\Delta F_y
=
F_y(x+\Delta x,y+\Delta y,z+\Delta z)
-
F_y(x,y,z)
$$

and

$$
\Delta F_y
\approx
\frac{\partial F_y}{\partial x}\Delta x
+
\frac{\partial F_y}{\partial y}\Delta y
+
\frac{\partial F_y}{\partial z}\Delta z.
$$

Third Component. Similarly,

$$
\Delta F_z
=
F_z(x+\Delta x,y+\Delta y,z+\Delta z)
-
F_z(x,y,z)
$$

and

$$
\Delta F_z
\approx
\frac{\partial F_z}{\partial x}\Delta x
+
\frac{\partial F_z}{\partial y}\Delta y
+
\frac{\partial F_z}{\partial z}\Delta z.
$$

Vector Change. Combining the three component changes gives

$$
\Delta\mathbf{F}
\approx
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x}\Delta x
+
\dfrac{\partial F_x}{\partial y}\Delta y
+
\dfrac{\partial F_x}{\partial z}\Delta z
\\[6pt]
\dfrac{\partial F_y}{\partial x}\Delta x
+
\dfrac{\partial F_y}{\partial y}\Delta y
+
\dfrac{\partial F_y}{\partial z}\Delta z
\\[6pt]
\dfrac{\partial F_z}{\partial x}\Delta x
+
\dfrac{\partial F_z}{\partial y}\Delta y
+
\dfrac{\partial F_z}{\partial z}\Delta z
\end{pmatrix}.
$$

Gradient. This matrix is the gradient of $\mathbf{F}$:

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

- $\operatorname{grad}\mathbf{F}$ is the gradient of $\mathbf{F}$.
- Each entry is a Cartesian gradient component.

Thus,

$$
(\operatorname{grad}\mathbf{F})_{ij}
=
\frac{\partial F_i}{\partial x_j}
$$

where

- $(x_1,x_2,x_3)=(x,y,z)$.
- $(F_1,F_2,F_3)=(F_x,F_y,F_z)$.

Matrix Multiplication. For

$$
\mathbf{a}
=
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
$$

and

$$
\mathbf{b}
=
\begin{pmatrix}
b_1 \\
b_2 \\
b_3
\end{pmatrix}
$$

where

- $\mathbf{a}$ is the first factor.
- $\mathbf{b}$ is the second factor.
- $a_{ij}$ are entries of $\mathbf{a}$.
- $b_1$, $b_2$, $b_3$ are components of $\mathbf{b}$.

The matrix product is

$$
\mathbf{a}\mathbf{b}
=
\begin{pmatrix}
a_{11}b_1+a_{12}b_2+a_{13}b_3
\\
a_{21}b_1+a_{22}b_2+a_{23}b_3
\\
a_{31}b_1+a_{32}b_2+a_{33}b_3
\end{pmatrix}
$$

where

- $\mathbf{a}\mathbf{b}$ is the matrix product.
- Each row is a Cartesian component.

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
\mathbf{a}=\operatorname{grad}\mathbf{F}
$$

and

$$
\mathbf{b}=\Delta\mathbf{x}.
$$

The matrix-product rule gives

$$
\Delta\mathbf{F}
\approx
\operatorname{grad}\mathbf{F}\,
\Delta\mathbf{x}
$$

where

- $\operatorname{grad}\mathbf{F}$ supplies the differential components.
- $\Delta\mathbf{x}$ supplies the coordinate increments.

Comparing with the component form,

$$
\operatorname{grad}\mathbf{F}
=
\mathbf{R}.
$$

Apply $\nabla$ separately to each scalar component of $\mathbf{F}$:

$$
\nabla F_x
=
\frac{\partial F_x}{\partial x}\mathbf{i}
+
\frac{\partial F_x}{\partial y}\mathbf{j}
+
\frac{\partial F_x}{\partial z}\mathbf{k}
$$

$$
\nabla F_y
=
\frac{\partial F_y}{\partial x}\mathbf{i}
+
\frac{\partial F_y}{\partial y}\mathbf{j}
+
\frac{\partial F_y}{\partial z}\mathbf{k}
$$

$$
\nabla F_z
=
\frac{\partial F_z}{\partial x}\mathbf{i}
+
\frac{\partial F_z}{\partial y}\mathbf{j}
+
\frac{\partial F_z}{\partial z}\mathbf{k}.
$$

These three component gradients form the rows of the gradient matrix:

$$
\operatorname{grad}\mathbf{F}
=
\begin{pmatrix}
(\nabla F_x)^{T}
\\
(\nabla F_y)^{T}
\\
(\nabla F_z)^{T}
\end{pmatrix}.
$$

Directional Change. Let

$$
\mathbf{u}
=
\begin{pmatrix}
u_x \\
u_y \\
u_z
\end{pmatrix}
$$

be a unit vector.

A small displacement in this direction is

$$
\Delta\mathbf{x}
=
\Delta s\,\mathbf{u}.
$$

Substituting into

$$
\Delta\mathbf{F}
\approx
\operatorname{grad}\mathbf{F}\,
\Delta\mathbf{x}
$$

gives

$$
\Delta\mathbf{F}
\approx
\operatorname{grad}\mathbf{F}\,
\mathbf{u}\,\Delta s.
$$

Dividing by $\Delta s$,

$$
\frac{\Delta\mathbf{F}}{\Delta s}
\approx
\operatorname{grad}\mathbf{F}\,\mathbf{u}.
$$

Taking the limit as $\Delta s\to0$ gives

$$
D_{\mathbf{u}}\mathbf{F}
=
\operatorname{grad}\mathbf{F}\,\mathbf{u}
$$

where

- $D_{\mathbf{u}}\mathbf{F}$ is the directional derivative of the vector field.
- $\mathbf{u}$ specifies the direction.

Jacobian Form. The ordinary derivative of a map may be written

$$
J_{\mathbf{F}}
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

- $\mathbf{F}:\mathbb{R}^{3}\to\mathbb{R}^{3}$ is a vector-valued map.
- $J_{\mathbf{F}}$ is the Jacobian matrix.

Replacing the Jacobian by the gradient matrix gives

$$
\operatorname{grad}\mathbf{F}
=
J_{\mathbf{F}}.
$$

Hence,

$\displaystyle \operatorname{grad}\mathbf{F} = J_{\mathbf{F}} = \begin{pmatrix} \dfrac{\partial F_{x}}{\partial x} & \dfrac{\partial F_{x}}{\partial y} & \dfrac{\partial F_{x}}{\partial z} \\ \dfrac{\partial F_{y}}{\partial x} & \dfrac{\partial F_{y}}{\partial y} & \dfrac{\partial F_{y}}{\partial z} \\ \dfrac{\partial F_{z}}{\partial x} & \dfrac{\partial F_{z}}{\partial y} & \dfrac{\partial F_{z}}{\partial z} \end{pmatrix}$

## References

1. Anand, L., & Govindjee, S. *Continuum Mechanics of Solids*. Oxford University Press, 2020. Chapter 2, §§2.1–2.2, pp. 23–25 — directional derivatives of vector fields; the gradient of a vector field as a second-order tensor; $(\operatorname{grad}\mathbf{v})_{ij}=\partial v_i/\partial x_j$.

2. Bower, A. F. *Applied Mechanics of Solids*. CRC Press, 2009. Appendix A.2.8 — gradient of a vector field as a tensor field and its Cartesian matrix with entries $\partial v_i/\partial x_j$.

3. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. §1.7 — derivative of a map between finite-dimensional spaces and the Jacobian matrix formed from its first partial derivatives.

4. Kreyszig, E. *Advanced Engineering Mathematics*. 10th ed. Wiley, 2011. §9.4, p. 375 onward — vector and scalar functions and partial derivatives of vector functions; §9.6, p. 392 onward — functions of several variables, total differentials, and chain rules.

5. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. 3rd ed. Cambridge University Press, 2006. Chapter 10, especially §§10.1, 10.4, 10.6–10.7 — differentiation of vectors, vector functions of several variables, scalar and vector fields, and vector differential operators.
