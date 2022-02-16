"""

name: gravity.py

Model the gravitational pull of a galaxy.

Problem 5.14 from Newman's Computational Physics.

author: Shuri
date created: 22/3/2021


"""
import gaussxw as g
import numpy as np
import matplotlib.pyplot as plt

# function name: force
def integrand(x,y,z):

    """
    The integrand of the integral of F

    Parameters
    ----------
    x: INT
        x value to calculate force for.
    y: INT
        y value to calculate force for.
    z: INT
        z value to calculate force for.


    Returns
    -------
    value : INT
        Integrand at each x and y value.

    """
    y = (x**2+y**2+z**2)**-3/2    #formula from book
    
    return y


# function name: force
def force(z):

    """
    Calculate force as a function of distance above the sheet, z.

    Parameters
    ----------
    z : array of FLOAT
        z values to calculate force for.

    Returns
    -------
    F : array of FLOAT
        Force at each z value.

    """
    
    #givens
    N = 10
    a = -5
    b = 5
    mass = 1E4
    area = 100
    sigma = mass/area
    G = 6.674E-11
    
    
    x,w = g.gaussxwab(N,a,b)


    F = np.array([])
    
    for k in z:
        I = 0
        for i in range(len(x)):         #first integral
            for j in range(len(x)):      #second integral
                I += w[i]*w[j]*integrand(x[i],x[j],k)   #Eq. 5.82
                
        F = np.append(F,G*sigma*k*I)
            
    return F
        
    



# function name: make_plot
def make_plot(z):

    """
    Visualize force as a function of distance above the sheet, z.

    Parameters
    ----------
    z : array of FLOAT
        z values to visualize force for.

    Returns
    -------
    None.

    """
    

    plt.plot(z,force(z))
    plt.show()

def main():

    z = np.linspace(0,10,1000)
    make_plot(z)

if __name__ == "__main__":
    main()
