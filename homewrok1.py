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
m = 50.0 # input for num of time 
x_minus = 0.0 # input of starting point 
x_plus = 10.0 #input of ending point 
r = 5.0 # any given for absolute value of x
c = 5.0 # any constant value 
time = 1.0 #in sec
tau = time/m # the variable "time" divides into num of m
h = (x_plus-x_minus)/n # the  variable "x1 to x2
alpha = (c*tau)/(h*h) # 差分方程式のalpha

y = np.arange(0, time, tau)
x = np.arange(0, x_plus, h)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = Axes3D(fig)

temp_U_n_plus_1 = 0

k = 0
j = x_minus + h

arr_2d = []

#Adding num. of k arrays in the arr2_d to prepared for the 2d array data structure
while k < time:
    arr_2d.append([])
    k = k + tau

arr_2d[0].append((-1)*2*j*(1-j)) #U0 = -U1

while j < x_plus:
    if j < r:
        arr_2d[0].append(2*j*(1-j)) #if Xj < R then u(Xj,0)=f(x) = 2*xj(1-xj)
    else:
        arr_2d[0].append(0) # if Xj >= Rtheb u(Xj,0) = 0
    j = j + h

j = j - h

#setting U_N+1
#if j < r:
#    arr_2d[0].append((-1)*2*(j-h)*(1-(j-h))) #if Xj < R then u(Xj,0)=f(x) = 2*xj(1-xj)
#else:
#    arr_2d[0].append(0) # if Xj >= Rtheb u(Xj,0) = 0
    

k = tau
j = 0
k_counter = 1
j_counter = 0
u_new = 0
temp = 0.

#fixed by multiplying alpha for the third term
while k < time:
    while j < x_plus:
        if j == 0:
            arr_2d[k_counter].append((((-1)*(alpha*arr_2d[(k_counter-1)][(j_counter)]+(1-2*alpha)*arr_2d[(k_counter-1)][(j_counter + 1)]+alpha*arr_2d[(k_counter-1)][j_counter+2]))))
        try:
            arr_2d[k_counter].append(alpha*arr_2d[(k_counter-1)][(j_counter-1)]+(1-2*alpha)*arr_2d[(k_counter-1)][(j_counter)]+alpha*arr_2d[(k_counter-1)][j_counter+1])
        except IndexError:
            break
            #arr_2d[k_counter].append(alpha*arr_2d[(k_counter-1)][(j_counter-2)]+(1-2*alpha)*arr_2d[(k_counter-1)][(j_counter-1)]+alpha*arr_2d[(k_counter-1)][j_counter])
        j = j + h        
        j_counter = j_counter + 1
    j = 0
    j_counter = 0
    k = k + tau
    k_counter = k_counter + 1
    
Z = np.array(arr_2d)
ax.plot_wireframe(X,Y,Z)
print(Z)
plt.show()