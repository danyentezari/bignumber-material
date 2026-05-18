# Confidence Intervals in Regression

1. **Short definition**: Range of likely values for regression parameters.

2. **Long definition**: Confidence intervals in regression provide a range of values within which the true regression parameters (like slope and intercept) are likely to fall, with a certain confidence level (e.g., 95%). For each estimated parameter, the confidence interval is calculated as:

$$\hat{\beta}_i \pm t_{\alpha/2, n-p} \cdot SE(\hat{\beta}_i)$$

where $\hat{\beta}_i$ is the estimated coefficient, $t_{\alpha/2, n-p}$ is the critical value, and $SE(\hat{\beta}_i)$ is the standard error.

3. **Related subtopics**:
   - 4 Linear Regression
   - 4 Confidence Level
   - 4 Standard Error of Estimate
   - 4 Hypothesis Testing in Regression
   - 4 Prediction Intervals

4. **Propositions in LaTeX**: None.

5. **Theorems in LaTeX**: None.

6. **Example 1**: In a simple linear regression model $Y = \beta_0 + \beta_1 X + \epsilon$, suppose the estimated slope is $\hat{\beta}_1 = 2.5$ with a standard error of $0.5$, and the 95% confidence interval is:

$$2.5 \pm 1.96 \cdot 0.5 = [1.52, 3.48]$$

This means we are 95% confident that the true slope $\beta_1$ lies between 1.52 and 3.48.

7. **Example 2**: For a multiple regression model with predictors $X_1$ and $X_2$, if the coefficient for $X_1$ is estimated as $\hat{\beta}_1 = 1.2$ with a standard error of $0.3$, and a critical value of $t = 2.04$ for a 95% confidence level, the confidence interval for $\beta_1$ is:

$$1.2 \pm 2.04 \cdot 0.3 = [0.588, 1.812]$$

Thus, we are 95% confident that the true value of $\beta_1$ lies within this range.