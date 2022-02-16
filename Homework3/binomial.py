"""

name: binomial.py

 This program calculates probabilities of coin flips

Problem 2.11 from Newman's Computational Physics.

author: Monica Rambeau
date created: 2/6/2018
date edited: 2/15/2021

"""



# part a: function name: binomial

def binomial(n,k):
    """
    Finds the binomial coefficient for n and k 

    Parameters
    ----------
    n : INT

    k : INT


    Returns
    -------
    INT
        binomial coefficient
    """
    
    #to calculate k!
    k_factorial = 1
    
    if k == 0:
        pass
    elif  k >= 1:
        for k in range(1, k+1):
            k_factorial = k*k_factorial
       
    
    #to calculate (n-k)!
    nk_factorial = 1
    
    nk = n-k
    
    if nk == 0:
        pass
    elif nk >= 1:
        for nk in range(1, nk+1):
            nk_factorial = nk_factorial*nk

    
    
    #to calculate n!
    n_factorial = 1
    if n == 0:
        pass
    elif  n >= 1:
        for n in range(1, n+1):
            n_factorial = n*n_factorial
    
    #to calculate the denominator
    denominator = k_factorial*nk_factorial
    
    #to calculate binomial coefficients
    binomial = n_factorial//denominator
    
    
    return binomial

    
    

# part b: function name: pascal_triangle


def pascal_triangle(N):
    """
    Prints N rows of Pascal's triangle

    Parameters
    ----------
    N : INT
        Number of rows in the triangle

    Returns
    -------
    None.

    """    

    for N in range(1,N+1):
        for k in range(0, N+1):
            print(binomial(N,k),end=" ")
        print()
            

#c-a: function name: prob

def prob(toss,heads):

    """
    Calculates the probability of tossing n_heads out of n_tosses
    
    Parameters
    ----------
    n_tosses : INT
        number of tosses
    n_heads : INT
        number of heads
    
    Returns
    -------
    FLOAT
        probability
    """
    

    
    prob = binomial(toss,heads)/(2**toss)
    
    return prob


#c-b: function name: prob_more_than

def prob_more_than(toss,heads):

    """
    Calculates the probability of tossing n_heads or more out of n_tosses
    
    Parameters
    ----------
    n_tosses : INT
        number of tosses
    n_heads : INT
        number of heads
    
    Returns
    -------
    FLOAT
        probability
    """
    
    prob_more_60 = 0.
    for i in range(heads,toss+1):
        prob_more_60 += prob(toss,i)
        
        
    return prob_more_60



def main():
    # some examples of using the functions
    
    print(binomial(4,2))
    
    pascal_triangle(20)
    
    
    toss = 100
    heads = 60

    print("the probability of exactly 60 heads is:",prob(toss,heads))    
    
    
    
    print("the probability of 60 or more heads is:",prob_more_than(toss,heads))
    
if __name__ == "__main__":
    main()
    
    