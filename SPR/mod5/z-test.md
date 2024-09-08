# z-Test

1. **Short definition**: Hypothesis test comparing sample means to population mean.

2. **Long definition**: A z-test is used to determine whether there is a significant difference between a sample mean and a population mean or between two sample means. It assumes a large sample size or known population variance. The test statistic is calculated as:
   \[
   z = \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}}
   \]
   where \( \bar{X} \) is the sample mean, \( \mu \) is the population mean, \( \sigma \) is the population standard deviation, and \( n \) is the sample size.

3. **Related subtopics**:
   - 4 Types of z-Test
     - 5 One-Sample z-Test
     - 5 Two-Sample z-Test
   - 4 Assumptions of z-Test
     - 5 Large Sample Size
     - 5 Known Population Variance
   - 4 z-Test vs t-Test

4. **Propositions in LaTeX**: None.

5. **Theorems in LaTeX**: None.

6. **Example 1**: A pharmaceutical company claims that its drug increases a patient's blood oxygen level by an average of 95%. A random sample of 100 patients is taken, yielding an average increase of 94%. A one-sample z-test is performed to determine whether this deviation from the claimed 95% is statistically significant, given that the population standard deviation is known. Using a significance level of 0.05, the z-value is calculated, and the null hypothesis \( H_0: \mu = 95\% \) is tested.

7. **Example 2**: A marketing study aims to compare the average monthly sales of two regions. The sample includes 150 sales data points for each region, and the population variance is assumed to be known. A two-sample z-test is conducted to check if there is a significant difference in average sales between the regions. The z-test formula for comparing two sample means is applied:
   \[
   z = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}
   \]
   where \( \bar{X}_1 \) and \( \bar{X}_2 \) are the sample means, \( \sigma_1 \) and \( \sigma_2 \) are the population standard deviations, and \( n_1 \) and \( n_2 \) are the sample sizes.