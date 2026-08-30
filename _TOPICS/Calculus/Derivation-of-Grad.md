# Derivation of Grad

$\displaystyle \operatorname{grad}\mathbf{F} = J_{\mathbf{F}} = \begin{pmatrix} \dfrac{\partial F_{x}}{\partial x} & \dfrac{\partial F_{x}}{\partial y} & \dfrac{\partial F_{x}}{\partial z} \\ \dfrac{\partial F_{y}}{\partial x} & \dfrac{\partial F_{y}}{\partial y} & \dfrac{\partial F_{y}}{\partial z} \\ \dfrac{\partial F_{z}}{\partial x} & \dfrac{\partial F_{z}}{\partial y} & \dfrac{\partial F_{z}}{\partial z} \end{pmatrix}$

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{F}
&=
F_x\mathbf{i}+F_y\mathbf{j}+F_z\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Start from a Cartesian vector field</div>
</div>

</div>

where

- $\mathbf{F}$ is a vector field.
- $F_x$ is the $x$-component of $\mathbf{F}$.
- $F_y$ is the $y$-component of $\mathbf{F}$.
- $F_z$ is the $z$-component of $\mathbf{F}$.
- $\mathbf{i}$ is the unit vector along $x$.
- $\mathbf{j}$ is the unit vector along $y$.
- $\mathbf{k}$ is the unit vector along $z$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
(\operatorname{grad}\mathbf{F})_{11}
&=
\dfrac{\partial F_x}{\partial x}
\\
(\operatorname{grad}\mathbf{F})_{12}
&=
\dfrac{\partial F_x}{\partial y}
\\
(\operatorname{grad}\mathbf{F})_{13}
&=
\dfrac{\partial F_x}{\partial z}
\\
(\operatorname{grad}\mathbf{F})_{21}
&=
\dfrac{\partial F_y}{\partial x}
\\
(\operatorname{grad}\mathbf{F})_{22}
&=
\dfrac{\partial F_y}{\partial y}
\\
(\operatorname{grad}\mathbf{F})_{23}
&=
\dfrac{\partial F_y}{\partial z}
\\
(\operatorname{grad}\mathbf{F})_{31}
&=
\dfrac{\partial F_z}{\partial x}
\\
(\operatorname{grad}\mathbf{F})_{32}
&=
\dfrac{\partial F_z}{\partial y}
\\
(\operatorname{grad}\mathbf{F})_{33}
&=
\dfrac{\partial F_z}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Define the nine Cartesian differential components</div>
</div>

</div>

where

- $(\operatorname{grad}\mathbf{F})_{ij}$ is the differential component in row $i$ and column $j$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\partial$ denotes partial differentiation.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{R}
&=
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
\end{align*}
$$

</div>
<div class="derivation-just">Assemble those components into a matrix</div>
</div>

</div>

where

- $\mathbf{R}$ is the resulting matrix field.
- Each entry is a Cartesian differential component.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{R}
&=
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
\end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Rewrite the matrix in index form</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{x}
&=
\begin{pmatrix} x \\ y \\ z \end{pmatrix}
\\
\Delta\mathbf{x}
&=
\begin{pmatrix} \Delta x \\ \Delta y \\ \Delta z \end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Take a position and a small change in position</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\mathbf{F}
&=
\mathbf{F}(\mathbf{x}+\Delta\mathbf{x})-\mathbf{F}(\mathbf{x})
\end{align*}
$$

</div>
<div class="derivation-just">Form the corresponding change in the field</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta F_x
&=
F_x(x+\Delta x,y+\Delta y,z+\Delta z)-F_x(x,y,z)
\\
\Delta F_y
&=
F_y(x+\Delta x,y+\Delta y,z+\Delta z)-F_y(x,y,z)
\\
\Delta F_z
&=
F_z(x+\Delta x,y+\Delta y,z+\Delta z)-F_z(x,y,z)
\end{align*}
$$

