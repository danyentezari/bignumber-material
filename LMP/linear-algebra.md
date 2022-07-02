# Linear Algebra


### Vectors
A vector is a set of elements. From set theory, we know that sets are denoted with curly brackets $\{$ $\}$. 

For example, 
> $v = \{1,2,3\}$. 

The elements of $v$ are $1,2,3$

In linear algebra, however, vectors are commonly denoted with $()$ and $[$ $]$, and vector variables are denoted with an arrow $\vec{v}$.

Also, elements in a vector are usually referred to as components. 

Therefore, we will use the convention specific to linear algebra.

We will now denote the vector $v$ again using linear algebra convention as follows
> $\vec{v} = (1,2,3)$

Also, we will now call $1,2,3$ the components of $v$.

<br/>

### Matrices

##### Strang's 4 Subspaces
- Row Space
- Nullspace
- Column Space
- Left Nullspace


##### Systems of Equations
$2x+y+z=12$
$6x+5y-3z=6$
$4x-y+3z=5$

$\rightarrow$

$\begin{bmatrix}
2 & 1 & 1 & 12 \\
6 & 5 & -3 & 6 \\
4 & -1 & 3 & 5
\end{bmatrix}$
<br/>


##### Square Matrix
A square matrix whose values that are not on the principal diagonal are equal to 0.

$\begin{bmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 3
\end{bmatrix}$

<br/>

##### Diagonalization
Given a square matrix $A$

$B = P^{-1}AP$

**Application in Physics (Dynamics)**

The moment of a force is given by

$M = d \times F$

and, in vector form,

$\mathbf{M} = \mathbf{r} \times \mathbf{F}$


##### Linear Combination
For vectors $\mathbf{v}_1,\mathbf{v}_2,...,\mathbf{v}_k \in \mathbb{R}^n$ and
For constants $a_1,a_2,...,a_k \in \mathbb{R}$

<br/>

##### Linear Span
Give a Vector Space, $V$ with elements $\mathbf{v}_1,\mathbf{v}_2,\cdots,\mathbf{v}{v}_k \in V$

and the set $S = \{ {v}_1,{v}_2,\cdots,{v}_k \}$

The linear span of $X$, denoted $Lin(X)$ is the set of linear combinations. Thus,

$Lin(X) = \{ a_1\mathbb{v}_1 + a_1\mathbb{v}_1  + \cdots + a_k\mathbb{v}_k | a_1,a_2,...,a_k \in \mathbb{R} \}$


##### Row Space
Given an $m \times n$ matrix $A$, the null space of $A$ denoted by $N(A) = \{\mathbf{x} \in \mathbb{R}^n | A\mathbf{x} = 0 \}$

##### Null Space (or Kernel)