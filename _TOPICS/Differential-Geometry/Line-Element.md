# Line Element

An expression for an infinitesimal squared distance from the metric that is used to compute length of a path.

<i>

**definition [d]** (*Line Element = Infinitesimal Arc Length Squared*) The quadratic form built from the metric components and the coordinate differentials:

- $ds^{2} = g_{ij}\, dx^{i}\, dx^{j}$ .

where

- $ds^{2}$ is the line element.
- $g_{ij}$ are the components of the metric tensor.
- $dx^{i}, dx^{j}$ are coordinate differentials.
- $ds$ is the infinitesimal arc length.

Note:

- also written $(ds)^{2} = g_{ij}\, du^{i}\, du^{j}$.
- $ds^{2}$ encodes lengths of infinitesimal displacements via the metric.

</i>

<i>

**definition [d]** (*Line Element = Spacetime Interval Squared*) The quadratic form built from the spacetime metric and the coordinate differentials:

- $ds^{2} = g_{\mu\nu}\, dx^{\mu}\, dx^{\nu}$ .

where

- $ds^{2}$ is the line element.
- $g_{\mu\nu}$ are the components of the spacetime metric.
- $dx^{\mu}, dx^{\nu}$ are spacetime coordinate differentials.
- $ds$ is the infinitesimal spacetime interval.

Note:

- in Minkowski spacetime with $\eta_{\mu\nu} = \operatorname{diag}(-1,\, 1,\, 1,\, 1)$, one has $ds^{2} = -c^{2}\, dt^{2} + dx^{2} + dy^{2} + dz^{2}$.
- the overall sign of $ds^{2}$ follows the metric signature convention.

</i>


## Elementary Example
### Simple

The line element $ds^{2}$ is the squared length from the metric on coordinate increments.

$$
ds^{2} = dx^{2} + dy^{2}
$$

$$
g = \operatorname{diag}(1,1)
$$

where

- $ds^{2}$ is the line element.
- $dx, dy$ are coordinate increments.
- $g$ is the metric matrix used to form $ds^{2}$.

### General

In three Euclidean dimensions the line element uses three squared increments.

$$
ds^{2} = dx^{2} + dy^{2} + dz^{2}
$$

$$
g = \operatorname{diag}(1,1,1)
$$

$$
ds^{2} = \sum_{i,j=1}^{3} g_{ij}\, dx^{i}\, dx^{j}
$$

where

- $g_{ij}$ are the metric components.
- $dx^{1}, dx^{2}, dx^{3}$ may be written $dx, dy, dz$.

## References

1. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — line element from the metric; $ds^{2}=g_{ij}\,dx^{i}\,dx^{j}$.
2. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — $(ds)^{2}=g_{ij}\,du^{i}\,du^{j}$.
3. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — spacetime line element $ds^{2}=g_{\mu\nu}\,dx^{\mu}\,dx^{\nu}$.
