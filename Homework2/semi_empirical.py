"""

name: semi_empirical.py

 This program calculates the binding energy and binding energy per 
 nucleon for a given isotope.

Problem 2.10 from Newman's Computational Physics.

author: Wanda Maximoff
date created: 2/2/2018
date edited: 2/7/2021

"""

# import statements


# user-defined functions
def binding_energy(A,Z):
    """
    calculates the binding energy of a single isotope

    Parameters
    ----------
    A : integer
        number of nucleons
    Z : integer
        number of protons

    Returns
    -------
    BE : float
        binding energy

    """
    
 
    
   #given values for a_x
    a_1 = 15.8
    a_2 = 18.3
    a_3 = 0.714
    a_4 = 23.2
    
    #figuring out which value to use for a_5
    if A%2==0 and Z%2==0:
        a_5 = 12
    elif A%2==0 and Z%2==1:
        a_5 = -12
    elif A%2==1:
        a_5 = 0
    
    BE = a_1*A-a_2*A**(2/3)-((a_3*Z**2)/(A**(1/3)))-((a_4*(A-2*Z)**2)/A)+(a_5/(A**0.5))
    
   
        
    
        
    
    
    
    return BE

def binding_energy_per_nucleon(A,Z):
    """
    calculates the binding energy per nucleon of a single isotope

    Parameters
    ----------
    A : integer
        number of nucleons
    Z : integer
        number of protons

    Returns
    -------
    BE_A : float
        binding energy per nucleon

    """
    
    
   
    
    BE = binding_energy(A,Z)
    BE_A = BE/A
    
    
    return BE_A


def main():
    #complete me for 58Ni (Nickel-58)
    
    # a)
    
    
    print("The binding energy is",binding_energy(58,28),"MeV")
    
    
    
    # b) 
    
    
   
    print("The binding energy per nucleon is", binding_energy_per_nucleon(58,28))

if __name__ == "__main__":
    main()