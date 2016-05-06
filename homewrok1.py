# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#changed the input
n = 10.0 # input for num of x
m = 20.0 # input for num of time 
x_minus = -10.0 # input of starting point 
x_plus = 10.0 #input of ending point 
r =100 # any given for absolute value of x
c = 5.0 # any constant value 
time = 4 #in sec
tau = time/m # the variable "time" divides into num of m
h = (x_plus-x_minus)/n # the  variable "x1 to x2
alpha = (c*tau)/(h*h) # 差分方程式のalpha

y = np.arange(0, time, tau)
x = np.arange(x_minus, x_plus+h, h)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = Axes3D(fig)

k = 0
j = x_minus 

arr_2d = []

#arr_2d[0].append((-1)*2*j*(1-j)) #U0 = -U1

def f_of_x(j, r, h, length):
    if abs(j) < r:
        if j == 0:
            j = j + h
        elif j == length:
            j = j - h
        return 2*j*(1-j)
    return 0
    
def calc(u,j,r,alpha):
    if abs(j) < r:
        if j == 0:
            return (-1)*(alpha*u[j]+(1-2*alpha)*u[(j+1)]+alpha*u[j+2])
        elif j == (len(u) - 1):
            return (-1)*(alpha*u[j-2]+(1-2*alpha)*u[(j-1)]+alpha*u[j])
        return alpha*u[j-1]+(1-2*alpha)*u[j]+alpha*u[j+1]
    return 0

while k < time:
    arr_2d.append(x)
    k = k + tau

Z = np.array(arr_2d)
print(Z)
for i, s in enumerate(Z[0]):
    Z[0][i] = f_of_x(s,r,h,len(Z[0]))

for i, s in enumerate(Z):
    if i != 0:
        for l, k in enumerate(s):
            Z[i][l] = calc(Z[i-1],l,r,alpha)

print(Z)

ax.plot_wireframe(X,Y,Z)
plt.show()
