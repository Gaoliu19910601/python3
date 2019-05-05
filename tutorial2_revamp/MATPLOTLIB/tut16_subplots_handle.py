import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
a = ['classic', 'default', 'seaborn', 'grayscale', 'dark_background', 'ggplot']
i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])

n = 101

x = np.linspace(0, 4.0*np.pi, n)

y1= np.sin(x)
y2 = np.cos(x)
r = np.random.random(n)


# create a figure handle
# fig = plt.figure(figsize=(10, 8)) # default size is 8 x 6 inches
fig = plt.figure()

# now start adding subplots
ax1 = fig.add_subplot(121)
ax1.scatter(x, r, edgecolor='None', facecolor='red', s=80, alpha=0.5, label='Random')
ax1.set_title('Randomised')
ax1.set_xlabel('Magnitude', color='red')
ax1.set_ylabel('Random values', color='red')
ax1.tick_params(axis='x', colors='grey')
ax1.tick_params(axis='y', colors='grey')
ax1.grid(True)
ax1.legend()

ax2 = fig.add_subplot(322)
ax2.plot(x, y1, '-b', alpha=0.9, label='Sine')
ax2.set_title('Sine curve')
ax2.set_xlabel('Angle', color='black')
ax2.set_ylabel('Function', color='black')
ax2.grid(True)
ax2.legend()

ax3 = fig.add_subplot(324)
ax3.plot(x, y2, '--r', alpha=0.9, label='Cosine')
ax3.set_title('Cosine curve')
ax3.set_xlabel('Angle', color='black')
ax3.set_ylabel('Function', color='black')
ax3.grid(True)
ax3.legend()

ax4 = fig.add_subplot(326)
ax4.plot(x, y1+y2, ':g', alpha=0.9, label='Total')
ax4.set_title('Added curve')
ax4.set_xlabel('Angle', color='black')
ax4.set_ylabel('Function', color='black')
ax4.grid(True)
ax4.legend()

plt.tight_layout()

plt.suptitle('Collection of Crap', fontweight='bold', fontsize=16)
plt.savefig('Collection.jpg', format='jpg', dpi=600, bbox_inches='tight')
plt.show()