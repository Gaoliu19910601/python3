import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


M = 1.5

pc = 100

x1 = np.linspace(0.0,100.0,101)
y1 = np.linspace(0.0,100.0,101)
z1 = np.linspace(0.0,100.0,101)


x_yield = []
y_yield = []
z_yield = []


for x in x1:
    for y in y1:
        for z in z1:
            qsquare = x**2+y**2+z**2-x*y-y*z-z*x
            p = (x+y+z)/3.0
            F = qsquare-M*M*p*(pc-p)
            if  F == 0.0:
                x_yield.append(x)
                y_yield.append(y)
                z_yield.append(z)



fig = plt.figure(2)
ax = fig.gca(projection='3d')
surf = ax.plot(x_yield, y_yield, z_yield,'bo')
ax.plot([0,pc+10],[0,pc+10],[0,pc+10],'-r',linewidth=2.0)
plt.show()

# plt.figure(3)
# plt.plot(x_yield,y_yield,'bo')
# plt.show()

