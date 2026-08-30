# Derivation of Curl

$\displaystyle \operatorname{curl} \mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ F_{x} & F_{y} & F_{z} \end{vmatrix}$

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
X
&=
\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}
\\
Y
&=
\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}
\\
Z
&=
\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}
\end{align*}
$$

</div>
<div class="derivation-just">Define the three Cartesian differential components</div>
</div>

</div>

where

- $X$ is the differential component along $x$.
- $Y$ is the differential component along $y$.
- $Z$ is the differential component along $z$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\partial$ denotes partial differentiation.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{R}
&=
X\mathbf{i}+Y\mathbf{j}+Z\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Assemble those components into one vector</div>
</div>

</div>

where

- $\mathbf{R}$ is the resulting vector field.
- $X$, $Y$, $Z$ are its Cartesian components.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{R}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
+\biggl(\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}\biggr)\mathbf{j}
+\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Substitute the differential components</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{curl}\mathbf{F}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
+\biggl(\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}\biggr)\mathbf{j}
+\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Name this vector the curl of F</div>
</div>

</div>

where

- $\operatorname{curl}\mathbf{F}$ is the curl of $\mathbf{F}$.
- Each coefficient is a Cartesian curl component.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
(\operatorname{curl}\mathbf{F})_x
&=
\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}
\\
(\operatorname{curl}\mathbf{F})_y
&=
\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}
\\
(\operatorname{curl}\mathbf{F})_z
&=
\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}
\end{align*}
$$

</div>
<div class="derivation-just">Read off the three Cartesian curl components</div>
</div>

</div>

where

- $(\operatorname{curl}\mathbf{F})_x$ is the $x$-component.
- $(\operatorname{curl}\mathbf{F})_y$ is the $y$-component.
- $(\operatorname{curl}\mathbf{F})_z$ is the $z$-component.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}
&=
a_1\mathbf{i}+a_2\mathbf{j}+a_3\mathbf{k}
\\
\mathbf{b}
&=
b_1\mathbf{i}+b_2\mathbf{j}+b_3\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Write two general Cartesian vectors</div>
</div>

</div>

where

- $\mathbf{a}$ is the first vector.
- $\mathbf{b}$ is the second vector.
- $a_1$, $a_2$, $a_3$ are components of $\mathbf{a}$.
- $b_1$, $b_2$, $b_3$ are components of $\mathbf{b}$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}\times\mathbf{b}
&=
(a_2b_3-a_3b_2)\mathbf{i}
+(a_3b_1-a_1b_3)\mathbf{j}
+(a_1b_2-a_2b_1)\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Form the cross product</div>
</div>

</div>

where

- $\mathbf{a}\times\mathbf{b}$ is the cross product.
- Each coefficient is a Cartesian component.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla
&=
\mathbf{i}\dfrac{\partial}{\partial x}
+\mathbf{j}\dfrac{\partial}{\partial y}
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
\nabla
\\
\mathbf{b}
&=
\mathbf{F}
\end{align*}
$$

</div>
<div class="derivation-just">Identify the cross-product factors with nabla and the field</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla\times\mathbf{F}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
+\biggl(\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}\biggr)\mathbf{j}
+\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Apply the cross-product rule</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{curl}\mathbf{F}
&=
\nabla\times\mathbf{F}
\end{align*}
$$

</div>
<div class="derivation-just">Compare with the component form</div>
</div>

</div>

where

- $\nabla$ supplies the differential operators.
- $\mathbf{F}$ supplies the field components.
- $\times$ applies the cross-product rule.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}\times\mathbf{b}
&=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Write the cross product as a determinant</div>
</div>

</div>

where

- The first row contains Cartesian unit vectors.
- The second row contains $\mathbf{a}$ components.
- The third row contains $\mathbf{b}$ components.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla\times\mathbf{F}
&=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Replace the two vectors by nabla and the field</div>
</div>

</div>

where

- The first row contains Cartesian unit vectors.
- The second row contains differential operators.
- The third row contains field components.
- The determinant is symbolic.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla\times\mathbf{F}
&=
\mathbf{i}
\begin{vmatrix}
\dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
F_y & F_z
\end{vmatrix}
-
\mathbf{j}
\begin{vmatrix}
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial z} \\
F_x & F_z
\end{vmatrix}
+
\mathbf{k}
\begin{vmatrix}
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} \\
F_x & F_y
\end{vmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Expand the determinant</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla\times\mathbf{F}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
-
\biggl(\dfrac{\partial F_z}{\partial x}-\dfrac{\partial F_x}{\partial z}\biggr)\mathbf{j}
+
\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Evaluate the minors</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla\times\mathbf{F}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
+
\biggl(\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}\biggr)\mathbf{j}
+
\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Rearrange the y-component</div>
</div>

</div>

Hence,

$\displaystyle \operatorname{curl} \mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ F_{x} & F_{y} & F_{z} \end{vmatrix}$

![A rectangular loop in the $yz$-plane with corners $(0,y,z)$, $(0,y+\Delta y,z)$, $(0,y+\Delta y,z+\Delta z)$, and $(0,y,z+\Delta z)$. The path is traversed counterclockwise as seen from the positive $x$-axis.](3d-coordinate-loop-diagram.png){#fig:3d-coordinate-loop-diagram}

## References

1. MacCullagh, J. *An Essay towards a Dynamical Theory of Crystalline Reflexion and Refraction*. Transactions of the Royal Irish Academy, Vol. XXI. Read 9 December 1839; published 1846.

2. Lunney, J. G. *James MacCullagh*. Trinity College Dublin, 2015.

3. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011.

4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*.
