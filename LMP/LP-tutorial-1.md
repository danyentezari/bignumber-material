# Linear Programming Example

#### Background

A sovereign state (breadbasket) that exports grain to importing countries is looking to export their commodity to the international market. They need container liners to ship the grain export.

The government contracts a state-owned manufacturer of agriculture equipment to deliver the right containers for this export.

The manufacturer produces two containers liners for storing and transporting grain: 
1. $C_s=$ standard container
2. $C_p=$ premium container

$C_s$ container can contain 100kg of barley and 100kg of of wheat.

$C_p$ container can contain 200kg of barley and 100kg of of wheat.

The manufacturer has now recieved a qoute for
- $3000 \times 10^4$ tonnes of wheat and 
- $4000 \times 10^4$ tonnes of barley.

They will earn 80 cents on the dollar for $C_p$ and 70 cents for $C_s$. 

They must now deliver the right combination of containers to meet the requirements of the export and also maximize their profit.

<br/>

#### Problem Tasks
1. Express the objective function for as a function of the two variables ($C_p$, $C_s$)
2. Maximize the object function given the constraints


#### Solution to Problem Task

We express the objective function as follows
> $f(C_p,C_s) = 80C_p + 70C_s$

<br/>

To simplify the notation of this LP problem, let 
> $x=C_p$ 
> $y = C_s$


<br/>

Thus, we will rewrite the objective function
> $f(x,y) = 80x + 70y$

With constraints
> $100x + 100y \leq 3000 \times 10^4$ and $x \geq 0$ (for wheat)

> $200x + 100y \leq 4000 \times 10^4$ and $y \geq 0$ (for barley)

<br>

#### LP Tasks
1. Find the feasible region for objective function
2. Find the best point for objective function

Formally, we express the LP problem as follows

| <!-- -->    | <!-- -->    |
|----------|----------------------|
| Maximize | $f(x,y) = 80x + 70y$ |
| Subject to | $100x + 100y \leq 3000 \times 10^4$ &nbsp;&nbsp;&nbsp;&nbsp; $x \geq 0$ <br/> $200x + 100y \leq 4000 \times 10^4$ &nbsp;&nbsp;&nbsp;&nbsp; $y \geq 0$|


<br/>
#### Solution to Task 1

To find the feasible region, we must find the roots of the constraint equations to find the point(s) outlining the feasible region.



Express the constraints as equations. Then, solve for roots, $x,y$.

> $200x + 100y = 4000^{} \times 10^4$ (eq 1)
> $100x + 100y = 3000  \times 10^4$ (eq 2)

<br/>

**Solving for $x$**

Subtracting (eq 2) from (eq 1)
> $100x + 0y = 1000  \times 10^4$

> $100x = 1000 \times 10^4$

Simplifying
> $x = (1000 \times 10^4)/100 = 10 \times 10^4$

<br/>

**Solving for $y$ (eq 2)**

Substituting $x$ in eq2
> $100(10) + 100y = 3000 \times 10^4$ (eq 3)

> $100y = (3000 \times 10^4) - (1000 \times 10^4) = 2000 \times 10^4$

>$y = (2000 \times 10^4)/100 = 20 \times 10 ^ 4$


>$ (x,y) = (10 \times 10^4, 20 \times 10^4) $

<br/>


#### Solution to Task 2

To find the best point, where "best" refers to the point that maximizes the objective function, we solve for the roots of the objective function.


Recall the objective function
> $f = f(x,y) = 80x + 70y$

Now solve for $y$
>$f = 80x + 70y$

Move $70y$ to the left side
>$-70y = 80x -f$ 

Divide $-70$ from both sides
>$-70y \dfrac{1}{-70} = 80x \dfrac{1}{-70} -f \dfrac{1}{-70}y$

Plugin values for $x,y$ in $f$
> $f = 80(10 \times 10 ^ 4) + 70(20 \times 10 ^ 4) = 2,200 \times 10 ^ 4 = 22,000,000$

Converting from cents to dollars, we get
> 22,000,000 cents = 220,000 dollars


<br/>

Solving the objective function for $y$
>$y = -\dfrac{8}{7}x + \dfrac{1}{70}f$



$y$ is now the slope of the objective function that goes through the feasible point
> $y = mx + b$

> $m = -\dfrac{8}{7} = - 1.142$

> $b = \dfrac{1}{70}f = \dfrac{1}{70}2,200 \times 10^4$

<br/>
<br/>
<br/>
<br/>
