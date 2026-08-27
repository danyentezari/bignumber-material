# Derivation of Jacobian

$$
J_{\mathbf F}
=
\frac{\partial(F_1,\ldots,F_m)}
{\partial(x_1,\ldots,x_n)}
=
\begin{pmatrix}
\dfrac{\partial F_1}{\partial x_1} & \cdots & \dfrac{\partial F_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\dfrac{\partial F_m}{\partial x_1} & \cdots & \dfrac{\partial F_m}{\partial x_n}
\end{pmatrix}
$$

Vector Function. Let

$$
\mathbf F
=
\begin{pmatrix}
F_1 \\
F_2 \\
\vdots \\
F_m
\end{pmatrix}
$$

depend on

$$
\mathbf x
=
\begin{pmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{pmatrix}.
$$

where

- $\mathbf F$ is a vector-valued function.
- $F_i$ is an output component.
- $\mathbf x$ is the input vector.
- $x_j$ is an input coordinate.
- $m$ is the number of outputs.
- $n$ is the number of inputs.

Small Input Change. Change the input by

$$
\Delta\mathbf x
=
\begin{pmatrix}
\Delta x_1 \\
\Delta x_2 \\
\vdots \\
\Delta x_n
\end{pmatrix}.
$$

The corresponding output change is

$$
\Delta\mathbf F
=
\mathbf F(\mathbf x+\Delta\mathbf x)
-
\mathbf F(\mathbf x).
$$

where

- $\Delta\mathbf x$ is the input change.
- $\Delta\mathbf F$ is the output change.

Component Change. Each output component changes according to

$$
\Delta F_i
=
F_i(\mathbf x+\Delta\mathbf x)
-
F_i(\mathbf x).
$$

For a differentiable function, the first-order Taylor expansion gives

$$
\begin{aligned}
\Delta F_i
&=
F_i(\mathbf{x}+\Delta\mathbf{x})-F_i(\mathbf{x})
\\
&=
F_i(x_1+\Delta x_1,\ldots,x_n+\Delta x_n)
-
F_i(x_1,\ldots,x_n)
\\
&\approx
\sum_{j=1}^{n}
\frac{\partial F_i}{\partial x_j}\Delta x_j
\\
&=
\frac{\partial F_i}{\partial x_1}\Delta x_1
+
\frac{\partial F_i}{\partial x_2}\Delta x_2
+
\cdots
+
\frac{\partial F_i}{\partial x_n}\Delta x_n.
\end{aligned}
$$


where

- $\Delta F_i$ is one output change.
- $\partial F_i/\partial x_j$ measures coordinate sensitivity.
- Higher-order terms vanish faster than $\Delta\mathbf x$.

Writing this for every output gives

$$
\Delta F_1
\approx
\frac{\partial F_1}{\partial x_1}\Delta x_1
+
\cdots
+
\frac{\partial F_1}{\partial x_n}\Delta x_n,
$$

$$
\Delta F_2
\approx
\frac{\partial F_2}{\partial x_1}\Delta x_1
+
\cdots
+
\frac{\partial F_2}{\partial x_n}\Delta x_n,
$$

$$
\vdots
$$

$$
\Delta F_m
\approx
\frac{\partial F_m}{\partial x_1}\Delta x_1
+
\cdots
+
\frac{\partial F_m}{\partial x_n}\Delta x_n.
$$

Matrix Form. These equations combine into

$$
\begin{pmatrix}
\Delta F_1 \\
\Delta F_2 \\
\vdots \\
\Delta F_m
\end{pmatrix}
\approx
\begin{pmatrix}
\dfrac{\partial F_1}{\partial x_1}
&
\dfrac{\partial F_1}{\partial x_2}
&
\cdots
&
\dfrac{\partial F_1}{\partial x_n}
\\
\dfrac{\partial F_2}{\partial x_1}
&
\dfrac{\partial F_2}{\partial x_2}
&
\cdots
&
\dfrac{\partial F_2}{\partial x_n}
\\
\vdots
&
\vdots
&
\ddots
&
\vdots
\\
\dfrac{\partial F_m}{\partial x_1}
&
\dfrac{\partial F_m}{\partial x_2}
&
\cdots
&
\dfrac{\partial F_m}{\partial x_n}
\end{pmatrix}
\begin{pmatrix}
\Delta x_1 \\
\Delta x_2 \\
\vdots \\
\Delta x_n
\end{pmatrix}.
$$

The matrix multiplying $\Delta\mathbf x$ is the Jacobian matrix:

$$
J_{\mathbf F}
=
\begin{pmatrix}
\dfrac{\partial F_1}{\partial x_1}
&
\dfrac{\partial F_1}{\partial x_2}
&
\cdots
&
\dfrac{\partial F_1}{\partial x_n}
\\
\dfrac{\partial F_2}{\partial x_1}
&
\dfrac{\partial F_2}{\partial x_2}
&
\cdots
&
\dfrac{\partial F_2}{\partial x_n}
\\
\vdots
&
\vdots
&
\ddots
&
\vdots
\\
\dfrac{\partial F_m}{\partial x_1}
&
\dfrac{\partial F_m}{\partial x_2}
&
\cdots
&
\dfrac{\partial F_m}{\partial x_n}
\end{pmatrix}.
$$

where

- $J_{\mathbf F}$ is the Jacobian matrix.
- Rows correspond to output components.
- Columns correspond to input coordinates.
- Each entry is a partial derivative.

Therefore,

$$
\Delta\mathbf F
\approx
J_{\mathbf F}\Delta\mathbf x.
$$

The Jacobian is the linear transformation that gives the first-order change in $\mathbf F$ from a small change in $\mathbf x$.

Two Dimensions. Let

$$
\mathbf F(x,y)
=
\begin{pmatrix}
F_x(x,y) \\
F_y(x,y)
\end{pmatrix}.
$$

A small displacement is

$$
\Delta\mathbf x
=
\begin{pmatrix}
\Delta x \\
\Delta y
\end{pmatrix}.
$$

The component changes are

$$
\Delta F_x
\approx
\frac{\partial F_x}{\partial x}\Delta x
+
\frac{\partial F_x}{\partial y}\Delta y
$$

and

$$
\Delta F_y
\approx
\frac{\partial F_y}{\partial x}\Delta x
+
\frac{\partial F_y}{\partial y}\Delta y.
$$

Thus,

$$
\begin{pmatrix}
\Delta F_x \\
\Delta F_y
\end{pmatrix}
\approx
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x}
&
\dfrac{\partial F_x}{\partial y}
\\
\dfrac{\partial F_y}{\partial x}
&
\dfrac{\partial F_y}{\partial y}
\end{pmatrix}
\begin{pmatrix}
\Delta x \\
\Delta y
\end{pmatrix}.
$$

Hence,

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

Jacobian Determinant. When the input and output dimensions are equal, the Jacobian matrix has a determinant.

For two dimensions,

$$
\det J_{\mathbf F}
=
\begin{vmatrix}
\dfrac{\partial F_x}{\partial x}
&
\dfrac{\partial F_x}{\partial y}
\\
\dfrac{\partial F_y}{\partial x}
&
\dfrac{\partial F_y}{\partial y}
\end{vmatrix}.
$$

Expanding gives

$$
\det J_{\mathbf F}
=
\frac{\partial F_x}{\partial x}
\frac{\partial F_y}{\partial y}
-
\frac{\partial F_x}{\partial y}
\frac{\partial F_y}{\partial x}.
$$

where

- $\det J_{\mathbf F}$ is the Jacobian determinant.
- Its magnitude gives local area scaling.
- Its sign gives orientation change.

Area Scaling. Consider the coordinate displacements

$$
d\mathbf x_1
=
\begin{pmatrix}
dx \\
0
\end{pmatrix},
\qquad
d\mathbf x_2
=
\begin{pmatrix}
0 \\
dy
\end{pmatrix}.
$$

Their original area is

$$
dA
=
dx\,dy.
$$

The Jacobian maps these displacements to

$$
d\mathbf F_1
=
J_{\mathbf F}d\mathbf x_1
$$

and

$$
d\mathbf F_2
=
J_{\mathbf F}d\mathbf x_2.
$$

Therefore,

$$
d\mathbf F_1
=
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x}dx \\
\dfrac{\partial F_y}{\partial x}dx
\end{pmatrix},
$$

