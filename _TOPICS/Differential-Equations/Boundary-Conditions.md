# Boundary Conditions

An equation that relates a derivative of a function at the edge of a domain to a value of the function is used to find a solution.

<i>

**definition [d]** (*Boundary Conditions*) From Riley, Hobson, and Bence: requirements that the general solution $y(x)$ obeys at specified points of the domain. For homogeneous boundary conditions, in which $y(x)$ and its derivatives are required to be zero at specified points, this may be arranged by demanding that a Green’s function $G(x,z)$ itself obeys the boundary conditions when considered as a function of $x$ alone. For example, if we require $y(a) = y(b) = 0$, then we also demand $G(a,z) = G(b,z) = 0$.

where

- $y$ is the unknown solution function.
- $a$ and $b$ are endpoints of the range.
- $G(x,z)$ is a Green’s function.

Note:

- Riley et al.: one boundary condition must be specified at each end of the range in the standard Sturm–Liouville setting they discuss.

</i>

<i>

**definition [d]** (*Boundary Conditions*) From Kreyszig: data given on the boundary of a region for a partial differential equation problem. In Neumann and mixed problems there are boundary points at which the outer normal derivative of the solution is given, while the solution $u$ itself is not given at those points.

where

- $u$ is the unknown solution.
- Neumann data prescribe a normal derivative on the boundary.

</i>

## References

1. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — boundary conditions; homogeneous cases $y(a)=y(b)=0$.
2. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — Neumann and mixed boundary problems.
