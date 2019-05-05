import numpy as np
import matplotlib.pyplot as plt


x_myval = np.linspace(-6,6,1000)


def f(x):
    return (np.exp(x))

def f2(x):
    return 789

def f3(x):
    return ((27*12*x**2)-(4*x**6))/(((x**4)+27)**2)

def f4(x):
    return 2*np.e*x-np.e

def f5(x):
    return x**2-4*x

def f6(x):
    return 2*x-8

a = []
a.append()

for i in range(0,100):




y = f(x_myval)
y2 = f2(x_myval)
y3 = f3(x_myval)
y4 = f4(x_myval)
y5 = f5(x_myval)
y6 = f6(x_myval)


plt.figure(1)
plt.plot(x_myval,y,'-r',lw=2)
plt.plot(x_myval,y2,'-b',lw=1)
# plt.plot(x_myval,y3,'-k',lw=1)
# plt.plot(x_myval,y4,'-g',lw=1)
# plt.plot(x_myval,y5,'-m',lw=1)
# plt.plot([2,4],[-4,0],'--m',lw=2)
# plt.plot(x_myval,y6,'-b',lw=1)
# plt.plot([1.0-(1.0/3.0),1.0-(1.0/3.0)],[-20,20],'-m',lw=1)
# plt.plot([1.0+(1.0/3.0),1.0+(1.0/3.0)],[-20,20],'-m',lw=1)
# plt.plot([-20,20],[2,2],'-m',lw=1)
# plt.plot([-20,20],[4,4],'-m',lw=1)
plt.grid('on')
plt.axis([-7.5,7.5,-2.5,2.5])
plt.show()