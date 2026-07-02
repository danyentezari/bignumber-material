# Topology

<i>

**definition** (_Topology_) A topology, $\mathcal{T}$, is a collection of subsets of X that satisfies the following conditions:

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

Beyond two dimensions, we just call these things n-manifold, where

* $n$ is the number of dimensions.

Let's look at a more formal definition of a manifold.

<i>

**definition** (_Topological Manifold_) A topological manifold is a topological space, $M$, that satisfies the following conditions:

- Locally Euclidean of Dimension $n$
- Hausdorff Space
- Second Countable

</i>

**definition** (_Smooth Manifold_)

### Topological Spaces

<i>

**definition** (_Topological Space_) A topological space is a pair $(X, \mathcal{T})$ on $X$, where

- $X$ is a set
- $\mathcal{T}$ is a topology

</i>

**definition** (_Hausdorff Space_) A Hausdorff space is a topological space, $X$, that satisfies the following condition:

- Disjoint neighborhoods: $U_1 \cap U_2 = \empty$, for any pair of points $p_1,p_2 \in X$

where

- $U_1, U_2$ are neighborhoods
- $p_1,p_2 \in X$ are distinct points
- $X$ is a topological space

<i>

**definition** (_Neighborhood_) A property of a subset $N$ of a topological space $X$ with respect to a point $p \in X$, where

* the following condition applies:

- There exists an open set $U$ such that $p \in U \subseteq N$.

where

- $X$ is a topological space.
- $p$ is a point in $X$.
- $N$ is a subset of $X$.
- $U$ is an open subset of $X$.
</i>

### Homeomorphism

A description of two spaces that have the same topological structure. 

Now about something called topological invariants.

Properties (such as numbers, groups, matrices, or vector spaces) of a topological space that are preserved by homeomorphisms. If two spaces possess different invariants, they cannot be topologically equivalent. Examples include the fundamental group, homology groups, and the Euler characteristic.

<i>

**definition** (_Homeomorphism_) A function between topological spaces $f: \mathbf{U} \to \mathbf{V}$ is called a homeomorphism if the following conditions hold.

- $f$ is a bijection and continuous
- $f^{-1}$ is continuous

where

- $f^{-1}$ is the inverse of $f$
- $\mathbf{U}$, $\mathbf{V}$ are topological spaces.

</i>

### Open Sets

The open set is central to topology, and it is required for definitions. We begin with a definition and then an example.

<i>

**definition** (_Open Set_) A subset $U$ of a topological space, $(X,\mathcal{T})$, where

* the following condition applies:

- $U \in \mathcal{T}$

where

- $X$ is a set
- $\mathcal{T}$ is a topology on $X$
- $U \subseteq X$

</i>

<i>

**example** (_Open Set_) Let

$$
X = \{1,2,3\}
$$

$$
\mathcal{T}
=
\{
\emptyset,
\{1\},
\{1,2\},
X
\}.
$$

Then, $(X,\mathcal{T})$ is a topological space, where

*$$
(X,\mathcal{T})
=
\left(
\{1,2,3\},
\{
\emptyset,
\{1\},
\{1,2\},
\{1,2,3\}
\}
\right)
$$


Let

$$
U = \{1,2\}.
$$

Since

$$
U \in \mathcal{T},
$$

it follows that $U$ is an open set.

Therefore,

$$
\{1,2\}
$$

is an open set in $(X,\mathcal{T})$.

</i>

## APPENDIX


### Preimages and Inverse Functions


<i>

**definition** (*Inverse function*) A function from the codomain of a function to its domain,

$$
f^{-1} : Y \rightarrow X,
$$

where

* the following condition applies:

- $f^{-1}(y) = x \iff f(x) = y$.

where

- $f : X \rightarrow Y$ is a one-to-one and onto function.
- $X$ is the domain of $f$.
- $Y$ is the codomain of $f$.
- $x \in X, y \in Y$.

</i>

<i>

**definition** (*Preimage*) A subset of the domain of a function,

$$
f^{-1}(Y_{subset}) \subseteq X,
$$

where

* the following condition applies:

- $f^{-1}(Y_{subset}) = \{x \in X : f(x) \in Y_{subset}\}$.

where

- $f : X \rightarrow Y$ is a function.
- $X$ is the domain of $f$.
- $Y$ is the codomain of $f$.
- $Y_{subset} \subseteq Y$.

