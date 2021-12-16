import numpy as np
import matplotlib.pyplot as plt
import time as time

# Define functions for the script
def tic():
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()
    
def toc():
    if 'startTime_for_tictoc' in globals():
        print( "Elapsed time is" + str(time.time() - startTime_for_tictoc) + "seconds." )
    else:
        print( "Toc: start time not set" )
        
tic()

# Input parameters for model - assume all quantities in SI units
D = 0.5           # drag coeff for sphere
rho = 1.29        # air density in kg/m^3
r = 0.11          # radius of sphere in m
A = np.pi*r**2     # frontal area of sphere
m = 7.26          # mass of sphere
g = 9.8           # acceleration due to gravity m/s^2
c = (1/2)*rho*A*D 
Vt = np.sqrt(m*g/c) # terminal velocity in m/s

tsteps=100      # number of iterations for 100 second interval
dt=100/tsteps   # time step in seconds

# Create arrays for kinematic quantities for each time step
vN = np.zeros(tsteps)
yN = np.zeros(tsteps)
T = np.zeros(tsteps)

# Calculate the approximated values for the kinematic equations
for t in range(tsteps-1):
    accel = g-D*rho*A*vN[t]**2/(m*2)
    vN[t+1] = vN[t] + accel*dt
    yN[t+1] = yN[t] + vN[t]*dt
    T[t+1] = T[t] + dt

# Create arrays for the analytical solutions of y(t) and v(t)
vN_exact = np.zeros(tsteps)
yN_exact = np.zeros(tsteps)
T_exact = np.arange(tsteps)

# Calculate the exact values for the kinematic equations
for j in range(tsteps):
    vN_exact[j] = Vt*np.tanh(g*T[j]/Vt)
    yN_exact[j] = (Vt**2/g)*np.log(np.cosh(g*T[j]/Vt))

# Plotting the data 
fig, axs = plt.subplots(2, 2)
fig.set_size_inches(8, 6)
axs[0, 0].plot(T, yN, 'g.')
axs[0, 0].set_title('Using Eulers Method to\n compute Position vs Time', fontweight='bold', fontsize=12)
axs[0, 0].set_xlabel('Time (s)')
axs[0, 0].set_ylabel('Position (m)')
axs[0, 0].grid(which='major', axis='both', color='0.70')
axs[0, 0].grid(which='minor', axis='both', color='0.90')
axs[0, 0].minorticks_on()

axs[0, 1].plot(T_exact, yN_exact, 'r.')
axs[0, 1].set_title('Using the Analytical Method to\n compute Position vs Time', fontweight='bold')
axs[0, 1].set_xlabel('Time (s)')
axs[0, 1].set_ylabel('Position (m)')
axs[0, 1].grid(which='major', axis='both', color='0.70')
axs[0, 1].grid(which='minor', axis='both', color='0.90')
axs[0, 1].minorticks_on()

axs[1, 0].plot(T, vN, 'b.')
axs[1, 0].set_title('Using Eulers Method to\n compute Velocity vs Time', fontweight='bold')
axs[1, 0].set_xlabel('Time (s)')
axs[1, 0].set_ylabel('Velocity (m/s)')
axs[1, 0].grid(which='major', axis='both', color='0.70')
axs[1, 0].grid(which='minor', axis='both', color='0.90')
axs[1, 0].minorticks_on()

axs[1, 1].plot(T_exact, vN_exact, 'm.')
axs[1, 1].set_title('Using the Analytical Method to\n compute Velocity vs Time', fontweight='bold')
axs[1, 1].set_xlabel('Time (s)')
axs[1, 1].set_ylabel('Velocity (m/s)')
axs[1, 1].grid(which='major', axis='both', color='0.70')
axs[1, 1].grid(which='minor', axis='both', color='0.90')
axs[1, 1].minorticks_on()

plt.subplots_adjust(hspace=0.7, wspace=0.7)

plt.savefig('quadDrag.png', dpi=300)
