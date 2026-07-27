# Functional

A mapping from a vector space into the scalars that is used to assign a number to each vector in its domain.

Note: When the mapping is linear it is called a linear functional.

<i>

**definition [d]** (*Functional*) From Kreyszig: a functional is an operator whose range lies on the real line $\mathbb{R}$ or in the complex plane $\mathbb{C}$.

where

- an operator is a mapping between vector spaces.
- the range of the functional is a set of scalars in $\mathbb{R}$ or $\mathbb{C}$.

</i>

<i>

**definition [d]** (*Functional*) From Griffel: a functional on a real or complex normed space is a map from the space to the real or complex numbers.

where

- the domain is a real or complex normed space.
- the value of the functional at each point is a scalar.

</i>

<i>

**definition [d]** (*Linear Functional*) From Kreyszig: a linear functional $f$ is a linear operator with domain in a vector space $X$ and range in the scalar field $K$ of $X$; thus

- $f : \mathcal{D}(f) \rightarrow K$ ,

where

- $K = \mathbb{R}$ if $X$ is real and $K = \mathbb{C}$ if $X$ is complex.
- $\mathcal{D}(f)$ is the domain of $f$.

</i>

<i>

**definition [d]** (*Linear Functional*) From Griffel: a linear functional $f$ is a functional such that

- $f(ax + by) = af(x) + bf(y)$

for any scalars $a,b$ and any $x,y$ in the space.

where

- $f$ maps the space into the scalars.
- $a,b$ are real or complex numbers matching the scalar field of the space.

</i>

## Elementary Example

### Simple

A fixed force maps each displacement vector to a work value. On three displacements in $\mathbb{R}^{3}$:

$$
F = (2,\ 0,\ 1)
$$

$$
V = \{ v_{1},\ v_{2},\ v_{3} \}
$$

$$
v_{1} = (1,0,0),\quad v_{2} = (0,1,0),\quad v_{3} = (0,0,3)
$$

$$
W(v) = F \cdot v
$$

$$
W(v_{1}) = 2,\quad W(v_{2}) = 0,\quad W(v_{3}) = 3
$$

where

- $W$ is the work functional.
- $F$ is the fixed force vector.
- $v$ is a displacement vector in $V$.

### General

The classical action maps a path $x(t)$ to a real number by integrating kinetic energy minus potential energy.

$$
S[x] = \int_{a}^{b}\left(\dfrac{m}{2}\left|\dfrac{dx}{dt}\right|^{2} - V\bigl(x(t)\bigr)\right)\, dt
$$

where

- $S$ is the action functional.
- $x(t)$ is a path over the time interval $[a,b]$.
- $m$ is the mass.
- $V$ is the potential energy.

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — §2.8: functional as operator with range in $\mathbb{R}$ or $\mathbb{C}$; linear functional $f:\mathcal{D}(f)\rightarrow K$.
2. Griffel, D. H. *Applied Functional Analysis*. Ellis Horwood, 1981. — Def. 7.52; fixed-$u$ functional $\ell_{u}(x)=u\cdot x$ on $\mathbb{R}^{3}$.
3. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms*. — work $W_{F}=F\cdot v$ as a scalar assigned to a displacement.
4. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — action $S[x]=\int_{a}^{b}\bigl(\dfrac{m}{2}\left|\dfrac{dx}{dt}\right|^{2}-V(x(t))\bigr)\,dt$.
5. Hassani, S. *Mathematical Physics*. Springer. — integration as a linear functional on continuous functions.
