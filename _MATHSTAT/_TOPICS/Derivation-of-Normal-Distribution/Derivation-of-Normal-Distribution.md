# Derivation and Proof of Normal Distribution

$\displaystyle
f(x;\mu,\sigma)
=
\frac{1}{\sigma\sqrt{2\pi}}
\exp\left[
-\frac{1}{2}
\left(
\frac{x-\mu}{\sigma}
\right)^2
\right],
\qquad
-\infty<x<\infty,
\qquad
\sigma>0
$

This derivation establishes the normal distribution from the normal approximation to the binomial distribution and proves that the resulting probability density integrates to one.

Change of Variables. For a one-dimensional integral, let

$$
u=g(x).
$$

Then

$$
\frac{du}{dx}
=
g'(x)
$$

and therefore

$$
du
=
g'(x)\,dx.
$$

Thus,

$$
\int f(g(x))g'(x)\,dx
=
\int f(u)\,du.
$$

For a definite integral,

$$
\int_a^b f(g(x))g'(x)\,dx
=
\int_{g(a)}^{g(b)}f(u)\,du.
$$

The same principle extends to several variables, except that changes in area or volume must also be accounted for.

Jacobian. Let

$$
x=x(u,v),
\qquad
y=y(u,v).
$$

The Jacobian matrix is

$$
J
=
\begin{pmatrix}
\dfrac{\partial x}{\partial u}
&
\dfrac{\partial x}{\partial v}
\\
\dfrac{\partial y}{\partial u}
&
\dfrac{\partial y}{\partial v}
\end{pmatrix}.
$$

Its determinant is

$$
\det J
=
\frac{\partial x}{\partial u}
\frac{\partial y}{\partial v}
-
\frac{\partial x}{\partial v}
\frac{\partial y}{\partial u}.
$$

The absolute value of the determinant gives the local area-scaling factor:

$$
dx\,dy
=
\left|
\det J
\right|
du\,dv.
$$

Therefore,

$$
\iint_R f(x,y)\,dx\,dy
=
\iint_S
f(x(u,v),y(u,v))
\left|
\det J
\right|
du\,dv.
$$

where

- $R$ is the region in the $(x,y)$ coordinate system.
- $S$ is the corresponding region in the $(u,v)$ coordinate system.
- $J$ is the Jacobian matrix of the transformation.

Jacobian Example. Consider a parallelogram with side vectors

$$
\mathbf{w}_1
=
\begin{pmatrix}
2\\
1
\end{pmatrix}
$$

and

$$
\mathbf{w}_2
=
\begin{pmatrix}
-1\\
1
\end{pmatrix}.
$$

Let its starting point be

$$
\mathbf{b}
=
\begin{pmatrix}
1\\
1
\end{pmatrix}.
$$

Every point in the parallelogram is

$$
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
u\mathbf{w}_1
+
v\mathbf{w}_2
+
\mathbf{b}.
$$

Therefore,

$$
x
=
2u-v+1
$$

and

$$
y
=
u+v+1.
$$

For

$$
0\leq u\leq1,
\qquad
0\leq v\leq1,
$$

the unit square in the $(u,v)$ coordinate system maps to the parallelogram in the $(x,y)$ coordinate system.

The vertices are

| $(u,v)$ | $(x,y)$ |
|---|---|
| $(0,0)$ | $(1,1)$ |
| $(0,1)$ | $(0,2)$ |
| $(1,0)$ | $(3,2)$ |
| $(1,1)$ | $(2,3)$ |

The Jacobian is

$$
J
=
\begin{pmatrix}
2 & -1\\
1 & 1
\end{pmatrix}.
$$

Therefore,

$$
\det J
=
(2)(1)-(-1)(1)
=
3.
$$

The area of the parallelogram is

$$
A
=
\iint_P1\,dx\,dy.
$$

Changing variables,

$$
A
=
\int_0^1
\int_0^1
3\,du\,dv.
$$

Thus,

$$
A
=
3.
$$

This demonstrates why the Jacobian determinant appears in a change of variables: it measures how an area element changes under the transformation.

Polar Coordinates. Define

$$
x
=
r\cos\theta
$$

and

$$
y
=
r\sin\theta.
$$

The Jacobian matrix is

