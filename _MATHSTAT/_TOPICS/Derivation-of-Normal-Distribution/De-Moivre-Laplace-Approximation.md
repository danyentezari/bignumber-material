# De Moivre-Laplace Approximation

<!-- pdf-page-width: wide -->

$$
\begin{align*}
P(X_n=k)
&=
\frac{n!}{k!(n-k)!}p^kq^{n-k}
\tag*{\just{Start from the binomial probability}}
\\[0.45em]
n!
&\approx
\sqrt{2\pi n}
\left(\frac{n}{e}\right)^n
\\
k!
&\approx
\sqrt{2\pi k}
\left(\frac{k}{e}\right)^k
\\
(n-k)!
&\approx
\sqrt{2\pi(n-k)}
\left(\frac{n-k}{e}\right)^{n-k}
\tag*{\just{Approximate each factorial using Theorem 1}}
\\[0.45em]
P(X_n=k)
&\approx
\sqrt{\frac{n}{2\pi k(n-k)}}
\frac{n^np^kq^{n-k}}
{k^k(n-k)^{n-k}}
\tag*{\just{Substitute the three approximations and simplify}}
\\[0.45em]
\delta
&=
k-np
\tag*{\just{Measure the displacement of $k$ from the binomial mean}}
\\[0.45em]
k
&=
np+\delta
\\
n-k
&=
nq-\delta
\tag*{\just{Express both success and failure counts in terms of the displacement}}
\\[0.45em]
L
&=
\log\left[
\frac{n^np^kq^{n-k}}
{k^k(n-k)^{n-k}}
\right]
\tag*{\just{Take the logarithm to convert powers into products}}
\\[0.45em]
&=
-k\log\left(\frac{k}{np}\right)
-(n-k)\log\left(\frac{n-k}{nq}\right)
\tag*{\just{Collect the terms involving $k$ and $n-k$}}
\\[0.45em]
&=
-(np+\delta)
\log\left(1+\frac{\delta}{np}\right)
-(nq-\delta)
\log\left(1-\frac{\delta}{nq}\right)
\tag*{\just{Substitute the displacement expressions}}
\\[0.45em]
\log(1+t)
&=
t-\frac{t^2}{2}+O(t^3)
\\
\log(1-t)
&=
-t-\frac{t^2}{2}+O(t^3)
\tag*{\just{Expand the logarithms for $k$ near the mean}}
\\[0.45em]
L
&\approx
-\frac{\delta^2}{2npq}
\tag*{\just{The first-order terms cancel, leaving the quadratic term}}
\\[0.45em]
\frac{n^np^kq^{n-k}}
{k^k(n-k)^{n-k}}
&\approx
\exp\left(
-\frac{\delta^2}{2npq}
\right)
\tag*{\just{Exponentiate to recover the original factor}}
\\[0.45em]
k
&\approx
np
\\
n-k
&\approx
nq
\tag*{\just{Near the mean, replace the counts by their expected values}}
\\[0.45em]
\sqrt{\frac{n}{2\pi k(n-k)}}
&\approx
\frac{1}{\sqrt{2\pi npq}}
\tag*{\just{Simplify the remaining prefactor}}
\\[0.45em]
P(X_n=k)
&\approx
\frac{1}{\sqrt{2\pi npq}}
\exp\left[
-\frac{(k-np)^2}{2npq}
\right]
\tag*{\just{Combine the prefactor and exponential approximations}}
\\[0.45em]
\mu
&=
np
\\
\sigma^2
&=
npq
\tag*{\just{Apply Proposition 1}}
\\[0.45em]
P(X_n=k)
&\approx
\frac{1}{\sigma\sqrt{2\pi}}
\exp\left[
-\frac{1}{2}
\left(
\frac{k-\mu}{\sigma}
\right)^2
\right]
\tag*{\just{Obtain the normal form of the binomial probability}}
\end{align*}
$$
