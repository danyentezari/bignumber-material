# Jacobian Example

Consider a parallelogram with side vectors

$$
\mathbf{w}_1
=
\begin{pmatrix}
2\\
1
\end{pmatrix}
$$

and

$$
\mathbf{w}_2
=
\begin{pmatrix}
-1\\
1
\end{pmatrix}.
$$

Let its starting point be

$$
\mathbf{b}
=
\begin{pmatrix}
1\\
1
\end{pmatrix}.
$$

Every point in the parallelogram is

$$
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
u\mathbf{w}_1
+
v\mathbf{w}_2
+
\mathbf{b}.
$$

Therefore,

$$
x
=
2u-v+1
$$

and

$$
y
=
u+v+1.
$$

For

$$
0\leq u\leq1,
\qquad
0\leq v\leq1,
$$

the unit square in the $(u,v)$ coordinate system maps to the parallelogram in the $(x,y)$ coordinate system.

The vertices are

| $(u,v)$ | $(x,y)$ |
|---|---|
| $(0,0)$ | $(1,1)$ |
| $(0,1)$ | $(0,2)$ |
| $(1,0)$ | $(3,2)$ |
| $(1,1)$ | $(2,3)$ |

The Jacobian is

$$
J
=
\begin{pmatrix}
2 & -1\\
1 & 1
\end{pmatrix}.
$$

Therefore,

$$
\det J
=
(2)(1)-(-1)(1)
=
3.
$$

The area of the parallelogram is

$$
A
=
\iint_P1\,dx\,dy.
$$

Changing variables,

$$
A
=
\int_0^1
\int_0^1
3\,du\,dv.
$$

Thus,

$$
A
=
3.
$$

This demonstrates why the Jacobian determinant appears in a change of variables: it measures how an area element changes under the transformation.
