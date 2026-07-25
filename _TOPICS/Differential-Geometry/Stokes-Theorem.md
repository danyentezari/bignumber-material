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