$$
J
=
\begin{pmatrix}
\dfrac{\partial x}{\partial r}
&
\dfrac{\partial x}{\partial\theta}
\\
\dfrac{\partial y}{\partial r}
&
\dfrac{\partial y}{\partial\theta}
\end{pmatrix}.
$$

Evaluating the derivatives,

$$
J
=
\begin{pmatrix}
\cos\theta
&
-r\sin\theta
\\
\sin\theta
&
r\cos\theta
\end{pmatrix}.
$$

Therefore,

$$
\begin{aligned}
\det J
&=
r\cos^2\theta
+
r\sin^2\theta
\\
&=
r
\left(
\cos^2\theta+\sin^2\theta
\right)
\\
&=
r.
\end{aligned}
$$

Hence,

$$
dx\,dy
=
r\,dr\,d\theta.
$$

Polar Area Element. The area of a circular sector of radius $r$ and angle $\theta$ is

$$
A
=
\frac{1}{2}r^2\theta.
$$

This follows because the sector occupies the fraction

$$
\frac{\theta}{2\pi}
$$

of a complete circle. Therefore,

$$
A
=
\frac{\theta}{2\pi}
\pi r^2
=
\frac{1}{2}r^2\theta.
$$

Consider a small polar region between radii $r_{i-1}$ and $r_i$ and angular width $\Delta\theta$.

Its area is

$$
\Delta A_i
=
\frac{1}{2}r_i^2\Delta\theta
-
\frac{1}{2}r_{i-1}^2\Delta\theta.
$$

Therefore,

$$
\Delta A_i
=
\frac{1}{2}
\left(
r_i^2-r_{i-1}^2
\right)
\Delta\theta.
$$

Factoring,

$$
\Delta A_i
=
\frac{1}{2}
\left(
r_i+r_{i-1}
\right)
\left(
r_i-r_{i-1}
\right)
\Delta\theta.
$$

Define

$$
r_i^*
=
\frac{r_i+r_{i-1}}{2}
$$

and

$$
\Delta r
=
r_i-r_{i-1}.
$$

Then

$$
\Delta A_i
=
r_i^*
\Delta r
\Delta\theta.
$$

In the limit,

$$
dA
=
r\,dr\,d\theta.
$$

Therefore, a double integral in polar coordinates becomes

$$
\iint_R f(x,y)\,dA
=
\iint_{R^*}
f(r\cos\theta,r\sin\theta)
r\,dr\,d\theta.
$$

Gaussian Integral. Define

$$
I
=
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx.
$$

The function has no elementary antiderivative. To evaluate the integral, square it:

$$
I^2
=
\left(
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
\right)
\left(
\int_{-\infty}^{\infty}
e^{-y^2/2}\,dy
\right).
$$

Combining the two integrals gives

$$
I^2
=
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
e^{-x^2/2}
e^{-y^2/2}
\,dx\,dy.
$$

Using

$$
e^a e^b
=
e^{a+b},
$$

we obtain

$$
I^2
=
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
e^{-(x^2+y^2)/2}
\,dx\,dy.
$$

The region of integration is the entire plane.

Switch to polar coordinates:

$$
x
=
r\cos\theta,
$$

$$
y
=
r\sin\theta,
$$

and

$$
x^2+y^2
=
r^2.
$$

The Jacobian gives

$$
dx\,dy
=
r\,dr\,d\theta.
$$

Therefore,

$$
I^2
=
\int_0^{2\pi}
\int_0^\infty
e^{-r^2/2}
r\,dr\,d\theta.
$$

Evaluate the inner integral. Let

$$
u
=
\frac{r^2}{2}.
$$

Then

$$
du
=
r\,dr.
$$

Thus,

$$
\int_0^\infty
e^{-r^2/2}
r\,dr
=
\int_0^\infty e^{-u}\,du.
$$

Therefore,

$$
\int_0^\infty e^{-u}\,du
=
\left[
-e^{-u}
\right]_0^\infty
=
1.
$$

Hence,

$$
I^2
=
\int_0^{2\pi}1\,d\theta.
$$

Therefore,

$$
I^2
=
2\pi.
$$

Since $I>0$,

$$
I
=
\sqrt{2\pi}.
$$

Thus,

