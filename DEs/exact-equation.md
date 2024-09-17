### 1. Short definition:
Exact equations have solutions directly integrable; inexact require adjustment.

### 2. Long definition:
In differential equations, an exact equation is one that can be solved by finding a potential function whose differential equals the given differential equation. Formally, an equation of the form:

$$
M(x, y) \, dx + N(x, y) \, dy = 0
$$

is exact if there exists a function \( \Phi(x, y) \) such that:

$$
\frac{\partial \Phi}{\partial x} = M \quad \text{and} \quad \frac{\partial \Phi}{\partial y} = N.
$$

An inexact equation does not satisfy this criterion and typically requires modification or integration factors to make it exact before solving. Exactness is a crucial property for simplifying the process of finding solutions to differential equations.

### 3. Subtopics:
- Integrating factors
- Conditions for exactness
- Solution methods for exact equations
- Application of exact equations in physics and engineering
- Conversion of inexact to exact equations

### 4. Proposition(s) in LaTeX:
None at the moment.

### 5. Theorem(s) in LaTeX:
None at the moment.

### 6. Example 1:
Consider the exact differential equation:

$$
(2xy + 3) \, dx + (x^2 + 4y) \, dy = 0
$$

To verify exactness, check:

$$
\frac{\partial}{\partial y} (2xy + 3) = 2x
$$
$$
\frac{\partial}{\partial x} (x^2 + 4y) = 2x
$$

Since these partial derivatives are equal, the equation is exact. The solution can be found by integrating \( M \) with respect to \( x \) and \( N \) with respect to \( y \), and then combining them appropriately.

### 7. Example 2:
Consider the inexact differential equation:

$$
(xy + 1) \, dx + (x^2 + y) \, dy = 0
$$

To check exactness, compute:

$$
\frac{\partial}{\partial y} (xy + 1) = x
$$
$$
\frac{\partial}{\partial x} (x^2 + y) = 2x
$$

Since these partial derivatives are not equal, the equation is inexact. An integrating factor, such as a function of \( x \) or \( y \), may be used to convert it into an exact equation for solving.
