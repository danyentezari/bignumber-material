# Nondegenerate Bilinear Form

<i>

**definition [d]** (**Nondegenerate Bilinear Form**) A bilinear map $\langle \cdot,\cdot \rangle : V \times V \rightarrow \mathbb{R}$ such that the only vector orthogonal to every vector is zero:

- $\langle U, V \rangle = 0$ for all $V \in V$ implies $U = 0$ .

where

- $V$ is a finite-dimensional real vector space (e.g. $T_{p}M$).
- bilinearity: linear in each argument separately.
- the form need not be positive-definite (metrics in GR are indefinite).

</i>

<i>

**definition [d]** (**Nondegenerate Bilinear Form**) A bilinear form whose component matrix is invertible:

- $\det(g_{\mu\nu}) \neq 0$ ,

equivalently $\langle U, V \rangle = 0$ for all $V$ implies $U = 0$.

where

- $g_{\mu\nu} = \langle e_{\mu}, e_{\nu} \rangle$ in a basis $\{e_{\mu}\}$.
- nondegeneracy ensures an inverse matrix $g^{\mu\nu}$ exists.
- this makes the map $V \rightarrow V^{*}$, $U \mapsto \langle U,\cdot\rangle$, an isomorphism.

</i>

## References

1. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — nondegenerate metric / bilinear form.
2. Nakahara, M. *Geometry, Topology and Physics*. IOP, 2003. — nondegeneracy; $\det g \neq 0$.
