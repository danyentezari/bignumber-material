# Sampling Distribution

The sampling distribution is the distribution of means of samples.

Read that again.

And take note that "sampling distribution" is not all a "sample distribution."

They sound similar but refer to different concepts.

1. **Short definition**: Distribution of a statistic over multiple samples.

2. **Long definition**: A sampling distribution is the probability distribution of a statistic (e.g., mean, variance) obtained from repeated random samples drawn from the same population. It shows how the statistic varies from sample to sample and is central to hypothesis testing and estimation.

3. **Related subtopics**:
   - 4 Central Limit Theorem
   - 4 Distribution of Sample Mean
   - 4 Standard Error
   - 4 Sample Size Effect on Distribution
   - 4 Sampling Distribution of Proportion

4. **Propositions in LaTeX**: None.

5. **Theorems in LaTeX**:
   - **Central Limit Theorem (CLT)**: If \(X_1, X_2, ..., X_n\) are independent and identically distributed (i.i.d.) random variables with mean \( \mu \) and variance \( \sigma^2 \), the sampling distribution of the sample mean \( \bar{X} \) approaches a normal distribution as the sample size \( n \) increases:
   \[
   \bar{X} \sim N\left( \mu, \frac{\sigma^2}{n} \right)
   \]
   regardless of the population's distribution.

6. **Example 1**: Consider a population of students' test scores. A researcher takes multiple random samples of 30 students each and calculates the sample mean for each group. The collection of these sample means forms a sampling distribution. According to the Central Limit Theorem, as more samples are drawn, the distribution of these sample means will approximate a normal distribution, even if the population is not normally distributed.

7. **Example 2**: In a factory producing light bulbs, the average lifespan of the bulbs is 1,000 hours with a standard deviation of 100 hours. If the quality control team repeatedly selects samples of 50 bulbs and records the average lifespan for each sample, the resulting distribution of sample means is the sampling distribution. The standard deviation of this sampling distribution, called the standard error, is smaller than the population standard deviation and helps in making inferences about the population mean.