import numpy as np
import matplotlib.pyplot as plt 

# set up z-coordinates and step size for difference equation
z_max = 10 # distance from origin
Nsteps = 1000 # number of steps from origin to z_max
dz = z_max / Nsteps

z = np.linspace(0, z_max, Nsteps+1)

""" Finite Square Well """
# create potential (array)
W = np.zeros(z.size)
WellHeight = 15
z_edge = 1

i = int(z_edge/dz)
W[i:] = WellHeight # potential for the finite square well


psi_1 = np.zeros(z.size)
psi_1[0] = 1
psi_1[1] = 1

psi_2 = np.zeros(z.size)
psi_2[0] = 0
psi_2[1] = 0.02

psi_3 = np.zeros(z.size)
psi_3[0] = 1
psi_3[1] = 1

energy_1 = 1.571617
energy_2 = 6.0720113
energy_3 = 12.7674

""" Simple Harmonic Oscillator """
def SHO(z):
    y = (z**2)
    return y

W2 = SHO(z)

psi_11 = np.zeros(z.size)
psi_11[0] = 0.3
psi_11[1] = 0.3

psi_22 = np.zeros(z.size)
psi_22[0] = 0
psi_22[1] = 0.008

psi_33 = np.zeros(z.size)
psi_33[0] = 0.3
psi_33[1] = 0.3

energy_11 = 1.00565
energy_22 = 2.99996
energy_33 = 5.014

""" Radial Equation of the Hydrogen Atom """
def hydrogen(z):
    y = (-2/z)
    return y

zh = np.linspace(0.000000000001, z_max, Nsteps+1) # to avoid dividing by zero
W3 = hydrogen(zh)

psi_111 = np.zeros(zh.size)
psi_111[0] = 0
psi_111[1] = 0.1

psi_222 = np.zeros(zh.size)
psi_222[0] = 0
psi_222[1] = 0.1

psi_333 = np.zeros(zh.size)
psi_333[0] = 0
psi_333[1] = 0.1

energy_111 = -0.9997
energy_222 = -0.24563
energy_333 = -0.055384

""" Difference Equation """

t = np.ones(z.size)
for i in range(2, z.size):
    psi_1[i] = (2 - dz**2*(energy_1 - W[i-1]))*psi_1[i-1] - psi_1[i-2]
    psi_2[i] = (2 - dz**2*(energy_2 - W[i-1]))*psi_2[i-1] - psi_2[i-2]
    psi_3[i] = (2 - dz**2*(energy_3 - W[i-1]))*psi_3[i-1] - psi_3[i-2]

    psi_11[i] = (2 - dz**2*(energy_11 - W2[i-1]))*psi_11[i-1] - psi_11[i-2]
    psi_22[i] = (2 - dz**2*(energy_22 - W2[i-1]))*psi_22[i-1] - psi_22[i-2]
    psi_33[i] = (2 - dz**2*(energy_33 - W2[i-1]))*psi_33[i-1] - psi_33[i-2]

    psi_111[i] = (2 - dz**2*(energy_111 - W3[i-1]))*psi_111[i-1] - psi_111[i-2]
    psi_222[i] = (2 - dz**2*(energy_222 - W3[i-1]))*psi_222[i-1] - psi_222[i-2]
    psi_333[i] = (2 - dz**2*(energy_333 - W3[i-1]))*psi_333[i-1] - psi_333[i-2]

""" Plot PSI solution & and Potentials """
fig = plt.figure(figsize=(6,8))
fig.set_facecolor('#E8E6E6')
ax1 = fig.add_subplot(311)

ax1.set_title('The Finite Square Well', fontweight='bold')
ax1.set_xlabel('x', fontweight='bold')
ax1.set_ylabel('V(x)', fontweight='bold')
ax1.plot(z, W, color='#6E6E6E', label='V(x)')
ax1.plot(z, psi_1+energy_1, color='#FF0000', label='psi_1(x)')
ax1.plot(z, psi_2+energy_2, color='#AA34FF', label='psi_2(x)')
ax1.plot(z, psi_3+energy_3, color='#047BF1', label='psi_3(x)')
ax1.plot(z, energy_1*t, color='#01C504', label='E_1')
ax1.plot(z, energy_2*t, color='#f1F004', label='E_2')
ax1.plot(z, energy_3*t, color='#F17804', label='E_3')
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, facecolor='white', edgecolor='black', frameon=True)
ax1.set_xlim([0, 5])
ax1.set_ylim([-0.5, 15])

ax2 = fig.add_subplot(312)

ax2.set_title('The Simple Harmonic Oscillator', fontweight='bold')
ax2.set_xlabel('x', fontweight='bold')
ax2.set_ylabel('V(x)', fontweight='bold')
ax2.plot(z, W2, color='#6E6E6E', label='V(x)')
ax2.plot(z, psi_11+energy_11, color='#FF0000', label='psi_1(x)')
ax2.plot(z, psi_22+energy_22, color='#AA34FF', label='psi_2(x)')
ax2.plot(z, psi_33+energy_33, color='#047BF1', label='psi_3(x)')
ax2.plot(z, energy_11*t, color='#01C504', label='E_1')
ax2.plot(z, energy_22*t, color='#f1F004', label='E_2')
ax2.plot(z, energy_33*t, color='#F17804', label='E_3')
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, facecolor='white', edgecolor='black', frameon=True)
ax2.set_xlim([0, 3])
ax2.set_ylim([0, 6])

ax3 = fig.add_subplot(313)

ax3.set_title('The Hydrogen Atom', fontweight='bold')
ax3.set_xlabel('x', fontweight='bold')
ax3.set_ylabel('V(x)', fontweight='bold')
ax3.plot(zh, W3, color='#6E6E6E', label='V(x)')
ax3.plot(zh, psi_111+energy_111, color='#FF0000', label='psi_1(x)')
ax3.plot(zh, psi_222+energy_222, color='#AA34FF', label='psi_2(x)')
ax3.plot(zh, psi_333+energy_333, color='#047BF1', label='psi_3(x)')
ax3.plot(zh, energy_111*t, color='#01C504', label='E_1')
ax3.plot(zh, energy_222*t, color='#f1F004', label='E_2')
ax3.plot(zh, energy_333*t, color='#F17804', label='E_3')
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, facecolor='white', edgecolor='black', frameon=True)
ax3.set_xlim([0, 5])
ax3.set_ylim([-14, 5])

plt.tight_layout()
plt.show()