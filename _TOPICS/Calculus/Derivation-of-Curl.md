# Derivation of Curl

Curl is obtained from circulation per unit area around a vanishing rectangular loop.

For a vector field $\mathbf{F}$,

$$
\begin{aligned}
(\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}
&=
\lim_{A\to 0}
\dfrac{1}{A}
\oint_{C}\mathbf{F}\cdot d\mathbf{s}.
\end{aligned}
$$

where

- $\nabla$ is the vector differential operator.
- $\mathbf{F}$ is a vector field.
- $\hat{\mathbf{n}}$ is the unit normal.
- $A$ is the enclosed area.
- $C$ is the closed curve.
- $d\mathbf{s}$ is the displacement along $C$.

Rectangular Loop. Consider a rectangle in the $xy$-plane with normal $\mathbf{k}$ and sides $\Delta x$ and $\Delta y$.

$$
\begin{aligned}
\int_{a}^{b}\mathbf{F}\cdot d\mathbf{s}
&\simeq
\left(
F_{x}-\dfrac{\Delta y}{2}\dfrac{\partial F_{x}}{\partial y}
\right)\Delta x \\[4pt]
\int_{b}^{c}\mathbf{F}\cdot d\mathbf{s}
&\simeq
\left(
F_{y}+\dfrac{\Delta x}{2}\dfrac{\partial F_{y}}{\partial x}
\right)\Delta y \\[4pt]
\int_{c}^{d}\mathbf{F}\cdot d\mathbf{s}
&\simeq
-\left(
F_{x}+\dfrac{\Delta y}{2}\dfrac{\partial F_{x}}{\partial y}
\right)\Delta x \\[4pt]
\int_{d}^{a}\mathbf{F}\cdot d\mathbf{s}
&\simeq
-\left(
F_{y}-\dfrac{\Delta x}{2}\dfrac{\partial F_{y}}{\partial x}
\right)\Delta y.
\end{aligned}
$$

where

- $F_{x}$, $F_{y}$, $F_{z}$ are the Cartesian components of $\mathbf{F}$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\Delta x$ and $\Delta y$ are the side lengths.
- $a$, $b$, $c$, $d$ are the vertices of the rectangle.

First-Order Taylor Expansion. For the right side of the rectangle,

$$
\begin{aligned}
F_{y}(x+h,y,z)
&\simeq
F_{y}(x,y,z)
+
h\dfrac{\partial F_{y}}{\partial x} \\[4pt]
h
&=
\dfrac{\Delta x}{2} \\[4pt]
F_{y}\left(x+\dfrac{\Delta x}{2},y,z\right)
&\simeq
F_{y}(x,y,z)
+
\dfrac{\Delta x}{2}
\dfrac{\partial F_{y}}{\partial x} \\[4pt]
&=
F_{y}
+
\dfrac{\Delta x}{2}
\dfrac{\partial F_{y}}{\partial x}.
\end{aligned}
$$

Similarly, the other three sides give the expressions above.

Circulation. Summing the four sides,

$$
\begin{aligned}
\oint_{abcd}\mathbf{F}\cdot d\mathbf{s}
&\simeq
\left(
\dfrac{\partial F_{y}}{\partial x}
-
\dfrac{\partial F_{x}}{\partial y}
\right)
\Delta x\,\Delta y.
\end{aligned}
$$

Since

$$
A=\Delta x\,\Delta y,
$$

divide by the area and take the vanishing limit:

$$
\begin{aligned}
(\nabla\times\mathbf{F})\cdot\mathbf{k}
&=
\dfrac{\partial F_{y}}{\partial x}
-
\dfrac{\partial F_{x}}{\partial y}.
\end{aligned}
$$

where $\mathbf{k}$ is the Cartesian unit vector along $z$.

Cyclic Permutation. Cycling the coordinates gives

