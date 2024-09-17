# Moments

Quantities describing the shape of a distribution.

Moments are statistical measures that provide information about the shape and characteristics of a probability distribution. They are derived from the expected values of powers of the random variable. For a random variable $X$ with probability density function $f(x)$, the $n$-th moment about the origin is given by:

Suppose the *probability distribution* of a *random variable*, \( X \), the number of points earned on a short quiz, is given by:

| \( x \)   | 0   | 1   | 2   | 3   |
|-----------|-----|-----|-----|-----|
| \( p(x) \) | 0.1 | 0.2 | 0.3 | 0.4 |

The first *moment* about \( 0 \) is the *mean*:

$$ \mu = E(X) = \sum_{i = 0}^{|X|} e^{xt_i} \cdot p(x_i) $$

Note that \( e^x \) corresponds to the *Maclaurin series*:

$$ e^{x} = \sum_{i=0}^{|X|} \frac{x^i}{i!} = \frac{x^0}{0!} + \frac{x^1}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots + \frac{x^{|X|}}{|X|!} $$

The first *moment* about \( 0 \) is the *mean*:

$$ \mu = E(X) = \sum_{i = 0}^{|X|} e^{xt} \cdot p(x) = M_X(t=0) $$

Writing out the summation expression gives:

$$ \sum_{i=0}^{|X|} e^{xt} \cdot p(x) = e^{x_1t} \cdot p(x) + e^{x_2t} \cdot p(x) + \dots + e^{x_{|X|}t} \cdot p(x_{|X|}) $$

Deriving the terms gives:

$$ \frac{d}{dx} \sum_{i=0}^{|X|} e^{xt} \cdot p(x) = x_1e^{x_1t} \cdot p(x) + x_2e^{x_2t} \cdot p(x) + \dots + x_{|X|}e^{x_{|X|}t} \cdot p(x_{|X|}) $$

Now, let's apply what we understand to find the first moment for this *probability distribution*:

$$ M_X(t=0) = \sum_{i = 0}^{|X|} e^{x_it} \cdot p(x) \\ = x_1e^{x_1t} \cdot p(x) + x_2e^{x_2t} \cdot p(x) + \dots + x_{|X|}e^{x_{|X|}t} \cdot p(x_{|X|}) \\ = (0)(0.1) + (1)(0.2) + (2)(0.3) + (3)(0.4) = 2 $$

The second moment about the mean is the variance:

$$ \sigma^2 = E[(X - \mu)^2] = \sum_{i = 0}^{|X|}(x - \mu)^2 \cdot p(x) $$

The third moment about the mean is the *skewness*, the lack of *symmetry* about the *mean*:

$$ E[(X - \mu)^3] = \sum_{i = 0}^{|X|}(x - \mu)^3 \cdot p(x) \\ = (0 - 2)^3 (0.1) + (1 - 2)^3 (0.2) + (2 - 2)^3 (0.3) + (3 - 2)^3 (0.4) = -0.5 $$

To make the value of this measure independent of a particular scale (e.g., inch, cm, etc.), the third *moment* about the *mean* is divided by:

$$ \frac{E[(X - \mu)^3]}{\sigma^3} = E \left[ \left( \frac{(X - \mu)}{\sigma} \right)^3 \right] $$

The fourth *moment* about the *mean* is the *kurtosis*, which is the measure of the *peakness* of the *bell curve*:

$$ \frac{E[(X - \mu)^4]}{\sigma^4} $$

Therefore:

$$ \frac{E[(X - \mu)^4]}{\sigma^4} = \sum_{x \in D = 1}^{|X|} \frac{(X - \mu)^4}{\sigma^4} \cdot p(x) $$

## Moment Exercise

For a new car, the number of defects \( X \) has the *probability distribution* given by the accompanying table.

| \( x \)   | 0   | 1   | 2   | 3   | 4   | 5   | 6   |
|-----------|-----|-----|-----|-----|-----|-----|-----|
| \( p(x) \) | 0.04| 0.20| 0.34| 0.20| 0.15| 0.04| 0.03|

Find \( M_X(t) \) and use it to find \( E(X) \) and \( V(X) \).

**Answer:**

First, we consider the formula of the *moment generating function*:

$$ M_X(t) = E(e^{tX}) = \sum_{x \in D} e^{tX} \cdot p(x) $$

$$ E[X] = M_X'(t=0) = (0.04)(0) + (0.20)(1) + (0.34)(2) + (0.20)(3) + (0.15)(4) + (0.04)(5) + (0.03)(6) = 2.46 $$

$$ E[X^2] = M_X''(t=0) = (0.04)(0)^2 + (0.20)(1)^2 + (0.34)(2)^2 + (0.20)(3)^2 + (0.15)(4)^2 + (0.04)(5)^2 + (0.03)(6)^2 = 7.84 $$

$$ V[X] = E[X^2] - (E[X])^2 = 7.84 - (2.46)^2 = 1.7884 $$