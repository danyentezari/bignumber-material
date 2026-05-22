# Topology

<i>

**definition** (*Topology*) A topology, $\mathcal{T}$, is a collection of subsets of X that satisfies the following conditions:

- Existence of the set. That is, $X$ is in $\mathcal{T}$.
- Existence of the empty set. That is, $\emptyset$ is in $\mathcal{T}$.
- Closure under finite intersections. That is, $U_1 \cap \dots \cap U_n$ is an element of $\mathcal{T}$.
- Closure under arbitrary unions. That is, $\bigcup_{\alpha \in A} U_\alpha$ is also an element of $\mathcal{T}$.

where

- $U_i$ are elements of $\mathcal{T}$
- $X$ is a set

</i>


### Manifolds

There are two main types of manifolds, generally: topological and smooth manifolds. We will start with an informal definition of a topological manifold. 

If a surface is a generalization of a curve, then a topological manifold is the generalization of both surfaces and curves.

Here's another way to understand a topological manifold.

A curve is a one-dimension manifold. <br/>
A surface is a two-dimension manifold.

Beyond two dimensions, we just call these things n-manifold, where $n$ is the number of dimensions.

Let's look at a more formal definition of a manifold. 

<i>

**definition** (*Topological Manifold*) A topological manifold is a topological space, $M$, that satisfies the following conditions:

- Locally Euclidean of Dimension $n$
- Hausdorff Space
- Second Countable

</i>


**definition** (*Smooth Manifold*) 


### Topological Spaces

<i>

**definition** (*Topological Space*) A topological space is a pair $(X, \mathcal{T})$ on $X$, where
- $X$ is a set
- $\mathcal{T}$ is a topology

</i>

**definition** (*Hausdorff Space*) A Hausdorff space is a topological space, $X$, that satisfies the following condition:

- Disjoint neighborhoods: $U_1 \cap U_2 = \empty$, for any pair of  points $p_1,p_2 \in X$

where

- $U_1, U_2$ are neighborhoods
- $p_1,p_2 \in X$ are distinct points
- $X$ is a topological space


<i>

**definition** (*Neighborhood*) A property of a subset $N$ of a topological space $X$ with respect to a point $p \in X$, where the following condition applies:

- There exists an open set $U$ such that $p \in U \subseteq N$.

where
- $X$ is a topological space.
- $p$ is a point in $X$.
- $N$ is a subset of $X$.
- $U$ is an open subset of $X$.
- Some authors define a neighborhood exclusively as an **open set** containing $p$, such that $N = U$.
  
</i>

### Homeomorphism

A description of a space that preserves the topological structure. An example is a sphere and a torus, which are homeomorphic to each other. By preserving the topological structure, we mean that the sphere and the torus have the same number of holes.


<i>

**definition** (*Homeomorphism*) A function between topological spaces $f: \mathbf{U} \to \mathbf{V}$ is called a homeomorphism if the following conditions hold.

- $f$ is a bijection and continuous
- $f^{-1}$ is continuous 

where
- $f^{-1}$ is the inverse of $f$
- $\mathbf{U}$, $\mathbf{V}$ are topological spaces.


</i>


### Open Sets

<i>

**definition** (*Open Set*) A subset $U$ of a topological space, $(X,\mathcal{T})$, where the following condition applies:

- $U \in \mathcal{T}$

where
- $X$ is a set
- $\mathcal{T}$ is a topology on $X$
- $U \subseteq X$

</i>

## APPENDIX

<i>

**definition** (*Continuity*) A property of a map between open subsets, 
$f: X \rightarrow Y$, where the following conditions apply:

- The preimage of every open subset of $Y$ is an open subset of $X$.

where
- $X, Y \subseteq \mathbb{R}^n$
- $f^{-1}(U) = \{x \in X : f(x) \in U\}$
- $f^{-1} : \mathcal{P}(Y) \rightarrow \mathcal{P}(X)$ is the preimage map from subsets of $Y$ to subsets of $X$.
- $U \subseteq Y$
- $\mathcal{P}(X)$ is the power set of $X$
  