$$
\boxed{
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
=
\sqrt{2\pi}
}
$$

and equivalently,

$$
\boxed{
\int_{-\infty}^{\infty}
e^{-x^2}\,dx
=
\sqrt{\pi}
}.
$$

Wallis Product. Define

$$
W_m
=
\int_0^{\pi/2}
\sin^m x\,dx.
$$

Integration by parts gives the recurrence

$$
W_m
=
\frac{m-1}{m}
W_{m-2}.
$$

Since

$$
W_0
=
\frac{\pi}{2}
$$

and

$$
W_1
=
1,
$$

we obtain

$$
W_{2n}
=
\frac{1\cdot3\cdot5\cdots(2n-1)}
{2\cdot4\cdot6\cdots(2n)}
\frac{\pi}{2}
$$

and

$$
W_{2n+1}
=
\frac{2\cdot4\cdot6\cdots(2n)}
{3\cdot5\cdot7\cdots(2n+1)}.
$$

This produces the Wallis product

$$
\boxed{
\frac{\pi}{2}
=
\prod_{n=1}^{\infty}
\frac{(2n)^2}
{(2n-1)(2n+1)}
}.
$$

The even integral can also be written

$$
W_{2n}
=
\frac{\pi}{2}
\frac{\binom{2n}{n}}{4^n}.
$$

The odd integral is

$$
W_{2n+1}
=
\frac{4^n}
{(2n+1)\binom{2n}{n}}.
$$

Since

$$
W_{2n+1}
<
W_{2n}
<
W_{2n-1},
$$

and

$$
\frac{W_{2n-1}}{W_{2n+1}}
=
\frac{2n+1}{2n}
\rightarrow1,
$$

it follows that

$$
\frac{W_{2n}}{W_{2n+1}}
\rightarrow1.
$$

Substituting the explicit expressions gives

$$
\frac{\pi}{2}
(2n+1)
\frac{\binom{2n}{n}^2}{16^n}
\rightarrow1.
$$

Therefore,

$$
\boxed{
\binom{2n}{n}
\sim
\frac{4^n}{\sqrt{\pi n}}
}.
$$

This result determines the constant that appears in Stirling's approximation.

Stirling's Approximation. Define

$$
a_n
=
\frac{n!e^n}{n^{n+1/2}}.
$$

Taking logarithms,

$$
\log a_n
=
\log(n!)
+
n
-
\left(
n+\frac{1}{2}
\right)
\log n.
$$

Consider consecutive terms:

$$
\log\frac{a_{n+1}}{a_n}
=
1
-
\left(
n+\frac{1}{2}
\right)
\log\left(
1+\frac{1}{n}
\right).
$$

Using

$$
\log(1+t)
=
t-\frac{t^2}{2}+\frac{t^3}{3}-\cdots,
$$

with

$$
t=\frac{1}{n},
$$

gives

$$
\log\frac{a_{n+1}}{a_n}
=
-\frac{1}{12n^2}
+
O\left(
\frac{1}{n^3}
\right).
$$

Because

$$
\sum_{n=1}^{\infty}
\frac{1}{n^2}
$$

converges, the sequence $\log a_n$ converges. Therefore,

$$
a_n
\rightarrow C
$$

for some positive constant $C$.

Hence,

$$
n!
\sim
C
n^{n+1/2}
e^{-n}.
$$

Apply this approximation to

$$
\binom{2n}{n}
=
\frac{(2n)!}{(n!)^2}.
$$

Then

$$
\binom{2n}{n}
\sim
\frac{
C(2n)^{2n+1/2}e^{-2n}
}{
C^2n^{2n+1}e^{-2n}
}.
$$

Simplifying,

$$
\binom{2n}{n}
\sim
\frac{\sqrt{2}}{C}
\frac{4^n}{\sqrt{n}}.
$$

But the Wallis result gives

$$
\binom{2n}{n}
\sim
\frac{4^n}{\sqrt{\pi n}}.
$$

Comparing the two expressions,

$$
\frac{\sqrt{2}}{C}
=
\frac{1}{\sqrt{\pi}}.
$$

Therefore,

$$
C
=
\sqrt{2\pi}.
$$

Thus,

