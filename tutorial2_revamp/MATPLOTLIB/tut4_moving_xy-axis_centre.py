
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2.0*np.pi,2.0*np.pi,201)
y = np.sin(x)
z = np.cos(x)

xnum = np.linspace(-7,7,15)
ynum = np.linspace(-1,1,11)


plt.figure(1)
plt.plot(x,y,color=(0.1,0.2,0.5,0.5)) # Can define any color with transparency [RGBA format]
plt.plot(x,z,color=(183/255, 20/255, 169/255, 1)) # RGB normalized + transparency (0 till 1)

plt.axes().spines['bottom'].set_position(('data',0)) # Spines defining the bottom border
plt.axes().spines['left'].set_position(('data',0)) # Spine defining the left border

# plt.axhline(y=-1.0)
plt.axhline(y=plt.ylim()[0],color='k') # adds a horizontal border
plt.axvline(x=plt.xlim()[0],color='k') # adds a vertical border

plt.title('Sin curve')
plt.xlabel('Angle in radians')
plt.ylabel('The Function')
# plt.xticks(xnum)
# plt.yticks(ynum)
plt.legend(['sine','cosine'])
plt.grid()
plt.show()