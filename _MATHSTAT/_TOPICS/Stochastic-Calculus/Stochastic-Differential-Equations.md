# Stochastic Differential Equations

Stochastic differential equations have applications in modeling systems with non-deterministic behavior. There is, however, a fundmanetla difference between SDEs and differential equations.

$$d\xi(t) = b(\xi(t), t)dt + \sigma(\xi(t), t)dw(t)$$

with initial condition

$$\xi(0) = \xi_0$$

Where:

- $ \xi(t) $ is the n-dimensional stochastic process being modeled.
- $ w(t) $ is an n-dimensional Brownian motion.
- $ b(x, t) = (b_1(x, t), \dots, b_n(x, t)) $ is the drift coefficient (an n-vector).
- $ \sigma(x, t) = (\sigma_{ij}(x, t))_{i,j=1}^n $ is the diffusion matrix (an n×n matrix).
