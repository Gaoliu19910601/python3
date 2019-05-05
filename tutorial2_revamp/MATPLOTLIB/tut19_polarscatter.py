import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
a = ['classic', 'default', 'seaborn', 'grayscale', 'dark_background', 'ggplot']
i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])

n = 101
n_bar=11

theta = np.linspace(0.0, 2.0*np.pi, n)
theta2 = np.linspace(0, 2*np.pi, n_bar)

curve1 = np.linspace(0.0, 1.0, n)
curve2 = curve1 + 0.10*np.random.uniform(-1.0, 1.0, n)
curve3 = np.random.random(n)
curve4 = np.random.rand(n_bar)


plt.figure(1)
ax1 = plt.subplot(111, polar=True)
# ax1.plot(theta, curve1, color='xkcd:salmon', label='curve1')
# ax1.scatter(theta, curve2, c='k', label='curve2')
ax1.scatter(theta, curve3,
            c=curve3,
            label='curve3',
            alpha=0.7,
            edgecolor='k',
            s = 400*np.abs(curve3),
            cmap = plt.cm.seismic)
ax1.set_title('Polar chart')
# ax1.legend()
ax1.set_ylim(0, 1.5)
ax1.set_yticks(np.linspace(0.0, 1.5, 4))
ax1.set_xticks(np.linspace(0, 2*np.pi, 17)[:-1])


plt.figure(2)
plt.plot(theta, curve1)
plt.scatter(theta, curve2)
plt.scatter(theta, curve2+0.5)




plt.figure(3)
ax2 = plt.subplot(111, polar=True)

ax2.bar(theta2, curve4,
            width=curve4,
            bottom = 0,
            label='curve4',
            alpha=0.7,
            edgecolor='k',
            color = plt.cm.jet(curve4)
        )
plt.title('Polar bar plot')
plt.grid(True)
plt.show()
