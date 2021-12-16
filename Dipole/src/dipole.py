import numpy as np
import matplotlib.pyplot as plt

# compute the electric potential, V, at a point in space (x,y) due to a point 
# charge, q0, located at position r0 = (x0, y0).
def potential(q0, r0, x, y):
    k = 8.99e+9
    r = np.sqrt((x-r0[0])**2+(y-r0[1])**2)
    V = k*q0/r
    
    return V

# Compute the electric field, E, at a point in space (x,y) due to a point 
# charge, q0, located at position r0 = (x0, y0)
def Efield(q0, r0, x, y):
    k = 8.99e+9
    r = np.sqrt((x-r0[0])**2+(y-r0[1])**2)
    Ex = (k*q0*(x-r0[0]))/r**3
    Ey = (k*q0*(y-r0[1]))/r**3
    
    return Ex, Ey

r0 = np.zeros(2)

# 2D grid of x, y points
nx, ny = 100, 100
x = np.linspace(-0.05, 0.05, nx)
y = np.linspace(-0.05, 0.05, ny)
X, Y = np.meshgrid(x, y)

# electric field vector, E = (Ex, Ey), as components
Ex = np.zeros((ny, nx))
Ey = np.zeros((ny, nx))

# define the charges (charge & position) that make up the electric dipole
q1 = 2.0; x1 = 0.02; y1 = 0.0
q2 = -2.0; x2 = -0.02; y2 = 0.0

V = potential(q1, (x1, y1), x=X, y=Y)
V += potential(q2, (x2, y2), x=X, y=Y)

Ex, Ey = Efield(q1, (x1, y1), x=X, y=Y)
Ex2, Ey2 = Efield(q2, (x2, y2), x=X, y=Y)

Ex = Ex + Ex2
Ey = Ey + Ey2

# creating and formatting a subplot to display a contour plot of the electric 
# potential and a streamplot of the electric field due to an electric dipole
Vmin = np.amin(np.absolute(V))
Vmax = np.amax(np.absolute(V))

VpLines = 10**np.linspace(10, 12, 11)
VpLines = sorted(list(-VpLines)+list(VpLines))

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.tight_layout(w_pad = 6, pad = 3)

ax1.contour(X, Y, V, levels = VpLines, colors = 'k', linewidths = 1)
ax2.streamplot(X, Y, Ex, Ey, color = 'g', linewidth= 1, density = 2, arrowstyle = '-|>', arrowsize = 0.7)

ax1.set_title("Equipotential Lines due to\n an Electric Dipole", fontweight = 'bold')
ax2.set_title("Electric Field due to\n an Electric Dipole", fontweight = 'bold')

ax1.set(xlabel = "x distance", ylabel = "y distance")
ax2.set(xlabel = "x distance", ylabel = "y distance")

ax2.set_xlim([-0.05, 0.05])
ax2.set_ylim([-0.05, 0.05])

fig.set_size_inches(8, 6)

plt.savefig('dipole.png', dpi = 900)
