"""

name: intensity.py

Compute and visualize diffraction of waves upon encountering a straight edge.
 
Problem 5.11 from Newman's Computational Physics.

author: Darcy Lewis
date created: 15/3/2021


"""
# Reminder: you can create other helper functions as long as the function
# behaviors below remain the same

from math import pi,cos,sin
import gaussxw as g
import numpy as np
import matplotlib.pyplot as plt




# C(u) integrand   
def f(t):

    """
    function of C(u) that we're taking an integral of

    Parameters
    ----------
    t : FLOAT
        input.

    Returns
    -------
    y : FLOAT
    
    """
    
    y = cos(0.5*pi*t**2)
    
    return y

#S(u) integrand
def h(t):

    """
    function of S(u) that we're taking an integral of

    Parameters
    ----------
    t : FLOAT
        input.

    Returns
    -------
    y2 : FLOAT
    
    """
    
    y2 = sin(0.5*pi*t**2)
    
    return y2


# function name: C   
def C(u):

    """
    C(u) term of integral.

    Parameters
    ----------
    u : FLOAT
        input.

    Returns
    -------
    cc : FLOAT
        C value at u.

    """
    
    N = 50
    a = 0
    b = u
    
    x,w = g.gaussxw(N)
    
    #from jupyter activity
    xp = 0.5*(b-a)*x+0.5*(b+a)
    wp = 0.5*(b-a)*w
    I = 0
    for a in range(len(xp)):
        I += wp[a]*f(xp[a])
        
    I_c = I
    
    return I_c
    print(I_c)
    


# function name: S
def S(u):

    """
    S(u) term of integral.    

    Parameters
    ----------
    u : FLOAT
        input.

    Returns
    -------
    ss : FLOAT
        S value at u.

    """
    
    N = 50
    a = 0
    b = u
    
    x,w = g.gaussxw(N)
    
    #from jupyter activity
    xp = 0.5*(b-a)*x+0.5*(b+a)
    wp = 0.5*(b-a)*w
    I = 0
    for a in range(len(xp)):
        I += wp[a]*h(xp[a])
        
    I_s = I
    
    return I_s
    print(I_s)

# function name: I_ratio
def I_ratio(a):
    """
    Compute I ratio at given x values

    Parameters
    ----------
    x : array of FLOAT
        x values to compute diffraction.

    Returns
    -------
    I_r : array of FLOAT
        I/I0 at given x values.

    """
    I_r = []            #empty list for ratio values
    z = 3
    
    for x in a:
        u = x*(2/z)**(1/2)              #given u function
        I = ((2*C(u)+1)**2+(2*S(u)+1)**2)/8     #given I function
        I_r = np.append(I_r,I)              #append ratios to list
        

    return(I_r)
    

# function name: plot_ratio
def plot_ratio(x,ratio):

    """
    plot I/I0 as a function of x

    Parameters
    ----------
    x : array of FLOAT
        x values.
    ratio : array of FLOAT
        I/Io.

    Returns
    -------
    None.

    """
    plt.xlabel("distance")
    plt.ylabel("Ratio of I/Io")
    plt.plot(x,ratio)

    
def main():    

    x = np.linspace(-5,5,100)
    I_ratio(x)
    plot_ratio(x,I_ratio(x))
    
if __name__ == "__main__":
    main()