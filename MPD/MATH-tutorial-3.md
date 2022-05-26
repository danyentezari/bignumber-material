### Topics

0. General Math Conventions
1. Set Theory
1.1 Set Notation
1.2 Basic Set Operations
1.3 More Set Operations
2. Propositional Calculus

<br/><br/>
### 0. General Math Conventions
> $a,b,c,...$ are used for constants

> $i,j,k,...$ are used for enumeration

> $n$ is used for quantity

> $x,y,z,...$ are used for variables



<br/><br/>
### 1. Set Theory

**1.1 Set Notation**

Set of indices
> $ I = \{ 0,1,2,3,4 \} $

Set of countries
> $ V = \{ ``America", ``Brazil", ``China", ``Denmark", ``Egypt" \} $


Element in a Set
> $ i_1 \in I $


Set representation of a Python List
> $ L = \{ (i_1, v_1), (i_2, v_2), (i_3, v_3),(i_4, v_4),(i_5, v_5) \}$ 

> $ L = \{ (i_k, v_j) \enspace | \enspace i_k \in I \text{ and } v_j \in V \}$

or colon

> $ L = \{ (i_k, v_j) \enspace : \enspace i_k \in I \text{ and } v_j \in V \}$



Cardinality of the set $L$

> $| L | = 5$

<br/><br/>

**1.2 Basic Set Operations**

Given
> $ A = \{ 1,2,3,4,5\} $

> $ B =  \{ 4,5,6,7,8,9,10 \} $

Union of Two Sets
> $ A \cup B = \{ 1,2,3,4,5,6,7,8,9,10 \} $ 

Intersection of Two Sets
> $ A \cap B = \{ 4,5 \} $


Union with Set Complement
> $ A \cup B' = \{ 1,2,3,4,5 \} = A$

Intersection with Set Complement
> $ A \cap B' = \{  \} = \emptyset $

<br/><br/>

**1.3 More Set Operations**
Given
> $ A = \{ 1,2,3 \} $

> $ B = \{ 4,5,6 \} $

> $ C = \{ 7,8,9 \} $

Union of Multiple Sets
> $ D = A \cup B \cup C = \{ 1,2,3,4,5,6,7,8,9 \}$
or
> $ D = \bigcup\limits_{i=1}^{n} S_i $ 

Intersection of Multiple Sets
> $ E = \bigcap\limits_{i=1}^{n} S_i = \{\} = \emptyset $ 


where
> $ S_1 = A, S_2=B, S_3 = C  $ 
> $ S = \{ S_1, S_2, S_3 \} $

and
> $n = 3 = |S|$




### Propositional Calculus

<br/><br/>
**2.1 Table of Symbols**
| Symbol             | Name                |
|--------------------|-------------------- |
|$ \land $           | And                 |
|$ \lor $            | Or                  |
|$ \neg $            | Not                 |
|$ \rightarrow $     | Implies             |


<br/><br/>
**2.2 Glossary of Words**

**Proposition**
A statement that can only either be true of false

**Argument**
A collection of propositions

**Premise**
A clause of argument that can affect the conclusion

**Conclusion**
The truth value of an argument



<br/><br/>
**2.3 Basic of Logic**
| p | q | p $\land$ q | p $\lor$ q | $\neg(p \land q)$ |
|---|---|-----------|----------|---|
| T | F | F | T | T |


> $p$ = "Fire is hot"
> $q$ = "Japan is in South America"



> $p \land q$ = "Fire is hot and Japan is in South America"

> $p \lor q$ = "Fire is hot or Japan is in South America"

<br/>

| $p$ | $q$ | $p \land q$ | $\neg (p \land q)$ |
|-----|-----|-------------|------------|
| T | T | T | F |
| T | F | F | T |
| F | T | F | T |
| F | F | F | T |


**2.3 Inference**

> $S_1 = $ "If you drive above speed limit, then you'll commit a crime"
> $S_2 = $ "If you commit a crime, then you'll be fined"

> $p = $ "You drive above the speed limit"
> $q = $ "You commit a crime"
> $r = $ "You are fined"

Rule of Inference: Syllogism
> $ p \rightarrow q$
> $ q \rightarrow r$
> $ \therefore p \rightarrow r$

Rule of Inference: Modus Tollens
> $ \neg q = $ "You DON'T commit a crime"
> $p \rightarrow q = $ "If you drive above the speed limit, then you commit a crime"
> $ \therefore \neg p = $ "You DON'T drive above the speed limit"


<br/><br/>

**2.4 Quantifiers**

$\forall$ "For all"
$\exists$ "There exists"

Example 1

> $p(x) = $ $x$ is greater than $5$ and less than $10$
> $T_p = \{ x | x \in \mathbb{N}, \quad p(x) \text{ is true} \}$


> $T_p = \{ 6,7,8,9\}$


Example 2
> $S_1 = \{ 3,4,5,6,8,12,14,20 \}$

> $p(x) = x \text{ ``is a multiple of " } 2 $
> $ (\forall x \in S_1)p(x) $




<br/><br/><br/><br/>
<br/><br/><br/><br/>
<br/><br/><br/><br/>
<br/><br/><br/><br/>
<br/><br/><br/><br/>