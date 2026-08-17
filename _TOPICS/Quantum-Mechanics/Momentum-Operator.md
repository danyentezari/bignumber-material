# Momentum Operator

An operator equal to $-i\hbar$ times differentiation that is used to represent the momentum observable in the position representation.

1\. In the position representation the momentum operator is $-i\hbar$ times the derivative. This principle is used to compute $\langle p\rangle$ and kinetic energy $p^{2}/2m$.

The momentum operator is

$$
P = -i\hbar\dfrac{d}{dx}
$$

where

- $P$ is the momentum operator.
- $\hbar$ is the reduced Planck constant.
- $x$ is the position coordinate.

2\. Plane waves are eigenfunctions of $P$. This principle is used to identify states of definite momentum.

The momentum eigenvalue equation is

$$
-i\hbar\dfrac{d\psi_{p}}{dx} = p\,\psi_{p}(x)
$$

where

- $\psi_{p}(x)$ is a momentum eigenfunction.
- $p$ is the momentum eigenvalue.

3\. Momentum generates translations. This principle is used to write an infinitesimal shift as $1-(i/\hbar)p\,dx$.

The infinitesimal translation operator is

$$
\mathcal{J}(dx') = 1 - \dfrac{i}{\hbar}\,p\,dx'
$$

where

- $\mathcal{J}(dx')$ is the translation by $dx'$.
- $p$ is the momentum operator.
- $\hbar$ is the reduced Planck constant.

Note: These principles are $P=-i\hbar d/dx$, momentum eigenfunctions, and momentum as the generator of translations. Also denoted $P$. Also denoted $\hat{p}$. Also denoted $p$.

## Elementary Example

### Simple

Acting on $\psi(x) = e^{ikx}$ with $k = 1$ and $\hbar = 1$ gives

$$
(P\psi)(x) = -i\dfrac{d}{dx}\bigl[e^{ix}\bigr] = e^{ix}
$$

where

- $P$ maps a plane wave to a constant multiple of itself.

### General

On a set of wave numbers $k \in \{1, 2, 3\}$ with $\psi_{k}(x) = e^{ikx}$ and $\hbar = 1$,

$$
(P\psi_{k})(x) = k\,e^{ikx}
$$

where

- each plane wave is an eigenvector of $P$ with eigenvalue $k$.

## References

1. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — Proposition 3.6, Definition 3.7: $(P\psi)(x)=-i\hbar\dfrac{d\psi}{dx}$.
2. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — Equations 1.214, 1.248, 1.249: $\langle x'|p|\alpha\rangle=-i\hbar\dfrac{\partial}{\partial x'}\langle x'|\alpha\rangle$.
3. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — Equations 24.30, 24.31: $P=-i\hbar D$.
