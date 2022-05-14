### Topics
1. Sets
2. Functions
3. Propositional Calculus
4. Relations
5. Graphs



<br/><br/>
### Symbols


**Set Operations**
| Symbol             | Name                |
|--------------------|-------------------- |
|$ \cap $            | Intersection        |
|$ \cup $            | Union               |
|$ \neg $            | Complement          |


**Logic**
| Symbol             | Name                |
|--------------------|-------------------- |
|$ \land $           | And                 |
|$ \lor $            | Or                  |
|$ \neg $            | Not                 |


<br/><br/>
### 1. Sets

A set is a mathematical structure; that is, it is a collection of mathematical objects to which some rules apply. 

>$
>A = \{  1,2,3,4,5 \} \\
>B = \{ 5,6, \{A\}, f, \vec{b} \} \\
>f: A \rightarrow |A|
>$



```
A = {1,2,3,4,5}
B = {1,2,3,A,f}

def f(someSet):
    return len(someSet)
```


<br/><br/>
### 2. Functions
Defining a function
```
def sum(numA, numB):
    numC = numA + numB
    return numC
```

>*Let*
>$\text{sum}: \mathbb{R}^2 \rightarrow \mathbb{R}$ 
> *be a function defined as*
> $\text{sum} (\text{numA},\text{numB}) = \text{numA} + \text{numB} = \text{numC} $


<br/>
Calling the function
```
print(sum(2,3))
```



>$(\text{print } \circ \text{ sum})(2,3) = \text{print}(\text{sum(2,3)})$

<br/>
Defining a function with conditions

```
def checkExists(element, theSet)
    if element in theSet:
        return True
    else:
        return False
```



>$
>\text{checkExists} = \begin{cases}
>    True \quad \text{element} \in \text{A} \\
>    False \quad \text{element} \notin \text{A}
>\end{cases}
>$


<br/><br/>
### 3. Sets

Example with Union
```
A = {1,2,3,4,5}
B = {6,7,8,9,10}
A.union(B) # {1,2,3,4,5,6,7,8,9,10}
```

>$A = \{  1,2,3,4,5 \}$
>$B = \{  6,7,8,9,10 \}$
>$A \cup B =  \{1,2,3,4,5,6,7,8,9,10\}$

<br/>
Example with Intersection

```
A.intersection(B) # {}
```

>$A \cap B =  \emptyset = \{\}$

<br/>
Example with Propositional Calculus

```
p = True
q = True
v = False

print(p and q)          # True
print(p and v)          # False
print(p and (q and v))  # False

print( !(p and q))      # False
```

>$p = T$ 
>$q = T$
>$v = F$

>$p \land q = $ True
>$p \land v = $ False
>$p \lor v = $ True

>$p \land (q \land v) =$ False 

>$\neg(p \land q) = $ False


<br/><br/>
### 4. Relations

**4.1 Practical Example**
A relation explains the association of two or more sets.

> $R = \{\text{ (Chicago}, \text{US} ), \text{ (Cape Town}, \text{SA} ), (\text{Manchester}, \text{UK} )\}$
>
> $A = \{ \text{Chicago},\text{Cape Town},\text{Berlin} \}$
> $B = \{ \text{US},\text{SA},\text{UK} \}$

If an element $a \in A$ is related to an element $b \in B$ such that $(a,b) \in R$, then we say that "$a$ is $R$-related to $b$" and we write $aRb$

In this case, we have $\text{Chicago} \in A$ and $\text{US} \in B$. Thus, we write:
> $ \text{Chicago } R \text{ US} $


**4.2 Formal Example**

> Definition: Let A and B be two sets. A binary relation from A to
> B is a subset of a Cartesian product A x B.
> - Let $R \subseteq A \times B$ means R is a set of ordered pairs of the form $(a,b)$ where $a \in A$ and $b \in B$.
> - We use the notation $a R b$ to denote $(a,b) \in R$ and  $a \sout{R} b$ to denote $(a,b) \notin R$. If $a R b$, we say a is related to b by R.
>
> Example: Let $A={a,b,c}$ and $B={1,2,3}$.
> • Is $R={(a,1),(b,2),(c,2)}$ a relation from A to B? Yes.
> • Is $Q={(1,a),(2,b)}$ a relation from A to B? No.
> • Is $P={(a,a),(b,c),(b,a)}$ a relation from A to A? Yes




<br/><br/>
###  5. Graphs
A graph is a space with two elements: (1) set of vertices and (2) set of edges. Formally, we indicate a graph as follows


> $G = (V,E)$


**5.1 Graphs and Multigraphs**
**5.1.1 Example**
> $G = (V,E)$
>
> $V = \{A,B,C,D\}$
> $E = \{ e_1, e_2, e_3, e_4, e_5 \}$
> 
> where 
> $e_1 = \{A,B\}$
> $e_2 = \{B,C\}$
> $e_3 = \{C,D\}$
> $e_4 = \{B,D\}$
> $e_5 = \{A,C\}$

> $\deg(B) = 2$

**5.1.2 Example**
> $G = (V,E)$
>
> $V = \{A,B,C,D\}$
> $E = \{ e_1, e_2, e_3, e_4, e_5 \}$
> 
> where 
> $e_1 = \{A,D\}$
> $e_2 = \{A,C\}$
> $e_3 = \{B,D\}$
> $e_4 = \{B,C\}$
> $e_5 = \{A,C\}$
> $e_6 = \{D,D\}$

> $\deg(D) = 4$