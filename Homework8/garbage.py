"""
name: garbage.py

Compute and visualize the trajectories of space garbage.

Problem 8.8 from Newman's Computational Physics.

author: Bucky Barnes
date created: 1/5/2018


"""

import numpy as np
import matplotlib.pyplot as plt



#glogbal constants
G = 1
M = 10
L = 2


# function name: f
def f(s):

    """
    Computes the x and y positions of trajectory.

    Parameters
    ----------
    r : array of FLOAT
        Initial condition: [x0,y0,vx0,vy0].

    Returns
    -------
    xs : array of FLOAT
        x values.
    ys : array of FLOAT
        y values.
    vxs : array of FLOAT
        x values.
    vys : array of FLOAT
        y values.    

    """
    
    
    x = s[0]
    y = s[1]
    vx = s[2]
    vy = s[3]
    
    r = (x**2+y**2)**0.5
    frac = -G*M/((r**2)*((r**2)+0.25*(L**2))**0.5)
    
    dx = vx
    dvx = x*frac
    dy = vy
    dvy = y*frac
    
    return np.array([dx,dy,dvx,dvy],float)


# function name: compute_trajectory
def compute_trajectory(s):

    """
    Computes the x and y positions of trajectory.

    Parameters
    ----------
    r : array of FLOAT
        Initial condition: [x0,y0,vx0,vy0]

    Returns
    -------
    xs : array of FLOAT
        x values.
    ys : array of FLOAT
        y values.

    """
    
    T = np.linspace(0,10,10000)
    ypoints = []
    xpoints = []
    h = (T[-1]-T[0])/len(T)
    for t in T:
        xpoints.append(s[0])
        ypoints.append(s[1])
        k1 = h*f(s)
        k2 = h*f(s+0.5*k1)
        k3 = h*f(s+0.5*k2)
        k4 = h*f(s+k3)
        s += ((k1+2*k2+2*k3+k4)/6)

    return xpoints,ypoints
        

# function name: plot_trajectory
def plot_trajectory(xs,ys):

    """
    Plot y vs. x positions. Make sure the distances on the x and y axes are equal.
    Look up plt.axis("equal") for more information.

    Parameters
    ----------
    xs : array of FLOAT
        x values.
    ys : array of FLOAT
        y values.

    Returns
    -------
    None.

    """
    plt.axis("equal")
    plt.plot(xs,ys)
    plt.show()



def main():
    
    s = [1,0,0,1]      #list of initial values
    xpoints,ypoints = compute_trajectory(s)
    plot_trajectory(xpoints,ypoints)


if __name__ == "__main__":
    main()
