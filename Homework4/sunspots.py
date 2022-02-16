"""

name: sunspots.py

This program finds the running average of number of sunspots
and plots the results.

 

Problem 2.12 from Newman's Computational Physics.

author: Monica Rambeau
date created: 2/26/2018 
date edited: 2/22/2021

"""

# imports here

import numpy as np
import matplotlib.pyplot as plt

# user defined functions:

# part a: function name: read_data

def read_data(filename):

    """
    reads data

    Parameters
    ----------
    filename : STRING
        String of filename with data

    Returns
    -------
    x : array of float
        array of month data
    y : array of float
        array of sunspot values
    """
    
    
    a = np.loadtxt(filename)
    x = a[:,0]                          #slicing to assign columns to x and y
    y = a[:,1]
    
    
    return x, y
    
    
    
# part b: function name: some_data

def some_data(x,y):

    """
    Returns a subset of the input arrays

    Parameters
    ----------
    x : array of float
        array of month data
    y : array of float
        array of sunspot values

    Returns
    -------
    x : array of float
        array of month data
    y : array of float
        array of sunspot values
    """

    x = x[0:1000]                           #slicing the data
    y = y[0:1000]
    
    return x,y
   
    


# part c: function name: running_average

def running_average(x,y):

    """
    

    Parameters
    ----------
    x : array of float
        array of month data
    y : array of float
        array of sunspot values

    Returns
    -------
    x : array of float
        array of month data
    y : array of float
        array of averaged sunspot values

    """
   
   
    y_array = np.array([])                  #creating empty array
    for i in range(0,1000):                 #testing first 1000 values
        total = 0                           #total is the sum
        counter = 0                         #counter is how I know what to divide by
        for n in range(i-5, i+6):           #range of m in equation
            if n>=0 and n<=999:             #making sure to only use values in range
                counter = counter+1         
                total += y[n]      
            else:
                continue
        if counter>0:                       #only positive counters
            total = total/(counter)
            
        
        y_array = np.append(y_array,total)  #adding it to my array


    
    x = x[0:1000]
    y = y_array[0:1000]     
        
    return x, y
    
 

# function name: make_plot (for parts a & b)

def make_plot(x,y):

    """
    This function takes in arrays of (x,y) points and plots them 
    with labeled axes

    Parameters
    ----------
    x : array of float
        array of x values for plotting
    y : array of float
        array of x values for plotting

    Returns
    -------
    None.
    """
   
    plt.xlabel("months after Jan. 1749")
    plt.ylabel("# of Sunspots")
    
    plt.plot(x,y)
    plt.show()
    
    
    
# function name: overlay_plots (for part c)    

def overlay_plots(x,y1,y2):

    """
    plotting for part c

    Parameters
    ----------
    x : array of float
        time in months
    y1 : array of float
        data
    y2 : array of float
        running average data

    Returns
    -------
    None.

    """
    
    
    plt.xlabel("months after Jan. 1749")
    plt.ylabel("# of Sunspots")
    
    plt.plot(x,y1)                              #the OG data
    plt.plot(x,y2)                              #the running average
    plt.show()
   

def main():

    # part a
    
    x,y = read_data("sunspots.txt")         #making an array for input
    make_plot(x,y)
    
    #part b
    
    bx,by = some_data(x,y)                 #making an array for input
    make_plot(bx,by)


    # part c
    cx,cy = running_average(x,y)            #making an array for input
    overlay_plots(cx,by,cy)
    
    


    
if __name__ == "__main__":
    main()
