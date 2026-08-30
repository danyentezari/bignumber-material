# Derivation of Curl

$\displaystyle \operatorname{curl} \mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ F_{x} & F_{y} & F_{z} \end{vmatrix}$

$$
\begin{align*}
\mathbf{F}
&=
F_x\mathbf{i}+F_y\mathbf{j}+F_z\mathbf{k}
&&
\qquad\just{Write the vector field}
\\[0.6em]
X
&=
\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}
&&
\qquad\just{Define the x differential component}
\\[0.6em]
Y
&=
\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}
&&
\qquad\just{Define the y differential component}
\\[0.6em]
Z
&=
\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}
&&
\qquad\just{Define the z differential component}
\\[0.6em]
\mathbf{R}
&=
X\mathbf{i}+Y\mathbf{j}+Z\mathbf{k}
&&
\qquad\just{Assemble the Cartesian vector}
\\[0.6em]
\mathbf{R}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
&&
\qquad\just{Substitute the differential components}
\\
&\quad
+\biggl(\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}\biggr)\mathbf{j}
\\
&\quad
+\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\\[0.6em]
\operatorname{curl}\mathbf{F}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
&&
\qquad\just{Name this vector the curl of F}
\\
&\quad
+\biggl(\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}\biggr)\mathbf{j}
\\
&\quad
+\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\\[0.6em]
(\operatorname{curl}\mathbf{F})_x
&=
\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}
&&
\qquad\just{Read the x-component}
\\[0.6em]
(\operatorname{curl}\mathbf{F})_y
&=
\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}
&&
\qquad\just{Read the y-component}
\\[0.6em]
(\operatorname{curl}\mathbf{F})_z
&=
\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}
&&
\qquad\just{Read the z-component}
\\[0.6em]
\mathbf{a}
&=
a_1\mathbf{i}+a_2\mathbf{j}+a_3\mathbf{k}
&&
\qquad\just{Take a general first vector}
\\[0.6em]
\mathbf{b}
&=
b_1\mathbf{i}+b_2\mathbf{j}+b_3\mathbf{k}
&&
\qquad\just{Take a general second vector}
\\[0.6em]
\mathbf{a}\times\mathbf{b}
&=
(a_2b_3-a_3b_2)\mathbf{i}
&&
\qquad\just{Form the cross product}
\\
&\quad
+(a_3b_1-a_1b_3)\mathbf{j}
\\
&\quad
+(a_1b_2-a_2b_1)\mathbf{k}
\\[0.6em]
\nabla
&=
\mathbf{i}\dfrac{\partial}{\partial x}
+\mathbf{j}\dfrac{\partial}{\partial y}
+\mathbf{k}\dfrac{\partial}{\partial z}
&&
\qquad\just{Define the vector differential operator}
\\[0.6em]
\mathbf{a}
&=
\nabla
&&
\qquad\just{Set the first factor to nabla}
\\[0.6em]
\mathbf{b}
&=
\mathbf{F}
&&
\qquad\just{Set the second factor to F}
\\[0.6em]
\nabla\times\mathbf{F}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
&&
\qquad\just{Apply the cross-product rule}
\\
&\quad
+\biggl(\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}\biggr)\mathbf{j}
\\
&\quad
+\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\\[0.6em]
\operatorname{curl}\mathbf{F}
&=
\nabla\times\mathbf{F}
&&
\qquad\just{Compare with the component form}
\end{align*}
$$

$$
\begin{align*}
\mathbf{a}\times\mathbf{b}
&=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
&&
\qquad\just{Write the cross product as a determinant}
\\[0.6em]
\nabla\times\mathbf{F}
&=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix}
&&
\qquad\just{Replace a by nabla and b by F}
\\[0.6em]
\nabla\times\mathbf{F}
&=
\mathbf{i}
\begin{vmatrix}
\dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
F_y & F_z
\end{vmatrix}
&&
\qquad\just{Expand the determinant}
\\
&\quad
-
\mathbf{j}
\begin{vmatrix}
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial z} \\
F_x & F_z
\end{vmatrix}
\\
&\quad
+
\mathbf{k}
\begin{vmatrix}
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} \\
F_x & F_y
\end{vmatrix}
\\[0.6em]
\nabla\times\mathbf{F}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
&&
\qquad\just{Evaluate the minors}
\\
&\quad
-
\biggl(\dfrac{\partial F_z}{\partial x}-\dfrac{\partial F_x}{\partial z}\biggr)\mathbf{j}
\\
&\quad
+
\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\\[0.6em]
\nabla\times\mathbf{F}
&=
\biggl(\dfrac{\partial F_z}{\partial y}-\dfrac{\partial F_y}{\partial z}\biggr)\mathbf{i}
&&
\qquad\just{Rearrange the y-component}
\\
&\quad
+
\biggl(\dfrac{\partial F_x}{\partial z}-\dfrac{\partial F_z}{\partial x}\biggr)\mathbf{j}
\\
&\quad
+
\biggl(\dfrac{\partial F_y}{\partial x}-\dfrac{\partial F_x}{\partial y}\biggr)\mathbf{k}
\end{align*}
$$

Hence,

$\displaystyle \operatorname{curl} \mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ F_{x} & F_{y} & F_{z} \end{vmatrix}$

![A rectangular loop in the $yz$-plane with corners $(0,y,z)$, $(0,y+\Delta y,z)$, $(0,y+\Delta y,z+\Delta z)$, and $(0,y,z+\Delta z)$. The path is traversed counterclockwise as seen from the positive $x$-axis.](3d-coordinate-loop-diagram.png){#fig:3d-coordinate-loop-diagram}

## References

1. MacCullagh, J. *An Essay towards a Dynamical Theory of Crystalline Reflexion and Refraction*. Transactions of the Royal Irish Academy, Vol. XXI. Read 9 December 1839; published 1846.

2. Lunney, J. G. *James MacCullagh*. Trinity College Dublin, 2015.

3. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011.

4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*.
