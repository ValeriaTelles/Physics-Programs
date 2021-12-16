# Simple Physics Programs 

### Electric Dipole
In the book, Introduction to Electrodynamics by David J. Griffith, he introduces approximate potentials at large distances in multipole expansions. An electric dipole consists of two equal and opposite charges ($\pm q$) separated by a distance $d$. If $r>>d$, we may approximate the potential. This means that the more you increase $r$, the better the approximation for $V_{dip}$. The electric dipole contribution to the potential eventually simplifies to:

$V_{dip}(r) = \frac{1}{4\pi \epsilon_{0}} \frac{\mathbf{p}\cdot \mathbf{\hat{r}}}{r^2}$

where $p$ is the dipole moment. To get the electric field due to the dipole, we would take the negative gradient of $V_{dip}$:

$E_{dip}(r, \theta) = \frac{p}{4\pi\epsilon_0 r^3} (2 \cos\theta \mathbf{\hat{r}} + \sin\theta \mathbf{\hat{\theta}}$

### Gradient, Divergence and Curl of 2D Scalar and Vector Fields

The vector field has the mathematical form:

$\vec{F} = ln(1+y^2)\hat{\mathbf{i}} + ln(1+x^2)\hat{\mathbf{j}}$

The divergence is given by:

$\nabla \cdot F = (\hat{\mathbf{x}} \frac{\partial}{\partial x} + \hat{\mathbf{y}} \frac{\partial}{\partial y} + \hat{\mathbf{z}} \frac{\partial}{\partial z})\cdot(F_x \hat{\mathbf{x}} +F_y \hat{\mathbf{y}}+F_z \hat{\mathbf{z}})$

The curl is given by:

$\nabla \times F = \begin{vmatrix}
\mathbf{\hat{x}} & \mathbf{\hat{y}} & \mathbf{\hat{z}} \\ 
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_x & F_y & F_z
\end{vmatrix}$

### Charge Integration

In this program we are looking at a uniformly charged line segment and arc segment. Two different methods of integration are used to calculate the the electric field components in the $x$ and $y$ direction: Simpson's rule and the trapezoidal method of integration.

### Magnetic Field

### Van der Waals Equation of State

### Einstein Solids

### Random Walk

### Quadratic Drag

### Potentials

### Fourier Series

### Wavefunction