</i>



<i>

**definition** (_Continuity_) A property of a map between open subsets,
$f: X \rightarrow Y$, where

* the following conditions apply:

- The preimage of every open subset of $Y$ is an open subset of $X$.

where

- $X, Y \subseteq \mathbb{R}^n$
- $f^{-1}(U) = \{x \in X : f(x) \in U\}$
- $f^{-1} : \mathcal{P}(Y) \rightarrow \mathcal{P}(X)$ is the preimage map from subsets of $Y$ to subsets of $X$.
- $U \subseteq Y$
- $\mathcal{P}(X)$ is the power set of $X$

</i>

<i>

**definition** (_Surjective_) A property of a function from a set $X$ to a set $Y$,
$F: X \rightarrow Y$, where

* the following condition applies:

- For every element $y$ in $Y$, there exists an element $x$ in $X$ such that $F(x) = y$.

where

- $X$ is the domain of $F$
- $Y$ is the co-domain of $F$
- $F(X) = Y$ (the range of the function is equal to its co-domain).
- $F(X) = \{y \in Y : y = F(x) \text{ for some } x \in X\}$ is the image of $X$ under $F$.

</i>

<i>

**definition** (_Injective_) A property of a function from a set $X$ to a set $Y$,
$F: X \rightarrow Y$, where

* the following condition applies:

- For all elements $x_1$ and $x_2$ in $X$, if $F(x_1) = F(x_2)$, then $x_1 = x_2$.

where

- $X$ is the domain of $F$.
- $Y$ is the co-domain of $F$.
- The condition is logically equivalent to saying that if $x_1 \neq x_2$, then $F(x_1) \neq F(x_2)$.
- For an injective function, each element of the co-domain is the image of at most one element of the domain.

</i>

<i>

**definition** (_Bijective_) A property of a function from a set $X$ to a set $Y$,
$F: X \rightarrow Y$, where

* the following conditions apply:

- The function $F$ is injective
- The function $F$ is surjective

where

- $X$ is the domain of $F$.
- $Y$ is the co-domain of $F$

</i>

## GLOSSARY

**Smooth Manifold:** -

**Locally:** -

**Homeomorphic:** A description of two spaces that have the same topological structure.

**Genus** 

**Holes:** An informal synonym for genus.

**Tori** A surface that looks like a donut. It has one hole.

**Topological Structure:** -

**Continuous Function:** -

**Differential Form** A function assigning an alternating k-linear function to each point of an open set or manifold.

**Surface** 
A 2-dimensional manifold, an object modeled locally on $\mathbb{R}^2$, specifying points with two independent parameters.

**Piecewise Smooth** 
A property of curves or surfaces composed of finitely many smooth segments meeting at corners or edges.

**Oriented Surface** A surface with a consistent choice of orientation at each point, typically specified by a nowhere

-vanishing 2-form.

**Smooth Surface** A 2-dimensional manifold equipped with a differentiable structure, allowing for calculus and well-defined tangent spaces.

**Surface Normal:** 

**Piecewise Smooth Simple Closed Curve** A non-self-intersecting closed path consisting of finitely many differentiable segments joined end-to-end.

**Open Set:**
A set that is open in a topological space.

**Open Set (Expanded):**
A subset of a topological space that contains a neighborhood around every one of its points.

**Differentiable Function** -

**Smooth Function** -

**K-Covector** An alternating $k$-linear function on a vector space, also known as a multicovector of degree $k$.

**K-Covector field = K-Form** A function assigning a $k$-covector to each point of a manifold, also called a differential $k$-form.

**K-Tensor** A multilinear function from the $k$-fold product of a vector space to the real numbers.

**K-Fold** A term denoting the repetition of a set or space $k$ times, typically within a Cartesian product.

**K-linear** A synonym for multilinear function.

**K-Fold product** The Cartesian product of $k$ copies of a set $X$, often denoted simply as $X^k$.

**Bijection** A function that is both injective and surjective, also referred to as a one-to-one correspondence.

**Hausdorff Space** A topological space where

* any two distinct points can be separated by disjoint open neighborhoods.

**Onto** A synonym for surjective function.

**One-to-One** A synonym for an injective function.

**Covariant vector = Covector = 1-form** 

