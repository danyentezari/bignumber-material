# Moments

A power-average of a random variable that is used to summarize location, spread, asymmetry, and tail weight of a probability distribution, where a random variable is a measurable function from a sample space to the real line, and where a probability distribution is a rule that assigns probability to sets of outcomes.

Note: Also called moments about the origin when the powers are uncentered.

Raw moment. The $k$th raw moment of $X$ is $E[X^k]$, provided $E[|X|^k]$ is finite. This principle is used to extract successive power averages from a distribution.

The $k$th raw moment is

$$
\mu_k'
=
E[X^k]
$$

where

- $X$ is a random variable.
- $k$ is a positive integer.
- $\mu_k'$ is the $k$th moment about the origin.

Central moment. The $k$th central moment of $X$ is $E[(X-\mu)^k]$, where $\mu=E[X]$ is finite. This principle is used to measure shape after centering at the mean.

The $k$th central moment is

$$
\mu_k
=
E[(X-\mu)^k]
$$

where

- $\mu=E[X]$ is the mean of $X$.
- $\mu_k$ is the $k$th central moment.

Mean. The mean is the first raw moment $E[X]$. The first central moment is $0$ whenever it exists. This principle is used to locate the center of mass of a distribution.

Variance. The variance is the second central moment $E[(X-\mu)^2]$. It equals $E[X^2]-(E[X])^2$. This principle is used to measure spread about the mean.

The variance is

$$
\mathrm{Var}(X)
=
E[(X-\mu)^2]
=
E[X^2]-(E[X])^2
$$

where

- $\mathrm{Var}(X)$ is the variance of $X$.
- $\mu=E[X]$ is the mean.

Skewness. Skewness is the third standardized moment $E[((X-\mu)/\sigma)^3]$, where $\sigma$ is the standard deviation. Positive skewness means a long right tail. This principle is used to quantify asymmetry.

The skewness is

$$
\gamma_1
=
\frac{E[(X-\mu)^3]}{\sigma^3}
$$

where

- $\sigma=\sqrt{\mathrm{Var}(X)}$ is the standard deviation.
- $\gamma_1$ is the skewness of $X$.

Kurtosis. Kurtosis is the fourth standardized moment minus $3$. A normal law then has kurtosis $0$. This principle is used to compare tail weight with the normal distribution.

Note: Also called excess kurtosis.

The kurtosis is

$$
\mathrm{Kurt}(X)
=
\frac{E[(X-\mu)^4]}{\sigma^4}-3
$$

where

- $\mathrm{Kurt}(X)$ is the kurtosis of $X$.

Moment generating function. The MGF of $X$ is $M(t)=E[e^{tX}]$ when this is finite on an open interval containing $0$. Then $E[X^k]=M^{(k)}(0)$. This principle is used to recover raw moments by differentiation.

The moment generating function is

$$
M(t)
=
E[e^{tX}]
$$

where

- $t$ is a real argument.
- $M$ is the moment generating function of $X$.

Uniqueness. If two random variables have the same MGF on a neighborhood of $0$, they have the same distribution. A full sequence of moments need not determine a law. This principle is used to identify distributions from MGFs and to recognize indeterminate moment problems.

<!--
## Elementary Example

### Simple

Let $X\sim\mathrm{Bin}(n,p)$. Then $M_X(t)=(pe^{t}+1-p)^n$.

### General

Differentiating the MGF and evaluating at $t=0$ yields $E[X]=np$ and $E[X^2]=n(n-1)p^2+np$. The variance identity then gives $\mathrm{Var}(X)=np(1-p)$. Skewness vanishes when $p=1/2$.

The binomial MGF is

$$
M_X(t)
=
(pe^{t}+1-p)^{n}
$$

where

- $n$ is the number of trials.
- $p$ is the success probability.
-->

## Problems

- Compute the first four raw moments of a specified distribution. [ChatGPT]
- Derive mean and variance from the first two raw moments. [ChatGPT]
- Compute skewness and excess kurtosis of Gamma and Beta random variables.
- Recover mean and variance by differentiating a moment generating function.
- Prove distinct densities can share all moments, so a moment sequence need not determine a law.
- Show that an MGF in a neighborhood of $0$ determines the distribution. [ChatGPT]
- Express the fourth central moment in terms of lower raw moments.

# References

1. Chakraborti, S., and Gibbons, J. D. *Nonparametric Statistical Inference*. Chapter 1, p. 9 — $\mu_k'=E(X^k)$ and $\mu_2=\mathrm{var}(X)=E(X^2)-\mu^2$.
2. Casella, G., and Berger, R. L. *Statistical Inference*. Chapter 2, §2.3, p. 48 — moments; pp. 53–54 — binomial MGF, Example 2.3.10 nonunique moments, Theorem 2.3.11 MGF uniqueness; p. 61 — normal MGF derivatives.
3. Schay, G. *Introduction to Probability with Statistical Applications*. Chapter 6, Definition 6.3.1, p. 201 — $k$th moment and $k$th central moment.
4. Ash, R. B. *Basic Probability Theory*. Chapter 3, §3.2, pp. 108–109 — central moments $\beta_k=E[(R-m)^k]$ and fourth central moment in raw moments.
5. Ash, R. B., and Doléans-Dade, C. A. *Probability & Measure Theory*. 2nd ed., Academic Press, 1999. Chapter 4, §4.10, p. 176 — mean as first moment, first central moment $0$, variance as second central moment.
6. Blitzstein, J. K., and Hwang, J. *Introduction to Probability*. Chapman & Hall/CRC, 2014. Chapter 6, §6.1, p. 249 — mean as center of mass; §6.2, pp. 250–251 — skewness and kurtosis; §6.4, Definition 6.4.1, p. 256 — MGF; Theorem 6.4.6, p. 257 — MGF determines the distribution; p. 258 — negative binomial MGF; p. 280 — Gamma and Beta skewness and kurtosis.
7. Gut, A. *Probability: A Graduate Course*. Springer, 2005. Chapter 4, §6, pp. 185–186 — skewness $\gamma_1$ and coefficient of excess $\gamma_2$; §8, Theorem 8.3, p. 191 — $EX^n=\psi_X^{(n)}(0)$ when the MGF exists near $0$.
8. Billingsley, P. *Probability and Measure*. §9, Example 9.2, p. 147 — binomial generating function.
