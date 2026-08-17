# Gauge Transformations

A change of the electromagnetic potentials that leaves the physical fields unchanged that is used to exploit freedom in choosing $V$ and $\mathbf{A}$.

1\. Adding the gradient of a scalar to $\mathbf{A}$ and subtracting the time derivative of that scalar from $V$ leaves $\mathbf{E}$ and $\mathbf{B}$ unchanged. This principle is used to pass from one allowed pair of potentials to another.

A gauge transformation is

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda
$$

$$
V' = V - \dfrac{\partial\lambda}{\partial t}
$$

where

- $\lambda$ is an arbitrary scalar function of position and time.
- $V$ and $\mathbf{A}$ are the original potentials.
- $V'$ and $\mathbf{A}'$ are the new potentials.
- $t$ is time.

2\. In magnetostatics the curl of a gradient vanishes, so $\mathbf{B}$ is automatically invariant. This principle is used to check the transformation on $\mathbf{B}$ alone.

The invariance of $\mathbf{B}$ is

$$
\mathbf{B}' = \nabla\times\mathbf{A}' = \nabla\times\mathbf{A} = \mathbf{B}
$$

where

- $\mathbf{B}$ is the magnetic field.
- $\mathbf{A}$ is the vector potential.

3\. The same freedom is a local change of frame in the fibers of a bundle. A bundle is a space that assigns an internal space to each point of spacetime. This principle is used to identify the electromagnetic gauge transformation with the geometric one.

Note: These principles are the gauge transformation of $V$ and $\mathbf{A}$, the invariance of $\mathbf{B}$, and the geometric reading as a change of fiber frame. Also called a gauge transformation of the potentials.

## Elementary Example

### Simple

In magnetostatics, adding $\nabla\lambda$ to $\mathbf{A}$ leaves

$$
\mathbf{B}' = \nabla\times\mathbf{A}' = \nabla\times\mathbf{A} = \mathbf{B}
$$

where

- the curl of a gradient vanishes.

### General

A full electrodynamic gauge change is

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda,\quad V' = V - \dfrac{\partial\lambda}{\partial t}
$$

where

- both potentials change together.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — gauge transformations of $V$ and $\mathbf{A}$.
2. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — gauge invariance of the vector potential.
3. Frankel, T. *The Geometry of Physics*. Cambridge University Press, 2012. — gauge transformation as change of fiber frame.
