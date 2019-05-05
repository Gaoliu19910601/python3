
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


a = ['classic','default']

i=1 # 0 - classic and 1 - default


mpl.style.use(a[i])

N = 1000
x = np.linspace(-2*np.pi,2*np.pi,N)


y = np.random.normal(0,1,N)+np.sin(x)

plt.figure(1)
plt.scatter(x,y,edgecolor='black',facecolor='blue',s = 60,alpha=0.5,marker='p',label='sine',linewidth=1.5)
plt.legend()
plt.xlabel('Angle')
plt.ylabel('Function')
plt.title('Sine wave with pure random variance')
plt.show()

