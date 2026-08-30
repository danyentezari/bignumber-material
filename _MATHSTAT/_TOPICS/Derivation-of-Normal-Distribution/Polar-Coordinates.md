# Polar Coordinates

<!-- pdf-page-width: wide -->

$$
\begin{align*}
x
&=
r\cos\theta
\tag*{\just{Define}}
\\[0.45em]
y
&=
r\sin\theta
\tag*{\just{and}}
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
\tag*{\just{The Jacobian matrix is}}
\\[0.45em]
J
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
\tag*{\just{Evaluating the derivatives,}}
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
\tag*{\just{Therefore,}}
\\[0.45em]
dx\,dy
&=
r\,dr\,d\theta
\tag*{\just{Hence,}}
\end{align*}
$$
