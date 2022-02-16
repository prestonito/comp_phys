"""

name: madelung.py

This program calculates the Madelung constant for sodium chloride

Problem 2.9 from Newman's Computational Physics.

author: Wanda Maximoff
date created: 2/2/2018
date edited: 2/7/2021

"""


def m_constant(L):
    """
    calculates the Madelung constant for 2L+1 atoms

    Parameters
    ----------
    L : integer
        Use 2L+1 atoms in calculation

    Returns
    -------
    m : float
        Madelung constant for sodium chloride

    """
    
    # complete me
  
    
    m = 0
        
    for k in range(-L,L+1):  #first sum
        for i in range(-L,L+1):    #second sum
            for j in range(-L,L+1):    #third sum
                if i==0 and j==0 and k==0:    #ignore to avoid divide by 0
                    pass
                else:
                    m = ((-1)**(k+i+j))/((k**2+i**2+j**2)**(1/2))+m
              
                    
                    
                    
    
    
    
    
    return m


def main():
    # make sure to choose a large enough L
    L = 80
    M = m_constant(L)
    print("the Madelung constant for L =", L, "is ", M)
    
    
if __name__ == "__main__":
    main()
