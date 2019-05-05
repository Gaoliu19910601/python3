import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

n1 = 101
n2 = 51

x1 = np.linspace(0,2*np.pi,n1)
x2 = np.linspace(0,2*np.pi,n2)

X1,X2 = np.meshgrid(x1,x2)

Z = np.sin(X1)*np.cos(X2)

breaks = np.linspace(-1,1,11) # values along which contours need to be drawn

plt.rcParams['contour.negative_linestyle'] = 'solid' # To override the dashed lines in the contour

plt.figure(1)
CS1 = plt.contour(x1,x2,Z,
                   breaks,
                  # cmap='seismic',
                  colors='k',
                  # extend='both',vmin=-1.0,vmax=1.0, # To create the cap on the colorbar and mention the maxmin values
                  # colors = ['k','c','b','r','y','m','orange','chocolate','grey'],
                  )
CS2 = plt.contourf(x1,x2,Z,
                   breaks,
                    cmap='Greys', # check cmap options for more colors
                    # cmap='jet',
                    # cmap='siesmic',
                  # colors='k',
                  extend='both',vmin=-1.0,vmax=1.0, # To create the cap on the colorbar and mention the maxmin values
                   # colors = ['k','c','b','r','y','m','orange','chocolate','grey'],
                  )
plt.colorbar(ticks=breaks,orientation='vertical')
plt.clabel(CS1,inline=1,fontsize=10)

plt.xlabel('Angle in radians')
plt.ylabel('Angle in radians')
plt.title('Sine cosine wave')
plt.grid(True)
# plt.show()




fig = plt.figure(2)
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X1, X2, Z, cmap='Greys',
                       linewidth=0, antialiased=False)
# surf = ax.plot_surface(X1, X2, Z)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()





fig = plt.figure(3)
ax2 = fig.gca(projection='3d')
cset = ax2.contourf(X1, X2, Z, cmap=cm.coolwarm)
ax2.clabel(cset, fontsize=9, inline=1)



fig = plt.figure(4)
ax3 = fig.gca(projection='3d')
cset = ax3.contour(X1, X2, Z, extend3d=True, cmap=cm.coolwarm)
ax3.clabel(cset, fontsize=9, inline=1)

plt.show()


