### Topics

0. General Math Conventions
1. Set Theory
1.1 Set Notation
1.2 Basic Set Operations
1.3 More Set Operations

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
