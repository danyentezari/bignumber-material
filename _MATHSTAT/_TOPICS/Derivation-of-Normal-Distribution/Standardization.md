# Standardization

Define

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
