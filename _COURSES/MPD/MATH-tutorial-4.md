### Mathematical Induction

Theorem
> Let $S_n$ be the sum of the first $n$ positive integers. That is, $S_n = \sum\limits_{i=1}^{n} i$



Proposition
>$P(n) = S_n = \dfrac{n(n+1)}{2}$

Prove
>$P(n+1) = S_{n+1} = \dfrac{n(n+1)}{2}$



Basic Step

> Let $n=3$
> $S_3 = \dfrac{3(3+1)}{2} $

> $ = \dfrac{12}{2} = 6$


Induction Step
>$S_{n+1} = \sum\limits_{i=1}^{n+1}i$

>$ = \sum\limits_{i=1}^{n}i + (n+1)$

>$ = \dfrac{n(n+1)}{2} + (n+1)$

>$ = \dfrac{n(n+1)}{2} + \dfrac{2(n+1)}{2}$

>$ = \dfrac{n(n+1) + 2(n+1)}{2}$

>$ = \dfrac{n^2+3n+2}{2}$

>$ = \dfrac{\left(n+1\right)\left(n+2\right)}{2}$

>$ = \dfrac{(n+1)(n+1+1)}{2}$



References:
(1) S. Weintraub, The Induction Book