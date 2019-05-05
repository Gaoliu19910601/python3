import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 10
n = 11

x = np.linspace(a, b, n)
y = x[::-1]

xerr = np.random.rand(n)
yerr = np.random.rand(n)


plt.errorbar(x, y,
             xerr=xerr,
             yerr = yerr,
             label='trend',
             fmt='.',
             color='g',
             ecolor='xkcd:salmon',
             elinewidth=1.5,
             capsize=2,
             capthick=1,
             barsabove=True,
             errorevery=1)
plt.xlabel('Angle in radians')
plt.ylabel('magnitude')
plt.title('Error function')
plt.xticks()
plt.yticks()
plt.legend()
plt.show()