# Jacobian

A matrix of first partial derivatives of a vector-valued map that is used to describe how small input changes produce output changes.

Jacobian matrix. For $n$ inputs and $m$ outputs, the Jacobian is the $m\times n$ matrix of partial derivatives.

$$
J_{\mathbf{F}}
=
\begin{pmatrix}
\dfrac{\partial F_{1}}{\partial x_{1}} & \cdots & \dfrac{\partial F_{1}}{\partial x_{n}} \\
\vdots & \ddots & \vdots \\
\dfrac{\partial F_{m}}{\partial x_{1}} & \cdots & \dfrac{\partial F_{m}}{\partial x_{n}}
\end{pmatrix}
$$

where


- $\mathbf{F}$ is the vector-valued map.
- $F_{1},\ldots,F_{m}$ are the outputs.
- $x_{1},\ldots,x_{n}$ are the inputs.
- $J_{\mathbf{F}}$ is the Jacobian matrix.

Linear approximation. A small input change produces an approximate output change by multiplication with the Jacobian.

$$
\Delta\mathbf{F}
\approx
J_{\mathbf{F}}\,\Delta\mathbf{x}
$$

where

- $\Delta\mathbf{x}$ is the input change.
- $\Delta\mathbf{F}$ is the output change.

Two-dimensional form. For two inputs and two outputs,

$$
J_{\mathbf{F}}
=
\begin{pmatrix}
\dfrac{\partial F_{x}}{\partial x} & \dfrac{\partial F_{x}}{\partial y} \\
\dfrac{\partial F_{y}}{\partial x} & \dfrac{\partial F_{y}}{\partial y}
\end{pmatrix}
$$

Jacobian determinant. For equal numbers of inputs and outputs, the Jacobian has a determinant. In two dimensions,

$$
\det J_{\mathbf{F}}
=
\dfrac{\partial F_{x}}{\partial x}\dfrac{\partial F_{y}}{\partial y}
-
\dfrac{\partial F_{x}}{\partial y}\dfrac{\partial F_{y}}{\partial x}
$$

Area scaling. The absolute value of the determinant gives the factor by which infinitesimal areas are scaled. Its sign records orientation.

$$
dA'
=
\left|\det J_{\mathbf{F}}\right|\,dA
$$

where

- $dA$ is the original infinitesimal area.
- $dA'$ is the transformed infinitesimal area.

Note: Also called the Jacobian matrix. The determinant of a square Jacobian matrix is called the Jacobian determinant.

## References

1. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. §1.7 — Jacobian matrix as the matrix of partial derivatives of a map $f:U\subset\mathbb{R}^{n}\to\mathbb{R}^{m}$.
2. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. §4.9–4.10 — Jacobian determinant when $m=n$; local volume scaling by $\lvert\det[D\phi(x)]\rvert$.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*. 7th ed. Academic Press, 2013. §4.4 — Jacobian as the determinant of the partial-derivative matrix; $d\tau=J\,du_{1}\,du_{2}\cdots$.
4. Boas, M. L. *Mathematical Methods in the Physical Sciences*. 3rd ed. Wiley, 2005. Chapter 5, §4 — two-dimensional Jacobian determinant; $dA=\lvert J\rvert\,ds\,dt$ and the three-dimensional volume factor.
5. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. 3rd ed. Cambridge University Press, 2006. Chapter 6 — Jacobian determinants in two and three dimensions; change of variables in multiple integrals.
6. Kreyszig, E. *Advanced Engineering Mathematics*. 10th ed. Wiley, 2011. §10.3 — $J=\partial(u,v)/\partial(x,y)$ and $dx\,dy=\lvert J\rvert\,du\,dv$.
7. Stewart, J., Clegg, D., & Watson, S. *Calculus: Early Transcendentals*. Section 15.9 — Jacobian determinant and change of variables in multiple integrals.