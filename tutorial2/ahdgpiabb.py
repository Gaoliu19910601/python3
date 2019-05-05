# matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x, y):
    return (1.0/8.0)*((1296.0/y)-(3.0*x))

x = np.linspace(1, 60, 30)
y = np.linspace(1, 60, 30)
z = np.linspace(1, 60, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

X2,Y2,Z2 = np.meshgrid(x,y,z)

fig = plt.figure()
ax = Axes3D(fig)
ax.contour3D(X2,Y2,Z2, 50, cmap='binary')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                 cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
plt.show()


# u=[]
# v = []
#
# for j in range(0,len(x)):
#     u.append(x**2-3*x+2)
#     v.append(y**2-3*y+2)
#
# plt.quiver(x,y,u,v)
# plt.show()