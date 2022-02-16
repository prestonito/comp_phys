"""

name: catalan.py

This program calculates the numbers in the Catalan series

Problem 2.7 from Newman's Computational Physics.

author: Wanda Maximoff
date created: 2/2/2018
date edited: 2/7/2021

"""

# imports


# user-defined functions

def calc_print_catalan(max_num):
    """
    This function calculates and prints the numbers in the Catalan series.
    It prints one number per line. 

    Parameters
    ----------
    max_num : integer
        print all catelan numbers up to this value

    Returns
    -------
    None.

    """

    
    # complete me
    
    
    out = 1
    n = 0
    c = 1
    while out<max_num:
        print(out)
        out = (((4*n)+2)*(c))//(n+2)
        c = out
        n = n+1
        

    
       
    
    
# main function
def main():
    # you should change the parameter below to something smaller while testing your code.
    calc_print_catalan(13)

# call main IFF we are executing *this* file
if __name__ == "__main__":
    main()