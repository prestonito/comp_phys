"""

name: romberg.py

Compute and vsualize diffraction of waves upon encountering a straight edge.
 
Problem 5.7 from Newman's Computational Physics.

author: Darcy Lewis
date created: 15/3/2021


"""

import numpy as np
from math import sin


# function name: f
def f(x): 
    """
    Compute values of the function that we want to integrate.

    Parameters
    ----------
    x : FLOAT
        x value.

    Returns
    -------
    FLOAT
        function value at x.

    """
    
    y = (sin((100*x)**(1/2)))**2
    
    return y


# function name: norm_trap
def norm_trap(a,b,N): 
    """
    Compute values of the function that we want to integrate.

    Parameters
    ----------
    a : FLOAT
        lower limit of integration.
    b : FLOAT
        upper limit of integration.
    N : INT
        number of divisions.

    Returns
    -------
    res*h : FLOAT
        function value at x.

    """
    #all from jupyter activity
    h = (b-a)/N
    res = 0.5*f(a)+0.5*f(b)
    for k in range(1,N):
        res += f(a+(k*h))
    
    return res*h

# a) Adaptive Trapezoidal Rule
# function name: adapt_trap
def adapt_trap(a,b):

    """
    Compute the integral of f(x) using the adaptive trapezoidal rule.

    Parameters
    ----------
    a : FLOAT
        lower limit of integration.
    b : FLOAT
        upper limit of integration.

    Returns
    -------
    N : INT
        number of divisions necessary for given accuracy.
    I : FLOAT
        integral value.
    err : FLOAT
        error of computation at N divisions.

    """
    #all from jupyter activity
    N = 1
    res = norm_trap(a,b,N)
    err = 1
    while err>=1E-6:
        N *= 2
        h = (b-a)/N
        res1 = 0
        for k in range(1,N,2):
            res1 += f(a+(k*h))
        I = (res/2)+res1*h
        err = abs(I-res)/3
        res = I

    return N, I, err

    
    
# b) Romberg Integration
# function name: romberg
def Romberg(a,b):

    """
    Compute the integral of f(x) using Romberg integration.
    
    Print the Romberg triangle.

    Parameters
    ----------
    a : FLOAT
        lower limit of integration.
    b : FLOAT
        upper limit of integration.

    Returns
    -------
    N : INT
        number of divisions necessary for given accuracy.
    I : FLOAT
        integral value.
    err : FLOAT
        error of computation at N divisions.

    """

    N = 1

    res = norm_trap(a,b,N)    

    error = 10
    Rprev = np.array([norm_trap(a,b,N)])
    print(Rprev)
    i = 2
    while error >= 1E-6:
        Rcurrent = np.zeros(i)
        N *= 2                      #adapt_trap rule start
        h = (b-a)/N               
        res1 = 0
        for k in range(1,N,2):
            res1 += f(a+(k*h))
        I = (res/2)+res1*h
        res = I                     #adapt_trap end
        Rcurrent[0] = I             #takes care of first value in each row
        
        #chanigng the 0's to correct values
        for m in range(1,i):

            calcR = Rcurrent[m-1]+(Rcurrent[m-1]-Rprev[m-1])/(4**m-1)  #eq5.51
            Rcurrent[m] = calcR
            error = abs(Rcurrent[m-1]-Rprev[m-1])/(4**m-1)          #error
            
        Rprev = Rcurrent
        I = calcR                       #setting the sum to I
        i += 1                          #counts the number of iterations through while loop
        print(Rcurrent)
        
    print(N,I,error)


    return N, I, error
        

def main():
    
    print(adapt_trap(0,1))
    #Romberg(0,1)

if __name__ == "__main__":
    main()