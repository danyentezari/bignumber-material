<!-- skip: backup of Polar-Coordinates.md; ignored by PDF/HTML builds -->
<!-- source: working-tree -->

# Polar Coordinates

<!-- pdf-page-width: wide -->

Define

$$
x
=
r\cos\theta
$$

and

$$
y
=
r\sin\theta.
$$

The Jacobian matrix is

$$
J
=
\begin{pmatrix}
\dfrac{\partial x}{\partial r}
&
\dfrac{\partial x}{\partial\theta}
\\
\dfrac{\partial y}{\partial r}
&
\dfrac{\partial y}{\partial\theta}
\end{pmatrix}.
$$

Evaluating the derivatives,

$$
J
=
\begin{pmatrix}
\cos\theta
&
-r\sin\theta
\\
\sin\theta
&
r\cos\theta
\end{pmatrix}.
$$

Therefore,

$$
\begin{aligned}
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
r.
\end{aligned}
$$

Hence,

$$
dx\,dy
=
r\,dr\,d\theta.
$$
