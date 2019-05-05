
import matplotlib.pyplot as plt
import numpy as np


y = np.linspace(0, 2.0*np.pi, 100)
x1 = np.sin(y)
x2 = np.sinh(y)

ynum = np.linspace(0, 7, 15)
x1num = np.linspace(-1, 1, 11)
x2num = np.linspace(0, 300, 11)


fig, ax1 = plt.subplots()

ax2 = ax1.twiny()

curve1,  = ax1.plot(x1, y, 'r', label='Sin')

curve2,  = ax2.plot(x2, y, 'b', label='Sinh')

curves = [curve1,  curve2]
# ax1.legend() # gives a separate legend for the ax1 handle
# ax2.legend()

# ax1.legend(curves, [amar.get_label() for amar in curves])
ax2.legend(curves, [amar.get_label() for amar in curves])

ax1.set_ylabel('Angle/value', color=curve1.get_color())
# ax2.set_ylabel('Angle/value', color=curve2.get_color())

ax1.set_xlabel('Magnitude', color=curve1.get_color())
ax2.set_xlabel('Magnitude', color=curve2.get_color())

ax1.tick_params(axis='x', colors=curve1.get_color())
ax1.tick_params(axis='y', colors=curve1.get_color())
ax2.tick_params(axis='x', colors=curve2.get_color())
# ax2.tick_params(axis='y', colors=curve2.get_color()) # This will not work

ax1.set_yticks(ynum)
ax1.set_xticks(x1num)
ax2.set_xticks(x2num)

# ax1.grid() # grid corresponding to first axis
# ax1.grid(color=curve1.get_color())


# grid corresponding to second axis
ax1.grid(color=curve1.get_color())
ax2.grid(color=curve2.get_color())
ax1.xaxis.grid(False)



# plt.grid('on') # gives a weird grid
plt.xlabel('Angle in radians')
plt.ylabel('The Function')
# plt.title('Two curves')

plt.show()




