import numpy as np
import matplotlib.pyplot as plt

Z = np.array((0.0,0.1,0.3,0.5,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0))

RH100 = np.array((60.0,70.0,80.0,75.0,60.0,50.0,80.0,90.0,60.0,40.0,20.0,5.0,2.0,1.0))

Z = Z*1000          # in m
RH = RH100*0.01        # not in percentage

Ts = 30.0           # in degree celsius
g  = 9.806          # m/s**2
Cp = 1005.0         # J/Kg-K
A = 2.53*(10**11)   # Pa
B = 5420.0          # K
Ps = 10**5          # Pa
R = 287.0           # J/Kg-K
L = 2.5006*(10**6)  # J/Kg
v0 = 100.0          # m/s

Zs = R*(Ts+274.15)/g

# T,es,P,rho,e,q,W,h,MSE,v,E,Tk = ([] for j in range(12))
#
#
#
# for i in range(0,len(Z)):
#     T.append(Ts - g*Z[i]/Cp)
#     Tk.append(T[i]+274.15)
#     es.append(A*np.exp(-B/Tk[i]))
#     e.append(RH100[i]*es[i]/100.0)
#     P.append(Ps*np.exp(-g*Z[i]/(R*Tk[i])))
#     rho.append(P[i]/(R*Tk[i]))
#     q.append(0.622*(e[i]/P[i]))
#     W.append(q[i]*rho[i])
#     h.append(q[i]*L+Cp*(Tk[i]))
#     MSE.append(h[i]+g*Z[i])
#     v.append(v0*((np.exp(Z[i]/Zs))-1.0))
#     E.append(MSE[i]+0.5*v[i]**2)
#
# print(T)
# print(E)

T = np.zeros(len(Z))
es = np.array(T)
P = np.array(T)
rho = np.array(T)
e = np.array(T)
q = np.array(T)
W = np.array(T)
h = np.array(T)
MSE = np.array(T)
v = np.array(T)
E = np.array(T)
Tk = np.array(T)


T = Ts - g*Z/Cp
Tk = T+274.15
es = A*np.exp(-B/Tk)
e = RH100*es/100.0
P = Ps*np.exp(-g*Z/(R*Tk))
rho = P/(R*Tk)
q = 0.622*(e/P)
W = q*rho
h = q*L+Cp*Tk
MSE = h+g*Z
v = v0*((np.exp(Z/Zs))-1.0)
E = MSE+0.5*v**2

# print(T)
# print(E)


# Same x axis
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(Z,P,'-r')
ax2.plot(Z,es,'-b')


# Superimposing figures
plt.figure(2)
plt.plot(es,Z,'b')
plt.plot(e,Z,'m')
plt.xlabel('Vapour pressure in Pa')
plt.ylabel('Altitude in m')
plt.xticks(np.linspace(0,5000,11))
plt.yticks(np.linspace(0,10000,11))
plt.axis([0,5000,0,10000])
plt.title("Vapoure pressure check")
plt.suptitle("Tutorial-Python")
plt.grid('on')
plt.legend(['es','e'])
# plt.savefig('tutorial.png',format='png',dpi=600)


# Superimposing figures with a scatter format
plt.figure(3)
plt.scatter(es,Z)
plt.scatter(e,Z)
plt.xlabel('Vapour pressure in Pa')
plt.ylabel('Altitude in m')
plt.xticks(np.linspace(0,5000,11))
plt.yticks(np.linspace(0,10000,11))
plt.axis([0,5000,0,10000])
plt.title("Vapoure pressure check")
plt.suptitle("Tutorial-Python")
plt.grid('on')
plt.legend(['es','e'])
# plt.savefig('tutorial2.png',format='png',dpi=600)







import matplotlib.mlab as mlab

m, s = 100, 15
iq = np.random.normal(m, s, 1000)
# Setting a random iq data normally distributed with mean, m and SD, s
num_bins = 50 # number of groups we want


plt.figure(4)

n, bins, patches = plt.hist(iq, num_bins, normed=1, facecolor='green')
# n = counts in each group
# bins = array of edges
# normed = 1 or true, returns n as fraction, else n as plain nos.
# Sum of fractions = 1 and Sum of counts = total no. of entries
l = mlab.normpdf(bins,m,s)
# Creates the pdf of normal distribution

plt.plot(bins,l,'r',label='pdf')
plt.xlabel('IQ bins')
plt.ylabel('Probability')
plt.title('Histogram of $\mu$=100 and $\sigma$=15')
plt.grid('on')
plt.savefig('histogram.png',format='png',dpi=600)
plt.show()
