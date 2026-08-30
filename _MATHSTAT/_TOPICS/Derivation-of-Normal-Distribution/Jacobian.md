# Jacobian

<!-- pdf-page-width: wide -->

$$
\begin{align*}
x
&=
x(u,v),
\qquad
y
=
y(u,v)
\tag*{\just{Let}}
\\[0.45em]
J
&=
\begin{pmatrix}
\dfrac{\partial x}{\partial u}
&
\dfrac{\partial x}{\partial v}
\\
\dfrac{\partial y}{\partial u}
&
\dfrac{\partial y}{\partial v}
\end{pmatrix}
\tag*{\just{The Jacobian matrix is}}
\\[0.45em]
\det J
&=
\frac{\partial x}{\partial u}
\frac{\partial y}{\partial v}
-
\frac{\partial x}{\partial v}
\frac{\partial y}{\partial u}
\tag*{\just{Its determinant is}}
\\[0.45em]
dx\,dy
&=
\left|
\det J
\right|
du\,dv
\tag*{\just{The absolute value of the determinant gives the local area-scaling factor:}}
\\[0.45em]
\iint_R f(x,y)\,dx\,dy
&=
\iint_S
f(x(u,v),y(u,v))
\left|
\det J
\right|
du\,dv
\tag*{\just{Therefore,}}
\end{align*}
$$

where

- $R$ is the region in the $(x,y)$ coordinate system.
- $S$ is the corresponding region in the $(u,v)$ coordinate system.
- $J$ is the Jacobian matrix of the transformation.
