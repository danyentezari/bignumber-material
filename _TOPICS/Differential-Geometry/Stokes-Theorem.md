# Stoke's Theorem and the Fundamental Theorem of Calculus

An equation that relates a definite integral of a derivative over a domain to a definite integral on the edge of that domain that is used to move a definite integral from a domain onto its edge.

The edge of a domain is the geometric boundary of the region of integration. For a surface, that edge is the simple closed curve that bounds the surface, like the wire loop holding a soap film. In higher dimension, the edge is a lower-dimensional boundary of the domain. Arfken describes this edge for a surface as the perimeter bounding the surface.

Stoke's Theorem is given by,

$$\int_D d\omega = \int_{\partial D} \omega$$

where

* $\omega$: A differential $(k-1)$-form.
* $d\omega$: The exterior derivative of the form $\omega$.
* $D$: A $k$-dimensional domain of integration.
* $\partial D$: The oriented boundary of the domain $D$.

<br/>

Stoke's Theorem is about manifolds, which are locally Euclidean. The integration applies to differential forms on those local regions. Differential forms are operators that allow applying calculus independent of any specific coordinate system.


## Elementary Example
### Simple

Stokes equates a definite integral over a domain set $A$ with a definite integral over its edge $B = \partial A$.

$$
\int_{A} d\omega = \int_{B} \omega
$$

$$
A = \{ a,\ b,\ c,\ d \},\quad B = \partial A = \{ x,\ y,\ z \}
$$

where

- $A$ is the domain of integration.
- $B = \partial A$ is the edge of $A$.
- both integrals are definite integrals.

### General

On the closed unit disc, the domain is the disc and the edge is the unit circle.

$$
A = \{ z : |z| \le 1 \},\quad B = \partial A = \{ z : |z| = 1 \}
$$

$$
\int_{A} d\omega = \int_{B} \omega
$$

where

- $A$ is the closed unit disc.
- $B$ is the unit circle.
- $\omega$ is a differential form and $d\omega$ is its exterior derivative.

## Examples

In set language, Stokes’s theorem is a before-and-after move under the boundary operation. Before: a definite integral lives on a domain set $A$. After: that definite integral lives on the edge set $B = \partial A$.

<i>

**example 1 [d]** (**Domain set to edge set** — Lee; Gowers) Before: take

- $A = \overline{B}^{2} = \{ x \in \mathbb{R}^{2} : |x| \le 1 \}$ .

After the boundary operation,

- $B = \partial A = S^{1} = \{ x \in \mathbb{R}^{2} : |x| = 1 \}$ .

Stokes’s theorem then equates the definite integrals on those two sets:

- $\displaystyle \int_{A} d\omega = \int_{B} \omega$ .

where

- $A$ is the domain set before $\partial$ acts.
- $B = \partial A$ is the edge set after $\partial$ acts.
- both integrals are definite integrals.

</i>
