from netCDF4 import Dataset as dt
import numpy as np
import matplotlib.pyplot as plt

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
#
# '''To plot a 2D animation contour plot '''
# plt.figure(2)

for i in range(0,31):
    plt.clf()
    us = np.linspace(-20, 20, 11, endpoint=True)
    plt.contourf(lon, lat, u10[i][:][:], us, cmap='seismic')
    plt.colorbar(ticks=us)
    plt.xlabel('Longitude', fontweight='bold')
    plt.ylabel('Latitude', fontweight='bold')
    plt.axis([0, 360, -90, 90])
    plt.grid(True)
    plt.title('Zonal Velocity in m/s at t = '+str(i), fontweight='bold')
    plt.suptitle('Demo of netCDF contour', fontweight='bold')
    # plt.rcParams['contour.negative_linestyle'] = 'solid'
    # plt.contour(lon, lat, u10[i][:][:], us, color='-k')
    plt.pause(0.001)
