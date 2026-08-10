# Conjugate Variable

A variable paired with another variable through a derivative that is used to replace that other variable in a Legendre transform.

Note: Also called a canonically conjugate variable. Also called conjugate momentum when paired with a coordinate.

## Applications

1. Defines the momentum paired with each generalized coordinate in classical mechanics.
2. Supplies the new independent variable when a Legendre transform builds the Hamiltonian.
3. Labels phase-space coordinates \((q,p)\) used in Hamilton’s equations.
4. Identifies position–momentum pairs that appear in uncertainty relations in quantum theory.

<i>

**definition [d]** (*Conjugate Momentum*) From Cahill: the momentum \(p_{i}\) canonically conjugate to the coordinate \(q_{i}\) is

- $p_{i} = \dfrac{\partial L}{\partial\!\left(\dfrac{dq_{i}}{dt}\right)}$ .

where

- $L$ is the Lagrangian.
- $q_{i}$ is the $i$-th generalized coordinate.
- $\dfrac{dq_{i}}{dt}$ is the $i$-th generalized velocity.
- $p_{i}$ is the momentum conjugate to $q_{i}$.
- $\dfrac{\partial L}{\partial\!\left(\dfrac{dq_{i}}{dt}\right)}$ is the partial derivative of $L$ with respect to that velocity.

</i>

<i>

**definition [d]** (*Conjugate Variables*) From Park: in classical dynamics, coordinates and momenta such as position and momentum are said to be conjugate to each other.

where

- a coordinate and its conjugate momentum form a conjugate pair.
- position and momentum are the standard example of such a pair.

</i>

## Elementary Example

### Simple

For $L = \dfrac{1}{2}m\left(\dfrac{dq}{dt}\right)^{2} - U(q)$ with $m = 2$,

$$
p = \dfrac{\partial L}{\partial\!\left(\dfrac{dq}{dt}\right)} = 2\dfrac{dq}{dt}
$$

so $q$ and $p$ are conjugate variables.

where

- $L$ is the Lagrangian.
- $m$ is the mass.
- $q$ is the coordinate.
- $\dfrac{dq}{dt}$ is the velocity.
- $U(q)$ is the potential energy.
- $p$ is the conjugate momentum.

### General

For $N$ coordinates with Lagrangian $L\left(q,\dfrac{dq}{dt}\right)$,

$$
p_{i} = \dfrac{\partial L}{\partial\!\left(\dfrac{dq_{i}}{dt}\right)} ,\qquad i = 1,\ldots,N
$$

and each pair $(q_{i},p_{i})$ is a conjugate pair.

where

- $N$ is the number of degrees of freedom.
- $L$ is the Lagrangian.
- $q_{i}$ is the $i$-th coordinate.
- $\dfrac{dq_{i}}{dt}$ is the $i$-th velocity.
- $p_{i}$ is the momentum conjugate to $q_{i}$.

## References

1. Cahill, K. *Physical Mathematics*. Cambridge University Press, 2019. — $p_{i}=\partial L/\partial(\mathrm{d}q_{i}/\mathrm{d}t)$ as momentum canonically conjugate to $q_{i}$.
2. Park, D. *Introduction to the Quantum Theory*. Dover, 2005. — coordinates and momenta are conjugate to each other.
