# Density to Probability

1. **Short definition**: Converting density functions to probability values.

2. **Long definition**: Converting density functions to probability values involves integrating the probability density function (PDF) over a specified range to obtain the probability of a random variable falling within that range. For a continuous random variable $X$ with PDF $f(x)$, the probability that $X$ falls within the interval $[a, b]$ is given by:

$$P(a \leq X \leq b) = \int_{a}^{b} f(x) \, dx$$

This process uses the area under the PDF curve within the interval to determine the likelihood of the random variable's values falling within that range.

3. **Related subtopics**:
   - 4 Probability Density Function (PDF)
   - 4 Cumulative Distribution Function (CDF)
   - 4 Integration of PDF
   - 4 Area Under Curve

4. **Propositions in LaTeX**: None.

5. **Theorems in LaTeX**: None.

6. **Example 1**: For a continuous random variable $X$ with a PDF $f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$, representing a standard normal distribution, to find the probability that $X$ falls between -1 and 1, integrate the PDF from -1 to 1:

$$P(-1 \leq X \leq 1) = \int_{-1}^{1} \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} \, dx$$

This integral equals approximately 0.6826, indicating the probability that $X$ falls within this interval.

7. **Example 2**: Suppose a random variable $X$ has an exponential distribution with a rate parameter $\lambda = 1$. The PDF is $f(x) = e^{-x}$. To find the probability that $X$ is less than 3, integrate the PDF from 0 to 3:

$$P(X \leq 3) = \int_{0}^{3} e^{-x} \, dx$$

Evaluating this integral gives:

$$P(X \leq 3) = 1 - e^{-3} \approx 0.9502$$

This result indicates the probability that $X$ will be less than or equal to 3.