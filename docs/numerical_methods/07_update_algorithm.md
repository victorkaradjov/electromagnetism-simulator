## 7.1 FDTD Update Algorithm

The FDTD method follows the general principle of time-stepping. At each time step, the electric and magnetic fields are updated successively.

Starting from the initialized field values, we first update the magnetic field $H_y^{n+\frac12}$ at the next half time step, using the electric field $E_x^n$ and the previously calculated magnetic field $H_y^{n-\frac12}$. The electric field is then updated to the next full time step, $E_x^{n+1}$, using the newly updated magnetic field $H_y^{n+\frac12}$ and the previously calculated electric-field value $E_x^n$.

We will now proceed with the general architecture of the update algorithm:

```text
Initialize simulation parameters
Initialize spatial grid
Initialize electric and magnetic fields

For each time step:
    Update magnetic field
    Update electric field
    Record field values if needed
```

As mentioned previously, each field update requires the previously calculated value of the field being updated, as well as the corresponding value of the other field at its staggered time level. Therefore, initial values for both fields must be provided before the time-stepping loop begins.

As for the time-stepping loop, each iteration corresponds to a time interval of $\Delta t$. Following the same principle as the Yee lattice, both fields are updated during each iteration, but at different time instants due to their temporal staggering. The field values can be recorded at user-defined intervals, expressed as an integer number of time steps.

The following pseudocode provides a more detailed representation of the algorithm:

```text
Initialize simulation parameters
Initialize spatial grid
Initialize material properties

Initialize electric field Ex
Initialize magnetic field Hy

For each time step n:

    Update magnetic field Hy at n + 1/2
        using Ex at n and Hy at n - 1/2

    Update electric field Ex at n + 1
        using Hy at n + 1/2 and Ex at n

    If recording interval is reached:
        Record electric and magnetic field values
```

This pseudocode provides a general overview of the operations required for a one-dimensional FDTD simulation. Compared with the initial outline, we have added the spatial grid and material properties. Boundary conditions and source excitation are omitted from this overview, as they will be discussed in later sections.

## 7.2 Initial Conditions and Initialization

To simulate an electromagnetic source introduced during the time-stepping process, both fields are initially set to zero. However, due to the temporal staggering of the Yee grid, their initial values are defined at different time levels.

The first magnetic-field update requires an initial value at $t=-\Delta t/2$, which is used along with the initial electric field to calculate the magnetic field at $t=\Delta t/2$. Therefore, the initial conditions are defined as follows:

$$
\begin{aligned}
E_x^0 (i) &= 0 \\[1.5em]
H_y^{-\frac12} (i+\frac12) &= 0
\end{aligned}
$$

These initial conditions are consistent with the temporal staggering of the Yee grid.

## 7.3 Source Excitation

The first electromagnetic source to be implemented in the FDTD simulator is a Gaussian pulse. A Gaussian-modulated sinusoidal pulse will be implemented at a later stage.

### 7.3.1 Gaussian Pulse Definition

The temporal profile of the Gaussian pulse follows a bell-shaped function centered at the time instant $t_0$.

$$
J_{s,x} (t) = J_0 \exp{ \bigg( - \frac{(t - t_0)^2}{2 \sigma_t^2}\bigg)}
$$

where the variables are defined as follows:

- $J_0$: Maximum amplitude of the impressed current density $(A/m²)$
- $t_0$: Time instant at which the pulse reaches its maximum amplitude $(s)$
- $\sigma_t$: Characteristic temporal width of the pulse $(s)$

To ensure that the initial amplitude of the Gaussian pulse is negligible, $t_0$ is generally chosen to be several times larger than $\sigma_t$.

The pulse width $\sigma_t$ also determines the characteristic width of the frequency spectrum:

$$
\sigma_f = \frac{1}{2\pi\sigma_t}
$$

Therefore, the pulse width must be selected in conjunction with the spatial and temporal resolutions of the simulation to ensure that its relevant frequency content can be adequately represented.

For convenience, we define a practical upper frequency cutoff $f_{\max}$ as:

$$
f_{max} = 3\sigma_f = \frac{3}{2\pi\sigma_t}
$$

At the cutoff frequency $f_{\max}=3\sigma_f$, the normalized spectral amplitude is:

$$
\begin{aligned}
\frac{|\tilde J_{s,x}(f_{\max})|}{|\tilde J_{s,x}(0)|}
&= \exp\left(-\frac{f_{\max}^2}{2\sigma_f^2}\right)
\\[1em]
&= \exp\left(-\frac{(3\sigma_f)^2}{2\sigma_f^2}\right)
\\[1em]
&= e^{-\frac92}
\\[1em]
&\approx 0.0111
\end{aligned}
$$
This cutoff is a practical choice. Frequency components above this limit have a spectral amplitude below approximately 1.1% of the maximum value and are therefore considered negligible for the simulation.

With $f_{\max}$ defined, we can calculate the minimum wavelength:

$$
\lambda_{min} = \frac{v_{min}}{f_{max}}
$$

where $v_{\min}$ is the minimum wave speed among all materials considered in the simulation, under the assumption that the media are non-dispersive. We define $v_{\min}$ as:

$$
v_{\min}=\min(v_1,v_2,\ldots,v_M)
$$

where $v_j$ is the wave speed in medium $j$, and $M$ is the number of distinct media considered in the simulation.

For a homogeneous material, we have the following relation:

$$
\lambda_{min} = \frac{v}{f_{max}}
$$

