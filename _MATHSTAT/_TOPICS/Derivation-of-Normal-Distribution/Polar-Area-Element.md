# Polar Area Element

<!-- pdf-page-width: wide -->

$$
\begin{align*}
A
&=
\frac{1}{2}r^2\theta
\tag*{\just{The area of a circular sector of radius $r$ and angle $\theta$ is}}
\\[0.45em]
&\frac{\theta}{2\pi}
\tag*{\just{This follows because the sector occupies the fraction}}
\\[0.45em]
A
&=
\frac{\theta}{2\pi}
\pi r^2
=
\frac{1}{2}r^2\theta
\tag*{\just{of a complete circle. Therefore,}}
\\[0.45em]
\Delta A_i
&=
\frac{1}{2}r_i^2\Delta\theta
-
\frac{1}{2}r_{i-1}^2\Delta\theta
\tag*{\just{Consider a small polar region between radii $r_{i-1}$ and $r_i$ and angular width $\Delta\theta$. Its area is}}
\\[0.45em]
\Delta A_i
&=
\frac{1}{2}
\left(
r_i^2-r_{i-1}^2
\right)
\Delta\theta
\tag*{\just{Therefore,}}
\\[0.45em]
\Delta A_i
&=
\frac{1}{2}
\left(
r_i+r_{i-1}
\right)
\left(
r_i-r_{i-1}
\right)
\Delta\theta
\tag*{\just{Factoring,}}
\\[0.45em]
r_i^*
&=
\frac{r_i+r_{i-1}}{2}
\tag*{\just{Define}}
\\[0.45em]
\Delta r
&=
r_i-r_{i-1}
\tag*{\just{and}}
\\[0.45em]
\Delta A_i
&=
r_i^*
\Delta r
\Delta\theta
\tag*{\just{Then}}
\\[0.45em]
dA
&=
r\,dr\,d\theta
\tag*{\just{In the limit,}}
\\[0.45em]
\iint_R f(x,y)\,dA
&=
\iint_{R^*}
f(r\cos\theta,r\sin\theta)
r\,dr\,d\theta
\tag*{\just{Therefore, a double integral in polar coordinates becomes}}
\end{align*}
$$
