import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from matplotlib import animation as am

# energyFlow will exchange energy between elements within a single Einstein
# solid.  numQ is the number of energy units ('q') to be exchanged, done one
# at a time.
def energyFlow(eSolid,numQ):
    N = eSolid.size -1
    
    for i in range(numQ):
        lose = rnd.randint(0,N)
        gain = rnd.randint(0,N)
        
        while eSolid[lose] == 0:
            lose = rnd.randint(0,N)
        
        eSolid[gain] += 1
        eSolid[lose] -= 1
    return eSolid

# This function is used with the animation to evolve the energy flow within the
# Einstein solid.  The variable input '*args' allows for a variable number of
# inputs.  The first input, arg[0], will be the frame number.
def evolve(*args):
    energyFlow(solid, 10000)
    imgPlot.set_data(np.reshape(solid, (L,L)))
    return [imgPlot] # return line object in a list

# set up Einstein solid #1, with 400 elements, each starting with 10 energy units
L = 40 
N = L*L 
qavg = 15 

solid = qavg*np.ones(N)

solid = energyFlow(solid, 10000)

img = np.reshape(solid, (L,L))

# creating a 2D image of the Einstein solid & animate
animate = False

if animate:
    fig = plt.figure()


# reshape the 1D array into an LxL rectangle; use "plt.imshow" to display it
# in the same way that you would with a pixelated image.
    img = np.reshape(solid, (L,L))

# set up a colorbar to display energy in each element.  vmin,vmax,cmap features
# set lower/upper range and a colormap. The colorbar displays range of values 
# beside the plot.  
    imgPlot = plt.imshow(img, interpolation='none', vmin=0, vmax=50, cmap='coolwarm')
    plt.colorbar(imgPlot)


# animate the evolution of the Einstein solid.  Note that the animation calls
# the function 'evolve' to update the contents of the figure (namely 'imgPlot')
    anim = am.FuncAnimation(fig, evolve, \
						interval=10, frames=500, repeat=False, blit=True)

else:
    solid = energyFlow(solid, 500*solid.size)
    
    energy, counts = np.unique(solid, return_counts=True)

    fig = plt.figure(figsize=(12,8))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    
    fig.suptitle('Energy Distribution in an Einstein Solid', fontweight = 'bold', fontsize = 14)
    
    ax1.set(xlabel = "Energy, q", ylabel = "Number of Oscillators, N")
    ax2.set(xlabel = "Energy, q", ylabel = "Number of Oscillators, N")
    
    ax1.grid(b = True, which = 'major', color = 'gainsboro', linestyle = '-')
    ax2.grid(b = True, which = 'major', color = 'gainsboro', linestyle = '-')
    
    ax1.plot(energy, counts, 'b.')
    ax2.semilogy(energy, counts, 'b.')
    
    plt.savefig('energy.png', dpi = 900)
    
# consider two Einstein solids, each with a different number of oscillators and total energy
    
L40 = 40
L20 = 20
qavg15 = 15
qavg30 = 30

N1 = L40*L40
N2 = L40*L20

solid1 = qavg15*(np.ones(N1))
solid2 = qavg30*(np.ones(N2))
    
solid1 = energyFlow(solid1, 10000)
solid2 = energyFlow(solid2, 10000)

# plotting the energy distribution of the two solids on the same axes

animate = False

if animate:
    fig = plt.figure()

    img = np.reshape(solid, (L,L)) 

    imgPlot = plt.imshow(img, interpolation='none', vmin=0, vmax=50, cmap='coolwarm')
    plt.colorbar(imgPlot)

    anim = am.FuncAnimation(fig, evolve, \
						interval=10, frames=500, repeat=False, blit=True)

else:
    solid1 = energyFlow(solid1, 500*solid1.size)
    energy1, counts1 = np.unique(solid1, return_counts=True)
    
    solid2 = energyFlow(solid2, 500*solid2.size)
    energy2, counts2 = np.unique(solid2, return_counts=True)
    
    
    # combine the two solids into a single array using numpy.append and evolve the system
    
    totalSolid = np.append(solid1, solid2)
            
    # plotting the different solids using matplotlib subplots 
    
    totalSolid = energyFlow(totalSolid, 500*totalSolid.size)
        
    energyTotal, countsTotal = np.unique(totalSolid, return_counts=True)
        
    fig = plt.figure(figsize = (12,8))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
            
    fig.suptitle('Energy Distribution in Einstein Solids 1, 2 and Combined', fontweight = 'bold', fontsize = 14)
    
    ax1.set(xlabel = "Energy, q", ylabel = "Number of Oscillators, N")
    ax2.set(xlabel = "Energy, q", ylabel = "Number of Oscillators, N")
    
    ax1.grid(b = True, which = 'major', color = 'gainsboro', linestyle = '-')
    ax2.grid(b = True, which = 'major', color = 'gainsboro', linestyle = '-')
    
    ax1.plot(energy1, counts1, 'b.')
    ax1.plot(energy2, counts2, 'g.')
    ax1.plot(energyTotal, countsTotal, 'r.')
        
    ax2.semilogy(energy1, counts1, 'b.')
    ax2.semilogy(energy2, counts2, 'g.')
    ax2.semilogy(energyTotal, countsTotal, 'r.')
    
    plt.savefig('twoSolids.png', dpi = 900)