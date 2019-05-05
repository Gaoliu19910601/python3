import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
a = ['classic', 'default', 'seaborn', 'grayscale', 'dark_background', 'ggplot']
i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])

n = 201

x = np.linspace(0, 4.0*np.pi, n)

y1= np.sin(x)
y2 = np.cos(x)

y = y1+y2

# opening a figure

plt.figure()
plt.subplot(311)
plt.plot(x, y1, '--b', label='sine')
plt.title('Curves')
# plt.xlabel('Angle')
plt.ylabel('Magnitude')
plt.legend()

plt.subplot(312)
plt.plot(x, y2, '-r', label='cos')
# plt.title('Cosine curve')
# plt.xlabel('Angle')
plt.ylabel('Magnitude')
plt.legend()

plt.subplot(313)
plt.plot(x, y, ':g', label='cos+sin')
# plt.title('Total curve')
plt.xlabel('Angle')
plt.ylabel('Magnitude')
plt.legend()

plt.tight_layout()

plt.show()
