# Electromagnetism

## Maxwell's Equations

Maxwell's equations express, formally, the properties of electromagnetic waves.

1. Gauss’s Law for Electricity
$$ \nabla \cdot \mathbf{D} = \rho_v $$

2. Gauss’s Law for Magnetism
$$ \nabla \cdot \mathbf{B} = 0 $$

3. Faraday’s Law
$$ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} $$

4. Ampere-Maxwell Law
$$ \nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t} $$

Where
- $\nabla$ = Vector differential operator.
- $\mathbf{D}$ = Electric flux density.
- $\mathbf{B}$ = Magnetic flux density.
- $\mathbf{E}$ = Electric field intensity.
- $\mathbf{H}$ = Magnetic field intensity.
- $\rho_v$ = Volume charge density.
- $\mathbf{J}$ = Current density.
- $\frac{\partial \mathbf{D}}{\partial t}$ = Displacement current density.

<br/>

## Stoke's Theorem Physics

Stokes' theorem relates the circulation of a vector field $\mathbf{A}$ around a closed path $L$ to the surface integral of its curl over an open surface $S$ bounded by $L$ [1]:

$$ \int_S (\nabla \times \mathbf{A}) \cdot d\mathbf{S} = \oint_L \mathbf{A} \cdot d\mathbf{l}$$

Where:
*   $d\mathbf{S}$ is the surface element vector [1].
*   The orientation follows the **right-hand rule** [2].

<br/>

## Stoke's Theorem for Flux Integral

$$\iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n} \, dA = \oint_C \mathbf{F} \cdot \mathbf{r}'(s) \, ds$$.

Or,

$$\iint_S (\text{curl} \times \mathbf{F}) \cdot \mathbf{n} \, dA = \oint_C \mathbf{F} \cdot \mathbf{r}'(s) \, ds$$.

In this formula:
* $S$ a piecewise smooth oriented surface in space
* $C$ a piecewise smooth simple closed curve boundary of $S$
* $\mathbf{n}$ is the unit normal vector of $S$.
* $\mathbf{r}'(s)$ is the unit tangent vector of $C$.
* $s$ is the arc length of $C$.
* $\mathbf{F}(x, y, z)$ is a continuous vector function

<br/>

## Surface Integrals and Fundamental Theorem of Calculus

$$\int_D d\omega = \int_{\partial D} \omega$$

Where

* $\omega$: A differential $(k-1)$-form.
* $d\omega$: The exterior derivative of the form $\omega$.
* $D$: A $k$-dimensional domain of integration.
* $\partial D$: The oriented boundary of the domain $D$.



<br/>

## Special Relativity and Electric Fields

Changes in the electric field cause changes in the magnetic field. According to special relativity, a magnetic field is actually an electric field distorted by the motion of electrons. 



<br/><br/><br/>




## Glossary

**Principle of Superposition**

See Physics Mathemematical Appendix.


**Electromagnetism** The phenomena of interactions between charges at rest and in motion.

**Electromagnetic Waves** Oscillations of electric and magnetic fields that propagate through space without the need for charges or currents.

**Reference Frame** A coordinate system where measurements can be made about the time and position about objects.

**Inertial Reference Frame**
A reference frame based on Newton's First Law, where all objects are at rest or in motion unless influenced by external force.

**Phase**
![](https://www.researchgate.net/profile/Irene-Van-De-Vijver/publication/336862739/figure/fig2/AS:839368331784194@1577132413781/A-Oscillations-are-characterized-by-their-frequency-the-number-of-cycles-per-time.ppm)

**Gradient** 

$\nabla V$ Operating on a scalar function $V$ produces a vector field.

**Divergence** 

$\nabla \cdot \mathbf{A}$ The dot product of the operator with a vector field $\mathbf{A}$ yields a scalar field.

**Curl** 

$\nabla \times \mathbf{A}$ The cross product of the operator with a vector field $\mathbf{A}$ results in another vector field.

**Laplacian** 

$\nabla^2 V$ This operator represents the divergence of the gradient ($\nabla \cdot \nabla V$).


<br/><br/><br/>

## Mathemematics Appendix


**Stoke's Theorem**

Let $S$ be a piecewise smooth oriented surface in space, and let the boundary of $S$ be a piecewise smooth simple closed curve $C$. If  with continuous first partial derivatives in a domain containing $S$, then:

$$\iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n} \, dA = \oint_C \mathbf{F} \cdot \mathbf{r}'(s) \, ds$$.

