"""
name: air_resistance.py

Compute and visualize the *realistic* trajectories of a cannonball.

Problem 8.7 from Newman's Computational Physics.

author: Bucky Barnes
date created: 1/5/2018

"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sin,cos

#global constants
rho = 1.22
C = 0.47
g = 9.81
R = 0.08
v0 = 100
theta = pi/6    #radians = 30 degrees


# function name: f
def f(r,m):
    
    """

    Parameters
    ----------
    r : array of FLOAT
        Initial condition [x0,y0,vx0,vy0].


    Returns
    -------
    TYPE
        DESCRIPTION.

    """

    vx = r[2]
    vy = r[3]
    
    
    dx = vx
    dy = vy    
    frac = (rho*C*pi*R**2)/(2*m)     #to shorten acceleration formula
    magv = (vx**2+vy**2)**0.5
    

    dvx = -frac*vx*magv
    dvy = -g-(frac*vy*magv)
    
   
    return np.array([dx,dy,dvx,dvy],float)


# function name: compute_trajectory
def compute_trajectory(r,m,dt):
    """

    Parameters
    ----------
    r : array of FLOAT
        Initial condition [x0,y0,vx0,vy0].
    m : FLOAT
        Mass of cannonball.
    dt : FLOAT
        Time step.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    xs = []
    ys = []
    h = dt
    
    while r[1] >= 0:       #r[1] is y position; run until it reaches 0
        xs.append(r[0])
        ys.append(r[1])
        k1 = h*f(r,m)
        k2 = h*f(r+0.5*k1,m)
        k3 = h*f(r+0.5*k2,m)
        k4 = h*f(r+k3,m)
        r += (k1+2*k2+2*k3+k4)/6
    return xs,ys
        



# function name: plot_trajectory
def plot_trajectory(xs,ys):

    """
    Plots cannonball trajectory.

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
    plt.plot(xs,ys)
    plt.xlabel("Distance in m")
    plt.ylabel("Height in m")
    plt.title("Cannonball's Path of Travel")
    plt.show


# function name: part_c
def part_c(r,dt):

    """

    Your choice on how this function behaves to demonstrate mass dependence on traectories

    """

    #list of different potential masses
    M = [0.1,1,10,25,50]
    
    for m in M:
        r = np.array([0,0,v0*cos(theta),v0*sin(theta)],float)
        dt = 0.01         #time small time step
        xps,yps = compute_trajectory(r,m,dt)
        plot_trajectory(xps,yps)
        
        #takes the last value in the list to show the total disatnce traveled
        print("total distance traveled by a cannonball of mass",m,"kg","is:",xps[-1],"m")

        

def main():

    
    #part b
    r = np.array([0,0,v0*cos(theta),v0*sin(theta)],float)
    dt = 0.01
    m = 1
    xs,ys = compute_trajectory(r,m,dt)
    plot_trajectory(xs,ys)
    
    #part c
    part_c(r,dt)

    return None

if __name__ == "__main__":
    main()
