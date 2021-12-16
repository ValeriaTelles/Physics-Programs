import numpy.random as rnd
import matplotlib.pyplot as plt
import numpy as np
import time as tm

# the function walk1D consists of N steps in the positive/negative direction based on a randomly generated value
def walk1D(steps):
    path = np.zeros(steps, dtype=int)

    for i in range(steps-1):
        if rnd.randint(2):
            path[i+1] = path[i] + 1
        else:
            path[i+1] = path[i] - 1
            
    return path[-1]

def walk1Dgooder(steps):
    direction = np.array([-1,1])
    
    path =  np.cumsum(direction[rnd.randint(2, size=steps)], axis=0)
    return path[-1]

def walk1Dstats(steps, numWalkers):
    xf = np.zeros(numWalkers)
    
    for i in range(numWalkers):
        xf[i] = walk1D(steps)
        
    displacement = np.mean(xf)
    stddev = np.std(xf)
    distance = np.mean(np.abs(xf))
    
    print("Average displacement: %f metres"  %(displacement))
    print("Standard deviation:   %f metres"  %(stddev))
    print("Average distance:     %f metres"  %(distance))
    
    return xf
    
# look at an individual random walk
numSteps = 100000

walk = walk1D(numSteps)
walk = walk1Dgooder(numSteps)

plotTheWalk = 0

# plot the walk:  plot position vs. step number (represented by index, below)
if plotTheWalk:
    index = np.arange(numSteps)
    plt.plot(index, walk)
    plt.plot(index, walk1Dgooder(numSteps), 'g')
    plt.plot(index, walk1Dgooder(numSteps), 'r')
    plt.plot(index, walk1Dgooder(numSteps), 'b')


# look at the statistics for many random walks
# vall the random walk function for each walker, and save into the final_pos array
numWalkers = 1000
numSteps = 1000

# the stats that we are interested in relates to final positions of the walks assuming that all walks start at the same initial position (x=0)
x_final = walk1Dstats(numSteps,numWalkers)

# for walk1Dstats, with function returning x_final:
plotStats = 1
if plotStats:
    r=100
    plt.hist(x_final, range=(-r,r), bins=r)
    
    plt.title('2-D Random Walk')
    plt.xlabel('Displacement')
    plt.ylabel('Number of Walkers')

# look at the relationship between final_x number of steps
plotRelationship = 0
if plotRelationship:
    num = np.array([10,50,100,500,1000,5000,10**4])
    Dist = np.zeros(num.size)
    
    for i in range(num.size):
        Dist[i]=walk1Dstats(num[i],numWalkers)
    
    plt.plot(num,Dist,'ok')
    
plt.savefig('distribution1D.png')