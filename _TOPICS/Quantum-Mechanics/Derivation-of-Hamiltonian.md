# Derivation of Hamiltonian

A derivation of the Hamiltonian that is used to obtain $H(p,q)=\displaystyle\sum_{i}p_{i}\dfrac{dq_{i}}{dt}-L$ from the Lagrangian by a Legendre transform.

<i>

**definition [d]** (*Derivation of Hamiltonian*) From MIT OpenCourseWare 8.223 Classical Mechanics II, Lecture 15:

1. Start from a Lagrangian function of position and velocity, since $H$ is the Legendre transform of $L$.
   - $L = L\left(q,\dfrac{dq}{dt}\right)$ .

2. Treat velocity as the variable to replace, since the goal is a description in position and momentum.

3. Define conjugate momentum as the slope of $L$ in velocity, since a Legendre transform uses that derivative as the new independent variable.
   - $p = \dfrac{\partial L}{\partial \left(\dfrac{dq}{dt}\right)}$ .

4. Form $H = p\dfrac{dq}{dt}-L$, which keeps the same information while switching the independent variable.
   - $H(p,q) = p\,\dfrac{dq}{dt}(p) - L\left(q,\dfrac{dq}{dt}(p)\right)$ .

5. Solve for velocity in terms of $p$ and substitute, so that $H$ is a function of $p$ and $q$ alone.
   For the simple Lagrangian
   - $L = \dfrac{1}{2}m\left(\dfrac{dq}{dt}\right)^{2} - U(q)$ ,
   one has $p = m\dfrac{dq}{dt}$, so $\dfrac{dq}{dt} = \dfrac{p}{m}$ and
   - $H(p,q) = \dfrac{p^{2}}{2m} + U(q)$ .
   In this case $H = T + U$.

6. For $N$ degrees of freedom, sum over each pair, since each velocity has its own conjugate momentum.
   - $H(p,q) = \displaystyle\sum_{i} p_{i}\dfrac{dq_{i}}{dt}(p) - L\left(q,\dfrac{dq}{dt}(p)\right)$ .

7. Expand $dL$ with Euler–Lagrange and rearrange to $dH$, so matching coefficients yields the first-order equations of motion.
   - $dH = -\displaystyle\sum_{i}\dfrac{dp_{i}}{dt}\,dq_{i} + \displaystyle\sum_{i}\dfrac{dq_{i}}{dt}\,dp_{i}$ ,
   hence
   - $\dfrac{dq_{i}}{dt} = \dfrac{\partial H}{\partial p_{i}}$ , $\qquad \dfrac{dp_{i}}{dt} = -\dfrac{\partial H}{\partial q_{i}}$ .

where

- $L$ is the Lagrangian.
- $q$ is a generalized coordinate.
- $\dfrac{dq}{dt}$ is the generalized velocity.
- $p$ is the conjugate momentum.
- $\dfrac{\partial L}{\partial \left(\dfrac{dq}{dt}\right)}$ is the partial derivative of $L$ with respect to velocity.
- $H$ is the Hamiltonian.
- $m$ is the mass.
- $U(q)$ is the potential energy.
- $T$ is the kinetic energy.
- $N$ is the number of degrees of freedom.
- $q_{i}$ and $p_{i}$ are the $i$-th coordinate and conjugate momentum.
- $\dfrac{dq_{i}}{dt}$ and $\dfrac{dp_{i}}{dt}$ are their time derivatives.
- $dL$ and $dH$ are the differentials of $L$ and $H$.
- $\dfrac{\partial H}{\partial p_{i}}$ and $\dfrac{\partial H}{\partial q_{i}}$ are the partial derivatives of $H$.

</i>

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

1. MIT OpenCourseWare. *8.223 Classical Mechanics II*, Lecture 15: Introduction to Hamiltonian Mechanics (IAP 2017). [PDF](https://ocw.mit.edu/courses/8-223-classical-mechanics-ii-january-iap-2017/09ab68ae8e7987debc025892e00c0f1f_MIT8_223IAP17_Lec15.pdf) — Legendre transform $H = p\dot{q}-L$, simple case $H=T+U$, and Hamilton’s equations.
