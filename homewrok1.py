# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def f_of_x(j, r, h, length):
    if abs(j) < r:
        """if j == 0:
            j = j + h
        elif j == length:
            j = j - h"""
        return 2*j*(1-j) + 900
    return 0
    
def calc(u,j,r,alpha):
    if j == 0:
        return 0#(-1)*(alpha*u[j]+(1-2*alpha)*u[(j+1)]+alpha*u[j+2])
    elif j == (len(u) - 1):
        return 0#(-1)*(alpha*u[j-2]+(1-2*alpha)*u[(j-1)]+alpha*u[j])
    return alpha*u[j-1]+(1-2*alpha)*u[j]+alpha*u[j+1]

def create_data(x_minus, x_plus, n, m, time, c, r ):
    tau = time/m # the variable "time" divides into num of m
    h = (x_plus-x_minus)/n # the  variable "x1 to x2
    alpha = (c*tau)/(h*h) # 差分方程式のalpha

    y = np.arange(0, time, tau)
    x = np.arange(x_minus-0.5*h, x_plus+1.5*h, h)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = Axes3D(fig)
    arr_2d = []
    
    for i in X:
        arr_2d.append(x)

    Z = np.array(arr_2d)

    for i, s in enumerate(Z[0]):
        Z[0][i] = f_of_x(s,r,h,len(Z[0]))

    for i, s in enumerate(Z):
        if i != 0:
            for l, k in enumerate(s):
                Z[i][l] = calc(Z[i-1],l,r,alpha)

    ax.plot_wireframe(X,Y,Z)
    plt.show()


create_data(20.0, -20.0, 20.0, 2000.0, 120, 5, 10)