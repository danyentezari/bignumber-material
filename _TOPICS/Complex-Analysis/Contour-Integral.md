# Contour Integral

<i>

**definition [d]** (*Contour Integral = Complex Line Integral*) The integral of a complex function $f(z)$ along a contour $C$ in the complex plane, parametrized by $z(t)$ for $a \leq t \leq b$:

- $\displaystyle \int_{C} f(z)\, dz = \int_{a}^{b} f\!\bigl(z(t)\bigr)\, z'(t)\, dt$ .

where

- $C$ is a contour.
- $f$ is a complex-valued function.
- $z(t)$ is a parametrization of $C$.
- $z'(t) = dz/dt$.

Note:

- a contour is a path in the complex plane.
- $C$ is also written $\Gamma$.

</i>

<i>

**definition [d]** (*Contour Integral = Complex Line Integral*) The limit of Riemann sums of a complex function $f$ along a contour $C$ partitioned by points $z_{0},\ldots,z_{n}$ with sample points $\zeta_{j}$ on each arc:

- $\displaystyle \int_{C} f(z)\, dz = \lim \sum_{j=1}^{n} f(\zeta_{j})\,(z_{j} - z_{j-1})$ ,

where the limit is taken as the mesh of the partition tends to zero.

where

- $C$ is a contour in the complex plane.
- $f$ is a complex-valued function defined on $C$.

</i>

<i>

**definition [d]** (*Contour Integral = Complex Line Integral*) The integral of a complex function along a path $C$ in the complex plane:

- $\displaystyle \int_{C} f(z)\, dz = \int_{a}^{b} f\!\bigl(z(t)\bigr)\, z'(t)\, dt$ .

For a closed contour, the integral is often written $\displaystyle \oint_{C} f(z)\, dz$.

where

- $C$ is a contour; $z(t)$ for $a \leq t \leq b$ parametrizes $C$.
- $f$ is a complex-valued function.

</i>

## References

1. Complex-analysis sources in the notebook (e.g. Arfken; Riley–Hobson–Bence). — parametric and Riemann-sum definitions of the contour / complex line integral.
2. Stewart, J. *Calculus*. — does not use the term “contour integral”; closest notion is the line / path integral (see Line Integral).
