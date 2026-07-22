# Group Theory

Group theory will provide the foundation for symmetry, the property of invariance in tensors. 

Symmetry, in turn, will be used to elaborate on both special and general covariance, the principles of special and general relativity.

The collection of transformations that maintain the symmetry of an object will always be a group. We will introduce the basics of a group here.

## Abstract Algebra Preliminaries 

**Binary Operations**
Mathematical operations (for example, arithmetic) that can be applied to elements in a set. Operators $+$ and $\times$ are both binary operators.

**Group**
A group is a tuple $(G, *)$ to which these axioms apply

1. Closure <br/>
$a * b \in S$

2. Identity <br/>
$a * i = i * a = a$

3. Inverse <br/>
$a * a^{-1} = a^{-1} * a = i$

4. Associativity <br/>
$a*(b*c) = (a*b)*c$

**Abelian Group**
An Abelian Group is a group with axioms (1) to (4) and,

1. Commutativity <br/>
$a * b = b * a$

**Ring**
A set to which the following axioms apply:


1. Associativity <br/>
$a+(b+c) = (a+b)+c$

2. Commutativity <br/>
$a+b = b+c$

3. Zero <br/>
$a+0 = 0$

4. Additive Inverse <br/>
$a+(-a) = 0$

5. Associativity (Multiplication) <br/>
$(ab)c = a(bc)$

6. Commutativity (Multiplication) <br/>
$ab = ba$

7. Unity <br/>
$a1 = a$

Note: also called Multiplicative Inverse.
8. Distributivity <br/>
$a(b+c)=a(b) + a(c)$


**Integral Domain**
A type of ring with axioms (1) to (8) but not (7).

**Field**
A type of ring with axioms (1) to (8) and

9. Multiplicative Inverse  <br/>
$a \cdot a^{-1} = a^{-1} \cdot a = a$
