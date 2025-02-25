**linear combination** Let $V$ be a vector space, and $U \subseteq V$ . We say that $U$ is closed with
respect to scalar multiplication if $ka \in U$ for every scalar $k$ and every $a \in U$. 

We call $U$ a subspace of $V$ if $U$ is closed with respect to addition and scalar multiplication. It is easy to see that if $V$ is a vector space over the field $F$, and $U$ is a subspace of $V$, then $U$ is a vector space over the same field $F$.
$a_{1},a_{2},...,a_{n}$ are in $V$ and $k_{1},k_{2},...,k$ , are scalars, then the
vector $k_{1}a_{1}+k_{2}a_{2}+\cdot\cdot\cdot+k_{n}a_{n}$ is called a linear combination of
$a_{1},a_{2},...,a_{n}$. 
The set of all the linear combinations of $a_{1},a_{2},...,a_{n}$ is a subspace of $V$. 

**second-order linear homogeneous equation** The general solution of the second-order linear homogeneous equation is a linear combination of two linearly independent solutions

**nth-order homogeneous equation**
$$a_{0}y^{(n)}+a_{1}y^{(n-1)}+\cdot\cdot\cdot+a_{n-1}y^{\prime}+a_{n}y=0$$



**Zero Condition of Homogeneous Linear Differential Equation**
The general linear equation (3) is homogeneous if $G=0$ for all $x$ and $y$ in the domain of the equation; otherwise, it is called nonhomogeneous. Of course, if $G$ is a constant, the equation is homogeneous if and only if $G=0$. 

For example,

$$\begin{equation} u_{t}=\alpha^{2}u_{xx} \end{equation}$$
$$\begin{equation} u_{t}=\alpha^{2}u_{xx}+1 \end{equation}$$
$$\begin{equation} u_{xx}+xu_{yy}=0 \end{equation}$$

Where $(3)$ and $(5)$ are homogeneous linear equations, and $(4)$ is a nonhomogeneous linear equation.

Since, 

in $(3)$, we have $u_{t} - \alpha^{2} u_{xx} = 0$
in $(4)$, we have $u_{t} - \alpha^{2} u_{xx} - 1 = 0$, but $-1$ is a constant.
in $(5)$, we have $u_{xx} + xu_{yy} = 0$

**Dependant Variables in Homogeneous Linear Differential Equation** A general system of first-order linear homogeneous ODEs with constant coefficients has the form

$$x_{1}^{\prime}=a_{11}x_{1}+a_{12}x_{2}+\cdot\cdot\cdot+a_{1n}x_{n} \\
x_{2}^{\prime}=a_{21}x_{1}+a_{22}x_{2}+\cdot\cdot\cdot+a_{2n}x_{r} \\
\vdots \\
x_{n}^{\prime}=a_{n1}x_{1}+a_{n2}x_{2}+\cdot\cdot\cdot+a_{nn}x_{r}$$

where 
- $a_{11}, a_{12},...,a_{n}$ are given constants.

Homogeneous means that there are no free terms, that is, terms that don't involve any $x_i$.
