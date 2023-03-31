#---- References ----------------------------------#
# [1] https://cran.r-project.org/web/packages/distributions3/index.html
# [2] Lecture 2, https://www.youtube.com/watch?v=ePK4L_qZgZI





#---- Essential Snippets -------------------------#

# To install external packages (only if not previously installed)
if(!require(rmarkdown)) {
  install.packages("distributions3")
}
# Load a library
# Note: 
# the distributions3 library [1] make it easier to work with probabilty
# distributions than the built-in functions in R.
library(distributions3)

# Explore available data for statistical analysis
data()





#---- Hypothesis Test -----------------------------#
#---- Z-Test (One Sample, Right-Tailed)  ----------#
# Description:
# The Z-Test is used when the data is normally distributed and its
# Variance is known. The One Sample Z-Test allows us to determine
# whether a particular Sample is significantly different from
# the Population from which it is drawn. A Right-Tailed test
# is used to when we are hypothesizing that the Test Statistic
# would be greater than the Population Parameter.


# (1) Generate random collection of normally-distrubuted data
population = rnorm(n=100, mean = 4.0, sd = 1) 
sample1 =  rnorm(n=9, mean = 4.6, sd = 1) 
mu = mean(population)
bar_x = mean(sample1)

# (2) The qqnorm() and qqline() functions, respectively, produce and fit a 
# a Quantile-Quantile plot. This plot allow us to easily visualize
# and quickly determine if our data is normally distributed or not.
# If the observations are scatted closely near the the fitted line, we can
# proceed to use the Z-Test for testing the hypothesis.
qqnorm(population)
qqline(population)

# (3) Quantile-Quantile plot for the sample
qqnorm(sample1)
qqline(sample1)

# (4) Choose Critical Regions
# We arbitrarily set alpha = 0.05.
# Alpha is the Rejection Region (for the Null Hypothesis) which means
# that the Acceptance Region for the Nul is 1 - alpha = 0.95
alpha = 0.05

# (5) Calculate Z-Statistic
zStatistic  <- (bar_x - mu) / (1 / sqrt(length(sample1)))

# Alternatively, to test specific values, you can hardcode
# the values for bar_x and mu (see [2])
# zStatistic  <- (4.6 - 4) / (1 / sqrt(length(sample1)))

# (6) Standardize the Normal Distribution
Z <- Normal(0, 1)

# (7) Calculate the p-value
# Note:
# The p-value is the probability that the test statistic (i.e, zStatistic)
# will be observed in the sample. If the p-value is less than or equal to
# alpha, our preferred rejection region, this may be grounds for rejecting
# the null hypothesis.

# To find the p-value, we calculate the CDF of the distribution to find
# the cumulative probability; that is, the probability that the Random
# Variable, Z, will observe the test statistic. 
# In other words, we are calculating
# P( Z >= 1.8) which is 0.9640697
#
# You can either (a) check the Z-Score table to confirm this value or
# Measure this probability with the CDF. We subtract this probabilit
# by 1 because we are measuring the probabilty within the Rejection 
# Region.
pVal = 1 - cdf(Z, abs(zStatistic))

# (8) View the p-value
pVal

# (9) Compare p-value and alpha
if( pVal <= alpha ) {
  print("Result is statistically significant")
  print("Reject the Null Hypothesis")
} else {
  print("Do not reject the Null Hypothesis")
}
