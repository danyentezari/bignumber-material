# Position Operator

An operator that multiplies a wavefunction by the coordinate that is used to represent the position observable in the position representation.

1\. In the position representation the position operator multiplies by $x$. This principle is used to compute $\langle x\rangle$ and to write potentials $V(\hat{x})$.

The position operator is

$$
(X\psi)(x) = x\psi(x)
$$

where

- $\psi$ is a wavefunction.
- $x$ is the position coordinate.
- $X$ is the position operator.

2\. The eigenkets of the position operator satisfy $x|x'\rangle=x'|x'\rangle$ and form a complete set. This principle is used to expand an arbitrary state in the position basis.

The position eigenvalue equation is

$$
x|x'\rangle = x'|x'\rangle
$$

where

- $x$ is the position operator.
- $|x'\rangle$ is a position eigenket.
- $x'$ is the corresponding eigenvalue.

3\. The wavefunction is the overlap $\psi(x)=\langle x|\psi\rangle$. This principle is used to pass from abstract kets to functions of $x$.

Note: These principles are multiplication by $x$, the position eigenkets, and the wavefunction as a position-basis coefficient. Also denoted $X$. Also denoted $\hat{x}$. Also denoted $x$.

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
