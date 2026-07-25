# Curl

A curl is a vector calculated from the derivative of a mapping of vectors that is used to calculate the change in a vector value within a neighborhood.

Note: Also written $\nabla \times \mathbf{v}$. Also written $\operatorname{rot} \mathbf{v}$.

<i>

**definition [d]** (*Curl = curl = rot = $\nabla \times \mathbf{v}$*) From Kreyszig: let $\mathbf{v}(x,y,z) = [v_{1}, v_{2}, v_{3}] = v_{1}\,\mathbf{i} + v_{2}\,\mathbf{j} + v_{3}\,\mathbf{k}$ be a differentiable vector function of the Cartesian coordinates $x$, $y$, $z$. Then the curl of the vector function $\mathbf{v}$, or of the vector field given by $\mathbf{v}$, is defined by the symbolic determinant

- $\displaystyle \operatorname{curl} \mathbf{v} = \nabla \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ v_{1} & v_{2} & v_{3} \end{vmatrix}$

which equals

- $\displaystyle \left( \dfrac{\partial v_{3}}{\partial y} - \dfrac{\partial v_{2}}{\partial z} \right)\mathbf{i} + \left( \dfrac{\partial v_{1}}{\partial z} - \dfrac{\partial v_{3}}{\partial x} \right)\mathbf{j} + \left( \dfrac{\partial v_{2}}{\partial x} - \dfrac{\partial v_{1}}{\partial y} \right)\mathbf{k}$ .

Instead of $\operatorname{curl} \mathbf{v}$ one also uses the notation $\operatorname{rot} \mathbf{v}$.

where

- $\mathbf{v}$ is a differentiable vector function.
- $v_{1}$, $v_{2}$, $v_{3}$ are the Cartesian components of $\mathbf{v}$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\operatorname{curl} \mathbf{v}$ and $\nabla \times \mathbf{v}$ denote the curl of $\mathbf{v}$.

</i>

## References

1. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — curl via symbolic determinant; expanded component form; synonym $\operatorname{rot} \mathbf{v}$.
