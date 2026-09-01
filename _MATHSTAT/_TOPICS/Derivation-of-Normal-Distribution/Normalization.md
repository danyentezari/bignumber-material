# Corollary 3: Normalization

<!-- pdf-page-width: wide -->

Corollary. The general normal density has total probability one.

$$
\begin{align*}
\int_{-\infty}^{\infty}
f(x;\mu,\sigma)\,dx
&=
\int_{-\infty}^{\infty}
\frac{1}{\sigma\sqrt{2\pi}}
\exp\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right]
dx
\tag*{\just{Integrate the general normal density}}
\\[0.45em]
z
&=
\frac{x-\mu}{\sigma}
\tag*{\just{Standardize}}
\\[0.45em]
dx
&=
\sigma\,dz
\tag*{\just{Transform the differential}}
\\[0.45em]
\int_{-\infty}^{\infty}
f(x;\mu,\sigma)\,dx
&=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
e^{-z^2/2}\,dz
\tag*{\just{Substitute and cancel the scale factor}}
\\[0.45em]
&=
\frac{1}{\sqrt{2\pi}}
\sqrt{2\pi}
\tag*{\just{Apply Lemma 1}}
\\[0.45em]
&=
1
\tag*{\just{The density is normalized}}
\end{align*}
$$

$\square$
