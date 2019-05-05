import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

x = np.linspace(0,2*np.pi,100)
y = np.sin(x) + np.random.random(100) * 0.2
lowess = sm.nonparametric.lowess(y, x, frac=0.1)

plt.plot(x, y,'+',label='Random Sine function')
plt.plot(lowess[:, 0], lowess[:, 1],label='Smoothed curve')
plt.xlabel('Angle in radians',fontweight='bold')
plt.ylabel('Sine value',fontweight='bold')
plt.legend()
plt.savefig('lowess.png',format='png',dpi=600)
# plt.show()