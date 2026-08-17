# Angular Momentum

An operator that is used to represent rotational motion of a quantum system, equal to the cross product of position and momentum in the orbital case.

1\. Orbital angular momentum is the operator $\mathbf{r}\times\mathbf{p}$. This principle is used to assign a rotational observable to spatial motion.

The orbital angular momentum is

$$
\mathbf{L} = \mathbf{r}\times\mathbf{p}
$$

where

- $\mathbf{L}$ is the angular momentum operator.
- $\mathbf{r}$ is the position operator.
- $\mathbf{p}$ is the momentum operator.

2\. The Cartesian components do not commute. This principle is used to explain why $L_{x}$, $L_{y}$, and $L_{z}$ cannot all have sharp values at once.

The angular-momentum commutation relations are

$$
[L_{i}, L_{j}] = i\hbar\sum_{k}\epsilon_{ijk}L_{k}
$$

where

- $L_{i}$ are the Cartesian components of $\mathbf{L}$.
- $\epsilon_{ijk}$ is the Levi-Civita symbol.
- $\hbar$ is the reduced Planck constant.

3\. $L^{2}$ commutes with each component, so $L^{2}$ and $L_{z}$ can be sharp together. This principle is used to label states by $\ell$ and $m$.

The simultaneous eigenvalue equations are

$$
L^{2}|\ell,m\rangle = \hbar^{2}\ell(\ell+1)|\ell,m\rangle
$$

$$
L_{z}|\ell,m\rangle = m\hbar|\ell,m\rangle
$$

where

- $\ell$ is the angular-momentum quantum number.
- $m$ is the projection quantum number.

4\. The same commutation relations hold for any angular momentum $\mathbf{J}$, including spin. This principle is used to treat $\mathbf{L}$, $\mathbf{S}$, and $\mathbf{J}$ with one algebra.

Note: These principles are $\mathbf{L}=\mathbf{r}\times\mathbf{p}$, the commutation relations, simultaneous eigenstates of $L^{2}$ and $L_{z}$, and the general $\mathbf{J}$ algebra. Also denoted $\mathbf{L}$. Also denoted $\hat{\mathbf{L}}$. Spin is an intrinsic angular momentum not built from $\mathbf{r}$ and $\mathbf{p}$.

## Elementary Example

### Simple

For motion in the $xy$-plane with $z$-component only,

$$
L_{z} = xp_{y} - yp_{x}
$$

where

- $L_{z}$ is the angular momentum about the $z$-axis.

### General

The three components obey

$$
[L_{x}, L_{y}] = i\hbar L_{z}
$$

where

- cyclic permutations give the other relations.

## References

1. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — generators and commutation relations.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — commutation relations.
3. Shankar, R. *Fundamentals of Physics*. Yale University Press. — operator $\mathbf{L}=\mathbf{r}\times\mathbf{p}$.
