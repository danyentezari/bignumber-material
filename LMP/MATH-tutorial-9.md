# Matrix Operations



**Representing inequalities in a matrix**

$100x + 100y \leq 3000 \times 10^4$

$200x + 100y \leq 4000 \times 10^4$

$\rightarrow$

$\begin{bmatrix}
(100) & (100) & (3000 \times 10^4) \\ 
(200) & (100) & (4000 \times 10^4)
\end{bmatrix}$


#### Reduced Row Ecehlon Form
<img src="https://i.stack.imgur.com/ST1qx.png" width="350">

<br/><br/>


#### Gaussian Elimination

$R_2 \rightarrow R_1$

$\begin{bmatrix}
200 & 100 & 4000 \\
100 & 100 & 3000 \\ 
\end{bmatrix}$

<br/>

$R_2 - R_1 \rightarrow R_1$

$\begin{bmatrix}
100 & 0 & 1000 \\
100 & 100 & 3000 \\ 
\end{bmatrix}$

<br/>

$R_1 - R_2 \rightarrow R_2$


$\begin{bmatrix}
100 & 0 & 1000 \\
0 & 100 & 2000 \\ 
\end{bmatrix}$

<br/>

$\dfrac{1}{100}R_1 \rightarrow R_1$

$\begin{bmatrix}
1 & 0 & 10 \\
0 & 100 & 2000 \\ 
\end{bmatrix}$

<br/>

$\dfrac{1}{100}R_2 \rightarrow R_2$

$\begin{bmatrix}
1 & 0 & 10 \\
0 & 1 & 20 \\ 
\end{bmatrix}$

<br/>

Put back the $\times 10 ^ 4$

$\begin{bmatrix}
1 & 0 & 10 \times 10^4 \\
0 & 1 & 20 \times 10^ 4\\ 
\end{bmatrix}$

<br/>

$1x + 0y = 10 \times 10 ^ 4$
$0x + 1y = 20 \times 10 ^ 4$

<br/>

$x = 10 \times 10 ^ 4$
$y = 20 \times 10 ^ 4$


<br/><br/>


### LU Decomposition


$\mathbf{A} = \mathbf{L}\mathbf{U}$

Where
- $A$ is the original matrix
- $U$ is upper-triangle matrix 
- $L$ is the lower-triangle is the product of elimination matrices

<br/>

**Example**



$\mathbf{A} = \begin{bmatrix}
1 & 2 & -3  \\
-3 & -4 & 13 \\
2 & 1 & 5 
\end{bmatrix}$

<br/>

#### Identity Matrix

<img src="https://dcvp84mxptlac.cloudfront.net/diagrams2/equation-3-multiplying-an-identity-matrix-times-a-non-unit-matrix.png">

<br/><br/>
<br/><br/>