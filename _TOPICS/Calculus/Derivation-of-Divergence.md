# Derivation of Divergence

$\displaystyle \operatorname{div}\mathbf{F} = \nabla\cdot\mathbf{F} = \dfrac{\partial F_{x}}{\partial x} + \dfrac{\partial F_{y}}{\partial y} + \dfrac{\partial F_{z}}{\partial z}$

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{F}
&=
F_x\mathbf{i}+F_y\mathbf{j}+F_z\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Start from a Cartesian vector field</div>
</div>

</div>

where

- $\mathbf{F}$ is a vector field.
- $F_x$ is the $x$-component of $\mathbf{F}$.
- $F_y$ is the $y$-component of $\mathbf{F}$.
- $F_z$ is the $z$-component of $\mathbf{F}$.
- $\mathbf{i}$ is the unit vector along $x$.
- $\mathbf{j}$ is the unit vector along $y$.
- $\mathbf{k}$ is the unit vector along $z$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
X
&=
\dfrac{\partial F_x}{\partial x}
\\
Y
&=
\dfrac{\partial F_y}{\partial y}
\\
Z
&=
\dfrac{\partial F_z}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Define the three Cartesian differential contributions</div>
</div>

</div>

where

- $X$ is the differential component along $x$.
- $Y$ is the differential component along $y$.
- $Z$ is the differential component along $z$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\partial$ denotes partial differentiation.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
R
&=
X+Y+Z
\end{align*}
$$

</div>
<div class="derivation-just">Add the contributions into one scalar</div>
</div>

</div>

where

- $R$ is the resulting scalar field.
- $X$, $Y$, $Z$ are its Cartesian contributions.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
R
&=
\dfrac{\partial F_x}{\partial x}
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Substitute the differential contributions</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\text{box sides}
&=
\Delta x,\ \Delta y,\ \Delta z
\end{align*}
$$

</div>
<div class="derivation-just">Take the side lengths of a small rectangular box</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta V
&=
\Delta x\,\Delta y\,\Delta z
\end{align*}
$$

</div>
<div class="derivation-just">Form the volume of the box</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta A_x
&=
\Delta y\,\Delta z
\end{align*}
$$

</div>
<div class="derivation-just">Write the area of a face perpendicular to x</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Phi_x^{+}
&=
F_x(x+\Delta x,y,z)\,\Delta y\,\Delta z
\end{align*}
$$

</div>
<div class="derivation-just">Estimate the outward flux through the face at x plus Dx</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Phi_x^{-}
&=
-
F_x(x,y,z)\,\Delta y\,\Delta z
\end{align*}
$$

</div>
<div class="derivation-just">Reverse the sign on the opposite face, whose outward normal points backward</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\Phi_x
&=
\bigl[F_x(x+\Delta x,y,z)-F_x(x,y,z)\bigr]
\Delta y\,\Delta z
\end{align*}
$$

</div>
<div class="derivation-just">Subtract to obtain the net outward flux through the two x-faces</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\dfrac{\partial F_x}{\partial x}
&=
\lim_{\Delta x\to0}
\dfrac{F_x(x+\Delta x,y,z)-F_x(x,y,z)}{\Delta x}
\end{align*}
$$

</div>
<div class="derivation-just">Recall the definition of the partial derivative</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
F_x(x+\Delta x,y,z)-F_x(x,y,z)
&\approx
\dfrac{\partial F_x}{\partial x}\Delta x
\end{align*}
$$

</div>
<div class="derivation-just">Replace the difference by its first-order increment</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\Phi_x
&\approx
\dfrac{\partial F_x}{\partial x}\Delta V
\\
\Delta\Phi_y
&\approx
\dfrac{\partial F_y}{\partial y}\Delta V
\\
\Delta\Phi_z
&\approx
\dfrac{\partial F_z}{\partial z}\Delta V
\end{align*}
$$

</div>
<div class="derivation-just">Convert each pair of opposite faces into a volume times a partial derivative</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\Phi
&=
\Delta\Phi_x+\Delta\Phi_y+\Delta\Phi_z
\end{align*}
$$

</div>
<div class="derivation-just">Add the three pairs to obtain the total outward flux</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\Phi
&\approx
\biggl(
\dfrac{\partial F_x}{\partial x}
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}
\biggr)
\Delta V
\end{align*}
$$

</div>
<div class="derivation-just">Substitute the three face contributions</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\dfrac{\Delta\Phi}{\Delta V}
&\approx
\dfrac{\partial F_x}{\partial x}
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Divide by the volume to obtain a flux density</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\lim_{\Delta V\to0}
\dfrac{\Delta\Phi}{\Delta V}
&=
\dfrac{\partial F_x}{\partial x}
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Shrink the box to a point</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{div}\mathbf{F}
&=
\dfrac{\partial F_x}{\partial x}
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Name this flux density the divergence of F</div>
</div>

</div>

where

