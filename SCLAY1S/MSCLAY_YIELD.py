import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


Mc = 1.5
Me = 1.1
m = Me/Mc

alpha0 = 0.5

alpha3 = 1.0+(2.0*alpha0/3.0)
alpha1 = 1.0-(alpha0/3.0)
alpha2 = 1.0-(alpha0/3.0)

pc = 100.0

x1 = np.linspace(0.0,100.0,501)
y1 = np.linspace(0.0,100.0,501)
z1 = np.linspace(0.0,200.0,501)

x_yield = []
y_yield = []
z_yield = []


for x in x1:
    for y in y1:
        for z in z1:
            p = (x + y + z) / 3.0

            J2_alpha = 0.5*((x-alpha1*p)**2+(y-alpha2*p)**2+(z-alpha3*p)**2)

            J3_alpha = (x-alpha1*p)*(y-alpha2*p)*(z-alpha3*p)

            # print(J2_alpha,J3_alpha)

            sin3theta = 2.6*(J3_alpha/J2_alpha**(3.0/2.0))

            M_theta = Mc*((2.0*(m**4))/(1.0+m**4+(1.0-m**4)*sin3theta))**(1.0/4.0)

            qsquare = (3.0/2.0)*((x-alpha1*p)**2+(y-alpha2*p)**2+(z-alpha3*p)**2)
            F = (qsquare/(M_theta**2-alpha0**2))+(p-0.5*pc)**2-(pc/2.0)**2

            if F <= 0.01 and F >= -0.01:
                x_yield.append(x)
                y_yield.append(y)
                z_yield.append(z)

# print(x_yield)
# print(y_yield)
# print(z_yield)

fig = plt.figure(2)
ax = fig.gca(projection='3d')
surf = ax.plot(x_yield, y_yield, z_yield,'bo')
ax.plot([0,pc+10],[0,pc+10],[0,pc+10],'-r',linewidth=2.0)
# ax.plot([0,pc],[0,pc],[0,pc],'-r',linewidth=2.0)
plt.show()