where $v$ is the wave speed in the homogeneous medium.

We initially choose a target value of $N_\lambda=15$ spatial cells per wavelength. This value will serve as a starting point and will be refined through a spatial convergence study.

Therefore, the corresponding spatial grid spacing is:

$$
\Delta z = \frac{\lambda_{min}}{N_\lambda}
$$

### 7.3.2 Source Injection

For the source that introduces an electromagnetic wave, we choose to develop the simulator with a soft source rather than a hard source.

This decision is based on the flexibility it provides. A soft source implies that the resulting field depends on both the already present waves and the excitation from the source.

The source excitation is introduced as an impressed current density defined as:

$$
\mathbf{J_s} = J_{s,x}\, \mathbf{\hat{x}}
$$

The impressed current density depends on both position and time. Its temporal variation is defined by a Gaussian pulse, while its spatial distribution determines the source location.

$$
J_{s,x}=J_{s,x}(z,t)
$$

This source term is introduced in the Ampère-Maxwell law in one dimension:

$$
\frac{\partial H_y}{\partial z} = - \epsilon \frac{\partial E_x}{\partial t} - J_{s,x}
$$

In Section 6.1, we derived the following finite-difference approximations:

$$
\begin{aligned}
\left.\frac{\partial H_y^{n+\frac12}}{\partial z}
\right|_{z=z_i,\;t=t_{n+\frac12}}
\approx
\frac{H_y^{n+\frac12}(i+\frac12)-H_y^{n+\frac12}(i-\frac12)}{\Delta z} 
\end{aligned}
$$
and
$$
\left.\frac{\partial E_x}{\partial t} \right|_{z=z_i,\;t=t_{n+\frac12}}
\approx \frac{E_x^{n+1} (i)\, - \, E_x^n (i)}{\Delta t}
$$

We now evaluate the impressed current density at the corresponding spatial and temporal locations:

$$
J_{s,x}^{n+\frac12}(i)=
\begin{cases}
J_{s,x}(t_{n+\frac12}), & i=i_s\\
0, & i\neq i_s
\end{cases}
$$

So the discretized update equation becomes:

$$
\frac{H_y^{n+\frac12}(i+\frac12)-H_y^{n+\frac12}(i-\frac12)}{\Delta z}  
= - \epsilon \frac{E_x^{n+1} (i)\, - \, E_x^n (i)}{\Delta t}
- J_{s,x}^{n+\frac12} (i)
$$

and by isolating $E_x^{n+1} (i)$, we obtain:

$$
\boxed{
E_x^{n+1}(i)=E_x^n(i)
+\frac{\Delta t}{\epsilon\Delta z}
\left[H_y^{n+\frac12}\left(i-\frac12\right)
-H_y^{n+\frac12}\left(i+\frac12\right)\right]
-\frac{\Delta t}{\epsilon}J_{s,x}^{n+\frac12}(i)
}
$$

## 7.4 Absorbing Boundary Conditions 

Because the simulation domain is finite, a wave reaching one of the simulation boundaries is at risk of being reflected back into the domain. These artificial reflections can superimpose on the physical waves, causing inaccurate results.

To address this problem, we implement an absorbing boundary condition to approximate an open domain, allowing outgoing waves to leave the computational domain while minimizing artificial reflections.

From the one-dimensional wave equation, we obtain the following outgoing-wave conditions:

At the right boundary:

$$
\frac{\partial E_x}{\partial t} + v \frac{\partial E_x}{\partial z} = 0 \tag{1}
$$

At the left boundary:

$$
\frac{\partial E_x}{\partial t}
-v\frac{\partial E_x}{\partial z}=0 \tag{2}
$$

For Mur's first-order absorbing boundary condition, we approximate the outgoing-wave equations with centered finite differences in space and time.

At the right boundary:

$$
\begin{aligned}
\frac{\partial E_x}{\partial t}
&\approx
\frac{
E_x^{n+1}(N)+E_x^{n+1}(N-1)
-E_x^n(N)-E_x^n(N-1)
}{2\Delta t}
\\[1.5em]
\frac{\partial E_x}{\partial z}
&\approx
\frac{
E_x^{n+1}(N)-E_x^{n+1}(N-1)
+E_x^n(N)-E_x^n(N-1)
}{2\Delta z}
\end{aligned}
$$

when substituted into equation (1), we obtain:

$$
E_x^{n+1}(N)=E_x^n(N-1)
+\frac{v\Delta t-\Delta z}{v\Delta t+\Delta z}
\left[E_x^{n+1}(N-1)-E_x^n(N)\right].
$$


By applying the same logic to the left boundary, we obtain:

$$
E_x^{n+1}(0)=
E_x^n(1)
+
\frac{v\Delta t-\Delta z}{v\Delta t+\Delta z}
\left[E_x^{n+1}(1)-E_x^n(0)\right]
$$

To simplify the implementation, we define the following coefficient:

$$
\alpha = \frac{v \Delta t - \Delta z}{v \Delta t + \Delta z}
$$

The conditions then become:

$$
\boxed{
\begin{aligned}
E_x^{n+1}(N)
&=E_x^n(N-1)+\alpha\left[E_x^{n+1}(N-1)-E_x^n(N)\right] \\[1.5em]
E_x^{n+1}(0)
&= E_x^n(1)+\alpha\left[E_x^{n+1}(1)-E_x^n(0)\right]
\end{aligned}
}
$$