Or,

$$\iint_S (\text{curl} \times \mathbf{F}) \cdot \mathbf{n} \, dA = \oint_C \mathbf{F} \cdot \mathbf{r}'(s) \, ds$$.

In this formula:
* $\mathbf{n}$ is the unit normal vector of $S$.
* $\mathbf{r}'(s)$ is the unit tangent vector of $C$.
* $s$ is the arc length of $C$.
* $\mathbf{F}(x, y, z)$ is a continuous vector function
  

**Surface**

A two-dimensional geometric shape or boundary in three-dimensional space. It can be represented mathematically by functions or sets of points, ranging from simple flat planes to complex, curved manifolds.

**Piecewise smooth** 

A surface is piecewise smooth if it consists of finitely many smooth portions. A common example of a piecewise smooth surface is the surface of a cube, which is composed of six smooth (flat) faces joined at edges.

**Oriented surface**

A surface where a consistent direction for the surface normal is chosen at every point. This distinguishes between the two sides, often designated as "inner" and "outer" or "positive" and "negative" orientations.

**Smooth surface**

A surface is considered smooth if its surface normal depends continuously on the points of the surface. At every point P of such a surface, there exists a unique tangent plane and a unique normal whose direction varies continuously.

**Surface Normal**

A vector that is normal to a surface.

**Piecewise smooth simple closed curve**

A path that starts and ends at the same point without intersecting itself, consisting of several smooth segments joined together. Examples include the boundary of a square or a triangle.


**Flux** 

Total amount of a field or fluid passing through a surface.

**Double Integral**

The double integral is defined by the following identity:
$$\iint_R f(x, y) \, dA = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*) \Delta A$$.

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

- $\nabla$ is the vector differential operator, commonly referred to as del or nabla.

- $\dfrac{\partial}{\partial x}, \dfrac{\partial}{\partial y}, \text{ and } \dfrac{\partial}{\partial z}$ are partial derivatives.

- $\mathbf{i}, \mathbf{j}, \text{ and } \mathbf{k}$ are the standard basis unit vectors pointing in the positive directions of the $x, y, \text{ and } z$ axes, respectively

<br/>

**Curl**

Let $\mathbf{v}(x, y, z)$ be a differentiable vector function expressed in Cartesian coordinates with components $[v_1, v_2, v_3]$, such that: $$\mathbf{v} = v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$$
The curl of $\mathbf{v}$ (also denoted as $\nabla \times \mathbf{v}$ or $\text{rot } \mathbf{v}$) is defined by the following symbolic determinant: $$\text{curl } \mathbf{v} = \nabla \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ v_1 & v_2 & v_3 \end{vmatrix}$$

**Divergence**

<br/>


**Differentiation of Vector**

$$\mathbf{v}'(t) = \lim_{\Delta t \to 0} \frac{\mathbf{v}(t + \Delta t) - \mathbf{v}(t)}{\Delta t}$$. 


<br/>

**Vector Function**

$$\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle = f(t)\mathbf{i} + g(t)\mathbf{j} + h(t)\mathbf{k}$$

where
- $f, g, h$ are components of the $\mathbf{r}(t)$

<br/>

**K-form**

<br/>

<br/><br/><br/>

## Physics Mathemematical Appendix

**Principle of Superposition**

$$D_\text{net} = D_{1}+D_{2}+\cdots=\sum_{i}D$$

where
- $D_{i}$ is the displacement caused by each wave
