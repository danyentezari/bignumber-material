# Relativistic Kinetic Energy Formula Derivation

A derivation of the relativistic kinetic energy formula that is used to obtain $K_{\mathrm{rel}} = (\gamma - 1)mc^{2}$ from the work done by a force.

<i>

**definition [d]** (*Relativistic Kinetic Energy Formula Derivation*) From OpenStax: the relativistic kinetic energy follows from the work-energy theorem. With force

- $\mathbf{F} = \dfrac{d\mathbf{p}}{dt} = m\dfrac{d(\gamma\mathbf{u})}{dt}$ ,

the work that accelerates a particle from rest to final speed $u$ is, in one dimension,

- $K = \displaystyle\int F\, dx = m\displaystyle\int u\,\dfrac{d}{dt}\!\left(\dfrac{u}{\sqrt{1-\left(\dfrac{u}{c}\right)^{2}}}\right) dt$ .

Integrating by parts from rest to speed $u$ gives

- $K = \dfrac{mu^{2}}{\sqrt{1-\left(\dfrac{u}{c}\right)^{2}}} - m\displaystyle\int\dfrac{u}{\sqrt{1-\left(\dfrac{u}{c}\right)^{2}}}\, du$ ,
- $K = \dfrac{mu^{2}}{\sqrt{1-\left(\dfrac{u}{c}\right)^{2}}} + mc^{2}\sqrt{1-\left(\dfrac{u}{c}\right)^{2}}\Big|_{0}^{u}$ ,
- $K = \dfrac{mc^{2}}{\sqrt{1-\left(\dfrac{u}{c}\right)^{2}}} - mc^{2}$ ,

hence

- $K_{\mathrm{rel}} = (\gamma - 1)mc^{2}$ ,

with

- $\gamma = \dfrac{1}{\sqrt{1-\dfrac{u^{2}}{c^{2}}}}$ .

At low speed, the binomial approximation $\gamma \approx 1 + \dfrac{1}{2}\left(\dfrac{u^{2}}{c^{2}}\right)$ yields

- $K_{\mathrm{rel}} \approx \dfrac{1}{2}mu^{2} = K_{\mathrm{class}}$ .

where

- $\mathbf{F}$ is the force.
- $F$ is the one-dimensional force component.
- $\mathbf{p}$ is the relativistic momentum.
- $t$ is time.
- $dt$ is the time differential.
- $m$ is the rest mass.
- $\gamma$ is the Lorentz factor.
- $\mathbf{u}$ is the velocity.
- $u$ is the particle speed.
- $c$ is the speed of light in vacuum.
- $dx$ is the displacement differential.
- $du$ is the speed differential.
- $K$ is the work integral equal to the gained kinetic energy.
- $K_{\mathrm{rel}}$ is the relativistic kinetic energy.
- $K_{\mathrm{class}}$ is the Newtonian kinetic energy.
- $\displaystyle\int F\, dx$ is the work done by the force.

</i>

## References

1. OpenStax. *University Physics Volume 3*, §5.9 Relativistic Energy. — $K=\int F\,dx$ with $F=\dfrac{dp}{dt}$ yields $K_{\mathrm{rel}}=(\gamma-1)mc^{2}$; electron example at $u=0.990c$. https://openstax.org/books/university-physics-volume-3/pages/5-9-relativistic-energy
