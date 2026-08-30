# Jacobian Example

<!-- pdf-page-width: wide -->

$$
\begin{align*}
\mathbf{w}_1
&=
\begin{pmatrix}
2\\
1
\end{pmatrix}
\tag*{\just{Consider a parallelogram with side vectors}}
\\[0.45em]
\mathbf{w}_2
&=
\begin{pmatrix}
-1\\
1
\end{pmatrix}
\tag*{\just{and}}
\\[0.45em]
\mathbf{b}
&=
\begin{pmatrix}
1\\
1
\end{pmatrix}
\tag*{\just{Let its starting point be}}
\\[0.45em]
\begin{pmatrix}
x\\
y
\end{pmatrix}
&=
u\mathbf{w}_1
+
v\mathbf{w}_2
+
\mathbf{b}
\tag*{\just{Every point in the parallelogram is}}
\\[0.45em]
x
&=
2u-v+1
\tag*{\just{Therefore,}}
\\[0.45em]
y
&=
u+v+1
\tag*{\just{and}}
\\[0.45em]
0
&\leq
u
\leq
1,
\qquad
0
\leq
v
\leq
1
\tag*{\just{For}}
\end{align*}
$$

the unit square in the $(u,v)$ coordinate system maps to the parallelogram in the $(x,y)$ coordinate system.

The vertices are

| $(u,v)$ | $(x,y)$ |
|---|---|
| $(0,0)$ | $(1,1)$ |
| $(0,1)$ | $(0,2)$ |
| $(1,0)$ | $(3,2)$ |
| $(1,1)$ | $(2,3)$ |

$$
\begin{align*}
J
&=
\begin{pmatrix}
2 & -1\\
1 & 1
\end{pmatrix}
\tag*{\just{The Jacobian is}}
\\[0.45em]
\det J
&=
(2)(1)-(-1)(1)
=
3
\tag*{\just{Therefore,}}
\\[0.45em]
A
&=
\iint_P1\,dx\,dy
\tag*{\just{The area of the parallelogram is}}
\\[0.45em]
A
&=
\int_0^1
\int_0^1
3\,du\,dv
\tag*{\just{Changing variables,}}
\\[0.45em]
A
&=
3
\tag*{\just{Thus,}}
\end{align*}
$$

\defaultwidthpar{This demonstrates why the Jacobian determinant appears in a change of variables: it measures how an area element changes under the transformation.}
