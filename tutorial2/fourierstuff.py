import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft

T = 1.0/64.0

N = 64.0

x = np.linspace(0,2*np.pi*T*N,N)

y1 = np.sin(20*x)
y2 = np.sin(10*x)
y3 = np.sin(5*x)

y = y1+y2+y3

fy = fft(y) # transforms into frequency domain

xf = np.linspace(0,1.0/(2.0*T),N/2.0)

plt.figure(1)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.figure(2)
plt.plot(xf,abs(fy[0:32]))

plt.figure(3)
y4 = ifft(fy) # brings back to the average time domain
plt.plot(x,y4,'-r')
plt.plot(x,y,'-b')
plt.show()
