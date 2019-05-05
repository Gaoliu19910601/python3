
import numpy as np
import matplotlib.pyplot as plt

from numpy.fft import fft, fftfreq, ifft

lx = 100 # time in seconds
n = 1000 # number of points

x = np.linspace(1, lx, n) # Time

omg = 2.0*np.pi/lx

y1 = 3.0*np.cos(5.0*omg*x)
y2 = 2.0*np.sin(10.0*omg*x)
y3 = 1.0*np.sin(20.0*omg*x)

y = y3+y2+y1

plt.figure(1)
plt.plot(x, y, '-b')
# plt.show()

ffts = fftfreq(n)
fftvals = fft(y)

#further processing
mask = ffts > 0
ffttheo = 2.0*abs(fftvals/n)


plt.figure(2)
plt.plot(ffts, fftvals, '-g')
# plt.plot(ffts[mask], ffttheo[mask], '-g')
plt.show()