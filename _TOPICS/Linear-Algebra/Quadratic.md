# Quadratic

A polynomial of degree two that is homogeneous of degree two that is used to express quadratic size and energy-type expressions in several variables.

<i>

**definition [d]** (*Quadratic Form*) A homogeneous polynomial of degree $2$ in several variables.

where

- the polynomial is homogeneous of degree $2$.
- the variables are the coordinates on the underlying vector space.

Note:

- quadratic integrability concerns the power $2$ in $|f|^{2}$, not this algebraic form.

</i>

## Elementary Example
### Simple

A quadratic form is a homogeneous polynomial of degree $2$.

$$
q(x,y) = x^{2} + xy + y^{2}
$$

$$
q(tx,ty) = t^{2} q(x,y)
$$

where

- $q$ is the quadratic form.
- $x, y$ are the variables.

### General

In three variables, a quadratic form is determined by a symmetric $3 \times 3$ matrix.

$$
q(x) = x^{T} A x,\quad
A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & 4 \end{pmatrix}
$$

$$
q(x_{1},x_{2},x_{3}) = 2 x_{1}^{2} + 3 x_{2}^{2} + 4 x_{3}^{2} + 2 x_{1} x_{2} + 2 x_{2} x_{3}
$$

where

- $A$ is a symmetric matrix.
- $x$ is a column vector of variables.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — quadratic form as homogeneous polynomial of degree $2$.
