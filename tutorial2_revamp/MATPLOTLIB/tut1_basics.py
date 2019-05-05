
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# mpl.style.use('default')
# mpl.style.use('classic')
mpl.style.use('bmh')
# mpl.style.use('ggplot')

print(mpl.style.available)

x = np.linspace(0,2.0*np.pi,100)
y = np.sin(x)
z = np.cos(x)

xnum = np.linspace(0,7,15)
ynum = np.linspace(-1,1,11)

plt.figure(1)
plt.plot(x,y,'r',x,z,'g')
plt.title('Sin curve')
plt.xlabel('Angle in radians')
plt.ylabel('The Function')
plt.xticks(xnum)
plt.yticks(ynum)
plt.legend(['sine','cosine'])
plt.grid('on')
plt.axis([0.0,6.5,-1.2,1.2])
plt.show()