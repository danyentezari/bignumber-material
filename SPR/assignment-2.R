#---- Assignment 2 -------------------------------# 

# Complete the code in the sections below. 

# In this assignment, you will perform ANOVA for the open prices 
# of the MSFT (Microsoft) stock.
# Note:
# Use 'example-3-anova.R' as a guide.

# (0) Explore the MSFT OHLC Data From Yahoo Finance 
# Note:
# This data is about OHLC (Open-High-Low-Close) prices for the 
# Microsoft stock. The library quantmod will provide access to
# the MSFT dataframe. The function, getSymbols(), will store
# the sybmol object in the environmet, accordingly.
if(!require(quantmod)) {
  install.packages("quantmod") # Install it again
}
library(quantmod)

getSymbols('MSFT',src='yahoo')

# dim() will return the number of rows and columns (in that order)
dim(MSFT)




# (1) Draw 3 samples from the population (MSFT)
ms1 <- as.vector(MSFT[0:9, 1])
ms2 <- as.vector(MSFT[10:19, 1])
ms3 <- as.vector(MSFT[20:29, 1])




# (2) Produce ANOVA with aov() and analyze the test with summary()




# (3) Create a box-and-whisker plot for the 3 sample open prices using
# the ggplot2 library




# (4) Produce an A Priori Test




# (5) Produce an A Posteriori Test


