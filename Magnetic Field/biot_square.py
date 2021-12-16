# Name: Valeria Telles
# Date: 2 March 2020
# Program: biot_square.py

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
L = 0.10    # side length of square, in m
N = 500     # number of segments per side of square
segL = L/N  # segment length in m 

# some useful segments to build a position array of the segments in square loop
A = L/2*np.ones(N)
B = np.arange(-L/2, L/2, segL)

# concatenate
wx = np.concatenate((B, A, -B, -A))
wy = np.concatenate((A, -B, -A, B))
wz = np.zeros(wx.size)

# column_stack
wire = np.column_stack((wx, wy, wz))



# test the biot function for a single point (the origin)
pointCalc = True
if pointCalc:
    # choose a point in space at which to calculate B
    point = np.array([0.0,0,0.0])
    Ti = time.time()
    
    # call the biot function to calculate B
    B = biot(point, wire,I)
    print(point)
    print(B)

    print("duration: %5f" % (time.time()-Ti) )
    
    
    
# Create a 2D grid of x, y points using numpy's meshgrid function
gridstep=50
nx, ny, nz = gridstep,gridstep,gridstep
x = np.linspace(-0.2, 0.2, nx)
y = np.linspace(-0.2, 0.2, ny)
z = np.linspace(-0.2, 0.2, nz)

# Set up meshgrid as needed for the particular 2D streamplot
X, Z = np.meshgrid(x,z)
# Set up 3D array, Bgrid, for x,y,z-components of B at points in space
Bgrid = np.zeros([nx,nz,3])

Ti = time.time()

# Use for loops to populate Bgrid array with relevant B-field values
for i in range(nx):
    for k in range(nz):
        Bgrid[k,i, :] = biot(np.array([x[i],0.,z[k]]),wire,I)
        #Bgrid[k,i, :] = biot(np.array([x[i],0.1,z[k]]),wire,I)

# you can change which plane you are viewing it from as well

print("duration: %5f" % (time.time()-Ti) )



# plotting and formatting
fig, ax = plt.subplots(figsize=(10,10))

# Use streamplot to show B-field
ax.streamplot(X,Z,Bgrid[:,:,0],Bgrid[:,:,2], color = '0.50')

ax.set_aspect('equal')
ax.set_xlim((-0.2,0.2))
ax.set_ylim((-0.2,0.2))

# add circles to plot to show where wire cross sections
ax.add_artist(Circle((L/2,0),0.005,color='#aa0000'))
ax.add_artist(Circle((-L/2,0),0.005,color='#0000aa'))

ax.set_ylabel('y-direction', fontsize = '14')
ax.set_xlabel('x-direction', fontsize = '14')
ax.set_title('Magnetic Field due to a Square Loop', fontweight = 'bold', fontsize = '18')