- $\operatorname{div}\mathbf{F}$ is the divergence of $\mathbf{F}$.
- Each term is a Cartesian differential contribution.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{div}\mathbf{F}
&=
X+Y+Z
\end{align*}
$$

</div>
<div class="derivation-just">Compare with the assembled scalar</div>
</div>

</div>

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}
&=
a_1\mathbf{i}+a_2\mathbf{j}+a_3\mathbf{k}
\\
\mathbf{b}
&=
b_1\mathbf{i}+b_2\mathbf{j}+b_3\mathbf{k}
\end{align*}
$$

</div>
<div class="derivation-just">Write two general Cartesian vectors</div>
</div>

</div>

where

- $\mathbf{a}$ is the first vector.
- $\mathbf{b}$ is the second vector.
- $a_1$, $a_2$, $a_3$ are components of $\mathbf{a}$.
- $b_1$, $b_2$, $b_3$ are components of $\mathbf{b}$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}\cdot\mathbf{b}
&=
a_1b_1+a_2b_2+a_3b_3
\end{align*}
$$

</div>
<div class="derivation-just">Form the ordinary dot product</div>
</div>

</div>

where

- $\mathbf{a}\cdot\mathbf{b}$ is the dot product.
- Each term is a Cartesian contribution.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla
&=
\mathbf{i}\dfrac{\partial}{\partial x}
\\
&\quad
+\mathbf{j}\dfrac{\partial}{\partial y}
\\
&\quad
+\mathbf{k}\dfrac{\partial}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Define the vector differential operator</div>
</div>

</div>

where

- $\nabla$ is the vector differential operator.
- $\dfrac{\partial}{\partial x}$ differentiates with respect to $x$.
- $\dfrac{\partial}{\partial y}$ differentiates with respect to $y$.
- $\dfrac{\partial}{\partial z}$ differentiates with respect to $z$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf{a}
&=
\nabla
\\
\mathbf{b}
&=
\mathbf{F}
\end{align*}
$$

</div>
<div class="derivation-just">Identify the dot-product factors with nabla and the field</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\nabla\cdot\mathbf{F}
&=
\dfrac{\partial F_x}{\partial x}
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Apply the dot-product rule</div>
</div>

</div>

where

- $\nabla$ supplies the differential operators.
- $\mathbf{F}$ supplies the field components.
- $\cdot$ applies the dot-product rule.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{div}\mathbf{F}
&=
\nabla\cdot\mathbf{F}
\end{align*}
$$

</div>
<div class="derivation-just">Compare with the component form</div>
</div>

</div>

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{grad}\mathbf{F}
&=
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x}
&
\dfrac{\partial F_x}{\partial y}
&
\dfrac{\partial F_x}{\partial z}
\\
\dfrac{\partial F_y}{\partial x}
&
\dfrac{\partial F_y}{\partial y}
&
\dfrac{\partial F_y}{\partial z}
\\
\dfrac{\partial F_z}{\partial x}
&
\dfrac{\partial F_z}{\partial y}
&
\dfrac{\partial F_z}{\partial z}
\end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Write the Cartesian gradient matrix of F</div>
</div>

</div>

where

- Each row contains partial derivatives of one field component.
- Each column contains partial derivatives along one coordinate.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{tr}(\operatorname{grad}\mathbf{F})
&=
\dfrac{\partial F_x}{\partial x}
\\
&\quad
+
\dfrac{\partial F_y}{\partial y}
\\
&\quad
+
\dfrac{\partial F_z}{\partial z}
\end{align*}
$$

</div>
<div class="derivation-just">Sum the diagonal entries</div>
</div>

</div>

where

- $\operatorname{tr}$ denotes the trace of a matrix.
- The trace is the sum of the diagonal entries.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\operatorname{div}\mathbf{F}
&=
\operatorname{tr}(\operatorname{grad}\mathbf{F})
\end{align*}
$$

</div>
<div class="derivation-just">Compare with the component form</div>
</div>

</div>

Hence,

$\displaystyle \operatorname{div}\mathbf{F} = \nabla\cdot\mathbf{F} = \dfrac{\partial F_{x}}{\partial x} + \dfrac{\partial F_{y}}{\partial y} + \dfrac{\partial F_{z}}{\partial z}$

## References

1. Kreyszig, E. *Advanced Engineering Mathematics*. 10th ed. Wiley, 2011. §9.8 — divergence of a vector field and its Cartesian representation.

2. Kreyszig, E. *Advanced Engineering Mathematics*. 10th ed. Wiley, 2011. §10.7 — Gauss's divergence theorem and the relation between divergence and outward flux.

3. Griffiths, D. J. *Introduction to Electrodynamics*. 4th ed. Pearson, 2013. Chapter 1 — divergence, flux, and the divergence theorem.

4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. 3rd ed. Cambridge University Press, 2006. Chapters 10–11 — vector differential operators and surface and volume integrals.

5. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists: A Comprehensive Guide*. 7th ed. Academic Press, 2012. Chapter 3 — vector analysis, differential vector operators, surface integrals, and integral theorems.
