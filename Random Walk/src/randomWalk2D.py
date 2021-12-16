import numpy.random as rnd
import matplotlib.pyplot as plt
import numpy as np

def walk2D(steps):
    pathX = np.zeros(steps, dtype=int)
    pathY = np.zeros(steps, dtype=int)
    
    pathX[0] = 0
    pathY[0] = 0

    for i in range(steps-1):
        value = rnd.randint(4)
        if (value == 0):
            pathX[i+1] = pathX[i] + 1  #+x
            pathY[i+1] = pathY[i]
        elif (value == 1):
            pathY[i+1] = pathY[i] + 1  #+y
            pathX[i+1] = pathX[i]
        elif (value == 2):
            pathX[i+1] = pathX[i] - 1  #-x
            pathY[i+1] = pathY[i]
        else: 
            pathY[i+1] = pathY[i] - 1  #-y
            pathX[i+1] = pathX[i]
            
    displacement = (pathX**2+pathY**2)**(1/2)
    
    return displacement[-1]
    
numSteps = 1000
num_walkers = 1000

XY_final = []

for i in range(num_walkers):
    final = walk2D(numSteps)
    XY_final.append(final)
    
displacement = np.mean(XY_final)
stddev = np.std(XY_final)
distance = np.mean(XY_final)
    
print("Average displacement: %f metres"  %(displacement))
print("Standard deviation:   %f metres"  %(stddev))
print("Average distance:     %f metres"  %(distance))

plotStats = 1
if plotStats:
    plt.hist(XY_final, bins=50)

plt.title('2-D Random Walk')
plt.xlabel('Displacement')
plt.ylabel('Number of Walkers')
    
plt.savefig('distribution2D.png')
plt.show()