$$
\begin{aligned}
(\nabla\times\mathbf{F})\cdot\mathbf{i}
&=
\dfrac{\partial F_{z}}{\partial y}
-
\dfrac{\partial F_{y}}{\partial z} \\[4pt]
(\nabla\times\mathbf{F})\cdot\mathbf{j}
&=
\dfrac{\partial F_{x}}{\partial z}
-
\dfrac{\partial F_{z}}{\partial x} \\[4pt]
(\nabla\times\mathbf{F})\cdot\mathbf{k}
&=
\dfrac{\partial F_{y}}{\partial x}
-
\dfrac{\partial F_{x}}{\partial y}.
\end{aligned}
$$

where $\mathbf{i}$, $\mathbf{j}$, and $\mathbf{k}$ are the Cartesian unit vectors along $x$, $y$, and $z$.

Therefore,

$$
\begin{aligned}
\nabla\times\mathbf{F}
&=
\left(
\dfrac{\partial F_{z}}{\partial y}
-
\dfrac{\partial F_{y}}{\partial z}
\right)\mathbf{i}
+
\left(
\dfrac{\partial F_{x}}{\partial z}
-
\dfrac{\partial F_{z}}{\partial x}
\right)\mathbf{j}
+
\left(
\dfrac{\partial F_{y}}{\partial x}
-
\dfrac{\partial F_{x}}{\partial y}
\right)\mathbf{k}.
\end{aligned}
$$

Determinant Form. The ordinary cross product expands as

$$
\begin{aligned}
\mathbf{a}\times\mathbf{b}
&=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_{1} & a_{2} & a_{3} \\
b_{1} & b_{2} & b_{3}
\end{vmatrix} \\[4pt]
&=
(a_{2}b_{3}-a_{3}b_{2})\mathbf{i}
+
(a_{3}b_{1}-a_{1}b_{3})\mathbf{j}
+
(a_{1}b_{2}-a_{2}b_{1})\mathbf{k}.
\end{aligned}
$$

Replacing the first vector by

$$
\nabla
=
\mathbf{i}\dfrac{\partial}{\partial x}
+
\mathbf{j}\dfrac{\partial}{\partial y}
+
\mathbf{k}\dfrac{\partial}{\partial z},
$$

gives

$$
\begin{aligned}
\operatorname{curl}\mathbf{F}
&=
\nabla\times\mathbf{F} \\[4pt]
&=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\dfrac{\partial}{\partial x}
&
\dfrac{\partial}{\partial y}
&
\dfrac{\partial}{\partial z} \\
F_{x} & F_{y} & F_{z}
\end{vmatrix}.
\end{aligned}
$$

The differential operators in the second row act on the components in the third row.

Curl is also written $\operatorname{rot}\mathbf{F}$. The determinant above is a symbolic determinant.

![A closed curve $C$ bounding an area $A$. The unit normal $\hat{\mathbf{n}}$ stands perpendicular to $A$. At a point of $C$ the field $\mathbf{F}$ and the displacement $d\mathbf{s}$ are shown.](closed-curve-vector-field.png){#fig:closed-curve-vector-field}

![Decomposition of $\mathbf{F}$ at a point of $C$ into a part parallel to $d\mathbf{s}$ and a part perpendicular to $d\mathbf{s}$. The included angle is $\theta$.](vector-decomposition-along-curved-path.png){#fig:vector-decomposition-along-curved-path}

## References

1. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — curl as circulation per unit area; symbolic determinant $\nabla\times\mathbf{F}$; Cartesian expansion.
2. Boas, M. L. *Mathematical Methods in the Physical Sciences*. — normal component of curl as the limit of circulation per unit area.
3. Feynman, R. P., Leighton, R. B., & Sands, M. *The Feynman Lectures on Physics*, Vol. II. — circulation around a square of sides $\Delta x$ and $\Delta y$ in the $xy$-plane; identification with $(\nabla\times\mathbf{C})\cdot\hat{\mathbf{n}}\,\Delta a$.
4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. — determinantal form; the partial derivatives in the second row act on the components in the third row.
