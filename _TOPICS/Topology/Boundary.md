# Boundary

A boundary is a closed set of elements associated with a subset that is used to define the limit of a neighborhood where a function of a variable has a constant scalar value.

<i>

**definition [d]** (*Boundary = Topological Boundary*) From Nash and Sen: the boundary of a set $U'$, written $b(U')$, is the complement of the interior of $U'$ in the closure of $U'$:

- $b(U') = \overline{U'} \setminus U'^{\circ}$ .

where

- $U'$ is a subset of a topological space.
- $U'^{\circ}$ is the interior of $U'$.
- $\overline{U'}$ is the closure of $U'$.
- $b(U')$ is the boundary of $U'$.

Note:

- Nash and Sen: if $U = [a,b)$ on the real line $\mathbb{R}$, then $U^{\circ} = (a,b)$ and $\overline{U} = [a,b]$, so $b(U) = \{a,b\}$.
- Nash and Sen: the sets $(a,b)$, $[a,b]$, $[a,b)$, and $(a,b]$ all have the same boundary $\{a,b\}$.
- Nash and Sen: $U^{\circ} = U$ if and only if $U$ is open.

</i>

<i>

**definition [d]** (*Boundary = Manifold Boundary*) From Lee: an $n$-dimensional manifold with boundary is a second countable Hausdorff space in which every point has a neighborhood homeomorphic either to an open subset of $\mathbb{R}^{n}$ or to an open subset of the closed upper half-space

- $\mathbb{H}^{n} = \{ (x_{1},\ldots,x_{n}) \in \mathbb{R}^{n} : x_{n} \ge 0 \}$ .

If $M$ is an $n$-manifold with boundary, a point $p \in M$ is called an interior point of $M$ if it is in the domain of an interior chart, and a boundary point of $M$ if it is in the domain of a boundary chart that takes $p$ to $\partial \mathbb{H}^{n}$. The boundary of $M$, denoted $\partial M$, is the set of all its boundary points, and its interior, denoted $\operatorname{Int} M$, is the set of all its interior points. Every point of $M$ is either an interior point or a boundary point.

where

- $M$ is an $n$-manifold with boundary.
- $\mathbb{H}^{n}$ is the closed upper half-space in $\mathbb{R}^{n}$.
- $\partial M$ is the manifold boundary of $M$.
- $\operatorname{Int} M$ is the manifold interior of $M$.

Note:

- Lee: despite the terminology, a manifold with boundary is not necessarily a manifold.

</i>

## References

1. Nash, C., & Sen, S. *Topology and Geometry for Physicists*. Academic Press, 1983. — $b(U') = \overline{U'} \setminus U'^{\circ}$; example $U=[a,b)$ gives $b(U)=\{a,b\}$.
2. Lee, J. M. *Introduction to Topological Manifolds*. Springer. — $\mathbb{H}^{n}$; manifold with boundary; interior point; boundary point; $\partial M$; $\operatorname{Int} M$.
