# Derivation of Curl

A derivation that is used to obtain the Cartesian determinant form of curl from circulation around a vanishing rectangle, where a circulation is the line integral of a field around a closed curve, and where a vanishing rectangle is a rectangular loop whose enclosed area tends to zero.

Circulation per unit area. The component of curl along a unit normal is the limit of circulation per unit area. A unit normal is a vector of length one perpendicular to the enclosed area.

The circulation definition is

$$
(\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}
=
\lim_{A\to 0}
\dfrac{1}{A}
\oint_{C}\mathbf{F}\cdot d\mathbf{s}
$$

where

- $\nabla$ is the vector differential operator.
- $\mathbf{F}$ is a vector field.
- $\hat{\mathbf{n}}$ is the unit normal.
- $A$ is the enclosed area.
- $C$ is the closed curve.
- $d\mathbf{s}$ is the displacement along $C$.

Rectangular loop. A rectangle in the $xy$-plane with normal $\mathbf{k}$ has sides $\Delta x$ and $\Delta y$. First-order Taylor expansions give the four side integrals.

The side contributions are

$$
\int_{a}^{b}\mathbf{F}\cdot d\mathbf{s}
\simeq
\left(F_{x}-\dfrac{\Delta y}{2}\dfrac{\partial F_{x}}{\partial y}\right)\Delta x
$$

$$
\int_{b}^{c}\mathbf{F}\cdot d\mathbf{s}
\simeq
\left(F_{y}+\dfrac{\Delta x}{2}\dfrac{\partial F_{y}}{\partial x}\right)\Delta y
$$

$$
\int_{c}^{d}\mathbf{F}\cdot d\mathbf{s}
\simeq
-\left(F_{x}+\dfrac{\Delta y}{2}\dfrac{\partial F_{x}}{\partial y}\right)\Delta x
$$

$$
\int_{d}^{a}\mathbf{F}\cdot d\mathbf{s}
\simeq
-\left(F_{y}-\dfrac{\Delta x}{2}\dfrac{\partial F_{y}}{\partial x}\right)\Delta y
$$

where

- $F_{x}$, $F_{y}$, $F_{z}$ are the Cartesian components of $\mathbf{F}$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\Delta x$ and $\Delta y$ are the side lengths.
- $a$, $b$, $c$, $d$ are the vertices of the rectangle.

The circulation around the rectangle is

$$
\oint_{abcd}\mathbf{F}\cdot d\mathbf{s}
\simeq
\left(\dfrac{\partial F_{y}}{\partial x}-\dfrac{\partial F_{x}}{\partial y}\right)\Delta x\,\Delta y
$$

$z$-component. Dividing by the enclosed area and taking the vanishing limit gives the third Cartesian component.

The $z$-component is

$$
(\nabla\times\mathbf{F})\cdot\mathbf{k}
=
\dfrac{\partial F_{y}}{\partial x}
-
\dfrac{\partial F_{x}}{\partial y}
$$

where

- $\mathbf{k}$ is the Cartesian unit vector along $z$.

Cyclic permutation. Cycling the coordinates and the components gives the remaining two Cartesian components.

The $x$-component is

$$
(\nabla\times\mathbf{F})\cdot\mathbf{i}
=
\dfrac{\partial F_{z}}{\partial y}
-
\dfrac{\partial F_{y}}{\partial z}
$$

The $y$-component is

$$
(\nabla\times\mathbf{F})\cdot\mathbf{j}
=
\dfrac{\partial F_{x}}{\partial z}
-
\dfrac{\partial F_{z}}{\partial x}
$$

where

- $\mathbf{i}$ is the Cartesian unit vector along $x$.
- $\mathbf{j}$ is the Cartesian unit vector along $y$.

Component form. The three components assemble into a single vector in the Cartesian basis.

The component form is

$$
\nabla\times\mathbf{F}
=
\left(\dfrac{\partial F_{z}}{\partial y}-\dfrac{\partial F_{y}}{\partial z}\right)\mathbf{i}
+
\left(\dfrac{\partial F_{x}}{\partial z}-\dfrac{\partial F_{z}}{\partial x}\right)\mathbf{j}
+
\left(\dfrac{\partial F_{y}}{\partial x}-\dfrac{\partial F_{x}}{\partial y}\right)\mathbf{k}
$$

Cross-product expansion. The ordinary cross product of two vectors expands by the same cofactor rule.

The cross product is

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

Symbolic determinant. Replacing the first factor by $\nabla$ yields the determinant form of curl. The operators in the second row act on the components in the third row.

The determinant form is

$$
\operatorname{curl}\mathbf{F}
=
\nabla\times\mathbf{F}
=
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
F_{x} & F_{y} & F_{z}
\end{vmatrix}
$$

Note: Also written $\operatorname{rot}\mathbf{F}$. Also called the symbolic determinant.


![A closed curve $C$ bounding an area $A$. The unit normal $\hat{\mathbf{n}}$ stands perpendicular to $A$. At a point of $C$ the field $\mathbf{F}$ and the displacement $d\mathbf{s}$ are shown.](closed-curve-vector-field.png){#fig:closed-curve-vector-field}

![Decomposition of $\mathbf{F}$ at a point of $C$ into a part parallel to $d\mathbf{s}$ and a part perpendicular to $d\mathbf{s}$. The included angle is $\theta$.](vector-decomposition-along-curved-path.png){#fig:vector-decomposition-along-curved-path}


## References

1. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — curl as circulation per unit area; symbolic determinant $\nabla\times\mathbf{F}$; Cartesian expansion.
2. Boas, M. L. *Mathematical Methods in the Physical Sciences*. — normal component of curl as the limit of circulation per unit area.
3. Feynman, R. P., Leighton, R. B., & Sands, M. *The Feynman Lectures on Physics*, Vol. II. — circulation around a square of sides $\Delta x$ and $\Delta y$ in the $xy$-plane; identification with $(\nabla\times\mathbf{C})\cdot\hat{\mathbf{n}}\,\Delta a$.
4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. — determinantal form; the partial derivatives in the second row act on the components in the third row.
