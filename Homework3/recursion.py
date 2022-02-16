"""

name: recursion.py

This program uses recursion to find:
    a) The nth Catalan number
    b) the greatest divisor between to numbers
 
Problem 2.13 from Newman's Computational Physics.

author: Monica Rambeau
date created: 1/11/2018 
date edited: 2/15/2021

"""


# part a: function name: catalan

def catalan(n):

    """
     
    This function recursively calculates the nth 
    Catalan number
   

    Parameters
    ----------
    n : INT
        index n of Catalan number

    Returns
    -------
    INT
        nth Catalan number

    """    

    if n==0:
        return 1
    else:
        answer = (4*n-2)*catalan(n-1)//(n+1)
        return answer
      
# part b: function name: greatest_div     

def greatest_div(m,n):
    
    """
   
    This function recursively calculates the greatest
    common divisor between m and n


    Parameters
    ----------
    m : INT
        first value 
    n : INT
        second value

    Returns
    -------
   INT
       greatest common divisor of both m and n

    """

    if n==0:
        return m
    else:
        answer = greatest_div(n,m%n)
        return answer         


          
def main():
    # some examples 
    n = 100
    print("Catalan number",n,"is",catalan(n))
    n = 12
    print("Catalan number",n,"is",catalan(n))
    
    a, b = 192, 108
    print("The greatest divisor of",a,"and",b, "is",greatest_div(a,b))
    
    a,b = 244, 98
    print("The greatest divisor of",a,"and",b, "is",greatest_div(a,b))
if __name__ == "__main__":
    main()
        