</div>
<div class="derivation-just">Write the change in each Cartesian component</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta F_x
&\approx
\dfrac{\partial F_x}{\partial x}\Delta x
\\
&\quad
+
\dfrac{\partial F_x}{\partial y}\Delta y
\\
&\quad
+
\dfrac{\partial F_x}{\partial z}\Delta z
\\
\Delta F_y
&\approx
\dfrac{\partial F_y}{\partial x}\Delta x
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}\Delta y
\\
&\quad
+
\dfrac{\partial F_y}{\partial z}\Delta z
\\
\Delta F_z
&\approx
\dfrac{\partial F_z}{\partial x}\Delta x
\\
&\quad
+
\dfrac{\partial F_z}{\partial y}\Delta y
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}\Delta z
\end{align*}
$$

</div>
<div class="derivation-just">Keep the first-order increment of each component</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{grad}\mathbf{F}
&=
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
\end{align*}
$$

</div>
<div class="derivation-just">Name this matrix the gradient of F</div>
</div>

</div>

where

- $\operatorname{grad}\mathbf{F}$ is the gradient of $\mathbf{F}$.
- Each entry is a Cartesian gradient component.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
(\operatorname{grad}\mathbf{F})_{ij}
&=
\dfrac{\partial F_i}{\partial x_j}
\end{align*}
$$

</div>
<div class="derivation-just">Write the entries in index notation</div>
</div>

</div>

where

- $(x_1,x_2,x_3)=(x,y,z)$.
- $(F_1,F_2,F_3)=(F_x,F_y,F_z)$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}
&=
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
\\
\mathbf{b}
&=
\begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Write a general matrix and a general column vector</div>
</div>

</div>

where

- $\mathbf{a}$ is the first factor.
- $\mathbf{b}$ is the second factor.
- $a_{ij}$ are entries of $\mathbf{a}$.
- $b_1$, $b_2$, $b_3$ are components of $\mathbf{b}$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}\mathbf{b}
&=
\begin{pmatrix}
a_{11}b_1+a_{12}b_2+a_{13}b_3 \\
a_{21}b_1+a_{22}b_2+a_{23}b_3 \\
a_{31}b_1+a_{32}b_2+a_{33}b_3
\end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Form the ordinary matrix product</div>
</div>

</div>

where

- $\mathbf{a}\mathbf{b}$ is the matrix product.
- Each row is a Cartesian component.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla
&=
\mathbf{i}\dfrac{\partial}{\partial x}
\\
&\quad
+\mathbf{j}\dfrac{\partial}{\partial y}
\\
&\quad
+\mathbf{k}\dfrac{\partial}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Define the vector differential operator</div>
</div>

</div>

where

- $\nabla$ is the vector differential operator.
- $\dfrac{\partial}{\partial x}$ differentiates with respect to $x$.
- $\dfrac{\partial}{\partial y}$ differentiates with respect to $y$.
- $\dfrac{\partial}{\partial z}$ differentiates with respect to $z$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}
&=
\operatorname{grad}\mathbf{F}
\\
\mathbf{b}
&=
\Delta\mathbf{x}
\end{align*}
$$

</div>
<div class="derivation-just">Identify the factors with the gradient matrix and the displacement</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\mathbf{F}
&\approx
\operatorname{grad}\mathbf{F}\,\Delta\mathbf{x}
\end{align*}
$$

</div>
<div class="derivation-just">Apply the matrix-product rule</div>
</div>

</div>

where

- $\operatorname{grad}\mathbf{F}$ supplies the differential components.
- $\Delta\mathbf{x}$ supplies the coordinate increments.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{grad}\mathbf{F}
&=
\mathbf{R}
\end{align*}
$$

</div>
<div class="derivation-just">Compare with the assembled matrix</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla F_x
&=
\dfrac{\partial F_x}{\partial x}\mathbf{i}
\\
&\quad
+
\dfrac{\partial F_x}{\partial y}\mathbf{j}
\\
&\quad
+
\dfrac{\partial F_x}{\partial z}\mathbf{k}
\\
\nabla F_y
&=
\dfrac{\partial F_y}{\partial x}\mathbf{i}
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}\mathbf{j}
\\
&\quad
+
\dfrac{\partial F_y}{\partial z}\mathbf{k}
\\
\nabla F_z
&=
\dfrac{\partial F_z}{\partial x}\mathbf{i}
\\
&\quad
+
\dfrac{\partial F_z}{\partial y}\mathbf{j}
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Apply nabla separately to each scalar component</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{grad}\mathbf{F}
&=
\begin{pmatrix}
(\nabla F_x)^{T} \\
(\nabla F_y)^{T} \\
(\nabla F_z)^{T}
\end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Stack those component gradients as the rows of the matrix</div>
</div>

