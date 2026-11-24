## 2. Constitutive Relations

For a dielectric material subjected to an electric field, the general macroscopic electric displacement field is defined as:

$$
\mathbf{D} = \epsilon_0\mathbf{E}+\mathbf{P}
$$

Here, $\mathbf{E}$ is the total electric field within the dielectric, $\mathbf{P}$ is the polarization of the material, and $\epsilon_0$ is the permittivity of free space.

The bound volume charge density is related to the polarization vector $\mathbf{P}$ by the following relation:

$$
\rho_b=-\nabla\cdot\mathbf{P}
$$

For a linear, isotropic and homogeneous dielectric medium, the polarization can be expressed in terms of the electric susceptibility of the material $\chi_e$ as:

$$
\mathbf{P}=\epsilon_0\chi_e\mathbf{E}
$$

Therefore, the constitutive relation simplifies to:

$$
\begin{split}
\mathbf{D} & =
\epsilon_0(1+\chi_e)\mathbf{E}\\
& =\epsilon\mathbf{E}
\end{split}
$$

The absolute permittivity is defined as follows: 

$$
\epsilon=\epsilon_0\epsilon_r
=\epsilon_0(1+\chi_e)
$$

where $\epsilon$ is the absolute permittivity of the material, and $\epsilon_r$ is its relative permittivity.

In the first version of the FDTD simulator, $\epsilon$ is treated as a real-valued, positive scalar constant, independent of space, time and frequency. This corresponds to a homogeneous, time-invariant and non-dispersive dielectric medium. Dielectric losses and frequency-dependent effects are therefore neglected.

For magnetic materials, the general relation defining the magnetic flux density is:

$$
\mathbf{B}=\mu_0(\mathbf{H}+\mathbf{M})
$$

Here, $\mathbf M$ is the magnetization vector, which describes the macroscopic magnetic response of the material to an applied magnetic field.
For a linear, isotropic and homogeneous magnetic medium, the magnetization can be expressed as:

$$
\mathbf{M} = \chi_m \mathbf{H}
$$

where $\chi_m$ is the magnetic susceptibility of the material.

We can then substitute this relation into the general definition of the magnetic flux density:

$$
\begin{split}
\mathbf{B} & =
\mu_0(1+\chi_m)\mathbf{H}\\
& =\mu\mathbf{H}
\end{split}
$$

The absolute permeability $\mu$ is defined as follows:

$$
\mu = \mu_0\mu_r = \mu_0(1+\chi_m)
$$

where $\mu_r$ is the relative permeability of the material.

As with the absolute permittivity $\epsilon$, the absolute permeability $\mu$ is treated as a real-valued, positive scalar constant, independent of space, time and frequency. This corresponds to a homogeneous, time-invariant and non-dispersive magnetic medium. Magnetic losses and frequency-dependent effects are therefore neglected.

This gives the following constitutive relation:

$$
\mathbf{B} = \mu\mathbf{H}
$$
