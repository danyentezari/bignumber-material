# Bra and Ket

A notation that writes vectors and linear functionals in matching symbols that is used to compute inner products and matrix elements, where a linear functional is a map from states to complex numbers.

1\. A ket $|\psi\rangle$ is a vector in a complex Hilbert space. A Hilbert space is a complete inner-product space of states. This principle is used to write quantum states as kets.

2\. A bra $\langle\phi|$ is the linear functional that maps a ket to the inner product $\langle\phi|\psi\rangle$. This principle is used to compute amplitudes.

The action of a bra on a ket is

$$
\langle\phi| : \mathcal{H} \rightarrow \mathbb{C},\qquad |\psi\rangle \mapsto \langle\phi|\psi\rangle
$$

where

- $\mathcal{H}$ is the Hilbert space.
- $\langle\phi|\psi\rangle$ is the inner product.

3\. The bra is the Hermitian conjugate of the corresponding ket. This principle is used to pass from $|\phi\rangle$ to $\langle\phi|$.

The bra-ket relation is

$$
\langle\phi| = |\phi\rangle^{\dagger}
$$

where

- $\dagger$ is the Hermitian conjugate.

4\. The matrix element of an operator is $\langle\phi|A|\psi\rangle$. This principle is used to compute amplitudes and expectation values.

Note: These principles are the ket as a state vector, the bra as a linear functional, the dagger relation, and Dirac matrix elements. Also called Dirac notation.

## References

1. Schwichtenberg, J. *Physics from Symmetry*. Springer, 2018. — Eqs. 8.35–8.37 (Dirac notation, ket, bra, inner product).
2. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — bras, kets, and inner products.
3. Cahill, K. *Physical Mathematics*. Cambridge University Press, 2019.
4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006.
