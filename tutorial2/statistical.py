import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,1001)

y = 1 + np.sin(x)

y2 = 1 + np.cos(x)

a = np.mean(y)
b = np.std(y)
c = np.var(y)

print(a,b,c)

d = np.cov(y)
e = np.cov(y2)
f = np.cov(y,y2)

print(d,e,f)

plt.plot(x,y)
plt.plot(x,y2)
plt.show()