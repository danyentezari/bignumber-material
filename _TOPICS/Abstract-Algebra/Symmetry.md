# Symmetry

Symmetry is about invariance to coordinate systems.

<i>

**definition** (Symmetry) A property of a tensor or matrix where its components remain unchanged when their indices are interchanged or when the object is transposed, satisfying the following conditions:

- **(Tensor Component Form)** For a second-rank tensor $A$, it is symmetric if $A_{mn} = A_{nm}$ for all $m$ and $n$.
- **(Matrix Transposition)** A matrix is symmetric if it is unchanged by transposition, such that $\tilde{A} = A$.
- **(Resolution Property)** Every second-rank tensor can be resolved into a symmetric part, given by $\frac{1}{2}(A_{mn} + A_{nm})$, and an antisymmetric part.

where
- $A$ is a tensor or matrix.
- $m, n$ are indices identifying components.
- $\tilde{A}$ is the transpose of the matrix.


Note:

- $\tilde{A}$ is also written $A^T$.

</i>


<i>

**definition** (Antisymmetry) A property of a tensor or matrix where its components change sign when their indices are interchanged, satisfying the following conditions:

- **(Tensor Component Form)** For a second-rank tensor $A$, it is antisymmetric if $A_{mn} = -A_{nm}$ for all $m$ and $n$.
- **(Diagonal Property)** For any antisymmetric matrix, the diagonal elements (where $m=n$) must be zero.
- **(Dual Association)** In 3-D space, every antisymmetric second-rank tensor $C$ can be associated with a dual pseudovector $\mathbf{C}$.

where
- $A$ is a tensor or matrix.
- $m, n$ are indices identifying components.
- $C$ is an antisymmetric tensor.

</i>


<i>

**definition** (Permutational Antisymmetry = Fermion Antisymmetry) A property of identical-particle systems, specifically fermions, whose wave functions must change sign under pairwise particle interchanges, satisfying the following conditions:

- **(Permutation Condition)** A many-fermion wave function $\Psi_F(1, \dots, n)$ must satisfy $P\Psi_F(1, \dots, n) = \epsilon_P\Psi_F(1, \dots, n)$ for any permutation $P$.
- **(Representation Role)** $\Psi_F$ serves as the sole basis function for the totally antisymmetric representation of the symmetric group $S_n$.
- **(Levi-Civita Relation)** The sign of the transformation is determined by the Levi-Civita symbol $\epsilon_P$, where $\epsilon_P = 1$ for even permutations and $\epsilon_P = -1$ for odd permutations.

where
- $\Psi_F$ is a fermion wave function.
- $P$ is a permutation operator acting on particle numbers.
- $\epsilon_P$ is the parity of the permutation.
- $S_n$ is the symmetric group of order $n!$.

</i>
