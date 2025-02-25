# Classification of Ordinary Differential Equations

This is one of a number of lessons that will cover differential equations. First, we will enumerate the types of ordinary differential equations, and then, in a separate lesson, look at the methods for solving each ordinary differential equation.

### Types of ODEs and Solution Methods.

- First-Order Differential Equations
    - Separation of Variables
    - Integrating Factor Method
    - Exact Equations
    - Bernoulli's Method
- Second-Order Differential Equations
    - Characteristic Equation Method
    - Method of Undetermined Coefficients
    - Variation of Parameters
    - Reduction of Order
- Higher-Order Differential Equations:
   - Frobenius Method
   - Series Solutions
   - Laplace Transform Method


**Homogeneous Function** A function $g(x,y)$ is homogeneous of degree $n$ if $g(tx,ty)=t^{n}g(x,y)$ for all $t$.

<br/>

**Linear Combination** The sum of the products of two or more quantities, each multiplied by some constant value. The linear combination of the elements of a set of vectors and some scalars is written $a_{1}v_{1}+a_{2}v_{2}+...+a_{k}v_{k}$, where each $a_{i}$ represents a real number and each $v_{i}$ represents a vector.

<br/>

**Order of Differential Equations** The order of a differential equation is the order of the highest derivative that appears in the equation.

For example,

$$ \dfrac{dv}{dt}+v\dfrac{k}{m}=g \qquad (1)$$

$$ \dfrac{d^{2}y}{dx^{2}}+2\dfrac{dy}{dx}=0 \qquad (2)$$


Where $(1)$ and $(2)$ are first-order and second-order differential equations, respectively.

<br/>

**Linear Differential Equation** An $n$-th order ordinary differential equation is linear when it can be written in the form

$$a_{0}(x)\frac{d^{n}y}{dx^{n}} + a_{1}(x)\frac{d^{n-1}y}{dx^{n-1}} + \dots + a_{n}(x)y = f(x), \quad a_{0}(x) \ne 0$$

where:
- $a_i(x)$ are functions called the coefficients of the differential equation,
- $f(x)$ is called the non-homogeneous term. 
  
If $f(x) = 0$, the equation is homogeneous.

The linearity refers to how each term is a product of (1) a coefficient and (2) the function or its derivatives.

<br/>

**Homogeneous Differential Equation** This is a class of differential equations, of which ordinary differential equations are a subtype. There are several subtypes so they will be defined in a separate lesson. However, two types of homogeneous differential equations will be mentioned here because they are of the ordinary type.

<br/>

**Homogeneous First-Order ODE**
  - General form: $$M(x, y)dx + N(x, y)dy = 0$$
  - Example: $$(x^2 + y^2)dx - 2xydy = 0$$

    For the equation to be homogeneous, the functions $M(x, y)$ and $N(x, y)$ must be homogeneous of the same degree

<br/>

**Homogeneous Linear Differential Equation** A type of linear differential equation. Note that this type of differential equation is not always ordinary. There also exist homogeneous partial linear differential equations (which will be covered in a separate lesson).

There are two aspects about a homogeneous linear differential equations:

1. Zero condition: when the equation is zero
2. Dependent variable: where every term in the linear differential equation involves the dependent variable or its derivatives.

<br/>

**General Linear Differential Equation**

- **First-order:**
    $$a_{0}(x)\frac{dy}{dx} + a_{1}(x)y = F(x)$$


- **Second-order:**
    $$a_{0}(x)\frac{d^2y}{dx^2} + a_{1}(x)\frac{dy}{dx} + a_{2}(x)y = F(x)$$


- **$n$th-Order:**
    $$a_n(x)\frac{d^n y}{dx^n} + a_{n-1}(x)\frac{d^{n-1} y}{dx^{n-1}} + \cdots + a_1(x)\frac{dy}{dx} + a_0(x)y = F(x)$$

where:
  - $ a_n(x), a_{n-1}(x), \dots, a_0(x) $ are functions of $ x $
  - $ F(x) = 0 $ is the non-homogeneous term, also called a forcing function
  - $ y $ is the unknown function

<br/>

**Forcing Function** The input to a system in a differential equation. The forcing function, $F(X)$, is said to homogeneous when $F(X)=0$ and non-homogeneous  when $F(X) \neq 0$. The forcing function can also be a constant or function of $x$. It cannot be a function of the unknown function, however.

## References:
1. S. Farlow, Introduction to Differential Equations with Applications, 2013.
2. Boyce, W. E., & DiPrima, R. C. (2012). Elementary differential equations and boundary value problems (10th ed.). John Wiley & Sons.