$$
d\mathbf F_2
=
\begin{pmatrix}
\dfrac{\partial F_x}{\partial y}dy \\
\dfrac{\partial F_y}{\partial y}dy
\end{pmatrix}.
$$

These vectors form a parallelogram. Its signed area is

$$
dA'
=
\begin{vmatrix}
\dfrac{\partial F_x}{\partial x}dx
&
\dfrac{\partial F_x}{\partial y}dy
\\
\dfrac{\partial F_y}{\partial x}dx
&
\dfrac{\partial F_y}{\partial y}dy
\end{vmatrix}.
$$

Factoring out $dx\,dy$ gives

$$
dA'
=
\begin{vmatrix}
\dfrac{\partial F_x}{\partial x}
&
\dfrac{\partial F_x}{\partial y}
\\
\dfrac{\partial F_y}{\partial x}
&
\dfrac{\partial F_y}{\partial y}
\end{vmatrix}
dx\,dy.
$$

Therefore,

$$
dA'
=
\det(J_{\mathbf F})\,dA.
$$

Thus, the Jacobian matrix gives the first-order transformation, while its determinant gives the corresponding area or volume scaling.

Hence,

$$
J_{\mathbf F}
=
\frac{\partial(F_1,\ldots,F_m)}
{\partial(x_1,\ldots,x_n)}
=
\begin{pmatrix}
\dfrac{\partial F_1}{\partial x_1} & \cdots & \dfrac{\partial F_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\dfrac{\partial F_m}{\partial x_1} & \cdots & \dfrac{\partial F_m}{\partial x_n}
\end{pmatrix}
$$

## References

1. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. Prentice Hall, 1998, §1.7, pp. 107–112.

2. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*, 3rd ed. Cambridge University Press, 2006, §5.7, pp. 160–161.

3. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*, 3rd ed. Cambridge University Press, 2006, §6.4, pp. 199–206.