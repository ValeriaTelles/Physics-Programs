import numpy as np

# Create a function that will produce arrays of (x,y) positions for a line 
# segment, from position ri to rf, divided into N equally spaced intervals
def lineSegment(ri, rf, N):
    x = np.linspace(ri[0], rf[0], N)
    y = np.linspace(ri[1], rf[1], N)
    dL = np.sqrt( (x[1] - x[0])**2 + (y[1] - y[0])**2 )
    return x, y, dL
	
# Return the electric field, E, due to a charge "q" located at position (xq,yq).
# Evaluate V at the given position (x,y).
def eField(q, xq, yq, x, y):
    k = 9.0e9
    denom = ( (x - xq)**2 + (y - yq)**2 )**1.5
    dEx = k * q * (x - xq) / denom
    dEy = k * q * (y - yq) / denom
    return dEx, dEy 

# Create a function that will integrate, using Trapezoid Rule
# Inputs should be A function f, and a segment length dL (associated with dQ)
def trapz (f, dL):     
    return dL/2*np.sum(f[1:] + f[:-1])

# Create a function that will integrate, using Simpson's Rule
def simps (f, dL):
    simp = 0
    for i in range (1, Nsegments-1):
        if (i%2 == 0):
            simp += 2*f[i]
        else:
            simp += 4*f[i]
            
    simp += f[0]
    simp += f[-1]
    simp = simp*(dL/3)
    
    return simp

# Define characteristics of the uniformly charged line segment
Ri = np.array([-5,0])
Rf = np.array([5,0])
Nsegments = 101
Qtot = 3e-6
L = np.sqrt( np.sum( (Rf - Ri)**2 ) ) #length of the stick 

# linear charge density & charge per segment dL
lamb = Qtot/L 
#dQ = 

# position at which electric field is calculated
Ro = np.array([0,5])
Ro2 = np.array([10,0])

X, Y, dL = lineSegment(Ri, Rf, Nsegments)

# compute dEx, dEy at position Ro due to each dQ contribution along the 
# charged line segment.
# NOTE:  the *Ro - assigns Ro values to appropriate variables, in order of how
#        they are defined in function
dEx, dEy = eField(lamb,X,Y,*Ro)
dEx2, dEy2 = eField(lamb,X,Y,*Ro2)

# Apply trapz function to integrate all contributions dEx, dEy to compute the 
# total electric field at position Ro
print("UNIFORMLY CHARGED LINE SEGMENT:\n")

Ex = trapz(dEx,dL)
Ey = trapz(dEy,dL)

print("Using the Trapezoid Rule at the point (0, 5): \nEx = %.4E \nEy = %.2f \n" % (Ex, Ey))

Ex2 = trapz(dEx2, dL)
Ey2 = trapz(dEy2, dL)

print("Using the Trapezoid Rule at the point (10, 0): \nEx = %.2f \nEy = %.4f \n" % (Ex2, Ey2))

# Apply simps function to integrate all contributions dEx, dEy to compute the
# total electric field at position Ro
Ex = simps(dEx,dL)
Ey = simps(dEy,dL)

print("Using Simpson's Rule at the point (0, 5): \nEx = %.4E \nEy = %.2f \n" % (Ex, Ey))

Ex2 = simps(dEx2, dL)
Ey2 = simps(dEy2, dL)

print("Using the Simpson's Rule at the point (10, 0): \nEx = %.2f \nEy = %.4f \n" % (Ex2, Ey2))