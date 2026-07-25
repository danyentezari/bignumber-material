# Boundary Operation

A mapping that sends a domain to its edge that is used to relate a definite integral over a domain to a definite integral on that edge.

Note: Also written $\partial$. Also called boundary operator.

<i>

**definition [d]** (*Boundary Operation = Boundary Operator = $\partial$*) From Emam: in more advanced discussions, the symbol $\partial$ is treated as an operator—a sort of derivative—and it has the property of being nilpotent, which means that applying it twice always vanishes:

- $\partial^{2} = 0$ .

where

- $\partial$ is the boundary operation.
- $\partial M$ is the edge of a manifold or domain $M$.
- $\partial^{2} = 0$ means the edge of an edge is empty.

</i>

<i>

**definition [d]** (*Boundary Operation*) From Gowers: in Stokes’s theorem,

- $\displaystyle \int_{S} d\omega = \int_{\partial S} \omega$

for an oriented manifold $S$ and form $\omega$, where $\partial S$ is the oriented boundary of $S$. Differentiation $\omega \mapsto d\omega$ is the adjoint of the boundary operation.

where

- $\partial S$ is the edge of $S$ under the boundary operation.
- $d\omega$ is the exterior derivative of $\omega$.

</i>

A mapping associates a function with another function. Under this mapping, the definite integral of a derivative over a domain has the same value as the definite integral of the function over the edge of the domain that is used to find a solution to an equation.

<i>

**definition [d]** (*Boundary Operation*) From Gowers, stated with elementary terms: an equation relates the definite integral of a derivative over a domain to the definite integral over its edge,

- $\displaystyle \int_{D} Df = \int_{\partial D} f$ .

where

- both integrals are definite integrals.
- $D$ is the domain, the set on which the definite integral of the derivative is taken.
- $\partial D$ is the edge of the domain under the boundary operation.
- $f$ is the function whose values appear in the definite integral on the edge.
- $Df$ is the derivative of $f$, which appears in the definite integral over the domain.
- $\partial$ denotes the boundary operation.

</i>

## Examples

Before the boundary operation acts, one has a domain set $A$. After the boundary operation acts, one has an edge set $B = \partial A$. Stokes’s theorem then relates a definite integral over $A$ to a definite integral over $B$.

<i>

**example 1 [d]** (**Closed interval to endpoints** — Nash and Sen; Emam) Before: take the domain set

- $A = [a,b] = \{ x \in \mathbb{R} : a \le x \le b \}$ .

After: the boundary operation sends $A$ to the edge set of endpoints

- $B = \partial A = \{ a, b \}$ .

Nash and Sen record the same edge for the half-open interval: if $U = [a,b)$, then $U^{\circ} = (a,b)$ and $\overline{U} = [a,b]$, so $b(U) = \overline{U} - U^{\circ} = \{ a, b \}$. Emam states the same passage of sets in manifold language: if $M = [a,b]$, then $\partial M$ has dimension zero and is the pair of points $\{ a, b \}$.

where

- $A$ is the domain set before $\partial$ acts.
- $B = \partial A$ is the edge set after $\partial$ acts.
- $a$ and $b$ are real numbers with $a < b$.

</i>

<i>

**example 2 [d]** (**Closed unit disk to circle** — Lee) Before: take the domain set

- $A = \overline{B}^{2} = \{ x \in \mathbb{R}^{2} : |x| \le 1 \}$ .

After: the boundary operation sends $A$ to the unit circle

- $B = \partial A = S^{1} = \{ x \in \mathbb{R}^{2} : |x| = 1 \}$ .

Lee: the closed unit disk $\overline{B}^{2}$ is a manifold with boundary whose manifold boundary is the circle. Its topological boundary as a subset of $\mathbb{R}^{2}$ is that same circle.

where

- $A$ is the domain set before $\partial$ acts.
- $B = \partial A$ is the edge set after $\partial$ acts.
- $|x|$ is the Euclidean length of $x$.

</i>

<i>

**example 3 [d]** (**Upper half-space to hyperplane** — Lee) Before: take the domain set

- $A = \mathbb{H}^{n} = \{ (x_{1},\ldots,x_{n}) \in \mathbb{R}^{n} : x_{n} \ge 0 \}$ .

After: the boundary operation sends $A$ to

- $B = \partial A = \partial \mathbb{H}^{n} = \{ (x_{1},\ldots,x_{n}) \in \mathbb{R}^{n} : x_{n} = 0 \}$ .

where

- $A$ is the domain set before $\partial$ acts.
- $B = \partial A$ is the edge set after $\partial$ acts.
- $n$ is a natural number with $n > 0$.

</i>

<i>

**example 4 [d]** (**Edge of an edge is empty** — Emam; Nakahara) Apply $\partial$ twice to a solid ball. Before the first application,

- $A = D^{3}$

is the solid ball. After one application,

- $B = \partial A = S^{2}$

is the sphere. After a second application the edge of that edge is empty:

- $\partial B = \partial^{2} A = \emptyset$ .

Emam: the boundary of a boundary is always vanishing; a closed manifold such as a circle has empty boundary, written $\partial M = 0$, and $\partial^{2} = 0$. The same holds for a sphere. Nakahara: the boundary of the solid ball $D^{3}$ is the sphere $S^{2}$, and the boundary of the sphere is an empty set.

where

- $A$ is the domain set before $\partial$ acts.
- $B = \partial A$ is the edge set after one application of $\partial$.
- $\partial^{2} A = \emptyset$ is the result after $\partial$ acts on $B$.

</i>

<i>

**example 5 [d]** (**Before and after in Stokes’s theorem** — Gowers) Before: a definite integral is taken over a domain set $A = D$. After the boundary operation produces $B = \partial D$, Stokes’s theorem moves that definite integral onto the edge set:

- $\displaystyle \int_{A} d\omega = \int_{B} \omega = \int_{\partial D} \omega$ .

The sets alone change from $A$ to $B = \partial A$; the equality says the two definite integrals have the same value.

where

- $A = D$ is the domain set before the move.
- $B = \partial D$ is the edge set after $\partial$ acts.
- both integrals are definite integrals.

</i>


## Elementary Example

The boundary operation sends a domain set to its edge set. Applying it twice yields the empty set.

$$
\partial : A \mapsto B
$$

$$
A = \{ a,\ b,\ c,\ d \}
$$

$$
B = \partial A = \{ a,\ b \}
$$

$$
\partial B = \partial^{2} A = \emptyset
$$

## References

1. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — $\partial$ as a nilpotent operator; $\partial^{2}=0$; line segment to endpoints.
2. Gowers, T., Barrow-Green, J., & Leader, I. (eds.). *The Princeton Companion to Mathematics*. Princeton University Press, 2008. — boundary operation in Stokes’s theorem; adjoint of differentiation.
3. Lee, J. M. *Introduction to Topological Manifolds*. Springer, 2011. — closed unit disk to circle; $\mathbb{H}^{n}$ to $\partial \mathbb{H}^{n}$.
4. Nash, C., & Sen, S. *Topology and Geometry for Physicists*. Academic Press, 1983. — $b(U) = \{ a, b \}$ for an interval.
5. Nakahara, M. *Geometry, Topology and Physics*. Institute of Physics Publishing, 2003. — $\partial D^{3} = S^{2}$ and $\partial S^{2}$ empty.
