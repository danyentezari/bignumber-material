# Measures of Dispersion

The measures of dispersion are numbers that represent the spread and variation in data.

The measures of dispersion include the range, interquartile range, variance, and standard deviation. They are calculated as follows:

Consider this set of values:

$$X = \{ 3, 3, 3, 4, 6, 8, 8, 9 \}$$

<br/>

Then, the measures are found as follows:

**Range**

The range is the difference between the smallest and largest values in $X$.

Range $= 9 - 3 = 6$

<br/>

**Interquartile Range**

The interquartile range (IQR) is the range of values within the first quartile (25th percentile) and the third quartile (75th percentile). It gives us a sense of the spread of the middle 50% of the data.

To calculate the interquartile range:
1. Arrange the data in ascending order
$$3, 3, 3, 4, 6, 8, 8, 9$$

2. Find the first quartile (Q1) and third quartile (Q3):
$$Q1 = 3$$
$$Q3 = 8$$

3. Calculate the interquartile range: 
$$ {IQR} = Q3 - Q1 = 8 - 3 = 5$$

<br/>

**Variance**

Variance measures the average of the squared differences between each data point and the mean. It gives us an idea of how much the data points deviate from the mean.

1. Find the mean (average) of the data: <br/>
$$\text{Mean} = \dfrac{3 + 3 + 3 + 4 + 6 + 8 + 8 + 9}{8} = \dfrac{44}{8} = 5.5$$

2. Calculate the squared differences between each data point and the mean:

$$(3 - 5.5)^2, (3 - 5.5)^2, ... , (8 - 5.5)^2, (9 - 5.5)^2$$

3. Calculate the average of the squared differences: <br/>
$$ \text{Variance} = \dfrac{(3 - 5.5)^2 + (3 - 5.5)^2 + ... + (8 - 5.5)^2 + (9 - 5.5)^2}{8}$$
$$ = \dfrac{44.5}{8} = 5.5625$$

<br/>

**Standard Deviation**

The standard deviation is the square root of the variance. It provides a measure of how spread out the data is from the mean.

$$ \text{Standard Deviation} = \sqrt{5.5625} \approx 2.357$$