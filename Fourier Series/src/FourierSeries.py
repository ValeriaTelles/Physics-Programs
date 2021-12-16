# Author: Valeria Telles
# Date: 19 October 2020
# Course: PHYS3230 - Quantum Mechanics I 

import numpy as np
import matplotlib.pyplot as plt

def trapz(X, Y):
    """ 
    Approximate the integral of f(x) from a to be by the trapezoid rule.
    
    Parameters
    ----------
    X : numbers - X values contained within the file 'wavedata.csv'
    Y : numbers - Y values contained within the file 'wavedata.csv'

    Returns
    -------
    float - approximation of the integral of f(x) using the trapezoid rule.
    """

    return 0.5*((X[1:]-X[:-1])*(Y[1:]+Y[:-1])).sum()


def coefficients(X, Y, n):
    """
    Calculate the coefficinents for the sine and cosine components of the trigonometric 
    Fourier Series

    Parameters
    ----------
    X : numbers - X values contained within the file 'wavedata.csv'
    Y : numbers - Y values contained within the file 'wavedata.csv'
    n : numbers - 0, 1, 2...

    Returns
    -------
    list - coefficients of the trigonometric Fourier Series up to n = 5.
    """
    A = 0
    B = 0

    An = []
    Bn = []

    while (n <= 5):
        X1 = X
        Y1 = Y*np.cos(2*np.pi*X*n/10)
        Y2 = Y*np.sin(2*np.pi*X*n/10)
       
        A += trapz(X1, Y1)
        B += trapz(X1, Y2)
        
        A = A*2/10
        B = B*2/10

        An.append(A)
        Bn.append(B)
        n = n + 1

    return An, Bn

def fourier(x, n, An, Bn):
    """
    Reconstructing the function f(x) using a restricted number of Fourier modes.

    Parameters
    ----------
    x : numbers - X values contained within the file 'wavedata.csv'
    n : numbers - 0, 1, 2...
    An : list of values for the coefficient 'An' up to n = 5
    Bn : list of values for the coefficient 'Bn' up to n = 5

    Returns
    -------
    ndarray - reconstructed fourier series of order 'n'.
    """
    a0 = An[0]
    series = np.zeros(np.size(x))
    for i in range(1, n+1):
        series += ( An[i] * np.cos(2*np.pi*x*i/10) + Bn[i] * np.sin(2*np.pi*x*i/10) )
    return (a0/2) + series

def main():
    X, Y = np.loadtxt("wavedata.csv", delimiter=',', usecols=(0,1), unpack=True)
    k = np.arange(0, 6, 1)
    n = 0
    
    An, Bn = coefficients(X, Y, 0)

    print(fourier(X, 2, An, Bn))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figheight(9)
    fig.set_figwidth(12)
    fig.tight_layout(pad=5.0)

    ax1.set_facecolor('#EAEAEA')
    ax1.bar(k, An, width=0.4, align='edge', label='An', color='#E40303')
    ax1.bar(k, Bn, width=-0.4, align='edge', label='Bn', color='#0402BD')
    ax1.legend(fontsize=12, shadow=True)
    ax1.set_xlabel('value of n', fontsize=12, fontweight='bold')
    ax1.set_ylabel('relative contribution', fontsize=12, fontweight='bold')
    ax1.set_title('Relative Contributions of An and Bn', fontsize=14, fontweight='bold')
    ax1.grid(color='#F6F6F6', linestyle='-')
    ax1.set_axisbelow(True)

    ax2.set_facecolor('#EAEAEA')
    ax2.plot(X, Y, label='original', color='#E40303')
    ax2.plot(X, fourier(X, 2, An, Bn), label='n = 2', color='#0402BD')
    ax2.plot(X, fourier(X, 3, An, Bn), label='n = 3', color='#38B748')
    ax2.plot(X, fourier(X, 5, An, Bn), label='n = 5', color='#F2AD12')
    ax2.legend(fontsize=12, shadow=True)
    ax2.set_xlabel('x', fontsize=12, fontweight='bold')
    ax2.set_ylabel('f(x)', fontsize=12, fontweight='bold')
    ax2.set_title('Fourier Reconstruction (n = modes)', fontsize=14, fontweight='bold')
    ax2.grid(color='#F6F6F6', linestyle='-')
    ax2.set_axisbelow(True)

    fig.savefig('FourierSeries.png', dpi = 900)

if __name__ == "__main__":
    main()
