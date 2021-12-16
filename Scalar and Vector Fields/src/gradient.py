import numpy as np
import matplotlib.pyplot as plt

#deriv computes 1D derivative, dF/dr, using central difference method
def deriv(F,r):
	# get the length of array F (assume same length for r)
    L = F.size
	
	# create empty array to store results
    result=  np.empty(L)
	
	# use central diff method for all interior points
    for i in range(L-2):
        result[i+1] = (F[i+2] - F[i]) / (r[i+2] - r[i])
        
    result[0] = (F[1] - F[0]) / (r[1] - r[0])
    result[L-1] = (F[L-1] - F[L-2]) / (r[L-1] - r[L-2])

    return result

# read in the file "sField.csv", which contains a 2D array representing a scalar field [e.g. V(x,y)]
sField = np.loadtxt('sField.csv',delimiter=',')

# create a 2D grid of x, y points using numpy's meshgrid function
nx, ny = 100,100
x = np.linspace(-5,5,nx)
y = np.linspace(-5,5,ny)
X, Y = np.meshgrid(x,y)

# compute the gradient of sField

# take derivatives in the x-direction
gradX = np.empty(X.shape)

for j in range(ny):
    gradX[j,:] = deriv(sField[j,:],x)

# take derivatives in the y-direction
gradY = np.empty(Y.shape)

for i in range(nx): 
    gradY[:,i] = deriv(sField[:,i], y)

gX = np.sign(gradX)
gY = np.sign(gradY)

fig, ax = plt.subplots()
ax.set_title('Gradient of a Scalar Field', fontweight = 'bold')
ax.set(xlabel = "X Directional Derivative", ylabel = "Y Directional Derivative")

ax.quiver(X,Y,gradX,gradY,pivot='mid')
s = 5 

fig.set_size_inches(8, 6)
ax.set_aspect('equal')

# save
plt.savefig('gradientPlot.png', dpi=300)

    




