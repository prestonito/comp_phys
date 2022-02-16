"""

name: semi_empirical.py

 This program calculates the most stable isotope for a given element
 and the overall most stable element.

Problem 2.10 from Newman's Computational Physics.

author: Wanda Maximoff
date created: 2/2/2018
date edited: 2/7/2021

"""


# import statements

# user-defned functions
def largest_BE_A(Z):
    """
    Computes the most stable isotope for a given element (part c).

    Parameters
    ----------
    Z : integer
        number of protons.

    Returns
    -------
    A : int
        number of nucleons for most stable isotope with Z protons.

    """
    #givens
    a_1 = 15.8
    a_2 = 18.3
    a_3 = 0.714
    a_4 = 23.2
    
    max_BE = -100
    max_A = -100
    
    for A in range(Z,3*Z+1):
        if A%2==0 and Z%2==0:
            a_5 = 12.
        elif A%2==0 and Z%2==1:
            a_5 = -12.
        elif A%2==1:
            a_5 = 0.
        BE_A = ((a_1*A-a_2*A**(2/3)-a_3*(Z**2)/(A**(1/3))-a_4*((A-2*Z)**2)/A+a_5/(A**0.5))/A)
        if BE_A > max_BE:
            max_BE = BE_A
            max_A = A
        else:
            pass
                
    
    
    
    return max_A

def most_stable():
    """
    Prints most stable A for each Z from 1 to 100 (part d) and returns the
    overall most stable Z.

    Returns
    -------
    Z : int
        number of protons for overall most stable element.

    """
   
    
    #givens
    a_1 = 15.8
    a_2 = 18.3
    a_3 = 0.714
    a_4 = 23.2
    
    max_BE = -100
    
   
    
    max_Z=0
    
    
    for Z in range(1,101):
        for A in range(Z,3*Z+1):
            if A%2==0 and Z%2==0:
                a_5 = 12.
            elif A%2==0 and Z%2==1:
                a_5 = -12.
            elif A%2==1:
                a_5 = 0.
            BE_A = ((a_1*A-a_2*A**(2/3)-a_3*(Z**2)/(A**(1/3))-a_4*((A-2*Z)**2)/A+a_5/(A**0.5))/A)
            if BE_A > max_BE:
                max_BE = BE_A
                max_Z = Z
            else:
                pass
           
        
    return max_Z

# main function 
def main():
    


        
    
    
    Z = 28
    A = largest_BE_A(Z)
    print("the most stable isotope with", Z, "protons has", A, "nucleons.")
    
    # part c.
    print("The most stable element has", most_stable(), "protons.")

# run main() iff we are executing THIS file
if __name__ == "__main__":
    main()