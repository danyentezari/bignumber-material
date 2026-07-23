# Homogeneity

A property that says scaling an input by a scalar scales the value by a matching power of that scalar. Used to measure vector lengths consistently and to track degree under scaling.

<i>

**definition [d]** (*Homogeneity of Degree $k$*) A property of a function $f$: there is a fixed $k$ such that

- $f(tx) = t^{k}\, f(x)$

for all admissible scalars $t$ and inputs $x$.

where

- $f$ is the function.
- $k$ is the degree of homogeneity.
- $t$ is a scalar.
- $x$ is the input.

Note:

- when $k=1$, this is ordinary linear scaling of the output.

</i>

<i>

**definition [d]** (*Absolute Homogeneity*) A property of a norm or seminorm $\lVert\,\cdot\,\rVert$:

- $\lVert \alpha x \rVert = |\alpha|\, \lVert x \rVert$

for all vectors $x$ and scalars $\alpha$.

where

- $\lVert\,\cdot\,\rVert$ is the norm or seminorm.
- $x$ is a vector.
- $\alpha$ is a scalar.
- $|\alpha|$ is the absolute value of $\alpha$.

Note:

- Kreyszig lists this among the defining axioms of a norm.

</i>

<i>

**definition [d]** (*Homogeneity of a Polynomial*) A property of a polynomial: all of its terms share one common total degree.

where

- the shared total degree is the degree of homogeneity of the polynomial.

Note:

- this is the same condition used to call a polynomial homogeneous of degree $k$.

</i>

<i>

**definition [d]** (*Homogeneity of a Linear Equation*) A property of a linear equation or linear system: the inhomogeneous term is zero, so every scalar multiple of a solution remains a solution.

where

- the equation is linear in the unknown.
- the right-hand side vanishes.

</i>

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — absolute homogeneity of norms; homogeneous linear equations.
2. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier Academic Press, 2013. — homogeneity of degree $k$ for functions; homogeneous linear ODEs.
3. Dummit, D. S., & Foote, R. M. *Abstract Algebra*. Wiley, 2004. — homogeneous polynomials.
