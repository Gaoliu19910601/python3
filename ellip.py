

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def Main():
    phi = np.linspace(0, 2*np.pi)
    theta = np.linspace(-np.pi/2, np.pi/2)
    phi, theta=np.meshgrid(phi, theta)

    x = np.cos(theta) * np.sin(phi) * 3
    y = np.cos(theta) * np.cos(phi) * 2
    z = np.sin(theta)

    fig = plt.figure(2)
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x, y, z)
    plt.show()

if __name__ == "__main__":

     Main()

     print("Program is activated")
