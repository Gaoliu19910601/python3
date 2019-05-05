import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

a = ['classic', 'default', 'seaborn', 'grayscale', 'dark_background', 'ggplot']
i=1 # 0 - classic and 1 - default

mpl.style.use(a[i])

Rmin = 0.0
Rmax = 4.0

Theta_min = 0.0
Theta_max = 2.0*np.pi

n = 21

radius = np.linspace(Rmin, Rmax, n)
Theta = np.linspace(Theta_min, Theta_max, n)

theta_matrix, radius_matrix = np.meshgrid(Theta, radius)

U, V = np.ones((n, n)), np.ones((n, n))
# U, V = radius_matrix*(1.0-radius_matrix**2)*(4-radius_matrix**2), 2.0-radius_matrix**2

resultant_vel = (U**2+(V*radius_matrix)**2)**0.5

# Linewidth parameter

lw = 3*resultant_vel/np.max(resultant_vel)

plt.figure(1)

ax1 = plt.subplot(111, polar=True)

# transverse coord, radial coord, transverse velocity,  radial velocity
stream = ax1.streamplot(theta_matrix, radius_matrix, V, U,
                        # color=resultant_vel,
                        color='xkcd:azure',
                        arrowsize=2,
                        arrowstyle='->',
                        density=1,
                        # linewidth=lw,
                        # cmap=plt.cm.jet
                        )
# plt.colorbar(stream.lines)
ax1.set_ylim(Rmin, Rmax)
ax1.set_rlabel_position(135)
ax1.legend(['Polar stream'])



plt.figure(2)
ax2 = plt.subplot(111, polar=True)
quiver = ax2.quiver(theta_matrix, radius_matrix, U*np.cos(theta_matrix)-V*np.sin(theta_matrix), U*np.sin(theta_matrix)+V*np.cos(theta_matrix))



plt.figure(3)
plt.quiver(theta_matrix, radius_matrix,V,U)
plt.show()