MacCullagh’s 1839 starting point was not circulation: he introduced three differential combinations of the displacement components and proved that they transform as vector components under rotations. His signs are opposite to the modern right-handed curl convention. ([Trinity College Dublin][1])

# Derivation of Curl

MacCullagh's Starting Point. Let

$$
\mathbf{u}
==========

\xi,\mathbf{i}
+
\eta,\mathbf{j}
+
\zeta,\mathbf{k}
$$

be a displacement field with Cartesian components $\xi$, $\eta$, and $\zeta$.

MacCullagh introduced the three quantities

$$
X_M
===

## \frac{\partial\eta}{\partial z}

\frac{\partial\zeta}{\partial y},
$$

$$
Y_M
===

## \frac{\partial\zeta}{\partial x}

\frac{\partial\xi}{\partial z},
$$

and

$$
Z_M
===

## \frac{\partial\xi}{\partial y}

\frac{\partial\eta}{\partial x}.
$$

He showed that under a rotation of Cartesian coordinates,

$$
\begin{pmatrix}
X_M\
Y_M\
Z_M
\end{pmatrix}
$$

transforms in the same manner as the components of a vector.

Modern Sign Convention. With the modern right-handed convention for curl,

$$
\nabla\times\mathbf{u}
======================

*

\begin{pmatrix}
X_M\
Y_M\
Z_M
\end{pmatrix}.
$$

Therefore,

$$
(\nabla\times\mathbf{u})_x
==========================

## \frac{\partial\zeta}{\partial y}

\frac{\partial\eta}{\partial z},
$$

$$
(\nabla\times\mathbf{u})_y
==========================

## \frac{\partial\xi}{\partial z}

\frac{\partial\zeta}{\partial x},
$$

and

$$
(\nabla\times\mathbf{u})_z
==========================

## \frac{\partial\eta}{\partial x}

\frac{\partial\xi}{\partial y}.
$$

General Vector Field. Replace the displacement field by

$$
\mathbf{F}
==========

F_x\mathbf{i}
+
F_y\mathbf{j}
+
F_z\mathbf{k}.
$$

Then

$$
(\nabla\times\mathbf{F})_x
==========================

## \frac{\partial F_z}{\partial y}

\frac{\partial F_y}{\partial z},
$$

$$
(\nabla\times\mathbf{F})_y
==========================

## \frac{\partial F_x}{\partial z}

\frac{\partial F_z}{\partial x},
$$

and

$$
(\nabla\times\mathbf{F})_z
==========================

## \frac{\partial F_y}{\partial x}

\frac{\partial F_x}{\partial y}.
$$

Component Form. Combining the three components,

$$
\nabla\times\mathbf{F}
======================

\left(
\frac{\partial F_z}{\partial y}
-------------------------------

\frac{\partial F_y}{\partial z}
\right)\mathbf{i}
+
\left(
\frac{\partial F_x}{\partial z}
-------------------------------

\frac{\partial F_z}{\partial x}
\right)\mathbf{j}
+
\left(
\frac{\partial F_y}{\partial x}
-------------------------------

\frac{\partial F_x}{\partial y}
\right)\mathbf{k}.
$$

Cross-Product Form. For two vectors,

$$
\mathbf{a}
==========

a_1\mathbf{i}
+
a_2\mathbf{j}
+
a_3\mathbf{k},
$$

and

$$
\mathbf{b}
==========

b_1\mathbf{i}
+
b_2\mathbf{j}
+
b_3\mathbf{k},
$$

their cross product is

$$
\mathbf{a}\times\mathbf{b}
==========================

(a_2b_3-a_3b_2)\mathbf{i}
+
(a_3b_1-a_1b_3)\mathbf{j}
+
(a_1b_2-a_2b_1)\mathbf{k}.
$$

The vector differential operator is

$$
\nabla
======

\mathbf{i}\frac{\partial}{\partial x}
+
\mathbf{j}\frac{\partial}{\partial y}
+
\mathbf{k}\frac{\partial}{\partial z}.
$$

Replacing $\mathbf{a}$ by $\nabla$ and $\mathbf{b}$ by $\mathbf{F}$ gives

$$
\begin{aligned}
\nabla\times\mathbf{F}
&=
\mathbf{i}
\left(
\frac{\partial F_z}{\partial y}
-------------------------------

\frac{\partial F_y}{\partial z}
\right)
\
&\quad+
\mathbf{j}
\left(
\frac{\partial F_x}{\partial z}
-------------------------------

\frac{\partial F_z}{\partial x}
\right)
\
&\quad+
\mathbf{k}
\left(
\frac{\partial F_y}{\partial x}
-------------------------------

\frac{\partial F_x}{\partial y}
\right).
\end{aligned}
$$

Determinant Form. The same cofactor expansion is represented symbolically by

$$
\nabla\times\mathbf{F}
======================

\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \
\dfrac{\partial}{\partial x}
&
\dfrac{\partial}{\partial y}
&
\dfrac{\partial}{\partial z} \
F_x & F_y & F_z
\end{vmatrix}.
$$

Thus,

$$
\operatorname{curl}\mathbf{F}
=============================

\nabla\times\mathbf{F}.
$$

The determinant is symbolic because the second row contains differential operators.

## References

1. MacCullagh, J. *An Essay towards a Dynamical Theory of Crystalline Reflexion and Refraction*. Transactions of the Royal Irish Academy, Vol. XXI. Read 9 December 1839; published 1846. — original differential combinations of the displacement components and their transformation under rotation.

2. Lunney, J. G. *James MacCullagh*. Trinity College Dublin, 2015. — historical account of MacCullagh's rotational theory and the differential operator later called curl.

3. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — modern Cartesian component and determinant forms of curl.

4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. — modern vector differential operators and determinant notation.

[1]: https://www.tcd.ie/media/tcd/secretary/pdfs/discourses/2015_J-G-Lunney-on-James-MacCullagh.pdf?utm_source=chatgpt.com "Microsoft Word - 2015_J G Lunney on James MacCullagh.docx"
