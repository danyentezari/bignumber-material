# Covariant, Contravariant, and Coordinate Systems

The context if this section is the following. In physics and mathematics, points exist independently of the coordinates used to represent them.

First, we begin a discussion on covariant and contravariant vectors.

Covariant vectors are linear functionals.


<i>

**definition** (*Linear Functional*) A linear transformation from a vector space $V$ to its associated field of scalars $K$, The mapping $f: V \rightarrow K$ must satisfy the following linearity condition:

- $f(ax + by) = af(x) + bf(y)$ 

where

- $x, y \in V$ are vectors
- $a, b \in K$ are scalars
- $V$ is a vector space
- $K$ is the field of scalars.

</i>




<i>

**definition** (*k-Covector*) An alternating $k$-linear function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where

* the following conditions apply:

- The function $T$ is linear in each of its $k$ arguments.
- $T(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\text{sgn } \sigma) T(v_1, \dots, v_k)$ for every permutation $\sigma \in S_k$.

where

- $V$ is a vector space.
- $k$ is a positive integer representing the degree of the covector.
- $v_1, \dots, v_k \in V$ are vectors.
- $A^k(V)$ is the vector space of all $k$-covectors on $V$.
- $\text{sgn } \sigma$ is the sign of the permutation.

Note:

- $A^k(V)$ is also written $\Lambda^k(V^*)$.
- A $k$-covector is also called a multicovector of degree $k$.
- A $k$-covector is also called an alternating $k$-tensor.

</i>


<i>

**definition** (*k-Covector Field*) A function assigning a $k$-covector to each point of a manifold, $\omega: M \rightarrow \Lambda^k(T^*M)$, where

* the following condition applies:

- For each point $p$ in $M$, $\omega(p)$ is an alternating $k$-linear function on the tangent space $T_pM$.

where

- $M$ is a smooth manifold.
- $p$ is a point in $M$.
- $T_pM$ is the tangent space of $M$ at $p$.
- $T^*_pM$ is the cotangent space of $M$ at $p$.
- $\Lambda^k(T^*_pM)$ is the space of all alternating $k$-tensors on the tangent space $T_pM$.
- $\Lambda^k(T^*M)$ is the $k$-th exterior power of the cotangent bundle.

Note:

- $\Lambda^k(T^*_pM)$ is also written $A^k(T_pM)$.
- A $k$-covector field is also called a differential $k$-form.

</i>



<i>

**example** (*k-Covector*) Let

$$
V = \mathbb{R}^2.
$$

Define the function

$$
T : V^2 \rightarrow \mathbb{R}
$$

by

$$
T((a,b),(c,d))
=
ad-bc.
$$

where

* $$a,b,c,d \in \mathbb{R}$$

Let

$$
v_1=(1,2),
\qquad
v_2=(3,4).
$$

Then

$$
T(v_1,v_2)
=
(1)(4)-(2)(3)
=
-2.
$$

Interchanging the vectors gives

$$
T(v_2,v_1)
=
(3)(2)-(4)(1)
=
2
=
-T(v_1,v_2).
$$

Therefore, $T$ changes sign when its arguments are exchanged, so $T$ is alternating.

Furthermore, $T$ is linear in each argument. Hence, $T$ is an alternating $2$-linear function.

Therefore, $T$ is a $2$-covector on $\mathbb{R}^2$.

</i>
