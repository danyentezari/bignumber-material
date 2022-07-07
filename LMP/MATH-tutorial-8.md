#### Number Systems

Natural Numbers
>$\mathbb{N} = \{ 0,1,2,3,...,\infty  \}$

Integer Numbers
>$\mathbb{Z} = \{ -\infty,...,-2,-1,0,1,2,3,...,\infty \}$


Real Numbers
>$\mathbb{R} = \{ -\infty,...,-2,-1,0,1,2,3,...,\infty \}$

<br/>

#### Review of Set Builder Notation

To express this set
>$A = \{1,2,3\}$

using set build notation, we use the following expression
>$A = \{ x | x \in \mathbb{N} \text{ and } 1 \leq x \leq 3 \}$

<br/>


#### Members of a Vector
The words 'scalar', 'point', 'component', 'element' are all synonyms for members of a matrix

<br/>


#### Vector

Vectors are sets of elements. However, vectors are conventionally referred to as spaces with scalars.

>$\vec{a} = (1,2,3)$

>$\mathbf{a} = [1,2,3]$

<br/>


#### Vector Space
A vector space is the set of vectors to which the following axioms apply.

(1) Vector addition
>$\mathbf{u},\mathbf{v} \in V$  

>$ \mathbf{u} + \mathbf{v} \in V$ 

(2) Scalar Multiplication

>$c \in \mathbb{R},\mathbf{v} \in V$  

>$ c \times \mathbf{v} \in V$ 

Formally, we say we have $V$ over the field $K$ with the axioms (1) and (2).

(3) Inner Product (or Dot Product)
>$ \mathbf{u} \cdot \mathbf{v} = (u_1 \times v_1) + (u_2 \times v_2) + \dots + (u_n \times v_n) $


<br/>

#### The $\mathbb{R}^n$ Space

The space of all vectors over $\mathbb{R}^n$. In other words, this is the set of all vectors with $n$ dimensionality.

For example,

>$\mathbb{R}^3 = \{(a,b,c) \enspace | \enspace a,b,c \in \mathbb{R} \}$ 

or

>$\mathbb{R}^5 = \{(a,b,c,d,e) \enspace | \enspace a,b,c,d,e \in \mathbb{R} \}$ 


Note that both $(a,b,c)$ and $(a,b,c,d,e)$ denote vectors.

<br/>

#### Linear Combination

For vectors $\mathbf{v}_1,\mathbf{v}_2,...,\mathbf{v}_k \in \mathbb{R}^n$ and
For constants $a_1,a_2,...,a_k \in \mathbb{R}$


>$l = a_1\mathbf{v}_1 + a_2\mathbf{v}_2 + a_3\mathbf{v}_3$

<br/>

#### Linear Span

Given a vector space, $V$, with elements 
>$\mathbf{v}_1,\mathbf{v}_2,\cdots,\mathbf{v}_k \in V$

and the set 
>$X = \{ \mathbf{v}_1,\mathbf{v}_2,\cdots,\mathbf{v}_k \}$

The linear span of $X$, denoted $Lin(X)$ is the set of linear combinations. Thus,

>$\text{Lin}(X) = \{ a_1\mathbf{v}_1 + a_2\mathbf{v}_2  + \cdots + a_k\mathbf{v}_k | a_1,a_2,...,a_k \in \mathbb{R} \}$

<br/>

#### Matrices
A matrix is a space of scalars over $\mathbb{R}^{n \times m}$. 

For example, where $n=2$ and $m=3$,

>$\mathbf{M} = \begin{bmatrix}
2 & 1 & 1 \\
6 & 5 & -3
\end{bmatrix}$

<br/>

#### Magnitude (or Norm)

Given a vector $\mathbf{v} = (1,4,3,2)$

The magnitude of the vector is denoted as follows

>$ || \mathbf{v} || = | \mathbf{v} | = \sqrt{1^2+4^2+3^2+2^2} $

Note that the choice of using double or single bars is left to the writer. However, it is more common to use double bars since single bars are commonly used to denote the absolute value of some signed value.

<br>

#### Row Space

The row space, denoted $\text{RS(M)}$, is the linear span of row vectors of some matrix, $M$.

For example, given the set of rows of $\mathbf{M}$ denoted as $\mathbf{R}$
>$\mathbf{R} = \{ \mathbf{v} | \mathbf{v} \text{ is a row of } \mathbf{M}  \}$

The row space of $\mathbf{M}$ would the linear span of $\mathbf{R}$
>$\text{RS}(M) =  \text{Lin}(R) = \{ a_1\mathbf{v}_1 + a_2\mathbf{v}_2  + \cdots + a_k\mathbf{v}_k | a_1,a_2,...,a_k \in \mathbb{R} \}$




<br/>

#### Column Space
The column space, denoted $\text{CS(M)}$, is the linear span of column vectors of some matrix, $M$.

For example, given the set of columns of $\mathbf{M}$ denoted as $\mathbf{C}$
>$\mathbf{C} = \{ \mathbf{v} | \mathbf{v} \text{ is a column of } \mathbf{M}  \}$

The row space of $\mathbf{M}$ would the linear span of $\mathbf{R}$
>$\text{CS}(M) =  \text{Lin}(C) = \{ a_1\mathbf{v}_1 + a_2\mathbf{v}_2  + \cdots + a_k\mathbf{v}_k | a_1,a_2,...,a_k \in \mathbb{R} \}$