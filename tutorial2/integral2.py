import numpy as np
from scipy.integrate.quadpack import quad
from scipy.constants import codata
import matplotlib.pyplot as plt

D = codata.physical_constants

s = D['Stefan-Boltzmann constant'][0]

def spectra(l,T):
    k = D['Planck constant'][0]
    h = D['Boltzmann constant'][0]
    c = D['speed of light in vacuum'][0]
    func = ((2.0*np.pi*h*c**2)/(l**5))/((np.exp(h*c/(l*k*T)))-1.0)
    return func

s = 5.67e-8

T1 = 5770.0
T2 = 6000.0
T3 = 5000.0
T4 = 4000.0

int1, err1 = quad(spectra, 0.38e-6, 0.78e-6, args=(T1))

E1 = s*T1**4

l = np.linspace(0.0,5e-6,2**12+1)

s1 = spectra(l,T1)
s2 = spectra(l,T2)
s3 = spectra(l,T3)
s4 = spectra(l,T4)

print('The Energy flux is: ',E1)
print('The Energy flux in the band is: ',int1)
print('The Energy flux fraction is: ',int1/E1)
print('The Error is: ',err1)


section = np.linspace(0.0,5e-6,20)

plt.plot(l*1e6,s1,'k',label='T = 5770 K')
plt.plot(l*1e6,s2,'b',label='T = 6000 K')
plt.plot(l*1e6,s3,'g',label='T = 5000 K')
plt.plot(l*1e6,s4,'y',label='T = 4000 K')
plt.fill_between(section*1e6,spectra(section,T2),facecolor='red')
plt.grid('on')
# plt.axis([0.0,5.0,0.0e14,1.2e14])
plt.legend()
plt.show()
