"""

name: square_well.py

Computes the energy levels of a finite square well.

Problem 6.14 from Newman's Computational Physics.

author: Sam Wilson
date created: 29/3/2021


"""
import numpy as np
from math import tan,pi
import matplotlib.pyplot as plt

# part a

#blue line
def blue(x):
    
    m = 9.1094E-31
    w = 1E-9
    h = 6.62607E-34 
    hbar = h/(2*pi)
    eVJ = 1.6022E-19     #eV -> Joules constant
    return tan(((eVJ*x*m*w**2)/(2*hbar**2))**0.5)
    
#orange    
def orange(x):
    
    V = 20
    return ((V-x)/x)**0.5 

#green 
def green(x):
    
    V = 20
    return -(x/(V-x))**0.5

# function name: calc_ys
def calc_ys(Es):

    """
    Calculate the y functions for given energy values.

    Parameters
    ----------
    Es : array of FLOAT
        Energy values to calculate y functions at.

    Returns
    -------
    y1 : array of FLOAT
        y1 at Es values.
    y2 : array of FLOAT
        y2 at Es values.
    y3 : array of FLOAT
        y3 at Es values.

    """

    
    y1 = []
    y2 = []
    y3 = []

    for E in range(len(Es)):
        if Es[E] == 0:    #because can't divide by 0
            y2 = np.append(y2,None)
            y3 = np.append(y3,green(Es[E]))
        elif Es[E] == 20:   #because can't divide by 0
            y3 = np.append(y3,None)
            y2 = np.append(y2,orange(Es[E]))
        else:
            y2 = np.append(y2,orange(Es[E]))
            y3 = np.append(y3,green(Es[E]))
        y1 = np.append(y1,blue(Es[E]))    



    return np.array(y1), np.array(y2), np.array(y3)
    
#function name: plot_functions
def plot_functions(Es,y1,y2,y3):

    """
    Plots the lefthand and righthand sides of the transcendental equation

    Parameters
    ----------
    Es : array of FLOAT
        Energy values to calculate y functions at.
    y1 : array of FLOAT
        y1 at Es values.
    y2 : array of FLOAT
        y2 at Es values.
    y3 : array of FLOAT
        y3 at Es values.

    Returns
    -------
    None.

    """
    
    #plots 3 different ys over the same x
    plt.plot(Es,y1)
    plt.plot(Es,y2)
    plt.plot(Es,y3)
    plt.ylim(-10,10)

    
    plt.show()
        


# funton name: binaryorange
def binaryorange(a,b): 

    """
    binary search

    Returns
    -------
    a : FLOAT
        left bracket
    b : FLOAT
        right bracket

    """
    
    
    
    #from jupyter, uses a bunch of if/elif to find matching signs
    error = 10 
    while error > 1E-4:
        xp = (a+b)/2
        if blue(xp)-orange(xp)<0 and blue(a)-orange(a)>0:
            b = xp
        elif blue(xp)-orange(xp)>0 and blue(a)-orange(a)<0:
            b = xp
        elif blue(xp)-orange(xp)<0 and blue(b)-orange(b)>0:
            a = xp
        elif blue(xp)-orange(xp)>0 and blue(b)-orange(b)<0:
            a = xp
        error = abs(a-b)
        
    print(xp)

    return xp
    
# funton name: binaryorange
def binarygreen(a,b): 

    """
    binary search

    Returns
    -------
    a : FLOAT
        left bracket
    b : FLOAT
        right bracket

    """
    
    
    #from jupyter, uses a bunch of if/elif to find matching signs
    error = 10
    while error > 1E-4:
        xp = (a+b)/2
        if blue(xp)-green(xp)<0 and blue(a)-green(a)>0:
            b = xp
        elif blue(xp)-green(xp)>0 and blue(a)-green(a)<0:
            b = xp
        elif blue(xp)-green(xp)<0 and blue(b)-green(b)>0:
            a = xp
        elif blue(xp)-green(xp)>0 and blue(b)-green(b)<0:
            a = xp
        error = abs(a-b)
        
    print(xp)

    return xp
    
# funton name: calc_Es
def calc_Es(): 

    """
    Compute the first 6 energy levels of the finite square well

    Returns
    -------
    E0 : FLOAT
        Ground state energy level.
    E1 : FLOAT
        1st excited state.
    E2 : FLOAT
        2nd excited state.
    E3 : FLOAT
        3rd excited state.
    E4 : FLOAT
        4th excited state.
    E5 : FLOAT
        5th excited state.

    """
    
    #found the bounds for each thing by zooming in on graph to find each intersection point
    a = binaryorange(0.15,0.35)
    b = binarygreen(0.5,2.5)
    c = binaryorange(2,4)
    d = binarygreen(4,6)
    e = binaryorange(6,8)
    f = binarygreen(10,12)
                
    return a,b,c,d,e,f
    
    
def main(): 
    
    Es = np.linspace(0,20,1000)      #creates Es array
 
    y1,y2,y3 = calc_ys(Es)
    plot_functions(Es,y1,y2,y3)
    
    calc_Es()


if __name__ == "__main__":
    main()

