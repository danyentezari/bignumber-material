# Probability Density

1. **Short definition**: Value of the probability density function (PDF) at a point.

2. **Long definition**: Probability density refers to the value of the probability density function (PDF) at a specific point for a continuous random variable. It gives the relative likelihood of the random variable being near that point but does not represent actual probabilities. For a continuous variable $X$, the probability density at $x$ is $f(x)$. The probability that $X$ falls within an interval is found by integrating $f(x)$ over that interval:

$$P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx$$

3. **Related subtopics**:
   - 4 Probability Density Function (PDF)
   - 4 Cumulative Distribution Function (CDF)
   - 4 Continuous Random Variable
   - 4 Integration of PDF

4. **Propositions in LaTeX**: None.

5. **Theorems in LaTeX**: None.

6. **Example 1**: For a standard normal distribution with PDF $f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$, the probability density at $x = 0$ is:

$$f(0) = \frac{1}{\sqrt{2\pi}} \approx 0.3989$$

This value indicates the relative likelihood of $X$ being near zero.

7. **Example 2**: For an exponential distribution with rate $\lambda = 2$, the probability density at $x = 1$ is:

$$f(1) = 2 e^{-2(1)} = 2 e^{-2} \approx 0.2707$$

This shows the relative likelihood of the random variable being near $x = 1$.