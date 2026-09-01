# Variance

<!-- pdf-page-width: wide -->

$$
\begin{align*}
\operatorname{Var}(Z)
&=
E[Z^2]
\tag*{\just{Since $E[Z]=0$,}}
\\[0.45em]
E[Z^2]
&=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
z^2e^{-z^2/2}\,dz
\tag*{\just{Thus,}}
\\[0.45em]
u
&=
z
\tag*{\just{Using integration by parts,}}
\\[0.45em]
dv
&=
z e^{-z^2/2}\,dz
\tag*{\just{and}}
\\[0.45em]
du
&=
dz
\tag*{\just{Then}}
\\[0.45em]
v
&=
-e^{-z^2/2}
\tag*{\just{and}}
\\[0.45em]
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
\sqrt{2\pi}
\tag*{\just{Therefore,}}
\\[0.45em]
E[Z^2]
&=
1
\tag*{\just{Hence,}}
\\[0.45em]
\operatorname{Var}(Z)
&=
1
\tag*{\just{Therefore,}}
\\[0.45em]
X
&=
\mu+\sigma Z
\tag*{\just{Since}}
\\[0.45em]
\operatorname{Var}(X)
&=
\sigma^2\operatorname{Var}(Z)
\tag*{\just{we have}}
\\[0.45em]
\boxed{
\operatorname{Var}(X)
=
\sigma^2
}
\tag*{\just{Thus,}}
\end{align*}
$$


\defaultwidthpar{
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
}