$$
\boxed{
n!
\sim
\sqrt{2\pi n}
\left(
\frac{n}{e}
\right)^n
}
$$

or equivalently,

$$
\boxed{
\lim_{n\to\infty}
\frac{
n!
}{
\sqrt{2\pi n}
\left(
\dfrac{n}{e}
\right)^n
}
=
1
}.
$$

Binomial Distribution. Let

$$
X_n
\sim
\operatorname{Bin}(n,p)
$$

and define

$$
q
=
1-p.
$$

The probability of obtaining exactly $k$ successes is

$$
P(X_n=k)
=
\binom{n}{k}
p^kq^{n-k}.
$$

Therefore,

$$
P(X_n=k)
=
\frac{n!}{k!(n-k)!}
p^kq^{n-k}.
$$

The binomial mean is

$$
\mu
=
np
$$

and its variance is

$$
\sigma^2
=
npq.
$$

Therefore,

$$
\sigma
=
\sqrt{npq}.
$$

De Moivre-Laplace Approximation. Apply Stirling's approximation to each factorial:

$$
n!
\approx
\sqrt{2\pi n}
\left(
\frac{n}{e}
\right)^n,
$$

$$
k!
\approx
\sqrt{2\pi k}
\left(
\frac{k}{e}
\right)^k,
$$

and

$$
(n-k)!
\approx
\sqrt{2\pi(n-k)}
\left(
\frac{n-k}{e}
\right)^{n-k}.
$$

Substituting into the binomial probability gives

$$
P(X_n=k)
\approx
\sqrt{
\frac{n}
{2\pi k(n-k)}
}
\frac{
n^np^kq^{n-k}
}{
k^k(n-k)^{n-k}
}.
$$

Define the displacement from the mean:

$$
\delta
=
k-np.
$$

Thus,

$$
k
=
np+\delta
$$

and

$$
n-k
=
nq-\delta.
$$

Consider the logarithm of the exponential factor:

$$
L
=
\log
\left[
\frac{
n^np^kq^{n-k}
}{
k^k(n-k)^{n-k}
}
\right].
$$

This becomes

$$
L
=
-k
\log
\left(
\frac{k}{np}
\right)
-
(n-k)
\log
\left(
\frac{n-k}{nq}
\right).
$$

Substituting

$$
k=np+\delta
$$

and

$$
n-k=nq-\delta
$$

gives

$$
L
=
-(np+\delta)
\log
\left(
1+\frac{\delta}{np}
\right)
-
(nq-\delta)
\log
\left(
1-\frac{\delta}{nq}
\right).
$$

For values of $k$ near the mean, $\delta$ is small relative to $n$.

Use the expansions

$$
\log(1+t)
=
t-\frac{t^2}{2}
+
O(t^3)
$$

and

$$
\log(1-t)
=
-t-\frac{t^2}{2}
+
O(t^3).
$$

The first-order terms cancel. The leading remaining term is

$$
L
\approx
-\frac{\delta^2}{2npq}.
$$

Therefore,

$$
\frac{
n^np^kq^{n-k}
}{
k^k(n-k)^{n-k}
}
\approx
\exp
\left(
-\frac{\delta^2}{2npq}
\right).
$$

For $k$ near $np$,

$$
k
\approx
np
$$

and

$$
n-k
\approx
nq.
$$

Therefore,

$$
\sqrt{
\frac{n}
{2\pi k(n-k)}
}
\approx
\frac{1}{\sqrt{2\pi npq}}.
$$

Combining the two parts gives

$$
P(X_n=k)
\approx
\frac{1}{\sqrt{2\pi npq}}
\exp
\left[
-\frac{(k-np)^2}{2npq}
\right].
$$

Since

$$
\mu=np
$$

and

$$
\sigma^2=npq,
$$

this becomes

$$
P(X_n=k)
\approx
\frac{1}{\sigma\sqrt{2\pi}}
\exp
\left[
-\frac{1}{2}
\left(
\frac{k-\mu}{\sigma}
\right)^2
\right].
$$

This is the form of the normal density.

Standardization. Define

$$
z
=
\frac{k-np}{\sqrt{npq}}.
$$

Then

$$
z
=
\frac{k-\mu}{\sigma}.
$$

Because $k$ changes in integer increments,

