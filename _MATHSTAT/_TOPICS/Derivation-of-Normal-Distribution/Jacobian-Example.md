# Jacobian Example

<!-- pdf-page-width: wide -->

\defaultwidthpar{Consider a parallelogram with side vectors}

$$
\begin{align*}
\mathbf{w}_1
&=
\begin{pmatrix}
2\\
1
\end{pmatrix}
\\
\mathbf{w}_2
&=
\begin{pmatrix}
-1\\
1
\end{pmatrix}
\tag*{\just{Choose two side vectors}}
\\[0.45em]
\mathbf{b}
&=
\begin{pmatrix}
1\\
1
\end{pmatrix}
\tag*{\just{Choose the starting point}}
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
\tag*{\just{Parameterize every point in the parallelogram}}
\\[0.45em]
x
&=
2u-v+1
\\
y
&=
u+v+1
\tag*{\just{Expand the vector equation}}
\\[0.45em]
0
&\leq
u
\leq
1
\\
0
&\leq
v
\leq
1
\tag*{\just{The unit square maps to the parallelogram}}
\end{align*}
$$

\defaultwidthpar{

The vertices are

| $(u,v)$ | $(x,y)$ |
|---|---|
| $(0,0)$ | $(1,1)$ |
| $(0,1)$ | $(0,2)$ |
| $(1,0)$ | $(3,2)$ |
| $(1,1)$ | $(2,3)$ |

}

\defaultwidthpar{The Jacobian is}

$$
\begin{align*}
J
&=
\begin{pmatrix}
2 & -1\\
1 & 1
\end{pmatrix}
\tag*{\just{Differentiate the coordinate functions}}
\\[0.45em]
\det J
&=
(2)(1)-(-1)(1)
\\
&=
3
\tag*{\just{Compute the area-scaling factor}}
\\[0.45em]
A
&=
\iint_P
1\,dx\,dy
\tag*{\just{Express the parallelogram area as an integral}}
\\[0.45em]
&=
\int_0^1
\int_0^1
3\,du\,dv
\tag*{\just{Change variables to the unit square}}
\\[0.45em]
&=
3
\tag*{\just{Evaluate the integral}}
\end{align*}
$$

\defaultwidthpar{This demonstrates why the Jacobian determinant appears in a change of variables: it measures how an area element changes under the transformation.}
