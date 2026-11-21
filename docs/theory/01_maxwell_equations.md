## 1.1 Gauss's Law (Electricity)

$$
\nabla \cdot \mathbf{D} = \rho_f
$$

Gauss's law states that the divergence of the electric displacement $\mathbf{D}$ equals the free volume charge density $\rho_f$ of the medium. Free charges are distinct from bound charges, which are associated with the polarization of the material. This formulation is particularly useful because the effects of material polarization are accounted for in the electric displacement field. Consequently, Gauss's law for $\mathbf{D}$ involves only the free charge density. The constitutive relation defining the electric displacement field is presented in Section 3.

## 1.2 Gauss's Law (Magnetism)

$$
\nabla \cdot \mathbf{B} = 0
$$
Here, Gauss's law states that the divergence of the magnetic flux density $\mathbf{B}$ is zero. Since the divergence represents the local net outward magnetic flux per unit volume at a point, this relation implies that the same amount of magnetic flux enters a closed surface as leaves it. Hence, the magnetic field lines either form closed loops or extend to infinity; they have no starting or ending points. 

## 1.3 Faraday's Law

$$
\nabla \times \mathbf{E}
=
-\frac{\partial \mathbf{B}}{\partial t}
$$
Faraday's law states that the curl of the electric field equals the negative time derivative of the magnetic flux density. The curl of $\mathbf{E}$ represents the local circulation of the electric field per unit area. Therefore, this equation relates the local circulation of the electric field to the temporal variation of the magnetic flux density.

This relation is a consequence of Faraday's discovery that a wire loop is subject to an electromotive force when the magnetic flux through the loop varies. The negative sign in the equation is explained by Lenz's law, which states that the induced current in a closed conducting loop produces a magnetic field that opposes the change in magnetic flux that caused the induction. 


## 1.4 The Ampère-Maxwell Law

$$
\nabla \times \mathbf{H}
=
\mathbf{J}_f + \frac{\partial \mathbf{D}}{\partial t}
$$

The Ampère-Maxwell law states that the curl of the magnetic field $\mathbf{H}$ equals the free current density plus the time derivative of the electric displacement. Here, the curl of $\mathbf{H}$ measures the local circulation of the magnetic field strength per unit area. The second term on the right corresponds to the displacement current density, defined as follows:
 
$$
\mathbf{J_d} = \frac{\partial \mathbf{D}}{\partial t}
$$ 

The displacement current density introduced by Maxwell in Ampère's law plays a crucial role in the propagation of electromagnetic waves, as a changing electric displacement contributes to the generation of a magnetic field. When compared with Faraday's law, Ampère-Maxwell's law reveals a symmetry in the coupling between the spatial curl of each field and the temporal variation of the other field. This coupling between the electric and magnetic fields is essential for understanding the propagation of electromagnetic waves.

## 1.5 Summary of Variables

The following table summarizes the variables introduced so far.


| Symbol | Physical Quantity | SI Unit | Description |
|:---:|---|:---:|---|
| $\mathbf{E}$ | Electric field | $V/m$| Vector field representing the electric force per unit of positive test charge at any given point |
| $\mathbf{D}$ | Electric displacement field | $C/m^2$ | Vector field accounting for the effects of material polarization |
| $\mathbf{B}$ | Magnetic flux density | $T$ | Vector field describing the magnetic contribution to the Lorentz force exerted on a moving charge |
| $\mathbf{H}$ | Magnetic field strength | $A/m$ | Vector field describing the macroscopic magnetic field strength, accounting for the magnetization of the material |
| $\rho_f$ | Free volume charge density | $C/m^3$ | Scalar quantity representing the amount of free charge per unit volume |
| $\mathbf{J}_f$ | Free current density | $A/m^2$ | Vector field representing the free current per unit cross-sectional area |
| $\mathbf{J}_d$ | Displacement current density | $A/m^2$ | Vector field representing the time derivative of the electric displacement |
