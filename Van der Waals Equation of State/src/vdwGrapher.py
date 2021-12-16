import numpy as np
import matplotlib.pyplot as plt

#vdwEquation takes an array of volumes and calculates the corresponding 
#pressure for a particular temperature. The output is an array of pressure 
#values corresponding to the volume valumes.

def vdwEquation(v, t): 
    #v is the volume
    #t is the temperature
    
    p = (8*t)/(3*v-1) - (3)/(v**2)

    return p

volume = np.arange(0.1, 10, 0.01)
temp095 = np.zeros(volume.size) #temperature is set at 0.95
temp100 = np.zeros(volume.size) #temperature is set at 1.00
temp105 = np.zeros(volume.size) #temperature is set at 1.05

temp095 = vdwEquation(volume, 0.95)
temp100 = vdwEquation(volume, 1.00)
temp105 = vdwEquation(volume, 1.05)

plt.plot(volume, temp095, 'r', label = 't = 0.95')
plt.plot(volume, temp100, 'b', label = 't = 1.00')
plt.plot(volume, temp105, 'g', label = 't = 1.05')

plt.title("Reduced Van der Waals equation of state\n at varying reduced temperatures", fontweight = 'bold')
plt.xlabel('Reduced Volume, v', fontweight = 'bold')
plt.ylabel('Reduced Pressure, p', fontweight = 'bold')
plt.grid(b = True, which = 'major', color = 'gainsboro', linestyle = '-')
plt.xlim(0.4, 2.0)
plt.ylim(0.0, 8.0)
plt.legend()

plt.savefig('vdwGraph.png', figsize = (8, 8), dpi = 1000)
plt.show()
