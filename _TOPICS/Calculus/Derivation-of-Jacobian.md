# Derivation of Jacobian

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
J_{\mathbf F}
&=
\dfrac{\partial(F_1,\ldots,F_m)}{\partial(x_1,\ldots,x_n)}
=
\begin{pmatrix}
\dfrac{\partial F_1}{\partial x_1} & \cdots & \dfrac{\partial F_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\dfrac{\partial F_m}{\partial x_1} & \cdots & \dfrac{\partial F_m}{\partial x_n}
\end{pmatrix}
\end{align*}
$$

</div>
</div>

</div>

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf F
&=
\begin{pmatrix} F_1 \\ F_2 \\ \vdots \\ F_m \end{pmatrix}
\\
\mathbf x
&=
\begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Start from a vector-valued map and its input</div>
</div>

</div>

where

- $\mathbf F$ is a vector-valued function.
- $F_i$ is an output component.
- $\mathbf x$ is the input vector.
- $x_j$ is an input coordinate.
- $m$ is the number of outputs.
- $n$ is the number of inputs.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\mathbf x
&=
\begin{pmatrix} \Delta x_1 \\ \Delta x_2 \\ \vdots \\ \Delta x_n \end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Change the input by a small increment</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\mathbf F
&=
\mathbf F(\mathbf x+\Delta\mathbf x)-\mathbf F(\mathbf x)
\end{align*}
$$

</div>
<div class="derivation-just">Form the corresponding output change</div>
</div>

</div>

where

- $\Delta\mathbf x$ is the input change.
- $\Delta\mathbf F$ is the output change.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta F_i
&=
F_i(\mathbf x+\Delta\mathbf x)-F_i(\mathbf x)
\end{align*}
$$

</div>
<div class="derivation-just">Write the change in one output component</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta F_i
&\approx
\sum_{j=1}^{n}
\dfrac{\partial F_i}{\partial x_j}\Delta x_j
\end{align*}
$$

</div>
<div class="derivation-just">Keep the first-order Taylor increment</div>
</div>

</div>

where

- $\Delta F_i$ is one output change.
- $\partial F_i/\partial x_j$ measures coordinate sensitivity.
- Higher-order terms vanish faster than $\Delta\mathbf x$.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta F_1
&\approx
\dfrac{\partial F_1}{\partial x_1}\Delta x_1
\\
&\quad
+\cdots
\\
&\quad
+\dfrac{\partial F_1}{\partial x_n}\Delta x_n
\\
\Delta F_m
&\approx
\dfrac{\partial F_m}{\partial x_1}\Delta x_1
\\
&\quad
+\cdots
\\
&\quad
+\dfrac{\partial F_m}{\partial x_n}\Delta x_n
\end{align*}
$$

</div>
<div class="derivation-just">Repeat the increment for every output component</div>
</div>

</div>

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\begin{pmatrix}
\Delta F_1 \\
\Delta F_2 \\
\vdots \\
\Delta F_m
\end{pmatrix}
&\approx
\begin{pmatrix}
\dfrac{\partial F_1}{\partial x_1}
&
\cdots
&
\dfrac{\partial F_1}{\partial x_n}
\\
\vdots
&
\ddots
&
\vdots
\\
\dfrac{\partial F_m}{\partial x_1}
&
\cdots
&
\dfrac{\partial F_m}{\partial x_n}
\end{pmatrix}
\begin{pmatrix}
\Delta x_1 \\
\Delta x_2 \\
\vdots \\
\Delta x_n
\end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Collect the component increments into a matrix product</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
J_{\mathbf F}
&=
\begin{pmatrix}
\dfrac{\partial F_1}{\partial x_1}
&
\cdots
&
\dfrac{\partial F_1}{\partial x_n}
\\
\vdots
&
\ddots
&
\vdots
\\
\dfrac{\partial F_m}{\partial x_1}
&
\cdots
&
\dfrac{\partial F_m}{\partial x_n}
\end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Name that matrix the Jacobian of F</div>
</div>

</div>

where

- $J_{\mathbf F}$ is the Jacobian matrix.
- Rows correspond to output components.
- Columns correspond to input coordinates.
- Each entry is a partial derivative.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta\mathbf F
&\approx
J_{\mathbf F}\Delta\mathbf x
\end{align*}
$$

</div>
<div class="derivation-just">Read the first-order change as a linear map of the input increment</div>
</div>

</div>

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\mathbf F(x,y)
&=
\begin{pmatrix} F_x(x,y) \\ F_y(x,y) \end{pmatrix}
\\
\Delta\mathbf x
&=
\begin{pmatrix} \Delta x \\ \Delta y \end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Specialize to two input and two output coordinates</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\Delta F_x
&\approx
\dfrac{\partial F_x}{\partial x}\Delta x+\dfrac{\partial F_x}{\partial y}\Delta y
\\
\Delta F_y
&\approx
\dfrac{\partial F_y}{\partial x}\Delta x+\dfrac{\partial F_y}{\partial y}\Delta y
\end{align*}
$$

</div>
<div class="derivation-just">Write the two first-order component changes</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\begin{pmatrix} \Delta F_x \\ \Delta F_y \end{pmatrix}
&\approx
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x} & \dfrac{\partial F_x}{\partial y} \\
\dfrac{\partial F_y}{\partial x} & \dfrac{\partial F_y}{\partial y}
\end{pmatrix}
\begin{pmatrix} \Delta x \\ \Delta y \end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Collect those increments into a two-by-two product</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
J_{\mathbf F}
&=
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x} & \dfrac{\partial F_x}{\partial y} \\
\dfrac{\partial F_y}{\partial x} & \dfrac{\partial F_y}{\partial y}
\end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Read off the two-dimensional Jacobian</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\det J_{\mathbf F}
&=
\begin{vmatrix}
\dfrac{\partial F_x}{\partial x} & \dfrac{\partial F_x}{\partial y} \\
\dfrac{\partial F_y}{\partial x} & \dfrac{\partial F_y}{\partial y}
\end{vmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Form the Jacobian determinant when the dimensions match</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
\det J_{\mathbf F}
&=
\dfrac{\partial F_x}{\partial x}\dfrac{\partial F_y}{\partial y}
-
\dfrac{\partial F_x}{\partial y}\dfrac{\partial F_y}{\partial x}
\end{align*}
$$

</div>
<div class="derivation-just">Expand the two-by-two determinant</div>
</div>

</div>

where

- $\det J_{\mathbf F}$ is the Jacobian determinant.
- Its magnitude gives local area scaling.
- Its sign gives orientation change.

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
d\mathbf x_1
&=
\begin{pmatrix} dx \\ 0 \end{pmatrix}
\\
d\mathbf x_2
&=
\begin{pmatrix} 0 \\ dy \end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Take the two coordinate edge displacements</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
dA
&=
dx\,dy
\end{align*}
$$

</div>
<div class="derivation-just">Form the original area they span</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
d\mathbf F_1
&=
J_{\mathbf F}\,d\mathbf x_1
\\
d\mathbf F_2
&=
J_{\mathbf F}\,d\mathbf x_2
\end{align*}
$$

</div>
<div class="derivation-just">Map those edges by the Jacobian</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
d\mathbf F_1
&=
\begin{pmatrix}
\dfrac{\partial F_x}{\partial x}dx \\
\dfrac{\partial F_y}{\partial x}dx
\end{pmatrix}
\\
d\mathbf F_2
&=
\begin{pmatrix}
\dfrac{\partial F_x}{\partial y}dy \\
\dfrac{\partial F_y}{\partial y}dy
\end{pmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Write the images of the two edges</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
dA'
&=
\begin{vmatrix}
\dfrac{\partial F_x}{\partial x}dx
&
\dfrac{\partial F_x}{\partial y}dy
\\
\dfrac{\partial F_y}{\partial x}dx
&
\dfrac{\partial F_y}{\partial y}dy
\end{vmatrix}
\end{align*}
$$

</div>
<div class="derivation-just">Compute the signed area of the image parallelogram</div>
</div>

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
dA'
&=
\det(J_{\mathbf F})\,dA
\end{align*}
$$

</div>
<div class="derivation-just">Factor out the original area</div>
</div>

</div>

Hence,

<div class="derivation">

<div class="derivation-row">
<div class="derivation-math">

$$
\begin{align*}
J_{\mathbf F}
&=
\dfrac{\partial(F_1,\ldots,F_m)}{\partial(x_1,\ldots,x_n)}
=
\begin{pmatrix}
\dfrac{\partial F_1}{\partial x_1} & \cdots & \dfrac{\partial F_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\dfrac{\partial F_m}{\partial x_1} & \cdots & \dfrac{\partial F_m}{\partial x_n}
\end{pmatrix}
\end{align*}
$$

</div>
</div>

</div>

## References

1. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. Prentice Hall, 1998, §1.7, pp. 107–112.

2. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*, 3rd ed. Cambridge University Press, 2006, §5.7, pp. 160–161.

3. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*, 3rd ed. Cambridge University Press, 2006, §6.4, pp. 199–206.
