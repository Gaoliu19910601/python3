

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dampfunc(x,t):
    F0 = 10.0
    w = 1.0
    m = 2.0
    c = 1.0
    k = 20.0
    x0, x1 = x
    x2 = (F0*np.sin(w*t))/m - c*x1/m - k*x0/m
    return x1,x2

F0 = 10.0
w = 1.0
m = 2.0
c = 1.0
k = 20.0

init = [0.0,0.0]

t = np.linspace(0,10,101)

x = odeint(dampfunc,init,t)

acc = (F0*np.sin(w*t))/m - c*x[:,1]/m - k*x[:,0]/m

plt.plot(t,x[:,0],'-b',label='$x(m)$')
plt.plot(t,x[:,1],'-r',label='$\dot{x} (m/s)$')
plt.plot(t,acc,'-g',label='$\ddot{x} (m/s^2)$')
plt.xlabel('Time in secs',fontweight='bold',fontsize=12)
plt.ylabel('Acc($m/s^2$), vel(m/s), disp(m)',fontweight='bold',fontsize=12)
plt.legend(framealpha=0.5)
plt.grid('on')
plt.title('Solution to Mass-spring-damper system',fontweight='bold')
plt.show()