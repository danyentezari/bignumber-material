# Boundary Conditions

A constraint on a solution at the edge of a domain that is used to select a unique solution of a differential equation, where a domain is a region on which the unknown function is defined.

The boundary-value problem. A boundary-value problem is a differential equation together with constraints specified at the boundary of the domain. A boundary is the edge of the domain. This principle is used to model steady processes whose data are given on that edge.

The Dirichlet boundary condition. A Dirichlet condition specifies the exact value that the unknown solution must take on the boundary. A homogeneous Dirichlet condition forces the solution to vanish at the endpoints. This principle is used to model systems with fixed edges.

A homogeneous Dirichlet condition is

$$
y(a) = y(b) = 0
$$

where

- $y$ is the unknown solution.
- $a$ and $b$ are endpoints of the interval.

The Neumann boundary condition. A Neumann condition specifies the derivative of the solution perpendicular to the boundary. A normal derivative is that perpendicular rate of change. This principle is used to model a specified flux through a wall.

The mixed boundary condition. A mixed condition applies a Dirichlet constraint on one part of the boundary and a Neumann constraint on another part. This principle is used to model a body whose edges are not all of one kind.

The Sturm–Liouville problem. A Sturm–Liouville problem is a homogeneous second-order linear equation with homogeneous boundary conditions. It yields a complete set of orthogonal eigenfunctions. This principle is used to expand solutions of the wave equation and the diffusion equation.

The Green’s function method. A Green’s function $G(x,z)$ is the response to a concentrated source that already obeys the homogeneous boundary conditions. For $y(a)=y(b)=0$ one also demands $G(a,z)=G(b,z)=0$. This principle is used to write the solution of an inhomogeneous problem as an integral against $G$.

Note: Also called a boundary-value problem when the differential equation and the boundary data are taken together. A Dirichlet condition is also called the first boundary-value problem. A Neumann condition is also called the second boundary-value problem.

## References

1. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — boundary conditions; homogeneous cases $y(a)=y(b)=0$; Green’s function.
2. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — Neumann and mixed boundary problems.
3. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — Dirichlet, Neumann, and Sturm–Liouville problems.
