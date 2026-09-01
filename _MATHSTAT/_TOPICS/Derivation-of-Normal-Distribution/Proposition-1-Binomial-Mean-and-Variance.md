# Proposition 1: Binomial Mean and Variance

<!-- pdf-page-width: wide -->

Proposition. If

$$
\begin{align*}
X_n
&\sim
\operatorname{Bin}(n,p),
\qquad
q=1-p,
\tag*{\just{Assume a binomial random variable}}
\end{align*}
$$

then

$$
\begin{align*}
E[X_n]
&=
np
\\
\operatorname{Var}(X_n)
&=
npq
\tag*{\just{Mean and variance of the binomial distribution}}
\end{align*}
$$

Proof. Write the binomial count as a sum of Bernoulli indicators.

$$
\begin{align*}
X_n
&=
\sum_{i=1}^{n}X_i
\tag*{\just{Each $X_i$ records success or failure on trial $i$}}
\\[0.45em]
E[X_i]
&=
p
\tag*{\just{Mean of a Bernoulli random variable}}
\\[0.45em]
\operatorname{Var}(X_i)
&=
p(1-p)
\\
&=
pq
\tag*{\just{Variance of a Bernoulli random variable}}
\\[0.45em]
E[X_n]
&=
E\left[
\sum_{i=1}^{n}X_i
\right]
\\
&=
\sum_{i=1}^{n}
E[X_i]
\\
&=
np
\tag*{\just{Apply linearity of expectation}}
\\[0.45em]
\operatorname{Var}(X_n)
&=
\operatorname{Var}
\left(
\sum_{i=1}^{n}X_i
\right)
\\
&=
\sum_{i=1}^{n}
\operatorname{Var}(X_i)
\\
&=
npq
\tag*{\just{Independence makes the variances additive}}
\\[0.45em]
\mu
&=
np
\\
\sigma^2
&=
npq
\\
\sigma
&=
\sqrt{npq}
\tag*{\just{Introduce the binomial mean and standard deviation}}
\end{align*}
$$

$\square$
