import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

def psi(x, t):
    """ Expressing the wave function, Ψ(x, t), in terms of the basis(stationary) states for an infinite well """
    # constants
    E_2 = 4 # approximation
    E_5 = 25 # approximation
    a = 10

    pt_2 = np.exp(np.sqrt(-1+0j)*E_2*t) # time-dependent portion for E_2
    pt_5 = np.exp(np.sqrt(-1+0j)*E_5*t) # time-dependent portion for E_5

    psi_2 = np.sqrt(2/a)*(np.sin(2*np.pi*x/a))*pt_2 
    psi_5 = np.sqrt(2/a)*-4*(np.sin(5*np.pi*x/a))*pt_5

    return psi_2 + psi_5 # wavefunction

def probability(x, t):
    """ Probablity of finding the particle between x and (x + dx), at time t """
    return np.abs(np.conj(psi(x, t))*psi(x, t))

def main():
    x = np.arange(0, 2*np.pi, 0.01) # position
    t = np.arange(0, 2*np.pi, 0.01) # time 

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))
    fig.subplots_adjust(left=0.4, right=0.5, hspace=0.5)
    fig.set_facecolor('#E8E6E6')

    realPlot, = ax1.plot(x, psi(x, t).real, 'm', label='Real')
    imagPlot, = ax1.plot(x, psi(x, t).imag, 'c', label='Imaginary')

    ax1.set_title('Time Evolution of a Wave Function', fontweight='bold', fontsize=11)
    ax1.set_ylabel('Ψ(x, t)')
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, facecolor='white', edgecolor='black', frameon=True)
    ax1.set_xlim(0, 6)
   
    probabilityPlot, = ax2.plot(x, probability(x, t).real, 'y', label='Probability')

    ax2.set_title('Probability', fontweight='bold', fontsize=11)
    ax2.set_ylabel('$|Ψ(x,t)|^2$')
    ax2.set_xlabel('x')
    ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, facecolor='white', edgecolor='black', frameon=True)
    ax2.set_xlim(0, 6)

    def update(t):
        realPlot.set_ydata(psi(x, t).real)
        imagPlot.set_ydata(psi(x, t).imag)
        probabilityPlot.set_ydata(probability(x, t).real)

        return realPlot, imagPlot, probabilityPlot

    # instantiate the animator
    anim = FuncAnimation(fig, update, interval=1, blit=True)

    plt.tight_layout()
    plt.show()

    # save as mp4. This requires mplayer or ffmpeg to be installed
    # anim.save('waveFunction.mp4', fps=15, extra_args=['-vcodec', 'libx264'])

if __name__ == "__main__":
    main()
