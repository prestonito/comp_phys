"""

name: curves.py

This program plots various curves

Problem 3.2 from Newman's Computational Physics.

author: Jimmy Woo
date created: 2/6/2018
date edited: 2/22/2021

"""


# imports
from math import pi,sin,cos,e
import numpy as np
import matplotlib.pyplot as plt

# user-defined functions

# part a: function name: deltoid
def deltoid(theta):
    """
    

    Parameters
    ----------
    theta : array of float
        array of angles in radians to plot deltoid cruve

    Returns
    -------
    x : array of float
        array of x values for plotting curve
    y : array of float
        array of y values for plotting curve

    """
    
    
    deltoidx = np.array([])            #empty arrays
    deltoidy = np.array([])

        
    for a in (theta):
        xvalue = (2*cos(a)+cos(2*a))      #adding values to the arrays
        yvalue = (2*sin(a)-sin(2*a))
        deltoidx = np.append(deltoidx,xvalue)
        deltoidy = np.append(deltoidy,yvalue)
        
    return deltoidx, deltoidy
    
   
            

# part b: function name: polar_plot
def polar_plot(theta):
    """
    

    Parameters
    ----------
    theta : array of float
        array of angles in radians to plot deltoid cruve

    Returns
    -------
    x : array of float
        array of x values for plotting curve
    y : array of float
        array of x values for plotting curve

    """
    
    polarx = np.array([])
    polary = np.array([])                                #empty arrays
    
    
    for a in (theta):
        r = a**2                                #calculating r for every a
        xvalue = r*cos(a)
        yvalue = r*sin(a)
        polarx = np.append(polarx,xvalue)            #appending values to the array
        polary = np.append(polary,yvalue)
        
    return polarx,polary
        
        
  
# part c: function name: feys
def feys(theta):
    """
    

    Parameters
    ----------
    theta : array of float
        array of angles in radians to plot deltoid cruve

    Returns
    -------
    x : array of float
        array of x values for plotting curve
    y : array of float
        array of x values for plotting curve

    """
    
    
    feysx = np.array([])                             #creating two empty array
    feysy = np.array([])
    
    
    
    for a in (theta):
        r = (e**(cos(a)))-(2*cos(4*a))+(sin(a/12))**5   #calculating r for every a
        xvalue = r*cos(a)
        yvalue = r*sin(a)
        feysx = np.append(feysx,xvalue)                 #appending values to the lists
        feysy = np.append(feysy,yvalue)
        
    return feysx, feysy 
    
# function name: make_plot
def make_plot(x,y):
    """
    This function takes in arrays of (x,y) points and plots them 
    with labeled axes

    Parameters
    ----------
    x : array of float
        array of x values for plotting curve
    y : array of float
        array of x values for plotting curve

    Returns
    -------
    None.

    """
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    


def main():
    # use the functions defined above
    
    # a)

    theta = np.linspace(0,2*pi,100)            #creating an array to input
    deltoidx,deltoidy=deltoid(theta)
    make_plot(deltoidx,deltoidy)    


    # b)
    theta = np.linspace(0,10*pi,1000)          #creating an array to input
    polarx,polary=polar_plot(theta)
    make_plot(polarx,polary)
    
    
    # c)
    theta = np.linspace(0,24*pi,10000)         #creating an array to input
    feysx,feysy=feys(theta)
    make_plot(feysx,feysy)
    



if __name__ == "__main__":
    main()
