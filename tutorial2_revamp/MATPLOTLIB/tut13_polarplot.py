
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

a = ['classic', 'default', 'seaborn', 'grayscale', 'dark_background', 'ggplot']
i=4 # 0 - classic and 1 - default

mpl.style.use(a[i])

n = 1001
no_of_cycles = 1
f = np.pi
r = 5

theta = np.linspace(0, 2*no_of_cycles*np.pi, n)
func = r*np.cos(f*theta)
func2 = r*np.sin(f*theta)

plt.figure(1)
plt.plot(theta*180/np.pi, func, '-b', lw=1, label='cos curve')
plt.plot(theta*180/np.pi, func2, '-r', lw=1, label='sin curve')
plt.title('Curves for f = {} & r = {}'.format(f, r))
plt.xlabel('Theta (degrees)')
plt.ylabel('The Function')
# plt.xticks([0, 45, 90, 135, 180, 225, 270, 315, 360])
plt.grid(True)


plt.figure(2)
ax2 = plt.subplot(111, polar=True)
ax2.plot(theta, func, '-b', label='cos curve')
ax2.plot(theta, func2, '-r', label='sin curve')
ax2.set_yticks(np.linspace(-7, 7, 8))
ax2.set_xticks(np.linspace(0, 2*np.pi, 17)[:-1])
plt.title('Rose plot')
plt.grid(True)
plt.legend()
plt.show()
