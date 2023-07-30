#---- Setup --------------------------------------#

# Create three samples for the ANOVA. These are three
# samples whose means will be compared.
measurement1 <- c(95, 91, 89, 90, 99, 88, 96, 98, 95)
measurement2 <- c(83, 89, 85, 89, 81, 89, 90, 82, 84, 80)
measurement3 <- c(68, 75, 79, 74, 75, 81, 73, 77)

measurements <- c(measurement1, measurement2, measurement3)

# The rep() function produces a vector of values replicated by some
# criteria. This is done to create a table where the second column will contain
# each measurement and the first column will contain the name of the
# collection to which each measurement belongs. Run 'measurementsDataFrame' to 
# see the table. Also see 'ANOVA' section below for some context.
categories <- rep(
  c("measurement1", "measurement2", "measurement3"), 
  times=c(
    length(measurement1),  
    length(measurement2), 
    length(measurement3)
  )
)


measurementsDataFrame <- data.frame(categories,measurements)




#---- ANOVA --------------------------------------#

# The ANOVA test will reveal whether the means of the samples
# are equivalent. In ANOVA, the dependent variable needs to be continuous
# and there needs to be one categorical independent variable. In this example,
# the continuous and categorical variables are 'measurements' and 
# 'categories', respectively
analysis <-aov(measurements ~ categories,data = measurementsDataFrame)

summary(analysis)



# Visualize the the means with box-and-whisker plot
if(!require(ggplot2)) {
  install.packages("ggplot2") # Install it again
}
library(ggplot2)

ggplot(measurementsDataFrame, aes(x=categories, y=measurements))+
  stat_boxplot(geom="errorbar", width =.5) +
  geom_boxplot()



#---- A Priori Test (or Planned Contrast) --------#

# The ANOVA test will reveal whether the means of the samples
# are equivalent. However, if we want to determine which sample(s)
# are unequal and to what extent. Here, we will perform Post Hoc test...
contrasts(measurementsDataFrame$categories) <- matrix( c(0,1,-1,2,-1,-1),3,2 )
contrasts(measurementsDataFrame$categories)

anovaWithContrasts <- aov(
  measurements ~ categories, 
  data=measurementsDataFrame, 
  contrasts=contrasts(measurementsDataFrame$categories)
)

summary(
  anovaWithContrasts, 
  split=list(categories=list("2 vs 3"=1, "1 vs 2 & 3"=2))
)


model.tables(anovaWithContrasts, type='effects')

# Extracting the means
model.tables(anovaWithContrasts, type='means')





#---- A Posteriori Test (or Unplanned Contrast) --#

# Tukey Honest Significant Differences (or Multiple Comparison Test)

# diff is difference of means
# lwr is the lower point estimate of the confidence interval
# upr is the upper point estimate of the confidence inteeval
# p adj is the adjusted p-value after the multiple camparisons 
# Note:
# The adjusted p-value will reveal which samples differ the most
# and a smaller a p-value indicates more significance.
TukeyHSD(analysis)
