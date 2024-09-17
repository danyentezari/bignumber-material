## tree

0 ordinary Differential Equation 
0 Fundamental Theorem of Calculus
0 Separable equation
1 homogeneous
1 first-order homogeneous differential equations
2 first order differential equation 
1 homogeneous linear differential equation
1 linear differential equations
1 linear differential equations
1 nonlinear differential equations
1 standard form
0 exact equation 
0 inexact equation
0 Bernoulli equation 
1 integrating factor
0 implicit solution
0 explicit solution
0 Newton Law of Cooling

<br/>

  

## definition

**0 [4, pp.20] Ordinary Differential Equation**
An ODE is an equation that involves an independent variable (for example $x$, the function of $x$, and one or more of its derivatives.

<br/>

---

**Fundamental Theorem of Calculus**

$$
\int_a^b f(x) \, dx = F(x) \Big|_a^b =  F(b) - F(a).
$$

where
- $F$ is the integral of $f$

<br/>

---

**Separable equation [5, pp. 16]**

$M(x,y)dx+N(x,y)dy=0 \quad\quad (eq. 1)$

<br/>

Suppose a function $F(x,y)$ can be expressed as the product of two functions 

$$F(x,y)=f(x)+\phi(x) \quad\quad (eq. 2)$$

<br/>

$\dfrac{dy}{dx}=f(x)+\phi(y) \quad (eq. 3)$

<br/>

$g(y)dy=\phi(x)dx  \quad (eq. 4)$

Where 
- $g(y)=\dfrac{1}{\phi(y)}$

Then, intergrate both sides of (eq.4) with respect to the variables on each side.

Dany's note: The author's choice of expressing these two functions with $f$ and $\phi$ is arbitrary.


---
**Exact equation**

A differential equation of the form

$M(x,y)dx+N(x,y)dx=0$

where 
- $M(x,y)dx+N(x,y)dx$ is an exact differential 

<br/>

Here's an example. Consider this equation 

$$ (2xy + y^2)dx + (x^2 + 2xy)dy = 0 \enspace (1)$$ 

We check for exactness by taking the partial derivative of (1) with respect to its variables $x,y$

$\frac{\partial}{\partial y}(2xy + y^2) = 2x + 2y$

$\frac{\partial}{\partial x}(x^2 + 2xy) = 2x + 2y$

            
---
**1 [] First order differential equation**
 
 An equation in the form,
 
$$y' + a(x)y=b(x)$$

Where
- $a(x)$, $b(x)$ are known functions
  
 ---
  
**1[dany] homogeneous**

The word means different things for different classifications of differental equations. For example, "homogenous" in first-order differental equations does not mean the same thing in linear differential equations.

See
https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/core-mathematics/calculus/homogeneous-first-order-differential-equations.html

<br/>

---
**1 [] homogeneous function**

A homogeneous function is a function that remains unchanged when the arguments $x,y$ are multiplied by any constant, $k$.

$f(x,y)=f(kx,ky)$


<br/>

---
**first-order homogeneous differential equations**

$\dfrac{dy}{dx} = F ( \dfrac{y}{x} )$


where
- $F(\dfrac{y}{x})$ is a homogeneous function

---
**1[2, pp.14] standard form**

$y' = f(x,y)$

where
- $y$ is an unknown function

<br/>

---
**1[3, pp.  30] linear differential equation** 

One way to define a linear differential equation is a differential equation wherein there is no power, product, or quotient of the unknown function or it's derivative.

---
**1[1, pp.19] nonlinear differential equations**

$\dfrac{d^2\theta}{dt^2} + \dfrac{g}{L} \sin(\theta) = 0$

where
- $\theta$ is a function
- $\dfrac{g}{L}$ is a constant

This is a non-linear function because the equation involves a term nonlinear in $\theta$.

Another way to define a non-linear differential equation is a differential equation wherein there is a power, product, or quotient of the unknown function or it's derivative.

<br/>

---
**0 [3, pp. 36] Bernoulli Equation**

$$\dfrac{dy}{dx}+p(x)y=q(x)y^n$$

Where
- $n=2,3,4,...$ 

<br/>

**Example**


$$\dfrac{v_1^2-v_2^2}{2g}+\dfrac{p_1-p_2}{\rho g}+(y_1-y_21)=0$$

<br/>

---

**1[4, pp. 82] Integrating Factor
**

An integrating factor is a multiplying factor for converting an inexact differential equation to an exact differential equation.

Note that there is no general way to find integrating factors.

<br/>

---

**0 [1, pp. 44] explicit solution**

An equation of the form

$$y=f(x)$$

<br/>


**5 Newton Law of Cooling**

$$ \dfrac{dT}{dt} = -k(T - T_a) $$

where
- $T$  temperature of the object
- $T_a$ temperature of ambience
- $t$ is time
- $-k$ constant rate of change of temperature
- $\dfrac{dT}{dt}$ change in temperature with respect to time

<br/>

- **Example 1** 
	- asdas 

### references
1. S. Holzner,...Differential Equations for Dummies...
2. Bronson R., Costa G.B..., Schaum's
3. S. Farlow, Introduction to Differential Equations and their Applications.
4. Tenenbaum..., Ordinary Differential Equations
5. ChatGPT
6. Xie,..., differential equations for engineers
7. S. Farlow,..., An Introduction to Differential Equations


## Summary

$\dfrac{dp}{dt}=10c/\text{month}$

This is a differential equation, because it's an equation with a derivative in it.

The solution to a DE may be analytical or numerical. Here, then solution is analytical; specifically the integral of $p$ 