</div>

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{u}
&=
\begin{pmatrix} u_x \\ u_y \\ u_z \end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Take a unit direction</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\mathbf{x}
&=
\Delta s\,\mathbf{u}
\end{align*}
$$

</div>
<div class="derivation-just">Write a small displacement along that direction</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\mathbf{F}
&\approx
\operatorname{grad}\mathbf{F}\,\mathbf{u}\,\Delta s
\end{align*}
$$

</div>
<div class="derivation-just">Substitute the directed displacement</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\dfrac{\Delta\mathbf{F}}{\Delta s}
&\approx
\operatorname{grad}\mathbf{F}\,\mathbf{u}
\end{align*}
$$

</div>
<div class="derivation-just">Divide by the step length</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
D_{\mathbf{u}}\mathbf{F}
&=
\operatorname{grad}\mathbf{F}\,\mathbf{u}
\end{align*}
$$

</div>
<div class="derivation-just">Pass to the directional derivative</div>
</div>

</div>

where

- $D_{\mathbf{u}}\mathbf{F}$ is the directional derivative of the vector field.
- $\mathbf{u}$ specifies the direction.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
J_{\mathbf{F}}
&=
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
\end{align*}
$$

</div>
<div class="derivation-just">Write the Jacobian matrix of the map F</div>
</div>

</div>

where

- $\mathbf{F}:\mathbb{R}^{3}\to\mathbb{R}^{3}$ is a vector-valued map.
- $J_{\mathbf{F}}$ is the Jacobian matrix.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{grad}\mathbf{F}
&=
J_{\mathbf{F}}
\end{align*}
$$

</div>
<div class="derivation-just">Identify the gradient matrix with the Jacobian</div>
</div>

</div>

Hence,

$\displaystyle \operatorname{grad}\mathbf{F} = J_{\mathbf{F}} = \begin{pmatrix} \dfrac{\partial F_{x}}{\partial x} & \dfrac{\partial F_{x}}{\partial y} & \dfrac{\partial F_{x}}{\partial z} \\ \dfrac{\partial F_{y}}{\partial x} & \dfrac{\partial F_{y}}{\partial y} & \dfrac{\partial F_{y}}{\partial z} \\ \dfrac{\partial F_{z}}{\partial x} & \dfrac{\partial F_{z}}{\partial y} & \dfrac{\partial F_{z}}{\partial z} \end{pmatrix}$

## References

1. Anand, L., & Govindjee, S. *Continuum Mechanics of Solids*. Oxford University Press, 2020. Chapter 2, §§2.1–2.2, pp. 23–25 — directional derivatives of vector fields; the gradient of a vector field as a second-order tensor; $(\operatorname{grad}\mathbf{v})_{ij}=\partial v_i/\partial x_j$.

2. Bower, A. F. *Applied Mechanics of Solids*. CRC Press, 2009. Appendix A.2.8 — gradient of a vector field as a tensor field and its Cartesian matrix with entries $\partial v_i/\partial x_j$.

3. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. §1.7 — derivative of a map between finite-dimensional spaces and the Jacobian matrix formed from its first partial derivatives.

4. Kreyszig, E. *Advanced Engineering Mathematics*. 10th ed. Wiley, 2011. §9.4, p. 375 onward — vector and scalar functions and partial derivatives of vector functions; §9.6, p. 392 onward — functions of several variables, total differentials, and chain rules.

5. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. 3rd ed. Cambridge University Press, 2006. Chapter 10, especially §§10.1, 10.4, 10.6–10.7 — differentiation of vectors, vector functions of several variables, scalar and vector fields, and vector differential operators.
