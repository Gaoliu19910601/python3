
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

a = ['classic', 'default', 'seaborn', 'grayscale', 'dark_background', 'ggplot']
i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])

x = np.linspace(0, 2.0*np.pi, 100)
x2 = np.linspace(-2.0*np.pi, 2.0*np.pi, 100)
y2 = np.sin(x2)
z2 = np.cos(x2)
y = np.sin(x)
z = np.cos(x)

plt.figure(1)
plt.plot(x, y, 'r', x, z, 'g')
plt.plot(np.pi*0.5, np.sin(np.pi*0.5), 'go')
plt.plot(np.pi*1.5, np.sin(np.pi*1.5), 'go')

plt.annotate('Sine local\n maxima', xy = (np.pi*0.5, np.sin(np.pi*0.5)),
             xytext= (2.5, 0.75),  arrowprops=dict(arrowstyle="->"))
plt.annotate('Sine local\n minima', xy = (np.pi*1.5, np.sin(np.pi*1.5)),
             xytext= (4.5, -0.75),  arrowprops=dict(arrowstyle="->"))

plt.title('Curves')
plt.xlabel('Angle in radians')
plt.ylabel('The Function')
plt.legend(['sine', 'cosine'])
plt.grid('on')
plt.axis([0.0, 6.5, -1.2, 1.2])


plt.figure(2)
plt.plot(x2, y2, 'r')
plt.fill_between(x2, 0, y2)
plt.legend(['sine'])
plt.title('Sine Curve')
plt.xlabel('Angle in radians')
plt.ylabel('The Function')
plt.grid('on')


plt.figure(3)
plt.plot(x2, y2, 'r', x2, z2, 'b')
# plt.fill_between(x2, y2, z2, color='orange', alpha=0.4)
# plt.fill_between(x2[20:41], y2[20:41], z2[20:41], color='orange', alpha=0.6)
plt.fill_between(x2,y2,z2, where=(y2>=z2),color='green',interpolate=True,alpha=0.5)
plt.fill_between(x2,y2,z2, where=(y2<=z2),color='red',interpolate=True,alpha=0.5)
plt.legend(['sine'])
plt.title('Sine Curve')
plt.xlabel('Angle in radians')
plt.ylabel('The Function')
plt.grid('on')
plt.show()