# Jacobian

<!-- pdf-page-width: wide -->

Let

$$
\begin{align*}
x
&=
x(u,v)
\\
y
&=
y(u,v)
\tag*{\just{Define a transformation from $(u,v)$ to $(x,y)$}}
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
\tag*{\just{Form the Jacobian matrix}}
\\[0.45em]
\det J
&=
\frac{\partial x}{\partial u}
\frac{\partial y}{\partial v}
-
\frac{\partial x}{\partial v}
\frac{\partial y}{\partial u}
\tag*{\just{Take its determinant}}
\\[0.45em]
dx\,dy
&=
\left|
\det J
\right|
du\,dv
\tag*{\just{The determinant gives the local area-scaling factor}}
\\[0.45em]
\iint_R
f(x,y)\,dx\,dy
&=
\iint_S
f(x(u,v),y(u,v))
\left|
\det J
\right|
du\,dv
\tag*{\just{Apply the change-of-variables formula}}
\end{align*}
$$

\defaultwidthpar{

where

- $R$ is the region in the $(x,y)$ coordinate system.
- $S$ is the corresponding region in the $(u,v)$ coordinate system.
- $J$ is the Jacobian matrix of the transformation.

}
