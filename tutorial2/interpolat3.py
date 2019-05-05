import numpy as np
from scipy.integrate.quadpack import quad
from scipy.optimize.minpack import fsolve
import matplotlib.pyplot as plt


# b = 5.0

x = np.linspace(0.0,10.0,200)

def func(x):
    return np.array(x**2)

integral,err = quad(func,1,15)

print('integral:',integral)
print('error:',err)

section = np.linspace(1,15,20)

plt.plot(x,func(x))
plt.fill_between(section,func(section),facecolor='r')
plt.show()
