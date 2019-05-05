import numpy as np


file = open('rain_data.txt','r')

contents = file.readlines()

y = np.zeros(30597,dtype=np.int16)
sec = np.zeros(30597)
rain = np.zeros(30597)

i=0

for line in contents:
    y[i],sec[i],rain[i] = line.split()
    i += 1

file.close()

file2 = open('rain_data2.txt','w')

for i in range(0,30597):
    val = str(y[i])+'\t'+str(sec[i])+'\t'+str(rain[i])+'\n'
    file2.write(val)

file2.close()

