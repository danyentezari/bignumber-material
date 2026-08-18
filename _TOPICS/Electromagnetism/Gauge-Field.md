# Gauge Field

A field built from the curvature of a connection that is used to measure the physical strength of a gauge interaction, where a connection is a potential that tells how to compare internal frames at nearby points.

1\. The gauge field is the curvature of the gauge potential. This principle is used to obtain the physical field strength from $A$.

The curvature is related to the potential by

$$
F = dA + A \wedge A
$$

where

- $A$ is the gauge potential.
- $F$ is the gauge field.
- $d$ is the exterior derivative.
- $\wedge$ is the wedge product of forms.

2\. In electromagnetism the gauge group is abelian, so $A \wedge A = 0$ and the field strength reduces to $dA$. An abelian group is a group whose elements commute. This principle is used to recover $\mathbf{B}=\nabla\times\mathbf{A}$ and $F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu}$.

The abelian field strength is

$$
F = dA
$$

where

- $A$ is the electromagnetic potential.
- $F$ is the electromagnetic field strength.

3\. Under a gauge transformation the field strength transforms tensorially. This principle is used to keep $F$ physically meaningful while $A$ changes as a connection.

The adjoint transformation of the field strength is

$$
F' = h F h^{-1}
$$

where

- $h$ is a gauge transformation.
- $F$ is the gauge field.

Note: These principles are the curvature formula, the abelian reduction $F=dA$, and the tensorial transformation of $F$. Also called the field strength. Also called the field tensor. Also called the curvature of the gauge potential.

## References

1. Nash, C., & Sen, S. *Topology and Geometry for Physicists*. Academic Press, 1983. — gauge potential as connection; gauge field as curvature $F = dA + A\wedge A$.
