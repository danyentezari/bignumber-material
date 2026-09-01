# Corollary 1: Standard Normal Density

<!-- pdf-page-width: wide -->

Corollary. The limiting density in the De Moivre-Laplace theorem is

$$
\begin{align*}
\phi(z)
&=
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
\tag*{\just{Define the limiting Gaussian density}}
\\[0.45em]
\int_{-\infty}^{\infty}
e^{-z^2/2}\,dz
&=
\sqrt{2\pi}
\tag*{\just{Apply Lemma 1}}
\\[0.45em]
\int_{-\infty}^{\infty}
\phi(z)\,dz
&=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
e^{-z^2/2}\,dz
\\
&=
1
\tag*{\just{Normalize the limiting density}}
\end{align*}
$$

Hence,

$$
\begin{align*}
\boxed{
\phi(z)
=
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
}
&&
\tag*{\just{Standard normal probability density}}
\end{align*}
$$

\defaultwidthpar{is a probability density function.}

$\square$
