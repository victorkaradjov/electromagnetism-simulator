## 4.1. Discretization of the computational domain

As described in [One-Dimensional Propagation](../theory/03_one_dimensional_propagation.md), the electromagnetic field components $E_x(z,t)$ and $H_y(z,t)$ are represented as continuous functions of space and time. Since these fields are defined over continuous spatial and temporal domains, they can take values at infinitely many positions and time instants. However, a numerical simulation requires a finite number of field values. Therefore, the continuous spatial and temporal domains must be discretized.

For spatial discretization, we divide the computational domain into uniform spatial steps of size $\Delta z$, defined as:

$$
z_i = i\Delta z
$$ 

where:

- $z_i$ : spatial coordinate corresponding to index $i$
- $i$ : an integer index 
- $\Delta z$ : spatial step size

As for temporal discretization, the temporal domain is divided into uniform time intervals of duration $\Delta t$, defined as:

$$
t_n = n\Delta t
$$ 

where:

- $t_n$ : time instant corresponding to index $n$
- $n$ : an integer index 
- $\Delta t$ : time step
