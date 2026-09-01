# Definition 1: Binomial Distribution

<!-- pdf-page-width: wide -->

Definition. A binomial random variable $X_n$ with parameters $n$ and $p$ is written

$$
\begin{align*}
X_n
&\sim
\operatorname{Bin}(n,p)
\tag*{\just{$X_n$ counts successes in $n$ independent Bernoulli trials}}
\\[0.45em]
q
&=
1-p
\tag*{\just{$q$ is the probability of failure}}
\\[0.45em]
P(X_n=k)
&=
\binom{n}{k}
p^kq^{n-k}
\tag*{\just{Probability of exactly $k$ successes}}
\\[0.45em]
&=
\frac{n!}{k!(n-k)!}
p^kq^{n-k}
\tag*{\just{Expand the binomial coefficient}}
\end{align*}
$$

for

$$
\begin{align*}
k
&=
0,1,\ldots,n
\\
0
&\leq
p
\leq
1
\tag*{\just{Parameter and support conditions}}
\end{align*}
$$
