## 6.1 Discretization of Maxwell's Equations

To apply the Yee algorithm, we need finite-difference approximations for the spatial and temporal derivatives in Equations (1) and (2).

Starting with the spatial derivative of the magnetic field $H_y$, the general central-difference approximation can be applied as follows:

$$
\begin{aligned}
\left.\frac{\partial H_y^{n+\frac12}}{\partial z}
\right|_{z=z_i,\;t=t_{n+\frac12}}
&\approx
\frac{H_y^{n+\frac12}(z_i+h)-H_y^{n+\frac12}(z_i-h)}{2h}
\\
\\
&=
\frac{H_y^{n+\frac12}(z_i+\frac{\Delta z}{2})-H_y^{n+\frac12}(z_i-\frac{\Delta z}{2})}{2(\frac{\Delta z}{2})}
\\
\\
&=
\frac{H_y^{n+\frac12}(z_i+\frac{\Delta z}{2})-H_y^{n+\frac12}(z_i-\frac{\Delta z}{2})}{\Delta z}
\\
\\
&=
\frac{H_y^{n+\frac12}(i+\frac12)-H_y^{n+\frac12}(i-\frac12)}{\Delta z} 
\end{aligned}
$$

To complete the discretization of Ampère-Maxwell's equation, we also need to approximate the time derivative of $E_x$, as follows:

$$
\begin{aligned}
\left.\frac{\partial E_x}{\partial t} \right|_{z=z_i,\;t=t_{n+\frac12}}
&\approx \frac{E_x^{n+1} (i) -  E_x^n (i)}{\Delta t} 
\end{aligned}
$$

The discretized form of Ampère-Maxwell's equation is therefore:

$$
\begin{aligned}
\frac{H_y^{n+\frac12}(i+\frac12)-H_y^{n+\frac12}(i-\frac12)}{\Delta z} &= - \epsilon  \frac{E_x^{n+1} (i) -  E_x^n (i)}{\Delta t}  
\end{aligned}
$$

We can now solve for $E_x^{n+1} (i)$ in order to obtain the first FDTD update equation:

$$
\begin{aligned}
E_x^{n+1} (i) =  E_x^n (i) + \frac{\Delta t}{ \epsilon \Delta z} \Bigg[H_y^{n+\frac12}(i-\frac12) - H_y^{n+\frac12}(i+\frac12) \Bigg] 
\end{aligned}
\qquad\qquad\qquad \text{(1)}
$$

For Faraday's law, we need to solve for $H_y^{n+1/2}(i+1/2)$ in order to obtain the second update equation. The temporal derivative of the magnetic field is approximated using a centered finite difference:

$$
\begin{aligned}
\left.\frac{\partial H_y}{\partial t}
\right|_{z=z_{i+\frac12},\;t=t_{n}}
&\approx
\frac{H_y^{n+\frac12}(i+\frac12)-H_y^{n-\frac12}(i+\frac12)}{\Delta t} \\
\\
\end{aligned}
$$

The spatial derivative of the electric field is approximated as follows:

$$
\begin{aligned}
\left.\frac{\partial E_x}{\partial z} \right|_{z=z_{i+\frac12},\;t=t_{n}}
&\approx 
\frac{E_x^{n} (i+1) -  E_x^n (i)}{\Delta z} 
\end{aligned}
$$

We can now express the second update equation from Faraday's law approximation:

$$
\begin{aligned}
\frac{E_x^{n} (i+1)-E_x^n (i)}{\Delta z} 
&= -\mu \frac{H_y^{n+\frac12}(i+\frac12)-H_y^{n-\frac12}(i+\frac12)}{\Delta t}
\end{aligned}
$$

By isolating $H_y^{n+\frac12}(i+\frac12)$, we obtain:

$$
\begin{aligned}
H_y^{n +\frac12} (i + \frac12) = H_y^{n-\frac12}(i+\frac12) + \frac{\Delta t}{\mu \Delta z} \bigg[  E_x^n (i) - E_x^{n} (i+1) \bigg] 
\end{aligned}
\qquad\qquad\qquad \text{(2)}
$$

Although Ampère-Maxwell's equation was discretized first in this section, this is not the order in which the update equations are applied in the Yee algorithm. In fact, the magnetic field is first updated using Faraday's law, followed by the electric field using Ampère-Maxwell's law. The next section describes this sequence in more detail.
