#!/usr/bin/env python
# coding: utf-8

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gravity_acc=9.81 #gravity accleration
data_y=[]
pairs=np.array([("angle","velocity")])
direction=True

barrier=[75,100,300]
landing_zone=[50,70,0]
velocity_range=[80,100,1]
angle_range=[85,90,1]
time_range=[0,50,0.1] #start_time,end_time,step

line1_x=np.full(barrier[2],barrier[0])
line1_y=np.arange(0,barrier[2],1)
line2_x=np.arange(barrier[0],barrier[1],1)
line2_y=np.full(barrier[1]-barrier[0],barrier[2])
line3_x=np.full(barrier[2],barrier[1])
line3_y=np.arange(0,barrier[2],1)

# Calculation of X coordinate of value
def X_coordinate (value,angle):
    return value*math.cos(math.radians(angle))

# Calculation of Y coordinate of value
def Y_coordinate (value,angle):
    return value*math.sin(math.radians(angle))

def TrajectoryPointX (V,T,angle,direction,start_x):
    if direction:
        return start_x+X_coordinate(V,angle)*T
    else:
        return 2*start_x-X_coordinate(V,angle)*T

# Calculation of the reflection --- DOESN'T WORK ---
def TrajectoryPointY (V,T,angle,reflection,time_y,start_y):
    if reflection:
        return start_y+Y_coordinate(V*0.75,angle)*(T-time_y)-0.5*gravity_acc*(T-time_y)*(T-time_y)
    else:
        return Y_coordinate(V,angle)*T-0.5*gravity_acc*T*T

def XYcalc (velocity,angle,start_x,start_y,time_y,start_time,end_time,step):
    direction=True
    landing_check=False
    reflection=False
    for time in np.arange(start_time,end_time,step):
        x=TrajectoryPointX(velocity,time,angle,direction,start_x)
        y=TrajectoryPointY(velocity,time,angle,reflection,time_y,start_y)

        if x > barrier[0] and y > barrier[2]: #point is above the barrier
            above=True
            bellow=False
        elif x < barrier[0] and y < barrier[2]: #point is bellow the barrier
            above=False
            bellow=True

        if x > barrier[0] and y < barrier[2] and bellow: #point is in the barrier and comes from side
            direction=False #direction will change
            reflection=False #no reflection
            start_x=x

        if x > barrier[0] and y < barrier[2] and x < barrier[1] and y < barrier[2]and above: #point is in the barrier and comes from top
            direction=True #direction will not change
            reflection=True
            start_y=y
            time_y=time

        if ((x > landing_zone[0] and y < 0) and (x < landing_zone[1] and y < 0)): #getting to the LandingZone
            landing_check=True
            break

        if y < 0:
            break

        tmp_x.append(x)
        tmp_y.append(y)

    return tmp_x,tmp_y,landing_check


for velocity in np.arange(velocity_range[0],velocity_range[1],velocity_range[2]):
    for angle in np.arange(angle_range[0],angle_range[1],angle_range[2]):
        tmp_x=[]
        tmp_y=[]

        tmp_x,tmp_y,landing_check=XYcalc(velocity,angle,0,0,0,time_range[0],time_range[1],time_range[2])

#        if landing_check:
        data_x=data_x+tmp_x
        data_y=data_y+tmp_y


print(pairs)


plt.title('Graf')
plt.plot(data_x, data_y)
plt.plot(line1_x,line1_y,color='red',linewidth=3)
plt.plot(line2_x,line2_y,color='red',linewidth=3)
plt.plot(line3_x,line3_y,color='red',linewidth=3)
plt.show()
