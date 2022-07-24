# Neural Networks
See [10, pp. 694]

### Convolutional Layer

<br/>

**1D Convolution Example**

$\mathbf{x} = \{ x_1, x_2, ..., x_n \}$
$\mathbf{w} = \{ x_1, x_2, ..., x_k \}$

$\mathbf{x} * \mathbf{w} = \text{sum}( \mathbf{x}_k(i) \odot \mathbf{w} )$

where
- $\mathbf{x}$ is the data
- $\mathbf{w}$ is the filter
- $\odot$ is element-wise multiplication

<br/>

### Filter

Matrix of weights to "percieve" the outlines of the picture (e.g, vertical lines, horizontal lines, etc.)

<br/>

### Max Pooling

The max pooling matrix is used to achieve the following:
1. Reduce the computational load of computing activations
2. To become translationally invariant

