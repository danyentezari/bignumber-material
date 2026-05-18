# Moments

1. **Short definition**: Quantities describing the shape of a distribution.

2. **Long definition**: Moments are statistical measures that provide information about the shape and characteristics of a probability distribution. They are derived from the expected values of powers of the random variable. For a random variable $X$ with probability density function $f(x)$, the $n$-th moment about the origin is given by:

$$\mu'_n = E[X^n] = \displaystyle\int_{-\infty}^{\infty} x^n f(x) \, dx$$

The $n$-th central moment is the expected value of $(X - \mu)^n$, where $\mu$ is the mean of $X$:

$$\mu_n = E[(X - \mu)^n]$$

Moments include measures like the mean, variance, skewness, and kurtosis, which describe the central tendency, spread, asymmetry, and peakedness of the distribution, respectively.

1. **Related subtopics**:
   - 4 Mean
   - 4 Variance
   - 4 Skewness
   - 4 Kurtosis
   - 4 Central Moments
   - 4 Moment Generating Function

2. **Propositions in LaTeX**: None.

3. **Theorems in LaTeX**: None.

4. **Example 1**: For a discrete random variable $X$ with possible values 1, 2, and 3, and corresponding probabilities 0.2, 0.5, and 0.3, the first moment (mean) is calculated as:

$$E[X] = \sum_{i=1}^{3} x_i \cdot P(X = x_i) = 1 \cdot 0.2 + 2 \cdot 0.5 + 3 \cdot 0.3 = 2.1$$

The variance, which is the second central moment, is:

$$Var(X) = E[(X - E[X])^2] = \sum_{i=1}^{3} (x_i - 2.1)^2 \cdot P(X = x_i) = 0.81$$

7. **Example 2**: For a continuous random variable $X$ with a uniform distribution on the interval [0, 1], the $n$-th moment about the origin is:

$$E[X^n] = \displaystyle \int_{0}^{1} x^n \, dx = \dfrac{1}{n+1}$$

For example, the second moment about the origin is:

$$E[X^2] = \dfrac{1}{3}$$

The variance of this uniform distribution is:

$$Var(X) = E[X^2] - (E[X])^2 = \dfrac{1}{12}$$