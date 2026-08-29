# De Moivre-Laplace Approximation

Apply Stirling's approximation to each factorial:

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
