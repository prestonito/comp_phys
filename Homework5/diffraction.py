"""

name: diffraction.py

Calculate and visualize circular diffraction.

Problem 5.4 from Newman's Computational Physics.

author: Darcy Lewis
date created: 15/3/2021


"""
# Reminder: you can create other helper functions as long as the function
# behaviors below remain the same

import numpy as np
import matplotlib.pyplot as plt
from math import pi,sin,cos
from pylab import imshow, colorbar

# part (a) 
# function name: J
def J(m,x):
    
    """
    Calculate mth Bessel function for the values in x.

    Parameters
    ----------
    m : INT
        mth Bessel function.
    x : FLOAT
        x-value to calculate Bessel at.

    Returns
    -------
    bessel : FLOAT
        mth Bessel function at x.

    """
    
    N = 1000                               #givens
    b = pi
    a = 0
    h = (b-a)/N
    

    f_a = cos(m*a-(x*sin(a)))               #shortening expression for later
    f_b = cos(m*b-(x*sin(b)))
    
    integral_o = 0                          #have to do this for the for loop
    integral_e = 0
    
    for k in range(1,N):                          #summations
        arg = a+(k*h)                               #shortening the argument
        if k%2==1:                                  #for odd k
            odd_total = cos(m*(arg)-(x*sin(arg)))
            integral_o = odd_total+integral_o
        elif k%2==0:                                #for even k
            even_total = cos(m*(arg)-x*sin(arg))    
            integral_e = even_total+integral_e

                
    bessel = (f_a+f_b+(4*integral_o)+(2*integral_e))*h/(3*pi) 
    
    
    return bessel


# part (a)
# function name: plot_Bessel
def plot_Bessel():

    """
    Overlay the Bessel functions over the range of x for m=0,1,2,3.

    Returns
    -------
    None.

    """
    
    
    x_points = np.linspace(0,20,100)
    
    y_0 = []
    y_1 = []
    y_2 = []
    y_3 = []
    for x in np.linspace(0,20,100):
        y_0 = np.append(y_0,J(0,x))     #calling the J(m,x) function to calculate y points
        y_1 = np.append(y_1,J(1,x))
        y_2 = np.append(y_2,J(2,x))
        y_3 = np.append(y_3,J(3,x))
            
    plt.xlabel("x")
    plt.ylabel("Bessel Values")
    
    plt.plot(x_points,y_0)
    plt.plot(x_points,y_1)
    plt.plot(x_points,y_2)
    plt.plot(x_points,y_3)
    plt.show()
  
# part b    
# function name: calc_diffraction
def calc_diffraction(N):

    """
    Calculate the diffraction over an NxN grid which spans from -1e6 to 1e6 in x and y.

    Parameters
    ----------
    N : TYPE
        DESCRIPTION.

    Returns
    -------
    circular : TYPE
        DESCRIPTION.

    """
    lam = 500E-9
    k = 2*pi/lam
    rad = 1E-6
    
    circular = np.zeros((N,N),float)
    
    for a in range(0,np.size(circular,0)):        #goes through width of array
        for b in range(0,np.size(circular,1)):    #goes through height of array
            x = (b-(N//2))*2*rad/N                  #converts array "coordinates" to x and y
            y = (a-N//2)*2*rad/N
            r = (x**2+y**2)**(1/2)
            if r==0:
                circular[a,b] = 1/2                 #from hint
            else:
                circular[a,b] = ((J(1,k*r))/(k*r))**2       #formula for I(r)
    
    return circular


# part b  
# function name: plot_diffraction
def plot_diffraction(N):

    """
    Density plot of circular diffraction pattern.

    Parameters
    ----------
    N : INT
        discretization in the x and y dimensions.

    Returns
    -------
    None.

    """
    density = calc_diffraction(N)
    dif = imshow(density,vmax=0.01)
    colorbar(dif) 
    

    
def main():
    # part a
    J(10,10)
    plot_Bessel()
    # part b
    plot_diffraction(100)

    
    
    
if __name__ == "__main__":
    main()
