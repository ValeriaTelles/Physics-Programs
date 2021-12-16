import numpy as np
import matplotlib.pyplot as plt


# deriv computes 1D derivative, dF/dr, using central difference method
def deriv(F,r):
	# get the length of array F (assume same length for r)
    L = F.size
	
	# create empty array to store results
    result=  np.empty(L)
	
	# use central diff method for all interior points (we will build in tutorial)
    for i in range(L-2):
        result[i+1] = (F[i+2] - F[i]) / (r[i+2] - r[i])
        
    result[0] = (F[1] - F[0]) / (r[1] - r[0])
    result[L-1] = (F[L-1] - F[L-2]) / (r[L-1] - r[L-2])

    return result

# read in the files "vFieldX.csv" and "vFieldY.csv"
vFieldX= np.loadtxt( 'vFieldX.csv', delimiter = ',' )
vFieldY = np.loadtxt( 'vFieldY.csv', delimiter = ',' )

# Create a 2D grid of x, y points using numpy's meshgrid function (see Exercise 1)
nx, ny = 100,100
x = np.linspace(-5,5,nx)
y = np.linspace(-5,5,ny)
X, Y = np.meshgrid(x,y)

# Divergence 
divX = np.empty(X.shape)

for j in range(ny):
    divX[j,:] = deriv(vFieldX[j,:],x)

divY = np.empty(Y.shape)

for i in range(nx): 
    divY[:,i] = deriv(vFieldY[:,i], y)

totalDiv = divX + divY

# Curl
curlX = np.empty(X.shape)

for j in range(ny):
    curlX[j,:] = deriv(vFieldY[j,:], x)

curlY = np.empty(Y.shape)

for i in range(nx): 
    curlY[:,i] = deriv(vFieldX[:,i], y)

totalCurl = curlX - curlY

# Plotting the Divergence and Curl using subplots
lines = 10**np.linspace(10, 12, 11)
lines = sorted(list(-lines)+list(lines))
fig, (ax1, ax2) = plt.subplots( nrows = 1, ncols = 2, sharex = False, sharey = False )

ax1.contourf(X, Y, totalDiv) #levels = Lines, colors = 'k', linewidths = 1)
CS = ax2.contour(x, y, totalCurl, ) #levels = Lines, colors = 'k', linewidths = 1)

ax1.set_title('Divergence of a Vector Field', fontweight = 'bold' )
ax2.set_title('Curl of a Vector Field', fontweight = 'bold' )

ax1.set(xlabel = "X", ylabel = "Y")
ax2.set(xlabel = "X", ylabel = "Y")

ax2.clabel(CS, inline = 1, fontsize = 8)

fig.set_size_inches(9, 5)

plt.savefig('divCurlPlot.png', dpi=300)