$$
\Delta k
=
1.
$$

Therefore, the corresponding increment in $z$ is

$$
\Delta z
=
\frac{1}{\sqrt{npq}}.
$$

The binomial probability can therefore be written

$$
P(X_n=k)
\approx
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
\Delta z.
$$

For an interval

$$
a
\leq
\frac{X_n-np}{\sqrt{npq}}
\leq
b,
$$

the probability is a sum of these terms:

$$
P
\left(
a
\leq
\frac{X_n-np}{\sqrt{npq}}
\leq
b
\right)
\approx
\sum
\frac{1}{\sqrt{2\pi}}
e^{-z_i^2/2}
\Delta z.
$$

As

$$
n\rightarrow\infty,
$$

we have

$$
\Delta z
\rightarrow0.
$$

The sum becomes a Riemann integral:

$$
\boxed{
P
\left(
a
\leq
\frac{X_n-np}{\sqrt{npq}}
\leq
b
\right)
\rightarrow
\int_a^b
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
\,dz
}.
$$

This is the de Moivre-Laplace limit theorem.

Standard Normal Distribution. The limiting probability density is therefore

$$
\phi(z)
=
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}.
$$

The Gaussian integral proved that

$$
\int_{-\infty}^{\infty}
e^{-z^2/2}\,dz
=
\sqrt{2\pi}.
$$

Therefore,

$$
\int_{-\infty}^{\infty}
\phi(z)\,dz
=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
e^{-z^2/2}\,dz.
$$

Thus,

$$
\int_{-\infty}^{\infty}
\phi(z)\,dz
=
1.
$$

Hence,

$$
\boxed{
\phi(z)
=
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
}
$$

is a probability density function.

General Normal Distribution. Let

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

Normalization. Integrate the density:

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

Mean. For the standard normal distribution,

$$
E[Z]
=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
z e^{-z^2/2}\,dz.
$$

The integrand is an odd function over a symmetric interval. Therefore,

$$
E[Z]
=
0.
$$

Since

$$
X
=
\mu+\sigma Z,
$$

we obtain

$$
E[X]
=
\mu+\sigma E[Z].
$$

Therefore,

$$
\boxed{
E[X]
=
\mu
}.
$$

Variance. Since $E[Z]=0$,

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

## References

1. Ross, S. M. *A First Course in Probability*. 10th ed. Pearson, 2019. §5.4, “Normal Random Variables,” p. 200 onward — definition and normalization of the normal density, including evaluation of the Gaussian integral by polar coordinates.

2. Ross, S. M. *A First Course in Probability*. 10th ed. Pearson, 2019. §5.4.1, “The Normal Approximation to the Binomial Distribution,” p. 207 onward — the de Moivre-Laplace limit theorem and standardization of the binomial distribution.

3. Stewart, J. *Calculus: Early Transcendentals*. 8th ed. Cengage Learning, 2016. §15.3, “Double Integrals in Polar Coordinates,” p. 1011 onward — polar rectangles, sector areas, the factor $r$, and double integration in polar coordinates.

4. Stewart, J. *Calculus: Early Transcendentals*. 8th ed. Cengage Learning, 2016. §15.9, “Change of Variables in Multiple Integrals,” p. 1057 onward — Jacobian determinants and the change-of-variables formula for double integrals.

5. Kreyszig, E. *Advanced Engineering Mathematics*. 10th ed. Wiley, 2011. §24.8, “Normal Distribution” — the normal probability distribution within probability theory.

6. Conrad, K. *The Gaussian Integral*. University of Connecticut. §1, “First Proof: Polar Coordinates” — evaluation of the Gaussian integral by squaring the integral and changing to polar coordinates.

7. Conrad, K. *Stirling's Formula*. University of Connecticut. §1 — statement of Stirling's formula; §3 — proof and the appearance of $\sqrt{2\pi}$; §5 — historical relation among Stirling's formula, the Wallis product, de Moivre, and the normal approximation to the binomial distribution.

8. Hald, A. *A History of Probability and Statistics and Their Applications before 1750*. Wiley, 1990. Chapter 24, “De Moivre's Normal Approximation to the Binomial Distribution, 1733” — de Moivre's approximation, Stirling's formula, and Laplace's later extension.