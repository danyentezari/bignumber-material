### 1. Short definition:

Partial differential equations involving randomness or stochastic elements.

### 2. Long definition:

Random Partial Differential Equations (Random PDEs) incorporate random elements into the coefficients, boundary conditions, or forcing terms. These equations are commonly used to model systems where uncertainty or noise plays a role, such as in fluid dynamics, financial models, and physics. They are written in a general form similar to deterministic PDEs but include stochastic components that affect the solution behavior. The study of Random PDEs often focuses on understanding the probabilistic distribution of their solutions.

$$
\text{General form: } L(u, \omega) = f(x, \omega)
$$

where \( L \) is a differential operator, \( u \) is the unknown solution, \( \omega \) represents randomness, and \( f \) is a random forcing function.

### 3. Subtopics:

- Stochastic processes
- Stochastic calculus
- Numerical methods for Random PDEs
- Stochastic finite element methods
- Applications in fluid dynamics

### 4. Proposition(s) in LaTeX:

None at the moment.

### 5. Theorem(s) in LaTeX:

None at the moment.

### 6. Example 1:

Consider a simplified model of heat conduction where the thermal conductivity is uncertain due to material imperfections. The heat equation is given by:

$$
\frac{\partial u}{\partial t} - k(x, \omega) \Delta u = f(x, t)
$$

where \( u(x,t) \) is the temperature field, \( k(x, \omega) \) is a random field representing thermal conductivity, and \( f(x,t) \) is the heat source. The randomness in \( k(x, \omega) \) could model real-world variability in the material's properties.

To solve this Random PDE, one could apply stochastic finite element methods (SFEM), where the randomness in \( k(x, \omega) \) is represented by a finite set of random variables using techniques like Karhunen-Loève expansion. The solution would then provide not a single deterministic temperature profile but a distribution of possible temperature profiles, reflecting the uncertainty in thermal conductivity.

### 7. Example 2:

In the context of financial mathematics, Random PDEs can be used to model the pricing of financial derivatives under uncertain market conditions. Consider the Black-Scholes equation with a stochastic volatility model. The governing Random PDE for the option price \( V(S,t,\omega) \) can be written as:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2(S,\omega) S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - rV = 0
$$

where \( S \) is the underlying asset price, \( \sigma(S,\omega) \) is the stochastic volatility, \( r \) is the risk-free interest rate, and \( \omega \) represents the randomness in volatility. Solving this equation involves estimating the probability distribution of option prices based on the random nature of volatility. This approach provides more realistic models of market behavior than deterministic PDEs.
