# Exterior Algebra and Exterior Derivatives

Exterior algebra and exterior differentiation extend linear algebra and calculus for manifolds. Exterior algebra is the algebra of alternating tensors; exterior differentiation is the differentiation of differential forms—which assign alternating multilinear functions to points on manifolds.

It is required to extend linear algebra and calculus for manifolds because manifolds are only locally Euclidean. That is to say, Euclidean geometric axioms apply only to local regions of a manifold.


Consider [Figure 1](#fig:atlas-charts).

![Atlas and charts on a manifold.](atlas-and-charts.png){#fig:atlas-charts}

Exterior dertivatives are differential operators.

## Elementary Example
### Simple

The exterior product of two basis covectors is a $2$-form that changes sign under a swap of vector inputs.

$$
\{ e^{1},\ e^{2} \}
$$

$$
e^{1} \wedge e^{2}
$$

$$
(e^{1} \wedge e^{2})(e_{1},e_{2}) = 1,\quad (e^{1} \wedge e^{2})(e_{2},e_{1}) = -1
$$

where

- $e^{1}, e^{2}$ are basis covectors.
- $\wedge$ is the exterior product.
- $e_{1}, e_{2}$ are dual basis vectors.

### General

In three dimensions the exterior algebra includes $1$-forms and $2$-forms among three covectors, and $d$ raises degree by one.

$$
\{ e^{1},\ e^{2},\ e^{3} \}
$$

$$
e^{1} \wedge e^{2},\quad e^{1} \wedge e^{3},\quad e^{2} \wedge e^{3}
$$

$$
\text{if } f = x^{1},\quad df = e^{1}
$$

where

- $df$ is the exterior derivative of the function $f$.
- $e^{1} \wedge e^{2}$ is a basis $2$-form in $\mathbb{R}^{3}$.
