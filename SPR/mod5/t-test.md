# t-Test

The t-Test is used for comparing the means of two groups that are approximately normall distributed, especially the means of a sample and its population. The t-Test is also used when the size of the samples is small; conventionally, $ \leq 30$

The t in t-Test stands for "test". As in "test statistic."

Naming things in statistics is not very intuitive, as usual. Because we can compare population parameters and not just sample statistics.  

Here are the following variations of the t-Test and their applications,
- One-Sample t-Test: Used for comparing a sample to its population.

- Independent Samples t-Test: Used for comparing any two groups. The comparison is based on their means.
 
- Paired Samples t-Test: Used to compare the statistic of a group before and after some change has been introduced to it.
 

The following assumptions must hold for t-Test to be viable:
1. **Normality**: Data in each group should be approximately normally distributed, especially important for small sample sizes.

2. **Homogeneity of Variance**: Variances of the two groups being compared should be approximately equal.

3. **Independence**: Observations within and between groups should be independent. For paired t-tests, this means pairs of observations should be dependent but pairs themselves should be independent.

4. **Scale of Measurement**: The dependent variable should be measured at the interval or ratio scale, allowing for meaningful calculation of means and standard deviations.

If the standard deviation is known and the size of the sample is larger (i.e, $\geq 30$), then the z-Test is used.

## Examples

**Example 1**: To test if a new teaching method is more effective, researchers compare the average test scores of students using the new method with those using the traditional method. An independent samples t-test is used to evaluate if the difference in means is statistically significant.

**Example 2**: In a medical study, a paired samples t-test is used to compare the blood pressure of patients before and after taking a new medication. The test checks if the mean blood pressure has significantly changed after treatment, based on the differences in paired observations for each patient.


## References:
[1] L. Wasserman, *All of Statistics*. 2nd ed. New York: Springer, 2005.