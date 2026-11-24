## 6.1 Discretization of Maxwell's Equations

Using the one-dimensional field configuration introduced in [One-Dimensional Propagation](../theory/03_one_dimensional_propagation.md) and the staggered field locations defined in [Yee Lattice](05_yee_lattice.md), we can derive the finite-difference approximations required by the Yee algorithm.

For the following derivation, we first consider the source-free form of Ampère-Maxwell's equation. The impressed current density source will be incorporated into the electric-field update equation in Section 7.3.2.

Starting with the spatial derivative of the magnetic field $H_y$, the general central-difference approximation can be applied as follows:

$$
\begin{aligned}
\left.\frac{\partial H_y^{n+\frac12}}{\partial z}\right|_{z=z_i,\;t=t_{n+\frac12}}
&\approx \frac{H_y^{n+\frac12}(z_i+h)-H_y^{n+\frac12}(z_i-h)}{2h} \\
&= \frac{H_y^{n+\frac12}\left(z_i+\frac{\Delta z}{2}\right)-H_y^{n+\frac12}\left(z_i-\frac{\Delta z}{2}\right)}{2\left(\frac{\Delta z}{2}\right)} \\
&= \frac{H_y^{n+\frac12}\left(z_i+\frac{\Delta z}{2}\right)-H_y^{n+\frac12}\left(z_i-\frac{\Delta z}{2}\right)}{\Delta z} \\
&= \frac{H_y^{n+\frac12}\left(i+\frac12\right)-H_y^{n+\frac12}\left(i-\frac12\right)}{\Delta z}
\end{aligned}
$$

To complete the discretization of Ampère-Maxwell's equation, we also need to approximate the time derivative of $E_x$, as follows:

$$
\left.\frac{\partial E_x}{\partial t}\right|_{z=z_i,\;t=t_{n+\frac12}}
\approx \frac{E_x^{n+1}(i)-E_x^n(i)}{\Delta t}
$$

The discretized form of Ampère-Maxwell's equation is therefore:

$$
\frac{H_y^{n+\frac12}\left(i+\frac12\right)-H_y^{n+\frac12}\left(i-\frac12\right)}{\Delta z}
= -\epsilon\,\frac{E_x^{n+1}(i)-E_x^n(i)}{\Delta t}
$$

We can now solve for $E_x^{n+1}(i)$ in order to obtain the electric-field update equation:

$$
E_x^{n+1}(i) = E_x^n(i) + \frac{\Delta t}{\epsilon\,\Delta z}
\left[H_y^{n+\frac12}\left(i-\frac12\right)-H_y^{n+\frac12}\left(i+\frac12\right)\right]
\tag{1}
$$

For Faraday's law, we need to solve for $H_y^{n+\frac12}\left(i+\frac12\right)$ in order to obtain the second update equation. The temporal derivative of the magnetic field is approximated using a centered finite difference:

$$
\left.\frac{\partial H_y}{\partial t}\right|_{z=z_{i+\frac12},\;t=t_n}
\approx \frac{H_y^{n+\frac12}\left(i+\frac12\right)-H_y^{n-\frac12}\left(i+\frac12\right)}{\Delta t}
$$

The spatial derivative of the electric field is approximated as follows:

$$
\left.\frac{\partial E_x}{\partial z}\right|_{z=z_{i+\frac12},\;t=t_n}
\approx \frac{E_x^n(i+1)-E_x^n(i)}{\Delta z}
$$

We can now express the second update equation from Faraday's law approximation:

$$
\frac{E_x^n(i+1)-E_x^n(i)}{\Delta z}
= -\mu\,\frac{H_y^{n+\frac12}\left(i+\frac12\right)-H_y^{n-\frac12}\left(i+\frac12\right)}{\Delta t}
$$

By isolating $H_y^{n+\frac12}\left(i+\frac12\right)$, we obtain the magnetic-field update equation:

$$
H_y^{n+\frac12}\left(i+\frac12\right) = H_y^{n-\frac12}\left(i+\frac12\right) + \frac{\Delta t}{\mu\,\Delta z}
\left[E_x^n(i)-E_x^n(i+1)\right]
\tag{2}
$$

Although Ampère-Maxwell's equation was discretized first in this section, this is not the order in which the update equations are applied in the Yee algorithm. In fact, the magnetic field is first updated using Faraday's law, followed by the electric field using Ampère-Maxwell's law. The implementation of this update sequence is described in [FDTD Update Algorithm](07_update_algorithm.md).
