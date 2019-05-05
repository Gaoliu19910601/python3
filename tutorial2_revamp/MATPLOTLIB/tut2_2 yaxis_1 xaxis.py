
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2.0*np.pi, 100)
y = np.sin(x)
z = np.sinh(x)

xnum = np.linspace(0, 7, 15)
ynum = np.linspace(-1, 1, 11)
znum = np.linspace(0, 300, 11)


fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

curve1,  = ax1.plot(x, y, 'r', label='Sin')

curve2,  = ax2.plot(x, z, 'b', label='Sinh')

curves = [curve1,  curve2]
# ax1.legend() # gives a separate legend for the ax1 handle
# ax2.legend()

# ax1.legend(curves, [amar.get_label() for amar in curves])
ax2.legend(curves, [amar.get_label() for amar in curves])

ax1.set_xlabel('Angle/value', color=curve1.get_color())
# ax2.set_xlabel('Angle/value', color=curve2.get_color()) # Does not print since it does not have control over the x axis since it is just a twin of ax1

ax1.set_ylabel('Magnitude', color=curve1.get_color())
ax2.set_ylabel('Magnitude', color=curve2.get_color())

ax1.tick_params(axis='y', colors=curve1.get_color())
ax1.tick_params(axis='x', colors=curve1.get_color())
ax2.tick_params(axis='y', colors=curve2.get_color())
ax2.tick_params(axis='x', colors=curve2.get_color()) # This will not work

ax1.set_xticks(xnum)
ax1.set_yticks(ynum)
ax2.set_yticks(znum)

# ax1.grid() # grid corresponding to first axis
# ax1.grid(color=curve1.get_color())


# grid corresponding to second axis
ax2.grid()
ax1.grid()
ax1.yaxis.grid(False)



# plt.grid('on') # gives a weird grid
plt.xlabel('Angle in radians')
plt.ylabel('The Function')
plt.title('Two curves')

plt.show()




