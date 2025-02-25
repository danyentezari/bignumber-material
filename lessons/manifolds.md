# Manifolds

If a surface is a generalization of a curve, then a manifold is the generalization of both surfaces and curves.

Here's another way to understand a manifold.

A curve is a one-dimension manifold.
A surface is a two-dimension manifold.

Beyond two dimensions, we just call these things n-manifold, where $n$ is the number of dimensions.

**Smooth Manifold:** A smooth manifold is a manifold that is locally homeomorphic to a linear space, which is a vector space.

**Locally:** A description about how a manifold looks like around a point. When used, it means that it would take exactly $n$ points to describe the manifold around a point.

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



**Open Set:** A set that is not a subset of any other set.

**Holes:** The number of tori that can fit inside a manifold.

**Tori** A surface that looks like a donut. It has one hole.

**Topological Structure:** The properties of a space that are preserved under homeomorphisms, which is an operation that maps points in one space to points in another space while preserving the distance between points.

**Continuous Function:** A function that maps points in one space to points in another space while preserving the distance between points.

**Differential Form**