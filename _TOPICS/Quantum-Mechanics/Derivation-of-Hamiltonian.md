# Derivation of Hamiltonian

A derivation of the Hamiltonian that is used to obtain $H(p,q)=\displaystyle\sum_{i}p_{i}\dfrac{dq_{i}}{dt}-L$ from the Lagrangian by a Legendre transform, where a Legendre transform is a change from velocity variables to momentum variables.

1\. Start from a Lagrangian that depends on position and velocity. This principle is used to treat $H$ as the Legendre transform of $L$.

The Lagrangian is

$$
L = L\left(q,\dfrac{dq}{dt}\right)
$$

where

- $L$ is the Lagrangian.
- $q$ is a generalized coordinate.
- $\dfrac{dq}{dt}$ is the generalized velocity.

2\. The conjugate momentum is the slope of $L$ in velocity. This principle is used to introduce $p$ as the new independent variable.

The conjugate momentum is

$$
p = \dfrac{\partial L}{\partial \left(\dfrac{dq}{dt}\right)}
$$

where

- $p$ is the conjugate momentum.
- $L$ is the Lagrangian.

3\. The Hamiltonian is $p$ times velocity minus $L$, with velocity expressed in terms of $p$. This principle is used to write $H$ as a function of $p$ and $q$ alone.

The Hamiltonian is

$$
H(p,q) = p\,\dfrac{dq}{dt}(p) - L\left(q,\dfrac{dq}{dt}(p)\right)
$$

where

- $H$ is the Hamiltonian.
- $p$ is the conjugate momentum.
- $L$ is the Lagrangian.

4\. For $L=\dfrac{1}{2}m(\mathrm{d}q/\mathrm{d}t)^{2}-U(q)$ one obtains $H=p^{2}/2m+U(q)$. This principle is used to recover the energy $T+U$ and the quantum operator $P^{2}/2m+V(X)$.

The simple Hamiltonian is

$$
H(p,q) = \dfrac{p^{2}}{2m} + U(q)
$$

where

- $m$ is the mass.
- $U(q)$ is the potential energy.

5\. Matching the differential of $H$ yields Hamilton's equations. This principle is used to write first-order equations for $q$ and $p$.

Hamilton's equations are

$$
\dfrac{dq_{i}}{dt} = \dfrac{\partial H}{\partial p_{i}},\qquad \dfrac{dp_{i}}{dt} = -\dfrac{\partial H}{\partial q_{i}}
$$

where

- $q_{i}$ is a generalized coordinate.
- $p_{i}$ is the conjugate momentum.
- $H$ is the Hamiltonian.

Note: These principles are the Lagrangian starting point, conjugate momentum, the Legendre transform, $H=T+U$ for a standard kinetic term, and Hamilton's equations.

## Elementary Example

### Simple

For $L = \dfrac{1}{2}m\left(\dfrac{dq}{dt}\right)^{2} - U(q)$ with $m = 2$ and $U(q) = 3q^{2}$,

$$
p = 2\dfrac{dq}{dt},\qquad H = \dfrac{p^{2}}{4} + 3q^{2}
$$

where

- $L$ is the Lagrangian.
- $m$ is the mass.
- $\dfrac{dq}{dt}$ is the velocity.
- $U(q)$ is the potential energy.
- $q$ is the coordinate.
- $p$ is the conjugate momentum.
- $H$ is the Hamiltonian.

### General

For $N$ coordinates with $L\left(q,\dfrac{dq}{dt}\right)$, form $p_{i} = \dfrac{\partial L}{\partial \left(\dfrac{dq_{i}}{dt}\right)}$, invert for $\dfrac{dq_{i}}{dt}(q,p)$, and substitute into

$$
H(p,q) = \sum_{i} p_{i}\dfrac{dq_{i}}{dt} - L
$$

where

- $N$ is the number of degrees of freedom.
- $L$ is the Lagrangian.
- $q$ and $\dfrac{dq}{dt}$ are the coordinates and velocities.
- $p_{i}$ is the $i$-th conjugate momentum.
- $\dfrac{dq_{i}}{dt}$ is the $i$-th velocity expressed through $p$.
- $H$ is the Hamiltonian.

## References

1. MIT OpenCourseWare. *8.223 Classical Mechanics II*, Lecture 15: Introduction to Hamiltonian Mechanics (IAP 2017). — Legendre transform $H = p\dot{q}-L$, simple case $H=T+U$, and Hamilton’s equations.
