# Assignment 2: Matrix Operations


$\mathbf{A} = \begin{bmatrix}
3 & 5 & 4 \\
1 & 0 & 2 \\
3 & 2 & 2
\end{bmatrix}$

<br/>

#### Assignment Tasks
1. Find the norm of the matrix $\mathbf{A}$
2. Express the characteristic polynomial for $\mathbf{A}$
3. Find the eigenvalues and eigenvectors of $\mathbf{A}$ (see Note 4!)
4. Perform tasks 1, 2 and 3 in python (see assignment-2.ipynb)

<br/>

#### Notes:
1. For this assignment, you need to submit both the mathematical solution and programming solution
2. Show all the steps for the mathematical solution
3. Add comments for the programming solution 
4. The eigenvalues for this matrix are complex. You may use NumPy to find the roots of the characteristic polynomial (see code below).


```
import numpy as np
# Example cubic polynomial
# ax^3 + bx^2 + cx^1 + d = 0

a = 1
b = 5
c = 7
d = 9

coeff = [a,b,c,d]
np.roots(coeff)
```