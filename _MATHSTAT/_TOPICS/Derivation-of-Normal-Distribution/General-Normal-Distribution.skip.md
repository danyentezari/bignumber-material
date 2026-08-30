<!-- skip: backup of General-Normal-Distribution.md; ignored by PDF/HTML builds -->
<!-- source: working-tree -->

# General Normal Distribution

<!-- pdf-page-width: wide -->

Let

$$
Z
\sim
N(0,1)
$$

and define

$$
X
=
\mu+\sigma Z,
\qquad
\sigma>0.
$$

Solving for $Z$,

$$
Z
=
\frac{X-\mu}{\sigma}.
$$

For values,

$$
z
=
\frac{x-\mu}{\sigma}.
$$

Differentiating,

$$
\frac{dz}{dx}
=
\frac{1}{\sigma}.
$$

Therefore, the change-of-variables rule for probability densities gives

$$
f_X(x)
=
\phi
\left(
\frac{x-\mu}{\sigma}
\right)
\frac{1}{\sigma}.
$$

Substituting the standard normal density,

$$
f_X(x)
=
\frac{1}{\sigma}
\frac{1}{\sqrt{2\pi}}
\exp
\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right].
$$

Therefore,

$$
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
$$

for

$$
-\infty<x<\infty,
\qquad
\sigma>0.
$$
