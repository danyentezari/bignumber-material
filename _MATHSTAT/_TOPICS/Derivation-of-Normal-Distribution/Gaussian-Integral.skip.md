<!-- skip: backup of Gaussian-Integral.md; ignored by PDF/HTML builds -->
<!-- source: working-tree -->

# Gaussian Integral

<!-- pdf-page-width: wide -->

Define

$$
I
=
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx.
$$

The function has no elementary antiderivative. To evaluate the integral, square it:

$$
I^2
=
\left(
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
\right)
\left(
\int_{-\infty}^{\infty}
e^{-y^2/2}\,dy
\right).
$$

Combining the two integrals gives

$$
I^2
=
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
e^{-x^2/2}
e^{-y^2/2}
\,dx\,dy.
$$

Using

$$
e^a e^b
=
e^{a+b},
$$

we obtain

$$
I^2
=
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
e^{-(x^2+y^2)/2}
\,dx\,dy.
$$

The region of integration is the entire plane.

Switch to polar coordinates:

$$
x
=
r\cos\theta,
$$

$$
y
=
r\sin\theta,
$$

and

$$
x^2+y^2
=
r^2.
$$

The Jacobian gives

$$
dx\,dy
=
r\,dr\,d\theta.
$$

Therefore,

$$
I^2
=
\int_0^{2\pi}
\int_0^\infty
e^{-r^2/2}
r\,dr\,d\theta.
$$
