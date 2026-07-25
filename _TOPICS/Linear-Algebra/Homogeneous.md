# Homogeneous

A property under which scaling by a scalar preserves a single fixed degree for an expression that is used to classify polynomials and to simplify equations of one degree.

<i>

**definition [d]** (*Homogeneous Polynomial*) A property of a polynomial: every term has the same total degree $k$.

where

- $k$ is the common total degree of all terms.
- the polynomial is then said to be homogeneous of degree $k$.

Note:

- a quadratic form is a homogeneous polynomial of degree $2$.

</i>

<i>

**definition [d]** (*Homogeneous Function*) A property of a function $f$: scaling the input by $t$ scales the output by $t^{k}$,

- $f(tx) = t^{k}\, f(x)$ .

where

- $f$ is the function.
- $t$ is a scalar scaling factor.
- $k$ is the degree of homogeneity.
- $x$ is the input variable.

</i>

<i>

**definition [d]** (*Homogeneous Norm = Absolute Homogeneity*) A property of a norm $\lVert\,\cdot\,\rVert$ on a vector space:

- $\lVert \alpha x \rVert = |\alpha|\, \lVert x \rVert$

for every vector $x$ and every scalar $\alpha$.

where

- $\lVert\,\cdot\,\rVert$ is the norm.
- $x$ is a vector.
- $\alpha$ is a scalar.
- $|\alpha|$ is the absolute value of $\alpha$.

Note:

- this is one of the norm axioms.

</i>

<i>

**definition [d]** (*Homogeneous Linear Equation*) A property of a linear differential equation or linear algebraic system: the right-hand side is identically zero.

where

- the unknown appears linearly.
- the forcing term or inhomogeneous term vanishes.

Note:

- the same usage applies to systems of linear differential equations.

</i>

<i>

**definition [d]** (*Homogeneous Coordinates*) A representation of points of real projective space $\mathbb{RP}^{n}$ as lines through the origin in $\mathbb{R}^{n+1}$, written as equivalence classes $[x_{0}:x_{1}:\cdots:x_{n}]$.

where

- $\mathbb{RP}^{n}$ is real projective $n$-space.
- $[x_{0}:x_{1}:\cdots:x_{n}]$ are homogeneous coordinates.
- two tuples represent the same point when one is a nonzero scalar multiple of the other.

</i>

## Elementary Example
### Simple

A homogeneous expression keeps a single degree under scaling. The monomial $x^{2}$ is homogeneous of degree $2$.

$$
f(x) = x^{2}
$$

$$
f(tx) = t^{2} f(x)
$$

where

- $f$ is homogeneous of degree $2$.
- $t$ is a scalar.

### General

A sum of degree-$2$ terms in three variables is homogeneous of degree $2$.

$$
f(x,y,z) = x^{2} + 2xy + z^{2}
$$

$$
f(tx,ty,tz) = t^{2} f(x,y,z)
$$

where

- every term has total degree $2$.


## References

1. Dummit, D. S., & Foote, R. M. *Abstract Algebra*. Wiley, 2004. — homogeneous polynomials.
2. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — absolute homogeneity of a norm; homogeneous linear ODEs and systems.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier Academic Press, 2013. — homogeneous functions; homogeneous linear ODEs and PDEs.
4. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — homogeneous coordinates.
5. Shifrin, T., & Adams, M. *Linear Algebra: A Geometric Approach*. W. H. Freeman, 2010. — homogeneous coordinates on projective space.
