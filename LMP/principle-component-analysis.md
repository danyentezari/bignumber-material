\mathbf{}

## Principle Component Analysis (PCA)

#### Preliminaries
<br/>

##### Linear Combinations
$\mathbf{p}_m = w_{1m} \mathbf{x}_1 + w_{2m} \mathbf{x}_2 + \cdots + w_{nm} \mathbf{x}_n$

where
- $\mathbf{P}$ is the matrix of principle components
- $\mathbf{p}_m \in \mathbf{P}$ is $m$th column of $\mathbf{P}$
<br/>

##### Linear Independence
A condition where a linear combination is equal to 0
$\mathbf{p}_m = 0$
<br/>

##### Identity Matrix

A matrix whose components are 1 on the diagonal and 0 elsewhere

$\mathbf{I} = \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} $
<br/>

##### Inverse of Matrix

A condition about matrices when their products is equal to an identity matrix.

Consider matrices $\mathbf{A}$ and $\mathbf{B}$ where

- $\mathbf{A} = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix} $

- $\mathbf{B} = \begin{bmatrix}
-2 & 1 \\
3/2 & -1/2
\end{bmatrix} $

Then $\mathbf{A}$ and $\mathbf{B}$ are inverses of each other if

$\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A} = \mathbf{I}$

That is,

$ \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix} 
\begin{bmatrix}
-2 & 1 \\
3/2 & -1/2
\end{bmatrix}
= \begin{bmatrix}
-2 & 1 \\
3/2 & -1/2
\end{bmatrix}
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix} = 
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}  $
<br/>

##### Syntax of Inverse of Matrix
The inverse of a matrix is denoted by superscript $-1$. For example, if $\mathbf{B}$ is the inverse of $\mathbf{A}$, then we can denote $\mathbf{B} = \mathbf{A}^{-1}$.

Thus,

$\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A} = \mathbf{I}$

can also be expressed as

$\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1} \mathbf{A} = \mathbf{I}$
<br/>

##### Polynomial
A polynomial is a sum of monomials. Polynomials are expressed in this form

$a_{0}x^{m} + a_{1}x^{m-1} + ... + a_{m-1}x^{1} + a_{m}x^{0}$



##### Determinant Function
<br/>

##### Indicator Function
An indicator function is a piecewise function that maps to 1 or 0.

$\mathbb{1}(y) = \begin{cases} 
1, \enspace \text{if } y \in A \\
0, \enspace \text{otherwise}
\end{cases}$
<br/>

##### Characterisic Polynomial
 
 
$\begin{bmatrix}
1-\lambda & 3 \\
3 & 1-\lambda
\end{bmatrix} = \det \Big( \begin{bmatrix}
1 & 3 \\
3 & 1
\end{bmatrix} - \lambda\mathbf{I} 
\Big)$

<br/>


##### Spectral Decomposition
$\mathbf{A}\mathbf{W} = \mathbf{W}\mathbf{\Lambda}$
where
- $\mathbf{W}$ is the matrix of eigenvectors
- $\mathbf{\Lambda}$ is the matrix of eignenvalues
<br/>

### PCA
$\mathbf{V} = T^{-1} \: \mathbf{X}^{'} \mathbf{X}$
<br/>

##### The Principal Components
$\mathbf{P} = \mathbf{X} \mathbf{W}$
where
- $\mathbf{P}$ is the matrix of principal components
- $\mathbf{X}$ is the matrix of input data
- $\mathbf{W}$ is the matrix of eigenvectors
<br/>

**Bibliograpy**
(1) R. Bronson, Matrix Operations,...
(2) C. Alexander, Quantitative Methods in Finance,...
(3) M. Cohen, Linear Algebra,...
(4) https://web.ma.utexas.edu/users/gordanz/notes/continuous_color.pdf