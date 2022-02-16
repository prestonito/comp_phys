"""

name: velocities.py

Integrate velcity to compute displacement over time.
 
Problem 5.1 from Newman's Computational Physics.

author: Darcy Lewis
date created: 15/3/2021


"""
import numpy as np
import matplotlib.pyplot as plt

# function name: read_data

def read_data(filename):

    """
    Read data from file and returns contents.

    Parameters
    ----------
    filename : STRING
        filename with velocity and time data.

    Returns
    -------
    time : array of FLOAT
        time values.
    velocity : array of FLOAT
        velocities

    """
    
    a = np.loadtxt(filename)
    t = a[:,0]
    v = a[:,1]
    
    return t, v



# function name: calc_distance

def calc_distance(t,v):

    """
    Calculate distance via the trapezoidal rule.

    Parameters
    ----------
    t : array of FLOAT
        time array.
    v : array of FLOAT
        velocity array.
    Returns
    -------
    time : array of FLOAT
        time values.
    distance : array of FLOAT
        distance values.

    """
   
    
    time = t
    distance = [0]
    
    total = 0
    for x in range(1,len(t)):
        area = (v[x]+v[x-1])/2          #area of each trapezoid
        total = area+total              #adds it to the area of previous trapezoid
        distance = np.append(distance,total)
    
    
    return time,distance
    

# function name: make_plot

def make_plot(time,velocity,distance):

    """
    Overlay velocity and position as a function of time.
    
    Use a legend to distinguish the lines.

    Parameters
    ----------
    time : array of FLOAT
        time values.
    velocity : array of FLOAT
        velocity values.
    distance : array of FLOAT
        distance values.

    Returns
    -------
    None.

    """
    
    plt.plot(time,velocity)
    plt.plot(time,distance)
    plt.legend(['velocity','distance'])
    plt.xlabel("Time")
    plt.show
    


def main():
    t,v = read_data("velocities.txt")
    time,distance = calc_distance(t,v)
    make_plot(t,v,distance)

    
if __name__ == "__main__":
    main()