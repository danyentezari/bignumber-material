# Dual Space

A set of linear transformations from a domain of vectors to a codomain of scalars that is used to associate each vector with a scalar value.

Note: Also called dual vector space. Also called algebraic dual space. Also called conjugate space. Also called adjoint space.

<i>

**definition [d]** (*Dual Space = Dual Vector Space = Algebraic Dual Space = Conjugate Space = Adjoint Space*) The vector space $V^{*}$ of all linear functionals on a vector space $V$:

- $V^{*} = \{\, \varphi : V \rightarrow K \mid \varphi \text{ is linear} \,\}$ .

where

- $V$ is a vector space over a field $K$.
- $K$ is the scalar field.
- $\varphi$ is a linear functional from $V$ to $K$.
- $V^{*}$ is the dual space.
- elements of $V^{*}$ are called covectors.

Note:

- $K$ is typically $\mathbb{R}$.
- $K$ is also typically $\mathbb{C}$.
- $V^{*}$ is also written $V'$.
- a linear functional $\varphi$ maps each vector to a scalar in $K$.
- if $\dim V = n < \infty$, then $\dim V^{*} = n$.

</i>

## Elementary Example
### Simple

The dual space is the set of all linear functionals on $V$. On $\mathbb{R}^{2}$, each functional is a row of two components.

$$
V = \mathbb{R}^{2}
$$

$$
\varphi(x_{1},x_{2}) = 3 x_{1} - x_{2}
$$

$$
\varphi \in V^{*}
$$

where

- $V^{*}$ is the dual space.
- $\varphi : V \rightarrow \mathbb{R}$ is a linear functional.

### General

If $\dim V = 3$, then $\dim V^{*} = 3$, with dual basis $e^{1}, e^{2}, e^{3}$.

$$
V = \mathbb{R}^{3},\quad V^{*} = \operatorname{span}\{ e^{1},\ e^{2},\ e^{3} \}
$$

$$
e^{i}(e_{j}) = \delta^{i}_{\ j}
$$

where

- $e^{i}$ are the dual basis functionals.
- $\delta^{i}_{\ j}$ equals $1$ if $i = j$ and $0$ otherwise.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — algebraic dual space; also adjoint space, conjugate space.
2. Dummit, D. S., & Foote, R. M. *Abstract Algebra*. — dual space, dual vector space, algebraic dual space.
3. Szekeres, P. *A Course in Modern Mathematical Physics*. Cambridge University Press, 2004. — dual space, covectors, 1-forms.
