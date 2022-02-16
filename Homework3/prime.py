"""

name: prime.py

This program finds all of the prime numbers up through N

 

Problem 2.12 from Newman's Computational Physics.

author: Monica Rambeau
date created: 1/11/2018
date edited: 2/15/2021

"""

# imports here


# part a: function name: primes_a

def primes_a(N):

    """
    Finds prime numbers up to N 

    Parameters
    ----------
    N : INT
        Find prime numbers up to this value

    Returns
    -------
    prime_list : LIST of INTs
        list of prime numbers up to N
    """

   
  
        
    prime_list_a = [2]
    
    
    for a in range(2,N+1):      #to check all the numbers up to N
        prime = True            #assign a boolean value for prime
        for x in prime_list_a:
            if a%x == 0:
                prime = False   #changes the value for prime
            else:
                continue        #rerun the loop to check other factors in list
        if prime == True:       
            prime_list_a.append(a)  #add the numbers to list

        
                
                
    return prime_list_a
 
    
 
    

         
    
# part b: function name: primes_b

def primes_b(N):

    """
    Finds prime numbers up to N 

    Parameters
    ----------
    N : INT
        Find prime numbers up to this value

    Returns
    -------
    prime_list : LIST of INTs
        list of prime numbers up to N
    """
     
    
    prime_list_b = [2]
    
    
    for a in range(3,N+1):           
        prime = True
        for x in prime_list_b:
            if x>=(N**(1/2)):       #stops the for loop if x is bigger than root(n)
                break
            else:
                if a%x == 0:
                    prime = False
                else:
                    continue
        if prime == True:
            prime_list_b.append(a)

        
                
                
    return prime_list_b

  
# part c: function name: primes_c

def primes_c(N):
    

    """
    Finds prime numbers up to N 

    Parameters
    ----------
    N : INT
        Find prime numbers up to this value

    Returns
    -------
    prime_list : LIST of INTs
        list of prime numbers up to N
    """
 
    
 
    prime_list_c = [2]
 
    for a in range(3,N+1):           
        prime = True
        for x in prime_list_c:
            if x>=(N**(1/2)):       #stops the for loop if x is bigger than root(n)
                break
            else:
                if x < N**(1/2):
                    if a%x == 0:
                        prime = False
                    else:
                        continue
                else:
                    break
        if prime == True:
            prime_list_c.append(a)

        
                
                
    return prime_list_c
 
 
def main():
    # a smaller N is easier for developing / debugging!
    N = 10
    
    # the following should all give the same results, but each one is faster to
    # compute than the previous
    print("The primes up to", N, "are", primes_a(N))
    #print("The primes up to", N, "are", primes_b(N))
    #print("The primes up to", N, "are", primes_c(N))
    
if __name__ == "__main__":
    main()
