## 3.1. Geometry and propagation direction

To gradually develop the FDTD simulator, electromagnetic wave propagation will initially be modeled in one dimension along the z-axis to reduce the complexity of the problem. A two-dimensional extension will be considered afterward.

## 3.2. Field components and polarization

The electric field is polarized along the x-axis, while the magnetic field strength is polarized along the y-axis. The fields are represented by:

$$
\mathbf{E} = E_x\hat{\mathbf{x}}
\qquad
\mathbf{H} = H_y\hat{\mathbf{y}}
$$

```text
            x  (E_x)
              ^
              |
              |
              |
              +------------------ >  z  (propagation)
             /
           /
         /
       v
  y  (H_y)
```
The fields are perpendicular to each other and to the direction of propagation: $\mathbf{E} \times \mathbf{H}$ points along $+z$.

## 3.3. Model assumptions

The medium is assumed to be linear, isotropic, homogeneous, lossless, and non-dispersive, consistent with the assumptions made in Section 2.

## 3.4. Reduced Maxwell equations

Applying Faraday's law and the Ampère-Maxwell law to the selected field configuration gives:

$$
\frac{\partial E_x}{\partial z} = -\frac{\partial B_y}{\partial t}
$$

and

$$
\frac{\partial H_y}{\partial z} = -\frac{\partial D_x}{\partial t}
$$

We can then use the constitutive relations $D_x = \epsilon E_x$ and $B_y = \mu H_y$ to obtain the following relations:

$$
\begin{aligned}
\frac{\partial E_x}{\partial z}
&= -\mu\frac{\partial H_y}{\partial t}
&& \text{(1)}\\
\frac{\partial H_y}{\partial z}
&= -\epsilon\frac{\partial E_x}{\partial t}
&& \text{(2)}
\end{aligned}
$$



## 3.5. Wave propagation

To obtain the wave equations, we differentiate equation (1) with respect to the spatial coordinate $z$:

$$
\begin{equation} 
\begin{split}
\frac{\partial^2 E_x}{\partial z^2} =& - \mu \frac{\partial}{\partial z}\bigg(\frac{\partial H_y}{\partial t}\bigg) \\ 
=&  - \mu \frac{\partial}{\partial t}\bigg(\frac{\partial H_y}{\partial z}\bigg) \\
=& - \mu \frac{\partial}{\partial t}\bigg(-\epsilon\frac{\partial E_x}{\partial t}\bigg) \\
=&  \mu\epsilon \frac{\partial^2 E_x}{\partial t^2} \\
\end{split}
\end{equation} \tag{3}
$$

By following the same steps with equation (2), we obtain:

$$
\begin{equation} 
\begin{split}
\frac{\partial^2 H_y}{\partial z^2} =& - \epsilon \frac{\partial}{\partial z}\bigg(\frac{\partial E_x}{\partial t}\bigg) \\ 
=&  - \epsilon \frac{\partial}{\partial t}\bigg(\frac{\partial E_x}{\partial z}\bigg) \\
=& - \epsilon \frac{\partial}{\partial t}\bigg(-\mu\frac{\partial H_y}{\partial t}\bigg) \\
=&  \mu\epsilon \frac{\partial^2 H_y}{\partial t^2} \\
\end{split} 
\end{equation} \tag{4}
$$

Equations (3) and (4) now represent the governing wave equations for the selected field components. From these equations, we obtain the theoretical wave speed:

$$
v = \frac{1}{\sqrt{\mu\epsilon}}
$$

A sinusoidal solution for the electric and magnetic fields can be expressed as follows, with the relationship between the electric and magnetic field amplitudes obtained from Maxwell's equations:

$$
\begin{align}
E_x(z,t) &= E_0\cos(kz - \omega t + \delta)\ \\
H_y(z,t) &= H_0\cos(kz - \omega t + \delta)
\end{align}
$$

where the variables are defined as follows:
- $E_0$ : Electric field amplitude
- $H_0$ : Magnetic field strength amplitude
- $z$ : Spatial coordinate
- $\delta$ : Phase offset
- $k$ : Wave number
- $\lambda$ : Wavelength
- $\omega$ : Angular frequency
- $f$ : Frequency
- $v$ : Wave propagation speed
- $\eta$ : Intrinsic impedance of the medium

The following relations also apply:

$$
\begin{align*}
\lambda &= \frac{2\pi}{k}
& \omega &= 2\pi f
& v &= f\lambda = \frac{\omega}{k} \\
\eta &= \sqrt{\frac{\mu}{\epsilon}}
& H_0 &= \frac{E_0}{\eta}
\end{align*}
$$
