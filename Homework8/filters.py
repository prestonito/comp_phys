"""
name: filters.py

Compute and visualize the voltages on a low-pass filter.

Problem 8.1 from Newman's Computational Physics.

author: Bucky Barnes
date created: 1/5/2018

"""

import numpy as np
import matplotlib.pyplot as plt



#function name: f
def f(RC,T, V_out):
    
    """
    define functions for ODEs
    
    Parameters
    ----------
    RC : array of initial values
    t : array of FLOAT
        contains the time values
    Vout 
    
    
    Returns
    -------
    array of ODE values
    
    """
    
    #to determine what value V_in is 
    x = (2*T)//1
    
    if x%2 == 0:
        V_in = 1
    elif x%2 == 1:
        V_in = -1
        
    return(V_in-V_out)/RC

# function name: Vout
def Vout(T,RC):

    """
    Compute the voltages at given time values.

    Parameters
    ----------
    T : array of FLOAT
        Contains the time values to compute voltage at..
    RC : FLOAT
        Time constant for a given circuit.

    Returns
    -------
    vs : array of FLOAT
        voltage values associated with provided time values.

    """
    

    vs = [] # for plotting
    V_out = 0
    
    h = (T[-1]-T[0])/len(T)     #takes the last value-first value and divides by total

    for t in T:
        vs = np.append(vs,V_out)
        k1 = h*f(RC,t,V_out)
        k2 = h*f(RC,t+0.5*h,V_out+0.5*k1)
        k3 = h*f(RC,t+h,V_out+0.5*k2)
        k4 = h*f(RC,t+h,V_out+k3)
        V_out += (k1+2*k2+2*k3+k4)/6
    return vs

    
    



# function name: make_plots
def make_plots(RCs):
    """
    Produces a plot of voltage vs. time for each of the RC values provided.

    Parameters
    ----------
    RCs : list of FLOAT
        List of RC values to create plots for

    Returns
    -------
    None.

    """
    T = np.linspace(0,10,1000)
    List=[]
    List=np.append(List, Vout(T,RCs))
    plt.xlabel("Time (s)")
    plt.ylabel("V_out value")
    plt.title("Vout vs Time for different RC values")
    
    plt.plot(T,List)

    


def main():
    
    #to account for different RCs
    make_plots(1)
    make_plots(0.1)
    make_plots(0.01)

    



    return None

if __name__ == "__main__":
    main()
