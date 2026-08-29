# Polar Area Element

The area of a circular sector of radius $r$ and angle $\theta$ is

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
