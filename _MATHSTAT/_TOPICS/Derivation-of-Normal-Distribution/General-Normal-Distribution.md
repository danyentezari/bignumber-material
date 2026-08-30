# General Normal Distribution

<!-- pdf-page-width: wide -->

$$
\begin{align*}
Z
&\sim
N(0,1)
\tag*{\just{Let}}
\\[0.45em]
X
&=
\mu+\sigma Z,
\qquad
\sigma>0
\tag*{\just{and define}}
\\[0.45em]
Z
&=
\frac{X-\mu}{\sigma}
\tag*{\just{Solving for $Z$,}}
\\[0.45em]
z
&=
\frac{x-\mu}{\sigma}
\tag*{\just{For values,}}
\\[0.45em]
\frac{dz}{dx}
&=
\frac{1}{\sigma}
\tag*{\just{Differentiating,}}
\\[0.45em]
f_X(x)
&=
\phi
\left(
\frac{x-\mu}{\sigma}
\right)
\frac{1}{\sigma}
\tag*{\just{Therefore, the change-of-variables rule for probability densities gives}}
\\[0.45em]
f_X(x)
&=
\frac{1}{\sigma}
\frac{1}{\sqrt{2\pi}}
\exp
\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right]
\tag*{\just{Substituting the standard normal density,}}
\\[0.45em]
\boxed{
f(x;\mu,\sigma)
=
\frac{1}{\sigma\sqrt{2\pi}}
\exp
\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right]
}
\tag*{\just{Therefore,}}
\\[0.45em]
-\infty
&<
x
<
\infty,
\qquad
\sigma>0
\tag*{\just{for}}
\end{align*}
$$
