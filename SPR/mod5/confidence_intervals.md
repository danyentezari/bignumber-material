# Confidence Interval Estimation

1. **Short definition**: Range of values estimating a population parameter.

2. **Long definition**: Confidence interval estimation provides a range of values, calculated from sample data, that is likely to contain the true population parameter with a specified confidence level (e.g., 95%). It reflects the uncertainty in the estimate.

3. **Related subtopics**:
   - 4 Confidence Level
   - 4 Margin of Error
   - 4 Confidence Interval for Population Mean
   - 4 Confidence Interval for Proportions
   - 4 Large Sample Confidence Intervals
   - 4 Small Sample Confidence Intervals

4. **Propositions in LaTeX**: None.

5. **Theorems in LaTeX**: None.

6. **Example 1**: A researcher wants to estimate the average height of a population of students. A random sample of 50 students is taken, yielding a sample mean height of 170 cm and a standard deviation of 5 cm. Using a 95% confidence interval and applying the formula for large samples:

$$CI = \bar{X} \pm Z_{\alpha} \frac{\sigma}{\sqrt{n}}$$

where $\bar{X}$ is the sample mean, $Z_{\alpha/2}$ is the z-value corresponding to the 95% confidence level, $\sigma$ is the standard deviation, and $n$ is the sample size, the researcher calculates that the population mean height lies between 168.6 cm and 171.4 cm.

7. **Example 2**: A company wants to estimate the proportion of customers satisfied with a new product. From a random sample of 200 customers, 160 express satisfaction. Using a 95% confidence level, the confidence interval for the population proportion is calculated using:

$$CI = \hat{p} \pm Z_{\alpha/2} \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$$

where $\hat{p}$ is the sample proportion, $Z_{\alpha/2}$ is the z-value for 95% confidence, and $n$ is the sample size. The calculated interval suggests that the true population proportion of satisfied customers is between 0.74 and 0.86, providing a range for the company's estimate.