"""

name: solar_system.py

This program creates and animates a solar system
 
Problem 3.5 from Newman's Computational Physics.

author: Jimmy Woo
date created: 2/22/2021


"""
# imports
import vpython as vp
from math import pi,sin,cos

# user-defined functions



# part a: 
def make_solar_system():
    """
    This function visualizes the planets in the solar system in it's own canvas
   

    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """
    
    c=3E3
    solar_system = vp.canvas()
    vp.sphere(pos=vp.vector(57.9E6,0,0),canvas=solar_system,radius=2440*c,color=vp.vector(0.824,0.706,0.549))#mercury
    vp.sphere(pos=vp.vector(108.2E6,0,0),canvas=solar_system,radius=6052*c,color=vp.vector(0.45,1,0.4))#venus
    vp.sphere(pos=vp.vector(149.6E6,0,0),canvas=solar_system,radius=6371*c,color=vp.vector(0,0,1))#earth
    vp.sphere(pos=vp.vector(227.9E6,0,0),canvas=solar_system,radius=3386*c,color=vp.vector(1,0,0))#mars
    vp.sphere(pos=vp.vector(778.5E6,0,0),canvas=solar_system,radius=69173*c,color=vp.vector(0.5,0,0))#jupiter
    vp.sphere(pos=vp.vector(1433.4E6,0,0),canvas=solar_system,radius=57316*c,color=vp.vector(0.3,0.1,0.1))#saturn
    vp.sphere(pos=vp.vector(0,0,0),canvas=solar_system,radius=15000*c,color=vp.vector(1,1,0))#sun
    

      
# part b: function name: greatest_div     
def animate_solar_system():
    """
    This function visualizes the planets in the solar system in it's own canvas
    and animates the planets to orbit the sun 
   

    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """
    c=3E3
    
    #put all of the code (changing the canvas) from the first part into here to create the spheres
    animate = vp.canvas()
    mercury = vp.sphere(pos=vp.vector(57.9E6,0,0),canvas=animate,radius=2440*c,color=vp.vector(0.824,0.706,0.549))
    venus = vp.sphere(pos=vp.vector(108.2E6,0,0),canvas=animate,radius=6052*c,color=vp.vector(0.45,1,0.4))
    earth = vp.sphere(pos=vp.vector(149.6E6,0,0),canvas=animate,radius=6371*c,color=vp.vector(0,0,1))
    mars = vp.sphere(pos=vp.vector(227.9E6,0,0),canvas=animate,radius=3386*c,color=vp.vector(1,1,1))
    jupiter = vp.sphere(pos=vp.vector(778.5E6,0,0),canvas=animate,radius=69173*c,color=vp.vector(0.5,0,0))
    saturn = vp.sphere(pos=vp.vector(1433.4E6,0,0),canvas=animate,radius=57316*c,color=vp.vector(0.3,0.1,0.1))
    sun = vp.sphere(pos=vp.vector(0,0,0),canvas=animate,radius=15000*c,color=vp.vector(1,1,0))

    
    time=11000          #i wanted to have a time that would show Saturn orbit at least once

    for t in range(0,time):
        nume=2*t*pi     #shortcut so I don't have to type that expression everytime I calculate theta
        vp.rate(90)     #frequency of the for loop
        theta=nume/88  
        mercury.pos = vp.vector(57.9E6*cos(theta),57.9E6*sin(theta),0)
        theta=nume/224.7
        venus.pos = vp.vector(108.2E6*cos(theta),108.2E6*sin(theta),0)
        theta=nume/365.3
        earth.pos = vp.vector(146.6E6*cos(theta),146.6E6*sin(theta),0)
        theta=nume/687
        mars.pos = vp.vector(227.9E6*cos(theta),227.9E6*sin(theta),0)
        theta=nume/4331.6
        jupiter.pos = vp.vector(778.5E6*cos(theta),778.5E6*sin(theta),0)
        theta=nume/10759.2
        saturn.pos = vp.vector(1433.4E6*cos(theta),1433.4E6*sin(theta),0)
                   
def main():
    make_solar_system()
    animate_solar_system()
    
if __name__ == "__main__":
    main()
        