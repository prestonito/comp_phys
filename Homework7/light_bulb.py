"""

name: light_bulb.py

Computes the energy levels of a finite square well.

Problem 6.18 from Newman's Computational Physics.

author: Sam Wilson
date created: 29/3/2021


"""

from math import pi,e
import gaussxw as g
import matplotlib.pyplot as plt
import numpy as np

# part a

# function name: f(x)
def f(x):

    """
    Integrand

    Parameters
    ----------
    x : FLOAT
        x-value

    Returns
    -------
    FLOAT
        value of integrand

    """
    
    return (x**3)/(-1+e**x)


# function name: eta
def eta(T):

    """
    Compute efficiency, eta, for a given temperature

    Parameters
    ----------
    T : FLOAT
        Temperature.

    Returns
    -------
    FLOAT
        efficiency for given temperature.

    """
    #constants
    h = 6.62607E-34
    c = 2.998E8
    lamda1 = 390E-9
    lamda2 = 750E-9
    kb = 1.38065E-23
    N = 100  #from book
    
    
    a = h*c/(lamda2*kb*T)
    b = h*c/(lamda1*kb*T)
    
    constant = 15/(pi**4)
    
    #from other gauss
    x,w = g.gaussxwab(N,a,b)
    I = 0
    for a in range(len(x)):
        I += w[a]*f(x[a])
        
    return constant*I


# function name: make_plot
def make_plot(x1,x2):

    """
    Integrand

    Parameters
    ----------
    x1 : FLOAT
        x-value
    x2 : FLOAT
        x-value


    Returns
    -------
    FLOAT
        value of integrand

    """
    
    x_points = np.linspace(x1,x2,1000)   #1000 points inbetween x1 and x2
    y_points = []
    for i in range(len(x_points)):
        x = x_points[i]
        y_points = np.append(y_points,(eta(x)))     #appends values to the y point list
        
    
    plt.plot(x_points,y_points)
    

# part b
# function name: max_efficiency
def max_efficiency(x1,x4):

    """
    Compute temperature with maximum efficiency of a lightbulb.

    Parameters
    ----------
    x1 : FLOAT
        Left bracket.
    x4 : FLOAT
        Right bracket.

    Returns
    -------
    FLOAT
        Temperature with maximum efficiency.

    """
    
    z = 1.618    #golden ratio

    error = 10
    while error > 1:
        midpoint = x1+((x4-x1)/2)      #point inbetween x4 and x1
        x2 = midpoint-((x4-x1)/(2*z))   #calculates where x2 and x3 should be
        x3 = midpoint+((x4-x1)/(2*z))
        if eta(x2)>eta(x3):
            x4 = x3      #decreases bounds
        else:
            x1 = x2      #decreases bounds
        error = abs(x3-x2)/2


    print(midpoint)
    return midpoint


    
def main():

    make_plot(300,10000)
    max_efficiency(0,10000)

    print(eta(100))

if __name__ == "__main__":
    main()