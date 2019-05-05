import matplotlib.pyplot as plt

import numpy as np


x = np.arange(-4.0, 5.0, 1)
y = np.arange(-5.0, 6.0, 1)

print(x)
print(y)

xx,  yy = np.meshgrid(x, y)
xx1, yy1 = np.meshgrid(x, y, indexing='ij')

print(xx)
print(xx.shape)

print(np.all(xx == xx1.T)) # Check whether they are transpose to each other

Z1 = xx**2 + 4.0*yy**2

Z2 = np.random.random((11, 9))





plt.figure(1)
plt.contourf(xx, yy, Z1, cmap='jet')
plt.colorbar()
# plt.show()


plt.figure(2)
plt.contourf(xx, yy, Z2, cmap='jet')
plt.colorbar()
plt.show()