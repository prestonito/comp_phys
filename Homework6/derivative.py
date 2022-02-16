"""

name: derivative.py

Compute and visualize numerical and analytic derivatives.

Problem 5.15 from Newman's Computational Physics.

author: Shuri
date created: 22/3/2021


"""
# Reminder: you can create other helper functions as long as the function
# behaviors below remain the same

from math import tanh,cosh
import numpy as np
import matplotlib.pyplot as plt

# function name: f(x)
def f(x):
    """
    Compute f(x) value

    Parameters
    ----------
    x : INT
        x values to compute the derivative at.

    Returns
    -------
    y : INT
        values at associated x values

    """
    
    y = 1+(tanh(2*x))/2         #given function
    
    return y


# function name: analytic
def analytic(x):
    """
    Compute analytic derivative of f(x): df/dx

    Parameters
    ----------
    x : array of FLOAT
        x values to compute the derivative at.

    Returns
    -------
    df : array of FLOAT
        derivative values at associated x values

    """
    
    
    df = []
    
    for a in x:                      #going thru verything in the linspace array created in main
        calc = (1/cosh(2*a))**2         #found the derivative equation for f(x)
        df = np.append(df,calc)
        
    return df
        
        

#function name: central
def central(x):
    """
    Take derivative of f w.r.t x using central differences.

    Parameters
    ----------
    x : array of FLOAT
        x values to compute the derivative at.

    Returns
    -------
    df : array of FLOAT
        derivative values at associated x values

    """
    
    h = 0.001       #smaller the h, the more acccurate it is
    df2 = []        
    
    for a in x:
        calc = (f(a+(h/2))-f(a-(h/2)))/h   #central dif formula from jupyter
        df2 = np.append(df2,calc)
        

    return df2

# function name: make_plot
def make_plot(x,y_analytic,y_numeric):

    """
    

    Parameters
    ----------
    x : array of FLOAT
        DESCRIPTION.
    y_analytic : array of FLOAT
        DESCRIPTION.
    y_numeric : array of FLOAT
        DESCRIPTION.

    Returns
    -------
    None.

    """
    plt.plot(x,y_analytic,"o")
    plt.plot(x,y_numeric,"--")
    plt.xlabel("x")
    plt.ylabel("df")
    plt.title("Derivative vs x")
    plt.show()
    

def main():
    
    x = np.linspace(-2,2,100)
    make_plot(x,analytic(x),central(x))


if __name__ == "__main__":
    main()
