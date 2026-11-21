## 8.1 Courant-Friedrichs-Lewy (CFL) condition

The time step must be selected according to the Courant-Friedrichs-Lewy (CFL) condition.

For the one-dimensional model we previously defined the wave speed as:

$$
v = \frac{1}{\sqrt{\mu \epsilon}}
$$

In a single time interval $\Delta t$, the wave travels a physical distance:

$$
d = v \Delta t
$$

## 8.2 CFL stability condition in 1D

For the Yee grid in one dimension, the CFL stability condition is:

$$
v \frac{\Delta t}{\Delta z} \leq 1
$$

which becomes the following relation for a homogeneous, non-dispersive medium:

$$
\boxed{
\Delta t \leq \Delta z \sqrt{\mu\epsilon}
}
$$

## 8.3 Courant number

The Courant number $S$ is introduced to simplify the selection and implementation of the time step.

$$
S = \frac{v \Delta t}{\Delta z}
$$

with:

$$
S \leq 1
$$

The time step can then be calculated using:

$$
\Delta t = S \frac{\Delta z}{v}
$$


In the FDTD simulation, different media can be involved. Therefore, we consider the maximum wave speed:

$$
v_{max} = \text{max}(v_1, v_2,\ldots, v_M)
$$

The time step then becomes: 

$$
\boxed{\Delta t = S\frac{\Delta z}{v_{\max}}}
\qquad
0 < S \leq 1
$$
