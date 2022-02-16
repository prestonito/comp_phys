"""
name: Lorenz.py

Compute and visualize the Lorentz attractor.

Problem 8.3 from Newman's Computational Physics.

author: Bucky Barnes
date created: 1/5/2018


"""
import numpy as np
import matplotlib.pyplot as plt


#givens
sigma = 10.0
r = 28.0
b = 8/3


# function name: f
def f(s):

    """
    Compute the positions of the Lorentz attractor

    Parameters
    ----------
    s : array of FLOAT
        Initial condition: [x0,y0,z0].

    Returns
    -------
    xs : array of FLOAT
        x values.
    ys : array of FLOAT
        y values.
    zs : array of FLOAT
        z values.

    """
    x = s[0]
    y = s[1]
    z = s[2]

    dx = sigma*(y-x)
    dy = (r*x)-y-(x*z)
    dz = (x*y)-(b*z)   

    return np.array([dx,dy,dz],float)

# function name: compute_Lorentz
def compute_Lorentz(s,T):

    """
    Compute the positions of the Lorentz attractor

    Parameters
    ----------
    s : array of FLOAT
        Initial condition: [x0,y0,z0].
    T : array of FLOAT
        Time values to compute positions.

    Returns
    -------
    xs : array of FLOAT
        x values.
    ys : array of FLOAT
        y values.
    zs : array of FLOAT
        z values.

    """
    
    #for plotting
    xs = []
    ys = []
    zs = []
    
    #from jupyter
    h = (T[-1]-T[0])/len(T)
    for t in T:
        xs.append(s[0])
        ys.append(s[1])
        zs.append(s[2])
        k1 = h*f(s)
        k2 = h*f(s+0.5*k1)
        k3 = h*f(s+0.5*k2)
        k4 = h*f(s+k3)
        s += (k1+2*k2+2*k3+k4)/6
        
    return xs,ys,zs
    
    


# function name: make_plots
def make_plots(xs,ys,zs,T):

    """
    Make the two plots: y vs t and z vs x.

    Parameters
    ----------
    xs : array of FLOAT
        x values.
    ys : array of FLOAT
        y values.
    zs : array of FLOAT
        z values.
    T : array of FLOAT
        time values.

    Returns
    -------
    None.

    """
    
    plt.plot(xs,zs)
    plt.xlabel("x")
    plt.ylabel("z")
    plt.show()
    plt.plot(T,ys)
    plt.xlabel("Time")
    plt.ylabel("y")
    plt.show()




def main():
    
    #parameters for compute_Lorentz
    s = [0,1,0]
    T = np.linspace(0,50,10000)
    
    xs,ys,zs = compute_Lorentz(s,T)
    make_plots(xs,ys,zs,T)
    

    return None


if __name__ == "__main__":
    main()
