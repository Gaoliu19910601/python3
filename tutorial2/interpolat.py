import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

mat1 = {}

x = np.arange(0.0,10.0)
y = np.exp(-x/3.0)

f = interpolate.interp1d(x,y)

x1 = np.linspace(0.0,9.0,1000)
y1 = f(x1)

mat1['x'] = x
mat1['y'] = y

# plt.plot(x,y,'ro',x1,y1,'-b')


x2 = np.arange(-5.01,5.01,0.25)
y2 = np.arange(-5.01,5.01,0.25)

xx,yy = np.meshgrid(x2,y2) # Generates a 2D mesh

zz = xx**2+yy**2

f2 = interpolate.interp2d(xx,yy,zz,kind='quintic') #kind cubic throws from BVL errors

x3 = np.arange(-5.01,5.01,0.05)
y3 = np.arange(-5.01,5.01,0.05)

z3 = f2(x3,y3)

mat1['x3'] = x3
mat1['y3'] = y3
mat1['z3'] = z3

plt.figure(2)
plt.contourf(xx,yy,zz)

plt.figure(3)
plt.contourf(x3,y3,z3)
plt.show()