### Unbiased Estimation for Sample Variance

<br/>

$$s^2 = \dfrac{  \sum_{i=1}^{n} (x_{i} - \bar{x})^2 }{n-1}$$

<br/>

Suppose we have this table of values, with $\bar{x} = 4.6$.

| | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | 
|-|-|-|-|-|
| 1 | 2.6 | -2 | 4|
| 2 | 6.6 | 2 | 4 |
| 3 | 3.6 | -1 | 1 |
| 4 | 5.6 | 1 | 1 |
| 5 | 6.6 | 3 | 9 |
| 6 | 1.6 | -3 | 9 |
| **total** | 26.6 | 0 | 154.96 |

<br/>

Notice that the sum of the differences of $x_i$ and $\bar{x}$ add up to 0.

<br/>

Now, suppose we take the same table but imagine the 6th value to be unknown. We still know $\bar{x}$ and assume that is it an unbiased estimator of the population mean average, $\mu$. 

| | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ | 
|-|-|-|-|-|
| 1 | 2.6 | -2 | 4|
| 2 | 6.6 | 2 | 4 |
| 3 | 3.6 | -1 | 1 |
| 4 | 5.6 | 1 | 1 |
| 5 | 6.6 | 3 | 9 |
| 6 | ??? | ??? | ??? |
| **total** | 26.6 | 0 | 154.96 |

<br/>

**Degree of Freedom**

If we take the sum of the $n-1$ values, assuming the $n$th to be unknown, then we have

$$ \sum_{i=1}^{n-1} (x_{i} - \bar{x}) = 3$$

If we know $\bar{x} = 4.6$ and $\sum_{i=1}^{n-1} (x_{i} - \bar{x}) = 3$, then other value could possible determine total of the sum of the differences, which is 0?

The answer is one: $-3$.

There is only one number we are free to choose and that could determine the sum of the differences to be 0.

Thus, $n-1$ in the sample variance formula is said to degree of freedom $= 1$.

<br/>

**Unbiased Estimation**

The pupose $\bar{x}$ to estimate $\mu$.

If this is the case, then $\bar{x}$ must accurately (as much as possible) represent the magnitute of variance in the population.


