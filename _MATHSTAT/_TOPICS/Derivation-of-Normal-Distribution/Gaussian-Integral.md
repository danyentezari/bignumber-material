# Gaussian Integral

<!-- pdf-page-width: wide -->

$$
\begin{align*}
I
&=
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
\tag*{\just{Define}}
\\[0.45em]
I^2
&=
\left(
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
\right)
\left(
\int_{-\infty}^{\infty}
e^{-y^2/2}\,dy
\right)
\tag*{\just{The function has no elementary antiderivative. To evaluate the integral, square it:}}
\\[0.45em]
I^2
&=
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
e^{-x^2/2}
e^{-y^2/2}
\,dx\,dy
\tag*{\just{Combining the two integrals gives}}
\\[0.45em]
e^a e^b
&=
e^{a+b}
\tag*{\just{Using}}
\\[0.45em]
I^2
&=
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
e^{-(x^2+y^2)/2}
\,dx\,dy
\tag*{\just{we obtain}}
\\[0.45em]
x
&=
r\cos\theta
\\
y
&=
r\sin\theta
\\
x^2+y^2
&=
r^2
\tag*{\just{The region of integration is the entire plane. Switch to polar coordinates:}}
\\[0.45em]
dx\,dy
&=
r\,dr\,d\theta
\tag*{\just{The Jacobian gives}}
\\[0.45em]
I^2
&=
\int_0^{2\pi}
\int_0^\infty
e^{-r^2/2}
r\,dr\,d\theta
\tag*{\just{Therefore,}}
\end{align*}
$$
