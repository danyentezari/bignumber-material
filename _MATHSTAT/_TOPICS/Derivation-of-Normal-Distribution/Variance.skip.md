<!-- skip: backup of Variance.md; ignored by PDF/HTML builds -->
<!-- source: working-tree -->

# Variance

<!-- pdf-page-width: wide -->

Since $E[Z]=0$,

$$
\operatorname{Var}(Z)
=
E[Z^2].
$$

Thus,

$$
E[Z^2]
=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
z^2e^{-z^2/2}\,dz.
$$

Using integration by parts,

$$
u=z
$$

and

$$
dv
=
z e^{-z^2/2}\,dz.
$$

Then

$$
du
=
dz
$$

and

$$
v
=
-e^{-z^2/2}.
$$

Therefore,

$$
\begin{aligned}
\int_{-\infty}^{\infty}
z^2e^{-z^2/2}\,dz
&=
\left[
-z e^{-z^2/2}
\right]_{-\infty}^{\infty}
+
\int_{-\infty}^{\infty}
e^{-z^2/2}\,dz
\\
&=
\sqrt{2\pi}.
\end{aligned}
$$

Hence,

$$
E[Z^2]
=
1.
$$

Therefore,

$$
\operatorname{Var}(Z)
=
1.
$$

Since

$$
X
=
\mu+\sigma Z,
$$

we have

$$
\operatorname{Var}(X)
=
\sigma^2\operatorname{Var}(Z).
$$

Thus,

$$
\boxed{
\operatorname{Var}(X)
=
\sigma^2
}.
$$

Hence,

$\displaystyle
X\sim N(\mu,\sigma^2)
\quad\Longrightarrow\quad
f(x;\mu,\sigma)
=
\frac{1}{\sigma\sqrt{2\pi}}
\exp\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right].
$

The normal density therefore arises as the continuous limiting form of the binomial distribution under standardization, with the Gaussian integral supplying its normalization.
