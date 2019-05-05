from netCDF4 import Dataset as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib

file = 'ncfile2.nc'

ncfile = dt(file,'r')

# print(ncfile.variables)

lat = np.array(ncfile.variables['latitude'][:],dtype=np.float32)
lon = np.array(ncfile.variables['longitude'][:],dtype=np.float32)
time = np.array(ncfile.variables['time'][:],dtype=np.int32)
u10 = np.array(ncfile.variables['u10'][:],dtype=np.float32)
v10 = np.array(ncfile.variables['v10'][:],dtype=np.float32)
t2m = np.array(ncfile.variables['t2m'][:],dtype=np.float32)
al = np.array(ncfile.variables['al'][:],dtype=np.float32)

# print(u10)

us = np.linspace(-20,20,11,endpoint=True)
fig = plt.figure()
ax = plt.axis([0,360,-90,90])
# matplotlib.rcParams['contour.negative_linestyle'] = 'solid'

def animate(i):
    plt.clf()
    cont = plt.contourf(lon, lat, u10[i][:][:], us, cmap='seismic')
    plt.colorbar(ticks=us)
    plt.xlabel('Longitude', fontweight='bold')
    plt.ylabel('Latitude', fontweight='bold')
    plt.grid(True)
    plt.title('Zonal Velocity in m/s at t = ' + str(i), fontweight='bold')
    plt.suptitle('Demo of netCDF contour', fontweight='bold')
    # plt.rcParams['contour.negative_linestyle'] = 'solid'
    # plt.contour(lon, lat, u10[i][:][:], us, color='-k')
    return cont
# DO not use plt.pause(0.001) during animation due to memory overload


anima = anim.FuncAnimation(fig,animate,interval=10,frames=31)
# Interval between 2 plots is in milliseconds

anima.save('anima.mp4',fps=1)  #fps = frames per second