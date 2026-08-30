# Normalization

<!-- pdf-page-width: wide -->

$$
\begin{align*}
\int_{-\infty}^{\infty}
f(x;\mu,\sigma)\,dx
&=
\int_{-\infty}^{\infty}
\frac{1}{\sigma\sqrt{2\pi}}
\exp
\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right]
dx
\tag*{\just{Integrate the density:}}
\\[0.45em]
z
&=
\frac{x-\mu}{\sigma}
\tag*{\just{Let}}
\\[0.45em]
dx
&=
\sigma\,dz
\tag*{\just{Then}}
\\[0.45em]
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
1
\tag*{\just{Therefore,}}
\end{align*}
$$

Thus the normal density has total probability one.
