
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

a = ['classic', 'default', 'seaborn', 'grayscale', 'dark_background', 'ggplot']
i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])

radii = np.linspace(0.5, 1, 10)
thetas = np.linspace(0, 2*np.pi, 20)
theta,  r = np.meshgrid(thetas,  radii)

dr = 1
dt = 1

f = plt.figure(1)
ax = f.add_subplot(111,  polar=True)
ax.quiver(theta,  r,  dr * np.cos(theta) - dt * np.sin(theta),  dr * np.sin(theta) + dt * np.cos(theta))



plt.figure(2)

plt.plot(theta, r)


f2 = plt.figure(3)

ax2 = f2.add_subplot(111, polar=True)
ax2.plot(theta, r)
plt.show()