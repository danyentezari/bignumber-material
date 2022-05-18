### Logarithms

Used for multiplying large numbers more quickly. Developed by John Napier. For example,
> $8 \times 128 = 2^3 \times 2^7 = 2 ^ {10} = 1024$

You represent the integers you wish to multiply as powers of two (in this example), add up the exponents, and then lookup the table of logarithms to find answer (in this case, $2^{10}$) 

<br/><br/>

To see logarithm tables and see how they were created, watch these videos by Numberphile
- https://www.youtube.com/watch?v=VRzH4xB0GdM (part 1)
- https://www.youtube.com/watch?v=vzV50goW_WM (part 2)


<br/><br/>
#### Example with Logarithm
Consider the logarithm base 2. How are these calculated by hand or machine?
> $\log_2(1) = 0$
> $\log_2(2) = 1$
> $\log_2(3) = 1.585$
> $\log_2(4) = 2$
> $\log_2(5) = 2.322$

Evaluating base 2 using logarithms of another base (e.g, base $e$ or base $10$). This technique is called **Change of Base** (see proof).
> $ \log_2(x) = \dfrac{\ln(x)}{\ln(2)} = \dfrac{\log_e(x)}{\log_e(2)}$


or

>$\log_2(x) =\dfrac{\log_{10}(x)}{\log_{10}(2)} $

Note that
> $\log_e(n) = \ln(n)$


<br/><br/>

#### Proof for Change of Base


> $b^y = x\quad\quad\quad\quad\quad\quad\quad\quad$ (given)

> $x = b^y\quad\quad\quad\quad\quad\quad\quad\enspace\enspace$ (equivalently)

> $\log_b(x) = y \quad\quad\quad\quad\quad\quad$ (definition of logarithm)

Using a different base

> $\log_a(b^y) = \log_a(x)$

> $y \times \log_a(b) = \log_a(x)\quad\quad$  (by Power Rule)

> $y = \dfrac{\log_a(x)}{\log_a(b)}\quad\quad\quad\quad\quad\quad$ (by divison)

> $\therefore \log_b(x) = \dfrac{\log_a(x)}{\log_a(b)}\quad\quad\enspace$ (by substitution)



<br/><br/>

References:
1. D. Bressoud, Calculus Reordered: A History of the Big Ideas...
2. L. Hogben, Mathematics for the Millions