# Position Operator

An operator that multiplies a wavefunction by the coordinate that is used to represent the position observable in the position representation.

Note: Also denoted $X$. Also denoted $\hat{x}$. Also denoted $x$.

<i>

**definition [d]** (*Position Operator*) From Hall: in the case of position, we may introduce the position operator $X$ defined by

- $(X\psi)(x) = x\psi(x)$ .

where

- $\psi$ is a wave function.
- $x$ is the position coordinate.
- $X$ is the position operator.

</i>

<i>

**definition [d]** (*Position Operator*) From Shankar: it is called $X$ and this is what it does to any $f(x)$ placed to its right:

- $X\bigl[f(x)\bigr] = xf(x)$ ,

so that, for example, $X[\sin x] = x\sin x$.

where

- $f(x)$ is a function of position.
- $X$ is the position operator.

</i>

<i>

**definition [d]** (*Position Operator*) From Sakurai: the eigenkets $|x'\rangle$ of the position operator $x$ satisfying

- $x|x'\rangle = x'|x'\rangle$

are postulated to form a complete set.

where

- $x$ is the position operator.
- $|x'\rangle$ is a position eigenket.
- $x'$ is the corresponding eigenvalue.

</i>

## Elementary Example

### Simple

Acting on $\psi(x) = e^{-x^{2}}$ at $x = 1$ gives

$$
(X\psi)(1) = 1\cdot e^{-1}
$$

where

- $X$ multiplies by the coordinate value.

### General

On a set of sample points $x \in \{0, 1, 2\}$,

$$
(X\psi)(x) = x\psi(x)
$$

where

- each value of $\psi$ is scaled by its position.

## References

1. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — $(X\psi)(x)=x\psi(x)$.
2. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — $X[f(x)]=xf(x)$.
3. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — $x|x'\rangle=x'|x'\rangle$.
