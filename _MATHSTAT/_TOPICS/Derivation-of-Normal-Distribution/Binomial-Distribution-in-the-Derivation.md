# Binomial Distribution

<!-- pdf-page-width: wide -->

$$
\begin{align*}
X_n
&\sim
\operatorname{Bin}(n,p)
\tag*{\just{$X_n$ is a binomial random variable}}
\\[0.6em]
q
&=
1-p
\tag*{\just{$q$ is the probability of failure}}
\\[0.6em]
P(X_n=k)
&=
\binom{n}{k}p^kq^{n-k}
\tag*{\just{Probability of exactly $k$ successes}}
\\[0.6em]
&=
\frac{n!}{k!(n-k)!}p^kq^{n-k}
\tag*{\just{Expand the binomial coefficient}}
\\[0.6em]
\mu
&=
np
\tag*{\just{Mean of the binomial distribution}}
\\[0.6em]
\sigma^2
&=
npq
\tag*{\just{Variance of the binomial distribution}}
\\[0.6em]
\sigma
&=
\sqrt{npq}
\tag*{\just{Standard deviation}}
\end{align*}
$$