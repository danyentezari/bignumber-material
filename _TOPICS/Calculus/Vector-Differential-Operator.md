# Vector Differential Operator

<i>

**definition [d]** (*Vector Differential Operator = Del = Nabla = Gradient Operator*) The symbolic vector operator $\nabla$ that differentiates scalar and vector fields with respect to position. In Cartesian coordinates $(x, y, z)$:

- $\displaystyle \nabla \equiv \hat{\mathbf{x}}\, \frac{\partial}{\partial x} + \hat{\mathbf{y}}\, \frac{\partial}{\partial y} + \hat{\mathbf{z}}\, \frac{\partial}{\partial z}$ .

where

- $\hat{\mathbf{x}}, \hat{\mathbf{y}}, \hat{\mathbf{z}}$ are the Cartesian unit vectors.
- $\nabla$ is not an ordinary vector, but an instruction to differentiate.
- acting on a scalar $f$: $\nabla f$ (gradient); on a vector $\mathbf{v}$: $\nabla \cdot \mathbf{v}$ (divergence), $\nabla \times \mathbf{v}$ (curl).

</i>

## Examples

<i>

**example [d]** (**Gradient** — Riley et al.) The operator $\nabla$ with

- input $\phi = xy^{2}z^{3}$ .

acts as

- $\nabla\phi = y^{2}z^{3}\,\hat{\mathbf{i}} + 2xyz^{3}\,\hat{\mathbf{j}} + 3xy^{2}z^{2}\,\hat{\mathbf{k}}$ .

</i>

<i>

**example [d]** (**Divergence** — Riley et al.) The operator $\nabla\cdot$ with

- input $\mathbf{a} = x^{2}y^{2}\,\hat{\mathbf{i}} + y^{2}z^{2}\,\hat{\mathbf{j}} + x^{2}z^{2}\,\hat{\mathbf{k}}$ .

acts as

- $\nabla\cdot\mathbf{a} = 2(xy^{2} + yz^{2} + x^{2}z)$ .

</i>

<i>

**example [d]** (**Curl** — Kreyszig) The operator $\nabla\times$ with

- input $\mathbf{F} = [y,\, z,\, x]$ .

acts as

- $\nabla\times\mathbf{F} = [-1,\, -1,\, -1]$ .

</i>

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — del / nabla; gradient, divergence, curl.
2. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — vector differential operator.
3. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — nabla operator; curl example $\mathbf{F}=[y,z,x]\mapsto[-1,-1,-1]$.
4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — del operator; gradient of $\phi=xy^{2}z^{3}$; divergence of $\mathbf{a}=x^{2}y^{2}\,\hat{\mathbf{i}}+y^{2}z^{2}\,\hat{\mathbf{j}}+x^{2}z^{2}\,\hat{\mathbf{k}}$.
