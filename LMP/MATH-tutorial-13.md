## Diagonalization (or Eigendecomposition)

$ \mathbf{A} = \begin{bmatrix}
2 & 2 \\
1 & 3
\end{bmatrix}$

<br/>


$\mathbf{A} = \mathbf{P} \mathbf{D} \mathbf{P}$

Where
- $\mathbf{P}$ is the matrix with eigenvectors as columns
- $\mathbf{A}$ is the matrix contraining the eigenvalues
- $\mathbf{P}^{-1}$ is the inversion of the matrix

<br/>

**Step 1 ($\lambda \times I$)**


$ \mathbf{I} = \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} $ 


$ \lambda\mathbf{I} = \lambda \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
\lambda & 0 \\
0 & \lambda
\end{bmatrix} $ 



<br/>

**Step 2 (Characteristic Polynomial)**


$ \det(\mathbf{A} - \lambda\mathbf{I}) $


$ \det(\begin{bmatrix}
2-\lambda & 2 \\
1 & 3-\lambda
\end{bmatrix}) = \lambda^2-5\lambda+4 $


<br/>

**Step 3 (Roots of Characteristic Polynomial)**

$\lambda_1 = 1$
$\lambda_2 = 4$



<br/>


**Step 4 (Find the Eigenvectors for $\lambda_1 = 1$)** 

We want $(\mathbf{A}-\mathbf{I})\mathbf{\lambda} = \mathbf{b}$


$\begin{bmatrix}
1 & 2 \\
1 & 2
\end{bmatrix} \begin{bmatrix}
x_1 \\
x_2
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix}$


Expressing as systems of equations

$ 1x_1 + 2x_2 = 0 $

Solving for $x_1$ and $x_2$ 

$x_1 = -2$
$x_2 = 1$

Denote the first eigenvector

$v_1 = \begin{bmatrix}
-2 \\
1
\end{bmatrix}$


<br/>

**Step 5 (Find the Eigenvectors for $\lambda_2=4$)** 

$v_1 = \begin{bmatrix}
1 \\
1
\end{bmatrix}$

<br/>


**Step 5 (Plugin values for $\mathbf{P}$ and $\mathbf{D})$**


$A = \begin{bmatrix}
1 & 2 \\
1 & 2
\end{bmatrix}$

$P = \begin{bmatrix}
-2 & 1 \\
1 & 1
\end{bmatrix}$

$D = \begin{bmatrix}
1 & 0 \\
0 & 4
\end{bmatrix}$

$P^{-1} = \text{inversion of } P$

<br/>


