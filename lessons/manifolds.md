# Manifolds

If a surface is a generalization of a curve, then a manifold is the generalization of both surfaces and curves.

Here's another way to understand a manifold.

A curve is a one-dimension manifold.
A surface is a two-dimension manifold.

Beyond two dimensions, we just call these things n-manifold, where $n$ is the number of dimensions.

<br/>


**Smooth Manifold:** A smooth manifold is a manifold that is locally homeomorphic to a linear space, which is a vector space.

<br/>


**Locally:** A description about how a manifold looks like around a point. When used, it means that it would take exactly $n$ points to describe the manifold around a point.

<br/>


**Homeomorphic:** A description of a space that preserves the topological structure. An example is a sphere and a torus, which are homeomorphic to each other. By preserving the topological structure, we mean that the sphere and the torus have the same number of holes.

Let's look at a more formal definition of a manifold. Let $U \subseteq \mathbb{R}^n$ and $V \subseteq \mathbb{R}^m$. A function $f: U \to V$ is called a homeomorphism if it is a bijection and its inverse is continuous. Here, continuous means that for any open set $V \subseteq \mathbb{R}^m$, both $U$ and $V$ are open in $\mathbb{R}^n$ and, to each other, their domains and codomains remain open after the function is applied.

Now let's see homeomorphism in Python.



```
# Example of a homeomorphism in Python

# Define two lists representing subsets of R^n and R^m
U = [1, 2, 3, 4, 5]  # Subset of R^1
V = [2, 4, 6, 8, 10]  # Subset of R^1

# Define a homeomorphic function f: U -> V
def f(x):
    return 2 * x

# Define the inverse function f^(-1): V -> U
def f_inverse(y):
    return y // 2

# Demonstrate the homeomorphism
print("Original U:", U)
print("Mapped to V:", [f(x) for x in U])
print("Original V:", V)
print("Mapped back to U:", [f_inverse(y) for y in V])

# Check if f is bijective (one-to-one and onto)
is_bijective = len(set([f(x) for x in U])) == len(U) == len(V)
print("Is f bijective?", is_bijective)

f and f_inverse are continuous because they are linear functions since they are just multiplying by a constant.
```

<br/>


**Open Set:** A set that is not a subset of any other set.

<br/>


**Holes:** The number of tori that can fit inside a manifold.

<br/>


**Tori** A surface that looks like a donut. It has one hole.

<br/>


**Topological Structure:** The properties of a space that are preserved under homeomorphisms, which is an operation that maps points in one space to points in another space while preserving the distance between points.

<br/>


**Continuous Function:** A function that maps points in one space to points in another space while preserving the distance between points.

<br/>


**Differential Form**


<br/>


**surface**

A two-dimensional geometric shape or boundary in three-dimensional space. It can be represented mathematically by functions or sets of points, ranging from simple flat planes to complex, curved manifolds.

**piecewise smooth** 

A surface is piecewise smooth if it consists of finitely many smooth portions. A common example of a piecewise smooth surface is the surface of a cube, which is composed of six smooth (flat) faces joined at edges

<br/>

**oriented surface**

A surface where a consistent direction for the surface normal is chosen at every point. This distinguishes between the two sides, often designated as "inner" and "outer" or "positive" and "negative" orientations.

<br/>

**smooth surface**

A surface is considered smooth if its surface normal depends continuously on the points of the surface. At every point P of such a surface, there exists a unique tangent plane and a unique normal whose direction varies continuously.

<br/>

**surface normal**

A vector that is normal to a surface.

<br/>

**piecewise smooth simple closed curve**

A path that starts and ends at the same point without intersecting itself, consisting of several smooth segments joined together. Examples include the boundary of a square or a triangle.

<br/>
