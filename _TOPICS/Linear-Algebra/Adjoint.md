# Adjoint

A linear transformation paired with another mapping through an inner product that is used to move that inner product from one factor to the other in an equation.

Note: Also called Hilbert-adjoint operator.

<i>

**definition [d]** (*Adjoint = Hilbert-Adjoint Operator*) From Kreyszig: the Hilbert-adjoint operator $T^{*}: H \rightarrow H$ is defined to be the operator satisfying

- $(Tx, y) = (x, T^{*}y)$

for all $x, y \in H$.

where

- $H$ is a Hilbert space.
- $T: H \rightarrow H$ is a given operator.
- $T^{*}$ is the adjoint of $T$.
- $(\cdot,\cdot)$ is the inner product on $H$.

</i>

<i>

**definition [d]** (*Adjoint*) From Gowers, in the sense of Stokes’s theorem: one can view Stokes’s theorem as a definition of the derivative operation $\omega \mapsto d\omega$; thus differentiation is the adjoint of the boundary operation.

where

- $d$ is the exterior derivative on forms.
- $\partial$ is the boundary operation on the region of integration.
- Stokes’s theorem asserts $\displaystyle \int_{S} d\omega = \int_{\partial S} \omega$.

</i>

## Elementary Example
### Simple

The adjoint $T^{*}$ moves the inner product from $Tx$ onto $x$. On $\mathbb{R}^{2}$ with the dot product, the adjoint of a matrix is its transpose.

$$
T = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix},\quad T^{*} = \begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix}
$$

$$
(Tx,y) = (x, T^{*} y)
$$

where

- $T$ is the operator.
- $T^{*}$ is the adjoint of $T$.
- $(\cdot,\cdot)$ is the inner product.

### General

On $\mathbb{C}^{3}$, the adjoint is the conjugate transpose.

$$
T = \begin{pmatrix} 1 & i & 0 \\ 0 & 2 & 1+i \\ 0 & 0 & 3 \end{pmatrix}
$$

$$
T^{*} = \begin{pmatrix} 1 & 0 & 0 \\ -i & 2 & 0 \\ 0 & 1-i & 3 \end{pmatrix}
$$

where

- $T^{*} = T^{\dagger}$ for matrices on $\mathbb{C}^{n}$.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Hilbert-adjoint operator $T^{*}$ with $(Tx,y)=(x,T^{*}y)$.
2. Gowers, T., Barrow-Green, J., & Leader, I. (eds.). *The Princeton Companion to Mathematics*. Princeton University Press, 2008. — differentiation as the adjoint of the boundary operation.
