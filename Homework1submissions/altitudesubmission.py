"""
name: altitude.py

This program calculates the altitude of a satellite given a desired
period of orbit, T. Problem 2.2 from Newman's Computational Physics


author: Jessica Jones
date created: 1/11/2018 
date edited: 1/31/2021

"""


#imports
from math import pi

#user-defined functions
def alt(T):
    """

    Parameters
    ----------
    T : period of orbit in seconds

    Returns
    -------
    h : altitude in meters
    
    """  
    # complete me
    G = 6.67E-11
    M = 5.97E24
    R = 6371E3
    
    h = ((G*M*T**2)/(4*pi**2))**(1/3)-R
    
    
    return h

def ask_user():
    """

    Returns
    -------
    float
        altitude in meters for given T.

    """
    
    T = float(input("Enter the orbital period in seconds: "))  
    

    
    return alt(T)

# main function
def main():
    
    #part b
    h = ask_user()
    print("The height above the earth is:", h,"meters")
    print("or",h/1000,"kilometers")

    # part c
    # complete me, do NOT use ask_user()
    
    #orbit once a day
    print("A satellite with a period of one day orbits at an alitude of",alt(86400)/1000, "kilometers")
    #orbit once every 90 min
    print("A satellite with a period of 90 minutes orbits at an altitude of",alt(5400)/1000, "kilometers")
    #orbit once every 45 min
    print("A satellite with a period of 45 minutes orbits at an altitude of",alt(2700)/1000, "kilometers")
    
    
    #part d
    print("The difference in altitude of a satellite with an orbit of 23.93 hrs and 24 hrs is", alt(86400)-alt(86148), "kilometers")
     
 
# run this code
if __name__ == "__main__":
    main()