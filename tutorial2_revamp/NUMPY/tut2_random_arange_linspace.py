import matplotlib.pyplot as plt

import numpy as np


Z1 = np.random.random((3, 5))

Z2 = np.random.uniform(-5, 5, (3, 5))

print(Z1)
print()
print(Z2)
print()


x = np.arange(-5.00, 5.01, 0.1)

def norm_func(x, mean, var):
    return (1.0/(np.sqrt(2.0*np.pi*var)))*np.exp(-((x-mean)**2)/(2.0*var))



plt.figure(1)
plt.plot(x, norm_func(x, 0.0, 0.2), '-b', label='mean = {}  var = {}'.format(0.0, 0.2))
plt.plot(x, norm_func(x, 0.0, 1.0), '-r', label='mean = {}  var = {}'.format(0.0, 1.0))
plt.plot(x, norm_func(x, 0.0, 5.0), '-y', label='mean = {}  var = {}'.format(0.0, 5.0))
plt.plot(x, norm_func(x, -2.0, 0.5), '-g', label='mean = {}  var = {}'.format(-2.0, 0.5))
plt.legend()
plt.show()

