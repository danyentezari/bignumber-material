# Normalization

Integrate the density:

$$
\int_{-\infty}^{\infty}
f(x;\mu,\sigma)\,dx
=
\int_{-\infty}^{\infty}
\frac{1}{\sigma\sqrt{2\pi}}
\exp
\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right]
dx.
$$

Let

$$
z
=
\frac{x-\mu}{\sigma}.
$$

Then

$$
dx
=
\sigma\,dz.
$$

Therefore,

$$
\begin{aligned}
\int_{-\infty}^{\infty}
f(x;\mu,\sigma)\,dx
&=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
e^{-z^2/2}\,dz
\\
&=
\frac{1}{\sqrt{2\pi}}
\sqrt{2\pi}
\\
&=
1.
\end{aligned}
$$

Thus the normal density has total probability one.
