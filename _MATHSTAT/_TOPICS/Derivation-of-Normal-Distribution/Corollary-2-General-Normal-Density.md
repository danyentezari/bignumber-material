# Corollary 2: General Normal Density

<!-- pdf-page-width: wide -->

Corollary. If

$$
\begin{align*}
X
&=
\mu+\sigma Z,
\qquad
Z\sim N(0,1),
\qquad
\sigma>0,
\tag*{\just{Use Definition 3}}
\end{align*}
$$

then the density of $X$ is

$$
\begin{align*}
Z
&=
\frac{X-\mu}{\sigma}
\tag*{\just{Solve for the standardized variable}}
\\[0.45em]
z
&=
\frac{x-\mu}{\sigma}
\tag*{\just{Express the transformation for values}}
\\[0.45em]
\frac{dz}{dx}
&=
\frac{1}{\sigma}
\tag*{\just{Differentiate the transformation}}
\\[0.45em]
f_X(x)
&=
\phi\left(
\frac{x-\mu}{\sigma}
\right)
\frac{1}{\sigma}
\tag*{\just{Apply the density change-of-variables rule}}
\\[0.45em]
&=
\frac{1}{\sigma}
\frac{1}{\sqrt{2\pi}}
\exp\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right]
\tag*{\just{Substitute the standard normal density}}
\\[0.45em]
\boxed{
f(x;\mu,\sigma)
=
\frac{1}{\sigma\sqrt{2\pi}}
\exp\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right]
}
&&
\tag*{\just{General normal probability density}}
\end{align*}
$$

for

$$
\begin{align*}
-\infty
&<
x
<
\infty
\\
\sigma
&>
0.
\tag*{\just{Domain and scale conditions}}
\end{align*}
$$

$\square$
