# Singular Value Decomposition 

See [8, pp. 383, 9. pp. 193]

<br/>

Given 

> $\mathbf{A} = \begin{bmatrix}
10 & 2 \\
5 & 11
\end{bmatrix}$

<br/>

Find the SVD of $\mathbf{A}$

> $\mathbf{A} = \mathbf{U} \mathbf{S} \mathbf{V}^T$

<br/>

**Solution**

$\mathbf{A} = \begin{bmatrix}
10 & 2 \\
5 & 11
\end{bmatrix} = \begin{bmatrix}
0.6 & -0.8 \\
0.8 & 0.6
\end{bmatrix}
\begin{bmatrix}
14.14 & 0\\
0 & 7.07
\end{bmatrix}
\begin{bmatrix}
0.70 & -0.70\\
0.70 & 0.70
\end{bmatrix}$

Where

- $\mathbf{A}$ is an $m \times n$ matrix
- $\mathbf{U}$ is an $m \times m$ orthogonal matrix
- $\mathbf{S}$ is a diagonal matrix of singular values (eigenvalues)
- $\mathbf{V}^T$ is  $n \times n$ an orthogonal matrix


**Step 1 Product of $\mathbf{A}^T\mathbf{A}$**

$\mathbf{A}^T\mathbf{A} = \begin{bmatrix}
10 & 5 \\
2 & 11
\end{bmatrix}
\begin{bmatrix}
10 & 2 \\
5 & 11
\end{bmatrix}  = \begin{bmatrix}
104 & 72 \\
72 & 146
\end{bmatrix}$

**Step 2 Product of $\mathbf{A}\mathbf{A}^T$**

$\mathbf{A}\mathbf{A}^T = \begin{bmatrix}
10 & 2 \\
5 & 11
\end{bmatrix} \begin{bmatrix}
10 & 5 \\
2 & 11
\end{bmatrix} = \begin{bmatrix}
125 & 75 \\
75 & 125
\end{bmatrix}$

**Step 3 Calculate Singular Values for (1) and (2)**

$\sigma_1 = 200$
$\sigma_2 = 50$


**Step 4 Calculate Square Root of Singular Values**

$\mathbf{S} = \begin{bmatrix}
\sqrt{\sigma_1} & 0 \\
0 & \sqrt{\sigma_2} 
\end{bmatrix} = \begin{bmatrix}
14.14 & 0 \\
0 & 7.07
\end{bmatrix}$

**Step 5 Orthogonalize the $\mathbf{A}^T\mathbf{A}$**

$\mathbf{U} = \text{gramschmidt}(\mathbf{A}^T\mathbf{A})$

**Step 6 Orthogonalize the $\mathbf{A}\mathbf{A}^T$**

$\mathbf{V} = \text{gramschmidt}(\mathbf{A}\mathbf{A}^T)$

<br/>

<br/><br/>