import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt

x = np.linspace(-4.0,4.0,9)
y = np.linspace(-4.0,4.0,9)

x1,y1 = np.meshgrid(x,y)

z1 = x1**2+y1**2

xi = np.linspace(-4.0,4.0,17)
yi =  np.linspace(-4.0,4.0,17)

x2,y2 = np.meshgrid(xi,yi)

tck = interpolate.bisplrep(x1,y1,z1,s=1)

z2 = interpolate.bisplev(xi,yi,tck)

plt.figure(1)
plt.subplot(211)
plt.contourf(x1,y1,z1)
plt.title('Without Z regridding')
plt.subplot(212)
plt.contourf(x2,y2,z2)
plt.title('With Z regridding')
plt.show()

