# Probability Distribution Function

1. **Short definition**: Functions describing probabilities of random variables.

2. **Long definition**: Probability distribution functions describe the probability structure of random variables. There are three main types:
   - **Cumulative Distribution Function (CDF)**: Gives the probability that a random variable is less than or equal to a certain value. For a random variable $ X $, it is defined as $ F(x) = P(X \leq x) $.
   - **Probability Mass Function (PMF)**: For discrete random variables, it gives the probability that the variable takes a specific value. For a discrete random variable $ X $, it is $ p(x) = P(X = x) $.
   - **Probability Density Function (PDF)**: For continuous random variables, it describes the likelihood of the variable falling within a particular range. The probability of the variable being exactly at a specific value is zero. For a continuous random variable $ X $, it is $ f(x) $, and the probability that $ X $ falls in the interval $[a, b]$ is given by $ \int_a^b f(x) \, dx $.

3. **Related subtopics**:
   - 4 Cumulative Distribution Function (CDF)
     - 5 Properties of CDF
   - 4 Probability Mass Function (PMF)
     - 5 Properties of PMF
   - 4 Probability Density Function (PDF)
     - 5 Properties of PDF
   - 4 Relationship between CDF, PMF, and PDF

4. **Propositions in LaTeX**:
   - Cumulative Distribution Function (CDF):
     $$F(x) = P(X \leq x)$$
   - Probability Mass Function (PMF):
     $$p(x) = P(X = x) $$
   - Probability Density Function (PDF):
     $$ \int_{-\infty}^x f(t) \, dt = F(x) $$

5. **Theorems in LaTeX**: None.

6. **Example 1**: For a discrete random variable representing the roll of a fair die, the PMF is $ p(x) = \frac{1}{6} $ for $ x = 1, 2, 3, 4, 5, 6 $. The CDF for $ x \leq 3 $ is $ F(x) = \frac{3}{6} = 0.5 $, representing the probability of rolling a 3 or less.

7. **Example 2**: For a continuous random variable representing the height of adult males, suppose the height follows a normal distribution with a mean of 70 inches and a standard deviation of 3 inches. The PDF is given by:
   $$ f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}}$$
   
   where $ \mu = 70 $ and $ \sigma = 3 $. The CDF can be computed as the integral of the PDF from $-\infty$ to $x$, providing the probability that a randomly selected individual has a height less than or equal to $x$.