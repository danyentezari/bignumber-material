#---- Reading Available Data -----------------------------------#

# Viewing list of available data
data()

# Viewing one particular data
mtcars

# Identifying the programming type of data
# Note:
# Different data type will require different functions. For example,
# mtcars is a "data.frame"
class(mtcars)





#---- Reading and Writing External Data ------------------------#

# Get the file path of this script
filePath <- rstudioapi::getSourceEditorContext()$path

# Get the folder path of this script
folderPath <- dirname(rstudioapi::getSourceEditorContext()$path)

# Reading a CSV file
fileLocation = paste(folderPath, 'EuStockMarkets.csv', sep='/')
euStockTable = read.csv(file = fileLocation,header = TRUE, stringsAsFactors = FALSE)

# Exporting CSV to computer
fileLocation = paste(folderPath, 'EuStockMarkets.csv', sep='/')
write.csv(EuStockMarkets, file=fileLocation, row.names = TRUE, sep=',', col.names = TRUE)





#---- Summary Statistics ---------------------------------------#

# View the entire table
mtcars

# View a column within the table

# Note:
# What comes after the '$' sign is the column name.
# Here, mpg refers to the column for 'miles per gallon'
# of the provided mtcars data set in R.
mtcars$mpg

# The summary() function provides the following summary
# statisics: 
# (1) Interquartile Range
# (2) Mean Average
# (3) Minumum and maximum values
summary(mtcars$mpg)


# Get the mean average of values in a column
mean(mtcars$mpg)
median(mtcars$mpg)

# There is no built-in function for calculating
# the mode of the values. Here, we will create a
# function for calculating the mode
mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

mode(mtcars$mpg)





#---- Visualization --------------------------------------------#

# Install the library 'grammar of graphics'. This
# library provides enhanced features for statistical
# visualization.
if(!require(ggplot2)) {
  install.packages("ggplot2") # Install it again
}
library(ggplot2)


# Produce histogram
# Note:
# ggplot() produces a blank plot
# geom_histogram() superimposes the histogram on the plot
# aes() is for indicating the values for the x and y axes
ggplot(mtcars, aes(x=disp)) + 
  geom_histogram()


# Produce frequency chart
# Note:
# The argument stat='idenity' allows us to select the values for
# the y-axis. The other option is stat='count' which will have ggplot2
# automatically select the values for the y-axis.
ggplot(mtcars, aes(x=cyl, y=mpg)) + 
  geom_bar(stat='identity') + 
  labs(y="Miles Per Galon", title = 'Cylinders')


# Produce a scatter plot with simple regression model
# Note:
# lm() created a linear model. In this example, mpg (Miles Per Galon) 
# is the dependant variable and 'wt' (Weight) is the independant variable.
#
# abline() fits the model
#
# lowess() is the function name for 'locally weighted scatterplot smoothing'.
# This technique uses quadratic polynomials (2nd degree polynomial) to
# reveal more about the relationship between the dependant and independant
# variables. Also, this technique may reveal a non-linear relationship in
# the model.
plot(mtcars$wt, mtcars$mpg, main="Scatterplot Example",
     xlab="Car Weight ", ylab="Miles Per Gallon ", pch=19) 

regressionModel <- lm(mtcars$mpg~mtcars$wt)
abline(regressionModel, col="red")
lines(lowess(mtcars$wt,mtcars$mpg), col="blue")