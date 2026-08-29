# Wallis Product

Define

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
