"""

name: lattice.py

Visualize 3D lattice structures
 
Problem 3.4 from Newman's Computational Physics.

author: Jimmy Woo
date created: 2/22/2021


"""
# imports
import vpython as vp

# user-defined functions



# part a: 
def sodium_chloride():
    """
    This function visualizes soldium chloride
   

    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """
  
    
  
    L = 1
    R = 0.45
    lattice = vp.canvas() 
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):        
                if ((abs(i)%2)+(abs(j)%2)+(abs(k)%2))%2==1:     #this if statement will alternate the colors
                    vp.sphere(pos=vp.vector(i,j,k),canvas=lattice,radius=R,color=vp.vec(1,0,0))
                else:
                    vp.sphere(pos=vp.vector(i,j,k),canvas=lattice,radius=R,color=vp.vec(0,0,1))
                

      
# part b: function name: greatest_div     
def fcc_lattice():
    """
    This function visualizes a face-centered cubic lattice structure

    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """
                 
    L = 6
    R = 0.35
    fcc = vp.canvas() 
    
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):     
                if L%2==1:          
                    if ((abs(i)%2)+(abs(j)%2)+(abs(k)%2))%2==1:
                        vp.sphere(pos=vp.vector(i,j,k),canvas=fcc,radius=R,color=vp.vec(1,1,0.5))
                    else:
                        pass
                if L%2==0:
                    if ((abs(i)%2)+(abs(j)%2)+(abs(k)%2))%2==0:
                        vp.sphere(pos=vp.vector(i,j,k),canvas=fcc,radius=R,color=vp.vec(1,1,0.5))
                    else:
                        pass


def main():
    
    sodium_chloride()
    fcc_lattice()
    
if __name__ == "__main__":
    main()
        