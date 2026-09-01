# Corollary 4: Mean

<!-- pdf-page-width: wide -->

Corollary. If

$$
\begin{align*}
X
&\sim
N(\mu,\sigma^2),
\tag*{\just{Assume a general normal random variable}}
\end{align*}
$$

then

$$
\begin{align*}
E[X]
&=
\mu.
\tag*{\just{Mean of the normal distribution}}
\end{align*}
$$

Proof.

$$
\begin{align*}
E[Z]
&=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
z e^{-z^2/2}\,dz
\tag*{\just{Write the standard normal expectation}}
\\[0.45em]
&=
0
\tag*{\just{The integrand is odd over a symmetric interval}}
\\[0.45em]
X
&=
\mu+\sigma Z
\tag*{\just{Use Definition 3}}
\\[0.45em]
E[X]
&=
E[\mu+\sigma Z]
\\
&=
\mu+\sigma E[Z]
\tag*{\just{Apply linearity of expectation}}
\\[0.45em]
&=
\mu
\tag*{\just{Substitute $E[Z]=0$}}
\\[0.45em]
\boxed{
E[X]
=
\mu
}
&&
\tag*{\just{Mean of the general normal distribution}}
\end{align*}
$$

$\square$
