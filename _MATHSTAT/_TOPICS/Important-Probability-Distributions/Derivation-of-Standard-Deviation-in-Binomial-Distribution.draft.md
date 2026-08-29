# Derivation of Standard Deviation in Binomial Distribution

$\displaystyle
X\sim\operatorname{Bin}(n,p)
\qquad\Longrightarrow\qquad
\sigma
=
\sqrt{np(1-p)}
=
\sqrt{npq}
$

where

- $X$ is a binomial random variable.
- $n$ is the number of independent trials.
- $p$ is the probability of success in each trial.
- $q=1-p$ is the probability of failure.
- $\sigma$ is the standard deviation of $X$.

Binomial Distribution. A binomial random variable counts the number of successes in $n$ independent trials.

Its probability mass function is

$$
P(X=k)
=
\binom{n}{k}
p^kq^{n-k},
\qquad
k=0,1,\ldots,n.
$$

Rather than deriving the variance directly from this sum, represent the binomial random variable as a sum of individual Bernoulli random variables.

Bernoulli Random Variable. Let

$$
X_i
=
\begin{cases}
1, & \text{if trial } i \text{ is a success},\\
0, & \text{if trial } i \text{ is a failure}.
\end{cases}
$$

Then

$$
P(X_i=1)=p
$$

and

$$
P(X_i=0)=q=1-p.
$$

The total number of successes is

$$
X
=
X_1+X_2+\cdots+X_n.
$$

Thus,

$$
X
=
\sum_{i=1}^{n}X_i.
$$

Expected Value of One Trial. The expected value of a discrete random variable is

$$
E[X_i]
=
\sum_x xP(X_i=x).
$$

Since $X_i$ can take only the values $0$ and $1$,

$$
E[X_i]
=
(0)P(X_i=0)
+
(1)P(X_i=1).
$$

Substituting the probabilities gives

$$
E[X_i]
=
(0)q+(1)p.
$$

Therefore,

$$
E[X_i]
=
p.
$$

Expected Value of the Binomial Distribution. Since

$$
X
=
\sum_{i=1}^{n}X_i,
$$

linearity of expectation gives

$$
E[X]
=
\sum_{i=1}^{n}E[X_i].
$$

Since every trial has expected value $p$,

$$
E[X]
=
\sum_{i=1}^{n}p.
$$

Therefore,

$$
E[X]
=
np.
$$

Thus the mean of the binomial distribution is

$$
\boxed{
\mu=np
}.
$$

Variance. The variance of a random variable is

$$
\operatorname{Var}(X)
=
E\left[(X-E[X])^2\right].
$$

An equivalent form is

$$
\operatorname{Var}(X)
=
E[X^2]
-
(E[X])^2.
$$

We first find the variance of one Bernoulli trial.

Variance of One Trial. Since

$$
X_i
\in
\{0,1\},
$$

squaring either possible value leaves it unchanged:

$$
X_i^2
=
X_i.
$$

Therefore,

$$
E[X_i^2]
=
E[X_i].
$$

Since

$$
E[X_i]
=
p,
$$

we obtain

$$
E[X_i^2]
=
p.
$$

Now use

$$
\operatorname{Var}(X_i)
=
E[X_i^2]
-
(E[X_i])^2.
$$

Substituting,

$$
\operatorname{Var}(X_i)
=
p-p^2.
$$

Factoring,

$$
\operatorname{Var}(X_i)
=
p(1-p).
$$

Since

$$
q=1-p,
$$

we obtain

$$
\boxed{
\operatorname{Var}(X_i)
=
pq
}.
$$

Variance of the Sum. The binomial random variable is

$$
X
=
X_1+X_2+\cdots+X_n.
$$

In general,

$$
\operatorname{Var}
\left(
X_1+\cdots+X_n
\right)
=
\sum_{i=1}^{n}
\operatorname{Var}(X_i)
+
2
\sum_{i<j}
\operatorname{Cov}(X_i,X_j).
$$

where

- $\operatorname{Cov}(X_i,X_j)$ is the covariance between trials $i$ and $j$.

The binomial model requires the trials to be independent.

For independent random variables,

$$
\operatorname{Cov}(X_i,X_j)
=
0.
$$

Therefore,

$$
\operatorname{Var}(X)
=
\sum_{i=1}^{n}
\operatorname{Var}(X_i).
$$

Each Bernoulli trial has variance

$$
\operatorname{Var}(X_i)
=
pq.
$$

Thus,

$$
\operatorname{Var}(X)
=
\sum_{i=1}^{n}pq.
$$

There are $n$ identical terms, so

$$
\operatorname{Var}(X)
=
npq.
$$

Since

$$
q=1-p,
$$

this may also be written

