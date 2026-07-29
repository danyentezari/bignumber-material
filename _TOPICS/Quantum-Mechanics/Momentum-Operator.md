# Momentum Operator

An operator equal to $-i\hbar$ times differentiation that is used to represent the momentum observable in the position representation.

Note: Also denoted $P$. Also denoted $\hat{p}$. Also denoted $p$.

<i>

**definition [d]** (*Momentum Operator*) From Hall: define the momentum operator $P$ by

- $P = -i\hbar\dfrac{d}{dx}$ .

For a particle moving in $\mathbb{R}^{1}$, let the quantum Hilbert space be $L^{2}(\mathbb{R})$ and define the position and momentum operators $X$ and $P$ by

- $(X\psi)(x) = x\psi(x)$ ,
- $(P\psi)(x) = -i\hbar\dfrac{d\psi}{dx}$ .

where

- $\psi$ is a wave function.
- $x$ is the position coordinate.
- $P$ is the momentum operator.
- $\hbar$ is a reduced Planck constant that is used as the quantum of action.

</i>

<i>

**definition [d]** (*Momentum Operator*) From Sakurai: with this identification the infinitesimal translation operator $\mathcal{J}(dx')$ reads

- $\mathcal{J}(dx') = 1 - \dfrac{i}{\hbar}\,p\,dx'$ ,

where $p$ is the momentum operator. Comparison of both sides yields

- $\langle x'|p|\alpha\rangle = -i\hbar\dfrac{\partial}{\partial x'}\langle x'|\alpha\rangle$ .

where

- $p$ is the momentum operator.
- $|x'\rangle$ is a position eigenket.
- $|\alpha\rangle$ is a state ket.
- $\hbar$ is a reduced Planck constant that is used as the quantum of action.

</i>

<i>

**definition [d]** (*Momentum Operator*) From Shankar: in this language we may say that the states of definite momentum $\psi_{p}(x)$ are eigenfunctions of the operator

- $P = -i\hbar D$ ,

called the momentum operator in quantum theory, and therefore the solutions to

- $P\bigl[\psi_{p}(x)\bigr] \equiv -i\hbar\dfrac{d\psi_{p}}{dx} = p\,\psi_{p}(x)$ ,

where $D = \dfrac{d}{dx}$.

where

- $\psi_{p}(x)$ is a momentum eigenfunction.
- $P$ is the momentum operator.
- $p$ is the corresponding momentum eigenvalue.
- $\hbar$ is a reduced Planck constant that is used as the quantum of action.

</i>

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
