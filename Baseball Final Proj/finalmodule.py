#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:57:59 2021

@author: prestonito
"""

import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi,radians
import vpython as vp


#global constants 
cd = 0.4     #drag coefficient
rho = 1.2    #density of air
m = 0.1447     #mass of baseball in kg
rad = 0.07376/2       #radius of baseball in m
A = pi*rad**2      
omegax = 0      #none of these three types of pitches have spin on the x-axis
g = 9.8      #gravity
kd = cd*rho*A/(2*m)       #k_d constant used in diff eq
kl = rad*rho*A/(2*m)       #k_l constant used in diff eq

def ask():
    
    """
     Returns
    -------
    omegay : FLOAT
    omegaz : FLOAT
    v0y : FLOAT
    theta : FLOAT
    v0 : FLOAT
        
    """

    i = input("FB, CB, or SL")      #user chooses fastball, curveball, or slider
    if i == "FB":
        omegay = -200        #fastballs have backspin of ~200 rad/s
        omegaz = 0
        v0y = 0
        theta = radians(-1.2)      #fastballs are thrown at ~-1.8 degrees
        
    elif i == "CB":
        omegay = 315         #curveballs have topspin of ~315 rad/s
        omegaz = 0
        v0y = 0
        theta = radians(3)      #curveballs are thrown at ~3 degrees
    
    elif i == "SL":          #this slider simulation is thrown by a RHP
        omegaz = -250        #sliders have side spin of ~250 degrees 
        omegay = 0
        v0y = 2             #thrown slightly to the right with a small initial velocity
        theta = radians(1.2)    #sliders are thrown at ~1.5 degrees
        
    a = float(input("Velocity of pitch (mph)"))   #asks user to input initial velocity
    v0 = a/2.237
    
    return omegay,omegaz,v0y,theta,v0


def f(r,omegay,omegaz):
    """
    

    Parameters
    ----------
    r : TYPE
        array of initial values
    omegay : FLOAT
    omegaz : FLOAT

    Returns
    -------
    array
        array of position and velocities
    

    """
    
    #assigning variables to the r array of different initial values
    x = r[0]
    y = r[1]
    z = r[2]
    vx = r[3]
    vy = r[4]
    vz = r[5]
    
    v = (vx**2+vy**2+vz**2)**0.5      #magnitude of velocity 
    
    #diff eqs from Kuchera book pg. 152
    dx = vx 
    dvx = -kd*v*vx+((kl*(omegay*vz-omegaz*vy)))
    dy = vy
    dvy = -kd*v*vy+((kl*(omegaz*vx-omegax*vz)))
    dz = vz
    dvz = -kd*v*vz+((kl*(omegax*vy-omegay*vx)))-g
    
    return np.array([dx,dy,dz,dvx,dvy,dvz],float)  #IMPORTANT: in the diff eqs given, the z-axis is the vertical axis. 
                                                    #However, in vpython, the y-axis is the vertical axis
                                                    
                                                    
# define your fourth-order Runge-Kutta here
def runge(dt,v0,v0y,omegay,omegaz,theta):
    
    """
    

    Parameters
    ----------
    dt : float
        time step
    v0 : FLOAT
    v0y : FLOAT
    omegay : FLOAT
    omegaz : FLOAT
    theta : FLOAT
    

    Returns
    -------
    xs : LIST
        list of x position values.
    ys : LIST
        list of y position values.
    zs : LIST
        list of z position values.
    v0 : FLOAT
        user input v0.

    """

    #for plotting
    xs = [] 
    ys = []
    zs = []
    
    
    #taking the x and z components
    v0x = v0*cos(theta)         
    v0z = v0*sin(theta)
    
    r = np.array([0,0,1.8288,v0x,v0y,v0z])  #r array of initial values. starts at a height of ~6ft or ~1.8288m
    h = dt
    
    #4th order Runge-Kutta while ball is in air
    while r[2] >= 0:
        xs.append(r[0]) # calc x for plotting
        ys.append(r[1]) # calc y for plotting
        zs.append(r[2])
        k1 = h*f(r,omegay,omegaz)
        k2 = h*f(r+0.5*k1,omegay,omegaz)
        k3 = h*f(r+0.5*k2,omegay,omegaz)
        k4 = h*f(r+k3,omegay,omegaz)
        r += (k1+2*k2+2*k3+k4)/6
    return xs,ys,zs,v0            #return v0 for use later in vpython function



def plot(xs,ys,zs):
    """
    Parameters
    ----------
    xs : LIST
        list of x position values.
    ys : LIST
        list of y position values.
    zs : LIST
        list of z position values.
     Returns
    -------
    xf : LIST
        list of x position values in feet
    yf : LIST
        list of y position values in feet
    zf : LIST
        list of z position values in feet

    """
    
    #turning lists into arrays to do conversion from m to ft
    xf = np.array(xs)
    yf = np.array(ys)
    zf = np.array(zs)
    xf = 3.28084*xf
    yf = 3.28084*yf
    zf = 3.28084*zf
    
    # plots our $(x,z)$ coordinates of our ball (REMEMBER: the z-direction is up from the diff eqs)
    plt.plot(xf,zf,'o') 
    plt.xlim(0,60)
    plt.xlabel("distance in feet")
    plt.ylabel("height in feet")
    
    plt.show()
    
    return xf,yf,zf



def bigplot(xf,yf,zf):
    """
    Parameters
    ----------
    xf : LIST
        list of x position values in feet.
    yf : LIST
        list of y position values in feet.
    zf : LIST
        list of z position values in feet
    """
    
    ax = plt.axes(projection ='3d')
    ax.plot3D(xf,yf,zf)
    ax.set_xlabel("distance in ft")
    ax.set_ylabel("y position in ft")
    ax.set_zlabel("height in ft")
    ax.set_ylim(1,-1)


def makefield(xs,ys,zs,v0):
    '''
    Parameters
    ----------
    xs : LIST
        list of x position values.
    ys : LIST
        list of y position values.
    zs : LIST
        list of z position values.
    v0: FLOAT
        initial velocity 
    '''


    baseball = vp.canvas(center=vp.vector(12,0,0),width=600,height=200)
    ball = vp.sphere(pos=vp.vector(xs[0],zs[0],0),canvas=baseball,radius=5*rad,color=vp.vector(1,1,1))  #the ball's radius is enlarged for a better animation

    #ground
    ground = vp.box(pos=vp.vector(12,-0.5,0),canvas=baseball,size=vp.vector(30,0.5,5),color=vp.vector(0.5,0.48,0.1))
    
    #strikezone (enlarged for better animation)
    strikezone = vp.box(pos=vp.vector(xs[0]+18.288,1.1,0),canvas=baseball,size=vp.vector(0.05,3*0.6548,3*0.5065),color=vp.vector(1,0,0),opacity=0.4)  

    
    for i in range(len(xs)):
        vp.rate(v0*0.8)     #frequency of loop depends on v0 to make animation more realistic
        ball.pos = vp.vector(xs[i],zs[i],ys[i])
                                                               
        
        
def main():
    
    omegay,omegaz,v0y,theta,v0 = ask()  #initially, i had these in the global constants part. But, for it to work in the main file, i had to turn it into its own function. That's why I have lots of parameters for the functions below.
    
    xs,ys,zs,v0 = runge(0.01,v0,v0y,omegay,omegaz,theta)   #time step of 0.01 seconds
    makefield(xs,ys,zs,v0)
    xf,yf,zf = plot(xs,ys,zs)
    bigplot(xf,yf,zf)
    
if __name__=="__main__":
    main()
                                                    
                                                    
                                                    
                                                    
                                                    
    
