# Polar Area Element

<!-- pdf-page-width: wide -->

\defaultwidthpar{The same factor can be derived geometrically.}

$$
\begin{align*}
A
&=
\frac{1}{2}r^2\theta
\tag*{\just{Area of a circular sector}}
\\[0.45em]
\frac{\theta}{2\pi}
&=
\frac{\text{sector angle}}{\text{complete angle}}
\tag*{\just{Fraction of a complete circle occupied by the sector}}
\\[0.45em]
A
&=
\frac{\theta}{2\pi}
\pi r^2
\\
&=
\frac{1}{2}r^2\theta
\tag*{\just{Recover the sector-area formula}}
\\[0.45em]
\Delta A_i
&=
\frac{1}{2}r_i^2\Delta\theta
-
\frac{1}{2}r_{i-1}^2\Delta\theta
\tag*{\just{Area between two nearby circular arcs}}
\\[0.45em]
&=
\frac{1}{2}
\left(
r_i^2-r_{i-1}^2
\right)
\Delta\theta
\tag*{\just{Factor out the angular width}}
\\[0.45em]
&=
\frac{1}{2}
\left(
r_i+r_{i-1}
\right)
\left(
r_i-r_{i-1}
\right)
\Delta\theta
\tag*{\just{Factor the difference of squares}}
\\[0.45em]
r_i^*
&=
\frac{r_i+r_{i-1}}{2}
\\
\Delta r
&=
r_i-r_{i-1}
\tag*{\just{Define the average radius and radial increment}}
\\[0.45em]
\Delta A_i
&=
r_i^*
\Delta r
\Delta\theta
\tag*{\just{Rewrite the small polar area}}
\\[0.45em]
dA
&=
r\,dr\,d\theta
\tag*{\just{Take the limit}}
\\[0.45em]
\iint_R
f(x,y)\,dA
&=
\iint_{R^*}
f(r\cos\theta,r\sin\theta)
r\,dr\,d\theta
\tag*{\just{Write a double integral in polar coordinates}}
\end{align*}
$$
