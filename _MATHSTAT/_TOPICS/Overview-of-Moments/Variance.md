# Variance

The function for variance is given by
$$ Var(X) = E(X-\mu)^2 = \sigma^2 $$
where 

- $X$ is a random variable
- $\mu$ is the mean average of the random variable

Variance is a measurement of the spread of values of the random variable about the mean. Note that the square root of variance is the standard deviation. In other words, to arrive at the standard deviation of a random variable, the variance must first be calculated. Also, variance can be expressed as

$$ Var(X) = E[X^2] - (E[X])^2  $$
where

- $E[X^2] = \begin{cases} \sum_{i}^{k} x_i \cdot f(x_i)^2 \enspace ; \quad \text{ if } X \text{ is discrete} \\ \\ \int_{-\infty}^{\infty} x_i \cdot f(x_i)^2 \: dx_i \enspace ; \quad \text{ if } X \text{ is continuous} \end{cases}$

Note, the expression $E[X^2]$ means that the probability function in the function of expected value is squared!
