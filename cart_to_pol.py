"""
name: cart_to_poly.py

This program converts from cartesian to polar coordinates.
Problem 2.3 from Newman's Computational Physics.


author: Jessica Jones
date created: 1/11/2018
date edited: 1/31/2021

"""

#imports
from math import pi, atan, degrees


# user defined functions
def return_polar(x,y):
    """

    Parameters
    ----------
    x : x coordinate
    y : y coordinate

    Returns
    -------
    r : radius
    theta_deg : angle in degrees

    """
    # complete me

    r = (x**2+y**2)**(1/2)
    theta_deg = degrees(atan(y/x))

    return r, theta_deg


def main():
    #complete me: ask for user input
    x = float(input("Enter x:"))
    y = float(input("Enter y:"))
    
    
    r, theta = return_polar(x,y) # get the r, theta for a given x,y
    
    #complete me: print results in a readable manner
    print("r=",r,"theta",theta)

# run main function
if __name__ == "__main__":
    main()
