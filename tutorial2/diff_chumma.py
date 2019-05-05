import numpy as np
import matplotlib.pyplot as plt
from sympy import *


x_myval = np.linspace(1,10,100)


x = Symbol('x')

y = (20*x**2)+(180/x)

def y_plot(x1):
 return (20*x1**2)+(180/x1)


yprime = y.diff(x)
yprime2 = yprime.diff(x)

print(y)
print(yprime)
print(yprime2)


f = lambdify(x, yprime, 'numpy')
f2 = lambdify(x,yprime2,'numpy')



plt.figure(1)
plt.plot(x_myval,y_plot(x_myval),'-r',lw=1)
plt.plot(x_myval,f(x_myval),'-b',lw=1)
plt.plot(x_myval,f2(x_myval),'-k',lw=1)
# plt.plot([-10,10],[0,0],'--m',lw=1)
# plt.plot([0,0],[-600,600],'--m',lw=1)
plt.grid('on')
plt.show()
