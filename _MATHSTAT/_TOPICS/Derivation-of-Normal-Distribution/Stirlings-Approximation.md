# Stirling's Approximation

Define

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