$$
\boxed{
\operatorname{Var}(X)
=
np(1-p)
}.
$$

Standard Deviation. Standard deviation is defined as the positive square root of variance:

$$
\sigma
=
\sqrt{\operatorname{Var}(X)}.
$$

Since

$$
\operatorname{Var}(X)
=
npq,
$$

we obtain

$$
\sigma
=
\sqrt{npq}.
$$

Since

$$
q=1-p,
$$

we obtain

$$
\boxed{
\sigma
=
\sqrt{np(1-p)}
}.
$$

Therefore,

$$
\boxed{
X\sim\operatorname{Bin}(n,p)
\qquad\Longrightarrow\qquad
\mu=np,
\qquad
\sigma^2=np(1-p),
\qquad
\sigma=\sqrt{np(1-p)}
}.
$$

Direct Derivation of the Variance. The same result can be derived by expanding the square of the sum.

Since

$$
X
=
\sum_{i=1}^{n}X_i,
$$

we have

$$
X^2
=
\left(
\sum_{i=1}^{n}X_i
\right)^2.
$$

Expanding,

$$
X^2
=
\sum_{i=1}^{n}X_i^2
+
2
\sum_{i<j}X_iX_j.
$$

Taking expectations,

$$
E[X^2]
=
\sum_{i=1}^{n}E[X_i^2]
+
2
\sum_{i<j}E[X_iX_j].
$$

Because

$$
X_i^2=X_i,
$$

we have

$$
E[X_i^2]
=
p.
$$

Because different trials are independent,

$$
E[X_iX_j]
=
E[X_i]E[X_j].
$$

Therefore,

$$
E[X_iX_j]
=
p^2.
$$

There are

$$
\binom{n}{2}
=
\frac{n(n-1)}{2}
$$

pairs of distinct trials.

Thus,

$$
E[X^2]
=
np
+
2
\left(
\frac{n(n-1)}{2}
\right)
p^2.
$$

Therefore,

$$
E[X^2]
=
np+n(n-1)p^2.
$$

The variance is

$$
\operatorname{Var}(X)
=
E[X^2]
-
(E[X])^2.
$$

Since

$$
E[X]
=
np,
$$

we obtain

$$
\operatorname{Var}(X)
=
np+n(n-1)p^2-n^2p^2.
$$

Expanding,

$$
\operatorname{Var}(X)
=
np
+
n^2p^2
-
np^2
-
n^2p^2.
$$

The $n^2p^2$ terms cancel:

$$
\operatorname{Var}(X)
=
np-np^2.
$$

Factoring,

$$
\operatorname{Var}(X)
=
np(1-p).
$$

Hence,

$$
\boxed{
\operatorname{Var}(X)
=
npq
}.
$$

Taking the square root,

$$
\boxed{
\sigma
=
\sqrt{npq}
=
\sqrt{np(1-p)}
}.
$$

Relation to the Normal Approximation. For a binomial random variable,

$$
\mu=np
$$

and

$$
\sigma^2=npq.
$$

Therefore, standardization gives

$$
Z
=
\frac{X-\mu}{\sigma}.
$$

Substituting the binomial mean and standard deviation,

$$
\boxed{
Z
=
\frac{X-np}{\sqrt{npq}}
}.
$$

This is the scaling that appears in the de Moivre-Laplace theorem and in the normal approximation to the binomial distribution.

Hence,

$\displaystyle
X\sim\operatorname{Bin}(n,p)
\quad\Longrightarrow\quad
E[X]=np,
\qquad
\operatorname{Var}(X)=npq,
\qquad
\operatorname{SD}(X)=\sqrt{npq}.
$

## References

1. Ross, S. M. *A First Course in Probability*. 10th ed. Pearson, 2019. §4.5, “Variance” — definition and properties of variance; §4.6, “The Bernoulli and Binomial Random Variables” — Bernoulli and binomial random variables, including their means and variances.

2. Blitzstein, J. K., & Hwang, J. *Introduction to Probability*. 2nd ed. CRC Press, 2019. Chapter 4, Example 4.6.5, “Binomial variance” — derives $\operatorname{Var}(X)=np(1-p)$ by expressing a binomial random variable as a sum of independent indicator random variables.

3. Devore, J. L., & Berk, K. N. *Modern Mathematical Statistics with Applications*. 2nd ed. Springer, 2012. Chapter 3, “Discrete Random Variables and Probability Distributions” — binomial random variables and their expected values and variances.

4. Larsen, R. J., & Marx, M. L. *An Introduction to Mathematical Statistics and Its Applications*. 5th ed. Pearson, 2012. Discrete random variables and binomial distributions — derivation and use of the binomial mean $np$ and variance $np(1-p)$.