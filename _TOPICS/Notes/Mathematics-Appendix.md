# Mathematics Appendix


**Stokes' Theorem**

Let $S$ be a piecewise smooth oriented surface in space, and let the boundary of $S$ be a piecewise smooth simple closed curve $C$. If  with continuous first partial derivatives in a domain containing $S$, then:

$$\iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n} \, dA = \oint_C \mathbf{F} \cdot \mathbf{r}'(s) \, ds$$

Or,

$$\iint_S (\text{curl} \times \mathbf{F}) \cdot \mathbf{n} \, dA = \oint_C \mathbf{F} \cdot \mathbf{r}'(s) \, ds$$

In this formula

* $\mathbf{n}$ is the unit normal vector of $S$.
* $\mathbf{r}'(s)$ is the unit tangent vector of $C$.
* $s$ is the arc length of $C$.
* $\mathbf{F}(x, y, z)$ is a continuous vector function
  



**Flux:** Total amount of a field or fluid passing through a surface.

**Double Integral**

The double integral is defined by the following identity:
$$\iint_R f(x, y) \, dA = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*) \Delta A$$

where


*   $R$ is a closed bounded region in the $xy$-plane over which the function is integrated [1, 2].
*   $m$ and $n$ are the number of subrectangles into which the region $R$ is partitioned [3, 4].
*   $R_{ij}$ are the smaller subrectangles resulting from dividing $R$ using a grid of lines parallel to the axes [4, 5].
*   $\Delta A$ represents the area of each subrectangle $R_{ij}$ [4, 6].
*   $(x_{ij}^*, y_{ij}^*)$ is an arbitrary sample point chosen within the subrectangle $R_{ij}$ [4, 6].
*   The limit is taken as $m$ and $n$ approach infinity such that the maximum diameter (the greatest distance between any two points within a subregion) approaches zero [3, 7].
*   The function $f(x, y)$, the integrand, is typically assumed to be continuous on $R$ to ensure the limit exists and is independent of the choice of sample points [7, 8].

<br/>

**Double Integral Notational Variations**

There exist double integral with two equivalent notations:
* Differential Area Form: $\displaystyle \iint_R f(x, y) \, dA$.
* Coordinate Form: $\displaystyle \iint_R f(x, y) \, dx \, dy$.

<br/>

**Vector Differential Operator**

The vector differential operator for expressing the partial differentiation of a vector

$$\nabla = \frac{\partial}{\partial x} \mathbf{i} + \frac{\partial}{\partial y} \mathbf{j} + \frac{\partial}{\partial z} \mathbf{k}$$

where

- $\nabla$ is the vector differential operator.
- $\dfrac{\partial}{\partial x}, \dfrac{\partial}{\partial y}, \text{ and } \dfrac{\partial}{\partial z}$ are partial derivatives.

Note:

- $\nabla$ is also called del.
- $\nabla$ is also called nabla.
- $\mathbf{i}, \mathbf{j}, \text{ and } \mathbf{k}$ are the standard basis unit vectors pointing in the positive directions of the $x, y, \text{ and } z$ axes, respectively

<br/>

**Curl**

Let $\mathbf{v}(x, y, z)$ be a differentiable vector function expressed in Cartesian coordinates with components $[v_1, v_2, v_3]$, such that: $$\mathbf{v} = v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$$
The curl of $\mathbf{v}$ (also denoted as $\nabla \times \mathbf{v}$ or $\text{rot } \mathbf{v}$) is defined by the following symbolic determinant: $$\text{curl } \mathbf{v} = \nabla \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ v_1 & v_2 & v_3 \end{vmatrix}$$

**Divergence**

<br/>


**Differentiation of Vector**

$$\mathbf{v}'(t) = \lim_{\Delta t \to 0} \frac{\mathbf{v}(t + \Delta t) - \mathbf{v}(t)}{\Delta t}$$ 


<br/>

**Vector Function**

$$\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle = f(t)\mathbf{i} + g(t)\mathbf{j} + h(t)\mathbf{k}$$

where

- $f, g, h$ are components of the $\mathbf{r}(t)$

<br/>
