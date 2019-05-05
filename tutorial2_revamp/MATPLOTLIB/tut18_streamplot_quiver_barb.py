
import numpy as np
import matplotlib.pyplot as plt


def vanderpol(x, y, mu):
    u = mu*(x-(x**3/3)-y)
    v = x/mu
    return u, v



mu = 0.5

l = 8
n = 101

X1, X2 = np.meshgrid(np.linspace(-l, l, n), np.linspace(-l, l, n))

U, V = vanderpol(X1, X2, mu)

resultant_vel = (U**2+V**2)**0.5

# print(U)
# print(V)

plt.figure(1)
strm = plt.streamplot(X1,  X2,  # x and y coord positions
               U,  V,    # velocities
               color='xkcd:azure',
               density=1,   # density of arrows in the x and y direction
               arrowsize=2,  # size of arrows
               arrowstyle='->',  # arrow style
               linewidth=1,
               cmap=plt.cm.jet
                      )

# plt.colorbar(strm)
plt.title('Vander Pol Oscillator')
plt.xlabel('X-Position')
plt.ylabel('Y-Position')
plt.grid(True)

# plt.show()


slice_interval = 6

skip = (slice(None, None, slice_interval), slice(None, None, slice_interval))


plt.figure(2)
QUIVER = plt.quiver(X1[skip],  X2[skip],  # x and y coord positions
               U[skip],  V[skip],    # velocities
                resultant_vel[skip],
               units='height',
               angles='uv',   # density of arrows in the x and y direction
               scale=250,  # size of arrows
               pivot='mid',  # arrow style
               color='b',
               # cmap=plt.cm.jet
               # cmap=plt.cm.gist_heat_r
               cmap=plt.cm.seismic
                )

plt.quiverkey(QUIVER, 1.01, 1.01, 10, label='10 m/s', labelcolor='blue', labelpos='N', coordinates='axes')
plt.colorbar(QUIVER)
plt.title('Vander Pol Oscillator')
plt.xlabel('X-Position')
plt.ylabel('Y-Position')
plt.grid(True)

# plt.show()


plt.figure(3)
BARB = plt.barbs(X1[skip],  X2[skip], U[skip],  V[skip], resultant_vel[skip],
                 pivot='tip', cmap=plt.cm.jet, barb_increments={'half':10,  'full':20,  'flag':50})
# plt.colorbar(BARB)
plt.title('Vander Pol Oscillator - barb plot')
plt.xlabel('X-Position')
plt.ylabel('Y-Position')
plt.grid(True)

plt.show()