<!-- skip: backup of Jacobian.md; ignored by PDF/HTML builds -->
<!-- source: working-tree -->

# Jacobian

<!-- pdf-page-width: wide -->

Let

$$
x=x(u,v),
\qquad
y=y(u,v).
$$

The Jacobian matrix is

$$
J
=
\begin{pmatrix}
\dfrac{\partial x}{\partial u}
&
\dfrac{\partial x}{\partial v}
\\
\dfrac{\partial y}{\partial u}
&
\dfrac{\partial y}{\partial v}
\end{pmatrix}.
$$

Its determinant is

$$
\det J
=
\frac{\partial x}{\partial u}
\frac{\partial y}{\partial v}
-
\frac{\partial x}{\partial v}
\frac{\partial y}{\partial u}.
$$

The absolute value of the determinant gives the local area-scaling factor:

$$
dx\,dy
=
\left|
\det J
\right|
du\,dv.
$$

Therefore,

$$
\iint_R f(x,y)\,dx\,dy
=
\iint_S
f(x(u,v),y(u,v))
\left|
\det J
\right|
du\,dv.
$$

where

- $R$ is the region in the $(x,y)$ coordinate system.
- $S$ is the corresponding region in the $(u,v)$ coordinate system.
- $J$ is the Jacobian matrix of the transformation.
