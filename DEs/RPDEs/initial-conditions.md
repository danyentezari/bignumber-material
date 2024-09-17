### 1. Short definition:
Conditions specified at the initial time point.

### 2. Long definition:
Initial conditions refer to the values of the dependent variable(s) at the beginning of the time interval in which a differential equation is defined. They are used to solve time-dependent differential equations, such as ordinary differential equations (ODEs) and partial differential equations (PDEs), by providing the state of the system at time \( t = 0 \). Without initial conditions, the solution to such equations is not unique. These conditions are crucial in modeling time-evolving systems, such as heat distribution, population growth, and mechanical vibrations.

### 3. Subtopics:
- Initial value problems (IVP)
- Cauchy problems
- Boundary conditions vs. initial conditions
- Well-posed problems

### 4. Proposition(s) in LaTeX:
None at the moment.

### 5. Theorem(s) in LaTeX:
None at the moment.

### 6. Example 1:
In the heat equation problem:

$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$

an initial condition might specify the temperature distribution along a rod at \( t = 0 \), such as:

$$
u(x, 0) = f(x)
$$

where \( f(x) \) describes the initial temperature along the length of the rod.

### 7. Example 2:
In the case of Newton’s second law of motion, the position \( x(t) \) of a moving object satisfies the equation:

$$
m \frac{d^2 x}{dt^2} = F(x,t)
$$

To fully determine the motion of the object, initial conditions for the position and velocity must be provided at \( t = 0 \):

$$
x(0) = x_0, \quad \frac{dx}{dt}(0) = v_0
$$

These initial conditions specify where the object starts and how fast it is moving initially.