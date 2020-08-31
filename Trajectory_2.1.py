import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Gravity_Acc = 9.81  # gravity accleration
DataX = []
DataY = []
Pairs = np.array([("Angle", "Velocity")])
Direction = True

barrier = [75, 100, 300]
landing_zone = [50, 70, 0]
velocity_range = [80, 100, 1]
angle_range = [85, 90, 1]
time_range = [0, 50, 0.1]  # StartTime,EndTime,Step


def f_x(a, c, t):
    x = a * t + c
    print("x=", x)
    return x


def f_y(a, b, c, t):
    y = a * t ** 2 + b * t + c
    print("y=", y)
    return y


def trajectory(t1, t2, time_step, a1, c1, a2, b2, c2, barrier_hit):
    x_val = []
    y_val = []
    t = t1
    ground_hit = False
    while barrier_hit == False or ground_hit == False:
        x = f_x(a1, c1, t)
        y = f_y(a2, b2, c2, t)
        x_val.append(x)
        y_val.append(y)
        print("x_val:", x_val)
        print("y_val:", y_val)
        if y < 0:
            ground_hit == True
            #            y_grad=x_val[-1]-x_val[]
            break
        t = t + time_step
    return x_val, y_val, ground_hit, barrier_hit


v = 20
angle = 20
t1 = 0
t2 = 200
time_step = 1
data_x = []
data_y = []

v_x = v * np.cos(angle)
v_y = v * np.sin(angle)

ground_hit = False
barrier_hit = False

data_x, data_y, ground_hit, barrier_hit = trajectory(t1, t2, time_step, v_x, 0, -1 / 2 * 10, v_y, 20, barrier_hit)

plt.title('Graf')
plt.plot(data_x, data_y)
# plt.plot(Line1X,Line1Y,color='red',linewidth=3)
# plt.plot(Line2X,Line2Y,color='red',linewidth=3)
# plt.plot(Line3X,Line3Y,color='red',linewidth=3)
plt.show()
