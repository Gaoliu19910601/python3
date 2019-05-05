import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,2*np.pi,100)

y = np.sin(2*x)
y1 = np.gradient(y,x[1]-x[0])
y2 = np.gradient(y1,x[1]-x[0])


plt.plot(x,y,'-b',label='sin2x')
plt.plot(x,y1,'-g',label='2*cos2x')
plt.plot(x,y2,'-r',label='-4*sin2x')
plt.grid('on')
plt.legend(framealpha=0.0)
plt.show()
