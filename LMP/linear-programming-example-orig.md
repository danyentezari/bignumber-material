# Linear Programming Example


#### Background

A sovereign state (breadbasket) that exports grain to importing countries is looking to maximize their profit.

A state-owned manufacturer of agriculture equipment produces two containers liners for storing and transporting grain: 
1. $C_s=$ standard container
2. $C_p=$ premium container


$C_s$ container can contain 100kg of barley and 100kg of of wheat.

$C_p$ container can contain 200kg of barley and 100kg of of wheat.



#### Tasks
1. Find the feasible region for objective function
2. Find the best point for objective function


Objective function
> $f(x,y) = 30x + 20y$

Constraints
> $x + y \leq 3000$ and $x \geq 0$

> $2x + y \leq 4000$ and $y \geq 0$

<br/>



#### Task 1

To find the feasible region, we must find the roots of the constraints to find the point(s) outlining the feasible region.

Express the constraints as equations. Then, solve for roots, $x,y$.
> $2x + y = 4000$ (eq 1)
> $x + y = 3000$ (eq 2)

Subtracting eq2 from eq1
> $x = 1000$

Substituting $x$ in eq2
> $1000 + y = 3000$ (eq3)

Solving for $y$

> $y = 3000 - 1000 = 2000$

>$ (x,y) = (1000, 2000) $

<br/>

#### Task 2

To find the best point, where "best" refers to the point that maximizes the objective function, we solve for the roots of the objective function.

Recall the objective function
> $f = f(x,y) = 30x + 20y$

Now solve for $y$
>$f = 30x + 20y$

Move $20y$ to the left side
>$-20y = 30x -f$ 

Divide $-20$ from both sides
>$-20y \dfrac{1}{-20} = 30x \dfrac{1}{-20} -f \dfrac{1}{-20}y$

Evaluate the above expression
>$y = -\dfrac{3}{2}x + \dfrac{1}{20}f$
