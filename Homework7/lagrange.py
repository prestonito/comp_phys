"""

name: lagrange.py

Compute the distance to the Lagrange point.

Problem 6.16 from Newman's Computational Physics.

author: Sam Wilson
date created: 29/3/2021



"""


# function name: f(x)
def f(r):

    """
    function
    
    Input
    -------
    FLOAT
        x value

    Returns
    -------
    FLOAT
        y value

    """
    #constants
    G = 6.674E-11
    M = 5.974E24
    m = 7.348E22
    R = 3.844E8
    w = 2.662E-6

    
    return (G*M/(r**2))-(G*m/((R-r)**2))-r*w**2

# function name: f'(r)
def fprime(r):

    """
    function
    
    Input
    -------
    FLOAT
        x value

    Returns
    -------
    FLOAT
        y value

    """
    #constants
    G = 6.674E-11
    M = 5.974E24
    m = 7.348E22
    R = 3.844E8
    w = 2.662E-6

    
    return ((-2*G*M)/r**3)-(2*G*m/(R-r)**3)-w**2   #analytic derivative


# function name: L1_point()
def L1_point():

    """
    Comput the distance from earth to the L1 Lagrange point.

    Returns
    -------
    FLOAT
        Distance to the L1 point in km.

    """

    x = 9E2   #random guess
    error = 10
    while error > 1E-3:
        xp = x-f(x)/fprime(x)   #to find the new x point
        error = abs(xp-x)       
        x = xp                  #assigns the new x to the OG x to run through again
    r = x
    
    return r/1000
    
# main function
def main():

    print(L1_point())
    print(f(30),fprime(30))
       
        
# run main function IFF executing this file
if __name__ == "__main__":
    main()   
    
    
    
    
    