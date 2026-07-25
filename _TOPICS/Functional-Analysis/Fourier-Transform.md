# Fourier Transform

Used to transform a signal from its time domain signal to its frequency domain signal.

![FFT Time-Frequency View](https://www.nti-audio.com/portals/0/pic/news/FFT-Time-Frequency-View-540.png)

$$F(x) = \dfrac{1}{\sqrt{2 \pi}} \displaystyle \int_{-\infty}^{\infty} f(u) e^{ixu} \: du$$

where

*$e^{ix} = \cos(x) + i\sin(x)$

Derivation [3, pp.32]...

## Elementary Example
### Simple

The Fourier transform turns a time-domain sample into frequency content. On three sample values, list the discrete inputs.

$$
A = \{ 0,\ 1,\ 2 \}
$$

$$
f(0) = 1,\quad f(1) = 0,\quad f(2) = -1
$$

where

- $f$ is the time-domain function sampled on $A$.
- the transform maps $f$ to a frequency-domain function $F$.

### General

The continuous transform integrates $f$ against a complex exponential.

$$
F(x) = \dfrac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(u)\, e^{i x u}\, du
$$

$$
e^{i x} = \cos x + i \sin x
$$

where

- $F$ is the Fourier transform of $f$.
- $u$ is the integration variable in the time domain.
- $x$ is the frequency variable.

