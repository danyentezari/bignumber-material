# Curl

A curl is a vector calculated from the derivative of a mapping of vectors that is used to calculate the change in a vector value within a neighborhood.


<i>

**definition [d]** (*Curl = curl = rot = $\nabla \times \mathbf{F}$*) From Kreyszig: let $\mathbf{F}(x,y,z) = [F_{x}, F_{y}, F_{z}] = F_{x}\,\mathbf{i} + F_{y}\,\mathbf{j} + F_{z}\,\mathbf{k}$ be a differentiable vector function of the Cartesian coordinates $x$, $y$, $z$. Then the curl of the vector function $\mathbf{F}$, or of the vector field given by $\mathbf{F}$, is defined by the symbolic determinant

- $\displaystyle \operatorname{curl} \mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ F_{x} & F_{y} & F_{z} \end{vmatrix}$

which equals

- $\displaystyle \left( \dfrac{\partial F_{z}}{\partial y} - \dfrac{\partial F_{y}}{\partial z} \right)\mathbf{i} + \left( \dfrac{\partial F_{x}}{\partial z} - \dfrac{\partial F_{z}}{\partial x} \right)\mathbf{j} + \left( \dfrac{\partial F_{y}}{\partial x} - \dfrac{\partial F_{x}}{\partial y} \right)\mathbf{k}$ .

Instead of $\operatorname{curl} \mathbf{F}$ one also uses the notation $\operatorname{rot} \mathbf{F}$.

where

- $\mathbf{F}$ is a vector field.
- $F_{x}$, $F_{y}$, $F_{z}$ are the Cartesian components of $\mathbf{F}$.
- $x$, $y$, $z$ are Cartesian coordinates.
- $\operatorname{curl} \mathbf{F}$ and $\nabla \times \mathbf{F}$ denote the curl of $\mathbf{F}$.

</i>

## References

1. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — curl via symbolic determinant; expanded component form; synonym $\operatorname{rot} \mathbf{F}$.
