# Basic Derivation of Jacobian

Example. Let

$$
\mathbf F(x,y)
=
\begin{pmatrix}
x^2+3y \\
2x-y^2
\end{pmatrix}.
$$

where

- $F_x=x^2+3y$ is the first component.
- $F_y=2x-y^2$ is the second component.
- $x$ and $y$ are input coordinates.

The Jacobian is

$$
J_{\mathbf F}
=
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x}
&
\dfrac{\partial F_x}{\partial y}
\\
\dfrac{\partial F_y}{\partial x}
&
\dfrac{\partial F_y}{\partial y}
\end{pmatrix}.
$$

Calculate each partial derivative:

$$
\frac{\partial F_x}{\partial x}
=
2x,
$$

$$
\frac{\partial F_x}{\partial y}
=
3,
$$

$$
\frac{\partial F_y}{\partial x}
=
2,
$$

$$
\frac{\partial F_y}{\partial y}
=
-2y.
$$

Therefore,

$$
J_{\mathbf F}(x,y)
=
\begin{pmatrix}
2x & 3 \\
2 & -2y
\end{pmatrix}.
$$

Evaluation. Choose the point

$$
(x,y)=(1,2).
$$

Substituting these values gives

$$
J_{\mathbf F}(1,2)
=
\begin{pmatrix}
2 & 3 \\
2 & -4
\end{pmatrix}.
$$

This matrix gives the first-order change in $\mathbf F$ near $(1,2)$.

Choose a small input change

$$
\Delta\mathbf x
=
\begin{pmatrix}
0.1 \\
0.05
\end{pmatrix}.
$$

Then

$$
\Delta\mathbf F
\approx
J_{\mathbf F}(1,2)\Delta\mathbf x.
$$

Substituting the values,

$$
\Delta\mathbf F
\approx
\begin{pmatrix}
2 & 3 \\
2 & -4
\end{pmatrix}
\begin{pmatrix}
0.1 \\
0.05
\end{pmatrix}.
$$

Multiplying gives

$$
\Delta\mathbf F
\approx
\begin{pmatrix}
2(0.1)+3(0.05) \\
2(0.1)-4(0.05)
\end{pmatrix}
=
\begin{pmatrix}
0.35 \\
0
\end{pmatrix}.
$$

Thus, the input change

$$
\begin{pmatrix}
0.1 \\
0.05
\end{pmatrix}
$$

produces approximately the output change

$$
\begin{pmatrix}
0.35 \\
0
\end{pmatrix}.
$$

Exact Change. At the original point,

$$
\mathbf F(1,2)
=
\begin{pmatrix}
7 \\
-2
\end{pmatrix}.
$$

At the displaced point,

$$
\mathbf F(1.1,2.05)
=
\begin{pmatrix}
7.36 \\
-2.0025
\end{pmatrix}.
$$

Therefore, the exact change is

$$
\Delta\mathbf F
=
\begin{pmatrix}
0.36 \\
-0.0025
\end{pmatrix}.
$$

The Jacobian approximation was

$$
\Delta\mathbf F
\approx
\begin{pmatrix}
0.35 \\
0
\end{pmatrix}.
$$

The difference comes from the higher-order terms omitted by the linear approximation.

Jacobian Determinant. At $(1,2)$,

$$
\det J_{\mathbf F}
=
\begin{vmatrix}
2 & 3 \\
2 & -4
\end{vmatrix}.
$$

Therefore,

$$
\det J_{\mathbf F}
=
2(-4)-3(2)
=
-14.
$$

Hence,

$$
|\det J_{\mathbf F}|=14.
$$

A sufficiently small area near $(1,2)$ is therefore scaled by approximately a factor of $14$. The negative sign shows that the transformation reverses orientation.