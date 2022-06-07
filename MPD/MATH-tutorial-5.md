#### Basic Terminology

Alphabet
> $A = \{a,b,c\}$

Letters
> $a \in A$
> $b \in A$
> $c \in A$

Words
> $u = ababb$
> $v = acbacb $

Empty Word
> $\lambda$ or $\epsilon$

Set of All Words
> $A^* = \{ a, aa,...,abbb \}$

Length
> $|u| = 5$ or $l(u) = 5$

<br/><br/>

#### Language

A language is a subset of $A^*$
> $ L_1 = \{ a, aa, a^3, a^4, ... \} $

> $ L_2 = \{ b, bb, b^3, b^4, ... \} $

where
> $ L_1 \subset A^*$
> $ L_2 \subset A^*$


<br/><br/>

#### Regular Expression

> $( \quad ) \quad * \quad \lor \quad \lambda$

and

> $A_1 = \{ a,p,l,e \}$


Examples
> $r = a^*$ includes $\lambda$

> $r = aa^*$

> $r = a \lor b^* = \{ a, ab, abb,abbb,... \}$


> $r = a^* \lor b^* = b^* \lor a^* = \{ ab, ba,aab,aba,bba \}$

<br/><br/>


#### RegEx in Programming
| Math	|	Programming |
|-------|---------------|
|$*$	     |		{0,}
|$aa^*$      |	    aa{0,}
|$a \lor b$  |      a \| b
| $a (p \lor l)p^* (l \lor e) (e \lor l)$                   |    `a(p|l)p{0,}(l|e){0,}(e|l){0,}` |


<br/><br/>


### Finite State Machine (or Automaton)

> $M = (A,S,Y,s_0, F)$

where
> $A = \{ a,b \}$ is the set of input symbols
> $S = \{ s_0, s_1, s_2 \}$ is the set of internal states
> $Y = \{s_0, s_1\}$ is the set of yes states
> $s_0$ is the initial state
> $F : S \times A \rightarrow S$ is the next state function


| F   | a   | b   |
|-----|-----|-----|
| $s_0$ | $s_0$ | $s_1$ |
| $s_1$ | $s_0$ | $s_2$ |
| $s_2$ | $s_2$ | $s_2$ |

> ababba
> $P_1 = s_0 \xrightarrow{a} s_0 \xrightarrow{b} s_1 \xrightarrow{a} s_0 \xrightarrow{b} s_1 \xrightarrow{b} s_2 \xrightarrow{a} s_2$ 

Since $s_2 \notin Y$, the word $ababba$ will not matched by the automaton, $M$. 


<br/><br/><br/><br/><br/><br/><br/><br/>