import scipy.io as sio
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

mat = {}
mat['lat'] = lat
mat['lon'] = lon

um = np.mean(u10,axis=0)
vm = np.mean(v10,axis=0)
uv = (um**2+vm**2)**0.5

mat['um'] = um
mat['vm'] = vm

file1 = 'file1.mat'

sio.savemat(file1, mat)

'''Now read data from this mat file'''

filedict1 = sio.loadmat(file1)

longi1 = filedict1['lon']

print(longi1)


