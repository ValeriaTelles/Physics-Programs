import numpy as np

# Create a function that will produce arrays of (x,y) positions for an arc 
# segment, from position ri to rf, divided into N equally spaced intervals
def arcSegment(Ti, Tf, N):
    r = 5
    theta = np.linspace(Ti, Tf, N)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    dS = (r*(theta[1]-theta[0])) #ds = r*dtheta
    return x, y, dS
	
# Return the electric field, E, due to a charge "q" located at position (xq,yq).
# Evaluate V at the given position (x,y).
def eField(q, xq, yq, x, y):
    k = 9.0e9
    denom = ( (x - xq)**2 + (y - yq)**2 )**1.5
    dEx = k * q * (x - xq) / denom
    dEy = k * q * (y - yq) / denom
    return dEx, dEy 

# Create a function that will integrate, using Simpson's Rule
# Inputs should be A function f, and a segment length dS (associated with dQ)
def simps (f, dS):
    simp = 0
    for i in range (1, Nsegments-1):
        if (i%2 == 0):
            simp += 2*f[i]
        else:
            simp += 4*f[i]
            
    simp += f[0]
    simp += f[-1]
    simp = simp*(dS/3)
    
    return simp

# Create a function that will integrate, using Simpson's Rule
# Inputs should be A function f, and a segment length dS (associated with dQ)
def trapz (f, dL):     
    return dL/2*np.sum(f[1:] + f[:-1])

# Define characteristics of the uniformly charged arc segment
Ti = 0
Tf = np.pi

Nsegments = 101
Qtot = 3e-6
S = 5*np.pi #length of arc s=r*theta 

# linear charge density & charge per segment dS
lamb = Qtot/S

# position at which electric field is calculated
Ro = np.array([0,0])
Ro2 = np.array([10,0])

X, Y, dS = arcSegment(Ti, Tf, Nsegments)

# compute dEx, dEy at position Ro due to each dQ contribution along the 
# charged line segment.
# NOTE:  the *Ro - assigns Ro values to appropriate variables, in order of how
#        they are defined in function
dEx, dEy = eField(lamb,X,Y,*Ro)
dEx2, dEy2 = eField(lamb,X,Y,*Ro2)

# Apply simps function to integrate all contributions dEx, dEy to compute the 
# total electric field at position Ro
print("UNIFORMLY CHARGED ARC SEGMENT:\n")

Ex = trapz(dEx, dS)
Ey = trapz(dEy, dS)

print("Using the Trapezoid Rule at the point (0, 0): \nEx = %.6E \nEy = %.6f \n" % (Ex, Ey))

Ex2 = trapz(dEx2, dS)
Ey2 = trapz(dEy2, dS)

print("Using the Trapezoid Rule at the point (10, 0): \nEx = %.6f \nEy = %.6f \n" % (Ex2, Ey2))

Ex = simps(dEx, dS)
Ey = simps(dEy, dS)

print("Using Simpson's Rule at the point (0, 0): \nEx = %.6E \nEy = %.6f \n" % (Ex, Ey))

Ex2 = simps(dEx2, dS)
Ey2 = simps(dEy2, dS)

print("Using Simpson's Rule at the point (10, 0): \nEx = %.6f \nEy = %.6f \n" % (Ex2, Ey2))
