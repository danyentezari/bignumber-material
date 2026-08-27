# Derivation of Curl

$\displaystyle \operatorname{curl} \mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ F_{x} & F_{y} & F_{z} \end{vmatrix}$

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
\frac{\partial F_z}{\partial y}
-
\frac{\partial F_y}{\partial z}
$$

$$
Y
=
\frac{\partial F_x}{\partial z}
-
\frac{\partial F_z}{\partial x}
$$

$$
Z
=
\frac{\partial F_y}{\partial x}
-
\frac{\partial F_x}{\partial y}
$$

where

- $X$ is the differential component along $x$.
- $Y$ is the differential component along $y$.
- $Z$ is the differential component along $z$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\partial$ denotes partial differentiation.

These quantities transform together as Cartesian vector components. Therefore,

$$
\mathbf{R}
=
X\mathbf{i}
+
Y\mathbf{j}
+
Z\mathbf{k}
$$


where

- $\mathbf{R}$ is the resulting vector field.
- $X$, $Y$, $Z$ are its Cartesian components.


![A rectangular loop in the $yz$-plane with corners $(0,y,z)$, $(0,y+\Delta y,z)$, $(0,y+\Delta y,z+\Delta z)$, and $(0,y,z+\Delta z)$. The path is traversed counterclockwise as seen from the positive $x$-axis.](3d-coordinate-loop-diagram.png){#fig:3d-coordinate-loop-diagram}


Substituting the differential components gives

$$
\mathbf{R}
=
\left(
\frac{\partial F_z}{\partial y}
-
\frac{\partial F_y}{\partial z}
\right)\mathbf{i}
+
\left(
\frac{\partial F_x}{\partial z}
-
\frac{\partial F_z}{\partial x}
\right)\mathbf{j}
+
\left(
\frac{\partial F_y}{\partial x}
-
\frac{\partial F_x}{\partial y}
\right)\mathbf{k}
$$

where

- $\mathbf{i}$ gives the $x$ direction.
- $\mathbf{j}$ gives the $y$ direction.
- $\mathbf{k}$ gives the $z$ direction.

Curl. This vector is the curl of $\mathbf{F}$:

$$
\operatorname{curl}\mathbf{F}
=
\left(
\frac{\partial F_z}{\partial y}
-
\frac{\partial F_y}{\partial z}
\right)\mathbf{i}
+
\left(
\frac{\partial F_x}{\partial z}
-
\frac{\partial F_z}{\partial x}
\right)\mathbf{j}
+
\left(
\frac{\partial F_y}{\partial x}
-
\frac{\partial F_x}{\partial y}
\right)\mathbf{k}
$$

where

- $\operatorname{curl}\mathbf{F}$ is the curl of $\mathbf{F}$.
- Each coefficient is a Cartesian curl component.

Thus,

$$
(\operatorname{curl}\mathbf{F})_x
=
\frac{\partial F_z}{\partial y}
-
\frac{\partial F_y}{\partial z}
$$

$$
(\operatorname{curl}\mathbf{F})_y
=
\frac{\partial F_x}{\partial z}
-
\frac{\partial F_z}{\partial x}
$$

$$
(\operatorname{curl}\mathbf{F})_z
=
\frac{\partial F_y}{\partial x}
-
\frac{\partial F_x}{\partial y}
$$

where

- $(\operatorname{curl}\mathbf{F})_x$ is the $x$-component.
- $(\operatorname{curl}\mathbf{F})_y$ is the $y$-component.
- $(\operatorname{curl}\mathbf{F})_z$ is the $z$-component.

Cross Product. For

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

The cross product is

$$
\mathbf{a}\times\mathbf{b}
=
(a_2b_3-a_3b_2)\mathbf{i}
+
(a_3b_1-a_1b_3)\mathbf{j}
+
(a_1b_2-a_2b_1)\mathbf{k}
$$

where

- $\mathbf{a}\times\mathbf{b}$ is the cross product.
- Each coefficient is a Cartesian component.

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

The cross-product rule gives

$$
\nabla\times\mathbf{F}
=
\left(
\frac{\partial F_z}{\partial y}
-
\frac{\partial F_y}{\partial z}
\right)\mathbf{i}
+
\left(
\frac{\partial F_x}{\partial z}
-
\frac{\partial F_z}{\partial x}
\right)\mathbf{j}
+
\left(
\frac{\partial F_y}{\partial x}
-
\frac{\partial F_x}{\partial y}
\right)\mathbf{k}
$$

where

- $\nabla$ supplies the differential operators.
- $\mathbf{F}$ supplies the field components.
- $\times$ applies the cross-product rule.

Comparing with the component form,

$$
\operatorname{curl}\mathbf{F}
=
\nabla\times\mathbf{F}.
$$

Determinant Form. The ordinary cross product may be written

$$
\mathbf{a}\times\mathbf{b}
=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
$$

where

- The first row contains Cartesian unit vectors.
- The second row contains $\mathbf{a}$ components.
- The third row contains $\mathbf{b}$ components.

Replacing $\mathbf{a}$ by $\nabla$ and $\mathbf{b}$ by $\mathbf{F}$ gives

$$
\nabla\times\mathbf{F}
=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\dfrac{\partial}{\partial x}
&
\dfrac{\partial}{\partial y}
&
\dfrac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix}
$$

where

- The first row contains Cartesian unit vectors.
- The second row contains differential operators.
- The third row contains field components.
- The determinant is symbolic.

Expanding the determinant,

$$
\nabla\times\mathbf{F}
=
\mathbf{i}
\begin{vmatrix}
\dfrac{\partial}{\partial y}
&
\dfrac{\partial}{\partial z} \\
F_y & F_z
\end{vmatrix}
-
\mathbf{j}
\begin{vmatrix}
\dfrac{\partial}{\partial x}
&
\dfrac{\partial}{\partial z} \\
F_x & F_z
\end{vmatrix}
+
\mathbf{k}
\begin{vmatrix}
\dfrac{\partial}{\partial x}
&
\dfrac{\partial}{\partial y} \\
F_x & F_y
\end{vmatrix}.
$$

Evaluating the minors gives

$$
\nabla\times\mathbf{F}
=
\left(
\frac{\partial F_z}{\partial y}
-
\frac{\partial F_y}{\partial z}
\right)\mathbf{i}
-
\left(
\frac{\partial F_z}{\partial x}
-
\frac{\partial F_x}{\partial z}
\right)\mathbf{j}
+
\left(
\frac{\partial F_y}{\partial x}
-
\frac{\partial F_x}{\partial y}
\right)\mathbf{k}.
$$

Rearranging the $y$-component,

$$
\nabla\times\mathbf{F}
=
\left(
\frac{\partial F_z}{\partial y}
-
\frac{\partial F_y}{\partial z}
\right)\mathbf{i}
+
\left(
\frac{\partial F_x}{\partial z}
-
\frac{\partial F_z}{\partial x}
\right)\mathbf{j}
+
\left(
\frac{\partial F_y}{\partial x}
-
\frac{\partial F_x}{\partial y}
\right)\mathbf{k}.
$$

Hence,

$\displaystyle \operatorname{curl} \mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ F_{x} & F_{y} & F_{z} \end{vmatrix}$

## References

1. MacCullagh, J. *An Essay towards a Dynamical Theory of Crystalline Reflexion and Refraction*. Transactions of the Royal Irish Academy, Vol. XXI. Read 9 December 1839; published 1846.

2. Lunney, J. G. *James MacCullagh*. Trinity College Dublin, 2015.

3. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011.

4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. 