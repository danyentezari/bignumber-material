
- **Homogeneous Ordinary Differential Equations (ODEs)**
  - **Homogeneous First-Order ODE**
    - General form: $$M(x, y)dx + N(x, y)dy = 0$$
    - Example: $$(x^2 + y^2)dx - 2xydy = 0$$
  - **Homogeneous Linear ODE**
    - General form: $$a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + ... + a_1(x)y' + a_0(x)y = 0$$
    - Example: $$y'' + p(x)y' + q(x)y = 0$$

- **Homogeneous Partial Differential Equations (PDEs)**
  - **Homogeneous Linear PDE**
    - General form: $L(u) = 0$, where $L$ is a linear operator
    - Example: $u_t = αu_xx$
  - **Homogeneous Non-linear PDE**
    - Equation where all terms involve the dependent variable and its derivatives
    - Example: $u_xx + u_yy = u^2$

- **Homogeneous Systems of Differential Equations**
  - **Linear System**
    - General form: $A * y' + B * y = 0$
    - Example: ${ y'_1 = y_2, y'_2 = -y_1 }$

- **Homogeneous Boundary Conditions**
  - General form: $y(a) = 0$ or $y'(a) = 0$ at boundary points
  - Example: $y(0) = 0$, $y(L) = 0$