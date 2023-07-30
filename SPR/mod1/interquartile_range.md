# Interquartile Range

Unline the standard deviation, the interquartile range is not affected by outliers.

Suppose we have a set of values

$$ \{ 1,2,3,4,5,6,7,8,9 \} $$

<br/>

To find the IQR, we need to identify three numbers:
1. Median
2. Q1
3. Q3

The median is the number right in the middle of the set. So, That would be $5$.

To find Q1 and Q3, we divide the set into two subsets: the subset before $5$ and the subset after $5$. If we do this, we get these two subsets

$$ \{ 1,2,3,4 \}$$

$$ \{ 6,7,8,9 \}$$

<br/>

Q1 and Q2 are the numbers right in the middle of these two subsets. However, notice that both sets have an even number of values. 

When we have an even number of values, we simply take the average of the two numbers in the middle of both sets.

<br/>

So, for Q1,

$$ \dfrac{2+3}{4} =  1.25 $$

and for Q2,

$$ \dfrac{7+8}{4} =  9 $$

<br>

With these three values calculated, we now have our interquartile range

1. Median $=5$
1. Q1 $=1.25$
1. Q3 $=9$