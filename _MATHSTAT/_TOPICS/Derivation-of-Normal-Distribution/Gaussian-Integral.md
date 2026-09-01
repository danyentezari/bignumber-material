# Lemma 1: Gaussian Integral

<!-- pdf-page-width: wide -->

Lemma. The Gaussian integral satisfies

$$
\begin{align*}
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
&=
\sqrt{2\pi}
\tag*{\just{Gaussian integral}}
\end{align*}
$$

Proof.

$$
\begin{align*}
I
&=
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
\tag*{\just{Define the Gaussian integral}}
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
\tag*{\just{Square the integral}}
\\[0.45em]
&=
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
e^{-x^2/2}
e^{-y^2/2}
\,dx\,dy
\tag*{\just{Write the product as an integral over the plane}}
\\[0.45em]
e^ae^b
&=
e^{a+b}
\tag*{\just{Use the product rule for exponentials}}
\\[0.45em]
I^2
&=
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
e^{-(x^2+y^2)/2}
\,dx\,dy
\tag*{\just{Combine the exponential factors}}
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
\tag*{\just{Switch to polar coordinates}}
\\[0.45em]
dx\,dy
&=
r\,dr\,d\theta
\tag*{\just{Apply the polar Jacobian}}
\\[0.45em]
I^2
&=
\int_0^{2\pi}
\int_0^\infty
e^{-r^2/2}
r\,dr\,d\theta
\tag*{\just{Transform the integral over the entire plane}}
\\[0.45em]
u
&=
\frac{r^2}{2}
\\
du
&=
r\,dr
\tag*{\just{Substitute in the radial integral}}
\\[0.45em]
\int_0^\infty
e^{-r^2/2}
r\,dr
&=
\int_0^\infty
e^{-u}\,du
\tag*{\just{Transform the inner integral}}
\\[0.45em]
&=
\left[
-e^{-u}
\right]_0^\infty
\\
&=
1
\tag*{\just{Evaluate the inner integral}}
\\[0.45em]
I^2
&=
\int_0^{2\pi}
1\,d\theta
\\
&=
2\pi
\tag*{\just{Evaluate the angular integral}}
\\[0.45em]
I
&=
\sqrt{2\pi}
\tag*{\just{Take the positive square root because $I>0$}}
\end{align*}
$$

Therefore,

$$
\begin{align*}
\boxed{
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
=
\sqrt{2\pi}
}
&&
\tag*{\just{Gaussian integral}}
\\[0.45em]
\boxed{
\int_{-\infty}^{\infty}
e^{-x^2}\,dx
=
\sqrt{\pi}
}
&&
\tag*{\just{Equivalent scaled form}}
\end{align*}
$$

$\square$
