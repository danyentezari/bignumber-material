# Polar Coordinates

<!-- pdf-page-width: wide -->

Define

$$
\begin{align*}
x
&=
r\cos\theta
\\
y
&=
r\sin\theta
\tag*{\just{Define Cartesian coordinates in terms of polar coordinates}}
\\[0.45em]
J
&=
\begin{pmatrix}
\dfrac{\partial x}{\partial r}
&
\dfrac{\partial x}{\partial\theta}
\\
\dfrac{\partial y}{\partial r}
&
\dfrac{\partial y}{\partial\theta}
\end{pmatrix}
\tag*{\just{Form the Jacobian matrix}}
\\[0.45em]
&=
\begin{pmatrix}
\cos\theta
&
-r\sin\theta
\\
\sin\theta
&
r\cos\theta
\end{pmatrix}
\tag*{\just{Evaluate the partial derivatives}}
\\[0.45em]
\det J
&=
r\cos^2\theta
+
r\sin^2\theta
\\
&=
r
\left(
\cos^2\theta+\sin^2\theta
\right)
\\
&=
r
\tag*{\just{Use $\cos^2\theta+\sin^2\theta=1$}}
\\[0.45em]
dx\,dy
&=
r\,dr\,d\theta
\tag*{\just{Obtain the polar area element}}
\end{align*}
$$
