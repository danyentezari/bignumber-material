### 1. Short definition:
A PDE modeling heat distribution over time.

### 2. Long definition:
The heat equation is a second-order partial differential equation (PDE) that describes the distribution of heat (or temperature) in a given region over time. It is derived from Fourier's law of heat conduction and is commonly expressed as:

$$
\frac{\partial u}{\partial t} = \alpha \nabla^2 u
$$

where \( u(x,t) \) represents the temperature at position \( x \) and time \( t \), and \( \alpha \) is the thermal diffusivity constant. The equation models the flow of heat in materials and is used in various fields, including physics, engineering, and finance.

### 3. Subtopics:
- Fourier's law
- Heat conduction in one dimension
- Heat conduction in multiple dimensions
- Boundary and initial conditions
- Numerical methods for solving the heat equation

### 4. Proposition(s) in LaTeX:
None at the moment.

### 5. Theorem(s) in LaTeX:
None at the moment.

### 6. Example 1:
Consider the heat equation in one dimension:

$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$

Here, \( u(x,t) \) represents the temperature in a thin rod at position \( x \) and time \( t \), and \( \alpha \) is the thermal diffusivity of the material. If the rod is insulated at both ends, boundary conditions would be specified, such as:

$$
u(0, t) = u(L, t) = 0
$$

where \( L \) is the length of the rod. Initial conditions would also be provided, such as:

$$
u(x, 0) = f(x)
$$

The solution to this equation describes how heat diffuses along the rod over time.

### 7. Example 2:
In two dimensions, the heat equation becomes:

$$
\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)
$$

This models the distribution of heat over a two-dimensional surface. For example, it can be used to model the temperature distribution on the surface of a metal plate. Similar to the one-dimensional case, boundary conditions and initial conditions are needed to solve the equation. Numerical methods, such as finite difference methods, are often employed for complex geometries and boundary conditions.