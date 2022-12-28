import numpy as np 
import matplotlib.pyplot as plt
import time as time
from matplotlib.patches import Circle

def biot(Rvec, wire, I):
    mu_4pi = 10
    dB = np.zeros((len(wire), 3))

    R = Rvec - wire
    
    Rsqr = np.sum( R**2, axis = 1 )
    
    dL = (np.roll(wire, -1, axis = 0) - np.roll(wire, +1, axis = 0))/2
    
    cr = np.cross(dL, R, axis = 1 )
    dB = mu_4pi * I * cr/Rsqr[:,None]**(3/2)
    
    dB = np.concatenate((dB, [dB[0,:]]), axis = 0)
    
    Btot = np.array([simpson(dB[:,0], 1), simpson(dB[:,1], 1), simpson(dB[:,2], 1)])
    
    return Btot 

def simpson(f, dr):
    total = dr/3*(np.sum(f[1:] + f[:-1]) + 2*np.sum(f[1::2]))
    
    return total

def trapz(f, dL):
    return dL/2*np.sum(f[1:] + f[:-1])
    


# setting up the square loop of wire 
I = 0.01    # current, in amperes
L = 0.20    # length of helix in m
N = 500     # number of segments per side of square
segL = L/N  # segment length in m 
turns = 20  # number of loops in helix
radius = 0.03

# some useful segments to build a position array of the segments in helical wire
helix_x =  np.arange(-L/2, L/2, segL)
helix_y, helix_z =  np.zeros(helix_x.size), np.zeros(helix_x.size)

theta_steps = N/turns
dtheta =  2*np.pi/theta_steps

for i in range (N):
    helix_y[i] = -np.sin(i*dtheta)*radius
    helix_z[i] = np.cos(i*dtheta)*radius

helix = np.column_stack((helix_x, helix_y, helix_z))



# test the biot function for a single point (the origin)
pointCalc = True
if pointCalc:
    # choose a point in space at which to calculate B
    point = np.array([0.1,0.0,0.0])
    Ti = time.time()
    
    # call the biot function to calculate B
    B = biot(point, helix,I)
    print(point)
    print(B)

    print("duration: %5f" % (time.time()-Ti) )
    
    
    
# Create a 2D grid of x, y points using numpy's meshgrid function
gridstep=50
nx, ny, nz = gridstep,gridstep,gridstep
x = np.linspace(-0.2, 0.2, nx)
y = np.linspace(-0.2, 0.2, ny)
z = np.linspace(-0.2, 0.2, nz)

fig = plt.figure(figsize = (18,6))
ax1 = fig.add_subplot(2, 3, 1)
ax2 = fig.add_subplot(2, 3, 2)
ax3 = fig.add_subplot(2, 3, 3)

# Set up meshgrid as needed for the particular 2D streamplot
X, Z = np.meshgrid(x,z)
# Set up 3D array, Bgrid, for x,y,z-components of B at points in space
Bgrid = np.zeros([nx,nz,3])

Ti = time.time()

# Use for loops to populate Bgrid array with relevant B-field values
# XZ Plane
for i in range(nx):
    for k in range(nz):
        Bgrid[k,i, :] = biot(np.array([x[i],0.,z[k]]),helix,I)

# XY Plane
for i in range(nx):
    for k in range(nz):
        Bgrid[k,i, :] = biot(np.array([x[i],y[k],0.0]),helix,I)

print("duration: %5f" % (time.time()-Ti) )


# Use streamplot to show B-field
# XY plane 
ax1.streamplot(X,Z,Bgrid[:,:,0],Bgrid[:,:,1], color = '0.50')

ax1.set_aspect('equal')
ax1.set_xlim((-0.2,0.2))
ax1.set_ylim((-0.2,0.2))

# add circles to plot to show where wire cross sections
ax1.add_artist(Circle((L/2,0),0.005,color='#aa0000'))
ax1.add_artist(Circle((-L/2,0),0.005,color='#0000aa'))

ax1.set_ylabel('y-direction', fontsize = '10')
ax1.set_xlabel('x-direction', fontsize = '10')
ax1.set_title('Magnetic Field due to a Helix (XY Plane)', fontweight = 'bold', fontsize = '13')

# XZ plane
ax2.streamplot(X,Z,Bgrid[:,:,0],Bgrid[:,:,2], color = '0.50')

ax2.set_aspect('equal')
ax2.set_xlim((-0.2,0.2))
ax2.set_ylim((-0.2,0.2))

# add circles to plot to show where wire cross sections
ax2.add_artist(Circle((L/2,0),0.005,color='#aa0000'))
ax2.add_artist(Circle((-L/2,0),0.005,color='#0000aa'))

ax2.set_ylabel('y-direction', fontsize = '10')
ax2.set_xlabel('x-direction', fontsize = '10')
ax2.set_title('Magnetic Field due to a Helix (XZ Plane)', fontweight = 'bold', fontsize = '13')

# YZ plane
ax3.streamplot(X,Z,Bgrid[:,:,1],Bgrid[:,:,2], color = '0.50')

ax3.set_aspect('equal')
ax3.set_xlim((-0.2,0.2))
ax3.set_ylim((-0.2,0.2))

# add circles to plot to show where wire cross sections
ax3.add_artist(Circle((L/2,0),0.005,color='#aa0000'))
ax3.add_artist(Circle((-L/2,0),0.005,color='#0000aa'))

ax3.set_ylabel('y-direction', fontsize = '10')
ax3.set_xlabel('x-direction', fontsize = '10')
ax3.set_title('Magnetic Field due to a Helix (YZ Plane)', fontweight = 'bold', fontsize = '13')

fig.tight_layout()
