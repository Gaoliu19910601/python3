from netCDF4 import Dataset as dt
import numpy as np
import matplotlib.pyplot as plt
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

# print(lat)
# print(lon)

um = np.mean(u10,axis=0)
vm = np.mean(v10,axis=0)
uv = (um**2+vm**2)**0.5

# plt.figure(1)
# plt.contourf(lon,lat,uv)
# plt.xlabel('Longitude',fontweight='bold')
# plt.ylabel('Latitude',fontweight='bold')
# plt.colorbar()
# plt.axis([0,360,-90,90])
# plt.streamplot(lon,lat,um,vm,density=2,linewidth=1,color='k')
# plt.savefig('streamplot.eps',format='eps',dpi=2000)


plt.figure(2)
# plt.quiver(lon,lat,um,vm)
Q = plt.quiver(lon,lat,um,vm,pivot='mid',color='b',units='inches',scale=100)
plt.xlabel('Longitude',fontweight='bold')
plt.ylabel('Latitude',fontweight='bold')
plt.quiverkey(Q,330,-75,U=2,label='m/s')
# plt.streamplot(lon,lat,um,vm,density=2,linewidth=1,color='k')
plt.show()