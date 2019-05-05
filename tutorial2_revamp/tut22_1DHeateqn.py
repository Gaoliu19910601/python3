from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np


L = 100
T = 500

nx = 101
nt = 1001

t = np.linspace(0, T, nt)
x = np.linspace(0, L, nx)

dx = x[2]-x[1]
dt = t[2]-t[1]

print(dx, dt)

alpha = 0.61

F = alpha*dt/dx**2

u = np.zeros((nt, nx))

print(len(u[0, :]))
print(len(x))

u[0, :] = np.sin(2*np.pi*x/L)


for i in range(0, nt-1):
    u[i+1, 1:-1] = (1-2*F)*u[i, 1:-1] + F*(u[i, 0:-2]+u[i, 2:])


plt.figure(1)
plt.plot(x, u[0, :])
plt.plot(x, u[200, :])
plt.plot(x, u[400, :])
plt.plot(x, u[600, :])
plt.plot(x, u[800, :])
plt.plot(x, u[1000, :])
plt.grid(True)
plt.show()