</i>


<i>

**definition** (*Surjective*) A property of a function from a set $X$ to a set $Y$, 
$F: X \rightarrow Y$, where the following condition applies:

- For every element $y$ in $Y$, there exists an element $x$ in $X$ such that $F(x) = y$.

where
- $X$ is the domain of $F$
- $Y$ is the co-domain of $F$
- $F(X) = Y$ (the range of the function is equal to its co-domain).
- $F(X) = \{y \in Y : y = F(x) \text{ for some } x \in X\}$ is the image of $X$ under $F$.

</i>


<i>

**definition** (*Injective*) A property of a function from a set $X$ to a set $Y$, 
$F: X \rightarrow Y$, where the following condition applies:

- For all elements $x_1$ and $x_2$ in $X$, if $F(x_1) = F(x_2)$, then $x_1 = x_2$.

where
- $X$ is the domain of $F$.
- $Y$ is the co-domain of $F$.
- The condition is logically equivalent to saying that if $x_1 \neq x_2$, then $F(x_1) \neq F(x_2)$.
- For an injective function, each element of the co-domain is the image of at most one element of the domain.
  
</i>


<i>

**definition** (*Bijective*) A property of a function from a set $X$ to a set $Y$, 
$F: X \rightarrow Y$, where the following conditions apply:

- The function $F$ is injective
- The function $F$ is surjective

where
- $X$ is the domain of $F$.
- $Y$ is the co-domain of $F$
  
</i>


## GLOSSARY

**Smooth Manifold:** A smooth manifold is a manifold that is locally homeomorphic to a linear space, which is a vector space.



**Locally:** A description about how a manifold looks like around a point. When used, it means that it would take exactly $n$ points to describe the manifold around a point.



**Homeomorphic:** A description of a space that preserves the topological structure. An example is a sphere and a torus, which are homeomorphic to each other.



**Open Set:** A set that is not a subset of any other set.



**Holes:** The number of tori that can fit inside a manifold.



**Tori** A surface that looks like a donut. It has one hole.



**Topological Structure:** The properties of a space that are preserved under homeomorphisms, which is an operation that maps points in one space to points in another space while preserving the distance between points.



**Continuous Function:** A function that maps points in one space to points in another space while preserving the distance between points.



**Differential Form**




**Surface**

A two-dimensional geometric shape or boundary in three-dimensional space. It can be represented mathematically by functions or sets of points, ranging from simple flat planes to complex, curved manifolds.

**Piecewise Smooth** 

A surface is piecewise smooth if it consists of finitely many smooth portions. A common example of a piecewise smooth surface is the surface of a cube, which is composed of six smooth (flat) faces joined at edges


**Oriented Surface**

A surface where a consistent direction for the surface normal is chosen at every point. This distinguishes between the two sides, often designated as "inner" and "outer" or "positive" and "negative" orientations.


**Smooth Surface**

A surface is considered smooth if its surface normal depends continuously on the points of the surface. At every point P of such a surface, there exists a unique tangent plane and a unique normal whose direction varies continuously.


**Surface Normal**

A vector that is normal to a surface.


**Piecewise Smooth Simple Closed Curve**

A path that starts and ends at the same point without intersecting itself, consisting of several smooth segments joined together. Examples include the boundary of a square or a triangle.


**Differentiable Function**

A real function of a real variable that is differentiable that has, at all points, derivatives of all orders.


**Smooth Function**

A synonym for differentiable function.



**K-Covector**


**K-Covector field**

**K-Form**
Synonym for k-covector field

**K-Tensor**

**K-Fold**


**Bijection**

**Hausdorff Space**


**Onto** A synonym for surjective function.

**One-to-One** A synonym for an injective function.