# Point Estimation

We've already defined what are parameters and statistics.

Point estimation is the process by which the value of a parameter or statistic is, well, estimated.


Note the following notations,

| Symbol | Meaning |
|-|-|
| $\theta$ | Parameter |
| $\hat{\theta}$ | Point Estimate of $\theta$ |

## The Quality of a Point Estimate




1. **Bias**: The difference between the expected value of the estimator and the true parameter.
   
2. **Variance**: Variance about the mean of the estimator.
   
3. **Mean Squared Error (MSE)**: Combine bias and variance to evaluate overall estimation error.

4. **Consistency**: Ensure the estimate converges to the true parameter as the sample size increases.

5. **Efficiency**: Compare the variance of the estimator to that of the best possible estimator (Cramér-Rao lower bound).

6. **Asymptotic Normality**: Check if the distribution of the estimator approaches normality as sample size grows.

7. **Robustness**: Evaluate how sensitive the estimator is to deviations from assumptions or outliers.



### Variance [2, pp. 718]

The variance of the point estimate, $\bar{Y}$, is given by
$$\text{Var}(\overline{Y}) = \dfrac{\sigma^2}{n} \qquad (1)$$

Here we show the derivation of $(1)$

Given, 

$\text{Var}(\overline{Y})$ 

By definition of $\bar{Y}$,

$ =\text{Var}\left(\dfrac{1}{n} \displaystyle \sum_{i=1}^{n} Y_i\right)$ 


$ =\left(\dfrac{1}{n^2}\right) \text{Var} \left(\displaystyle \sum_{i=1}^{n} Y_i\right) $

$= \left(\dfrac{1}{n^2}\right) \left( \displaystyle \sum_{i=1}^{n} \text{Var}(Y_i) \right)$

$= \left(\dfrac{1}{n^2}\right) \left( \displaystyle \sum_{i=1}^{n} \sigma^2 \right)$ 

$= \left(\dfrac{1}{n^2}\right)(n\sigma^2)$

$= \dfrac{\sigma^2}{n}$$

<br/>

## References:

[1] L. Wasserman, *All of Statistics*. 2nd ed. New York: Springer, 2005.
[2] J. M. Wooldridge, *Introductory Econometrics: A Modern Approach*, 7th ed. Boston: Cengage Learning, 2020.