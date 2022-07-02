## Assignment 3

#### Question 1
Given
> $S_1 = \{10,15,20,25,30\}$
> $S_2 = \{15,25,35,45,55\}$
> $S_3 = \{ 30,35 \}$

>$ S_4 = \Big( \bigcup \limits_{i=1}^{2} S_i \Big) \cap S_3$

(A) What are the elements in the set $S_4$?
(B) What is the cardinality of the set $S_4$?

Ans:
(A)
> $\{10,15,20,25,30,35,45,55\} \cap \{30, 35\}$
> $=\{ 30,35 \}$

(B)
> $|\{ 30,35 \} = 2|$

<br/><br/><br/><br/><br/><br/>

#### Question 2

Given
> $p=T$, $q=F$, $r=T$

<br/>

Evaluate the expression 
> $\neg (p \lor (q \land \neg r))$ 


Ans:
> $\neg (T \lor (F \land \neg T))$ 
> $\neg (T \lor (F \land F))$
> $\neg (T \lor F)$
> $\neg T$
> $F$

<br/><br/><br/><br/><br/><br/>

#### Question 3

Given
> $(\forall x \in S_1)p(x)$
> where
> $p(x)$ is "$x\equiv 0$ (mod 5)"

Note:
See $S_1$ in Question 1.

Write the truth set $T_p$ for $p(x)$


> $S_1 = \{10,15,20,25,30\}$

> $ a \equiv b (\text{mod} n)$
> if
> $a - b$ is divisible by $n$ 

> $10 \equiv 0 (\text{mod } 5)$
> $15 \equiv 0 (\text{mod } 5)$
> $20 \equiv 0 (\text{mod } 5)$
> $25 \equiv 0 (\text{mod } 5)$
> $30 \equiv 0 (\text{mod } 5)$

> Thus, $T_p = S_1 = \{10,15,20,25,30\}$