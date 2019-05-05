import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


M = 1.0
alpha0 = 0.5

alpha3 = 1.0+(2.0*alpha0/3.0)
alpha1 = 1.0-(alpha0/3.0)
alpha2 = 1.0-(alpha0/3.0)

pc = 100.0

x1 = np.linspace(0.0,100.0,201)
y1 = np.linspace(0.0,100.0,201)
z1 = np.linspace(0.0,200.0,201)

x_yield = []
y_yield = []
z_yield = []

for x in x1:
    for y in y1:
        for z in z1:
            p = (x + y + z) / 3.0
            qsquare = (3.0/2.0)*((x-alpha1*p)**2+(y-alpha2*p)**2+(z-alpha3*p)**2)
            F = (qsquare/(M**2-alpha0**2))+(p-0.5*pc)**2-(pc/2.0)**2
            if F == 0.0:
                x_yield.append(x)
                y_yield.append(y)
                z_yield.append(z)


fig = plt.figure(2)
ax = fig.gca(projection='3d')
surf = ax.plot(x_yield, y_yield, z_yield,'bo')
ax.plot([0,pc+10],[0,pc+10],[0,pc+10],'-r',linewidth=2.0)
# ax.plot([0,pc],[0,pc],[0,pc],'-r',linewidth=2.0)
plt.show()


