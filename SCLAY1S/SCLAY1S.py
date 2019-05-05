#================================================================
#
#                SCLAY1S MODEL FOR PYTHON3
#
#                     [BY Amardeep A]
#
#                  Created on June 12-2018
#================================================================


import numpy as np
import matplotlib.pyplot as plt

analysis = 1 # only values 0-Tri Dr, 1-Tri Undr, 2-Oedo

#===================== Input parameters =======================

sig0 = 20.0             # Horizontal (kPa)
sig1 = 30.0             # Vertical stress (kPa)
sig2 = 20.0             # Horizontal (kPa)
sig3 =  0.0             # Shear stress (kPa)
sig4 =  0.0             # Shear stress (kPa)
sig5 =  0.0             # Shear stress (kPa)

sig = np.array([[sig0],[sig1],[sig2],[sig3],[sig4],[sig5]])
strain = np.array([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0]]) # rewinded to zero after initial loading to current stress state

kappa = 0.05            # Swelling index
lambda1 = 0.25          # Compression index
nu = 0.15               # poisson ratio
M = 1.5                 # critical state slope for compression
alpha0 = 0.58           # Initial inclination of yield surface
OCR = 0.0               # Overconsolidation ratio (OCR)
POP = 15.0              # Preoverburden pressure (kPa)
x0 = 3.0               # Initial bonding in the soil
e0 = 2.50               # Initial void ratio

# Derived parameters
phi = np.arcsin(3.0*M/(6.0 + M))
K0nc = 1.0 - np.sin(phi)
eta_k0 = 3.0*(1.0-K0nc)/(1.0+2.0*K0nc)
alphaK0 = (eta_k0**2+3.0*eta_k0-M**2)/3.0

print('Alpha: ',alpha0,' Alpha_K0nc: ',alphaK0)

#================== Calculate isotropic PCP ========================

sig_mod0 = (sig1+POP)*K0nc
sig_mod1 = (sig1+POP)
sig_mod2 = (sig1+POP)*K0nc
sig_mod3 = 0.0
sig_mod4 = 0.0
sig_mod5 = 0.0

#==================== Calculate stress invariants ===========================

pdash = (sig_mod0+sig_mod1+sig_mod2)/3.0

q = np.sqrt((3.0/2.0)*((sig_mod0-pdash)**2+(sig_mod1-pdash)**2+ \
    (sig_mod2-pdash)**2+2.0*(sig_mod3)**2+2.0*(sig_mod4)**2+2.0*(sig_mod5)**2))

pm = (((q-alpha0*pdash)**2)/(pdash*(M*M-alpha0*alpha0)))+pdash

pmi = pm/(1+x0)

#===================== Plotting the yield surface =============================

p_trial = np.linspace(0,pm,200)
p_triali = np.linspace(0,pmi,200)

q_trial1 = alpha0*p_trial + np.sqrt((pm-p_trial)*(M*M-alpha0*alpha0)*p_trial)
q_trial2 = alpha0*p_trial - np.sqrt((pm-p_trial)*(M*M-alpha0*alpha0)*p_trial)

q_triali1 = alpha0*p_triali + np.sqrt((pmi-p_triali)*(M*M-alpha0*alpha0)*p_triali)
q_triali2 = alpha0*p_triali - np.sqrt((pmi-p_triali)*(M*M-alpha0*alpha0)*p_triali)

pdash_given = (sig0+sig1+sig2)/3.0

q_given = np.sqrt((3.0/2.0)*((sig0-pdash)**2+(sig1-pdash)**2+ \
        (sig2-pdash)**2+2.0*(sig3)**2+2.0*(sig4)**2+2.0*(sig5)**2))

plt.figure(1)
plt.plot(p_trial,q_trial1,'-b')
plt.plot(p_trial,q_trial2,'-b')
plt.plot(p_triali,q_triali1,'-r')
plt.plot(p_triali,q_triali2,'-r')
plt.plot(pdash_given,q_given,'ro')
plt.plot([0,pdash+5],[0,(pdash+5)*M],'--m')
plt.plot([0,pdash+5],[0,-(pdash+5)*M],'--g')
plt.xlabel('Mean effective stress (kPa)')
plt.ylabel('Deviator stress (kPa)')
plt.title('Initial yield surface of SCLAY1S')
plt.grid(True)

#======================= Initialize the state variables =======================

StVar = np.array([[-(alpha0/3.0)+1.0],   # alpha_x
                 [(2.0*alpha0/3.0)+1.0], # alpha_y
                 [-(alpha0/3.0)+1.0],    # alpha_z
                 [0.0],                  # alpha_xy
                 [0.0],                  # alpha_yz
                 [0.0],                  # alpha_zx
                 [alpha0],               # alpha_scalar
                 [pm/(1+x0)],            # pmi
                 [x0],                   # x
                 [pm],                   # pm
                 [e0]])                  # current void ratio

# print(StVar)

#==============================================================================

strain_inc = 0.01/100           # strain increment
itr = 75                      # No of iterations

#==================== Initialization ==========================

# Updating at each iteration
p = np.zeros((itr,1))    # Mean effective stress (kPa)
p[0] = pdash_given

q = np.zeros((itr,1))    # Deviatoric stress (kPa)
u = np.zeros((itr,1))    # Pore pressure (kPa)
void = np.zeros((itr,1)) # Void ratio
epsV = np.zeros((itr,1)) # Volumetric strain
epsD = np.zeros((itr,1)) # Deviatoric strain


# Not updating for each iteration
D = np.zeros((6,6))      # Stiffness matrix
dfds = np.zeros((6,1))   # Yield surface derivative w.r.t stresses
dfdep = np.zeros((6,1))  # Yield surface derivative w.r.t volumetric strain



i = 0

# Calculate the initial yield surface

yield_s = ((q_given-alpha0*pdash_given)/(M*M-alpha0*alpha0))+(pdash_given-0.5*pm)**2-(0.5*pm)**2

while i<itr-1:
    K = nu*p[i]/kappa                           # Bulk modulus
    G = (3.0*K*(1.0-2.0*nu))/(2.0*(1.0+nu))    # Shear modulus
    if yield_s == 0:
        break
        # pc = (q[i]**2/ M**2 + p[i]**2) / p[i]
        # pm = (((q - alpha0 * pdash) ** 2) / (pdash * (M * M - alpha0 * alpha0))) + pdash
    else:
        pm = pm

    print('Iteration nr: ',i, '|| Yield value: ',yield_s,'|| pm: ',pm)

    # Considering isotropic elasticity inside the yield surface

    D[0, 0]=D[1, 1]=D[2, 2]= K+(4.0/3.0)*G
    D[0, 1]=D[0, 2]=D[1, 0]=D[1, 2]=D[2, 0]=D[2, 1]= K-(2.0/3.0)*G
    D[3, 3]=D[4, 4]=D[5, 5]= G


    if yield_s < 0:
        Dep = D
    else:
        break

    if analysis==0: # drained
        dstrain = np.array([[-Dep[1,0]/(Dep[1,1]+Dep[1,2])*strain_inc],
                   [strain_inc],
                   [-Dep[2,0]/(Dep[2,1]+Dep[2,2])*strain_inc],
                   [0.0],[0.0],[0.0]])

    elif analysis==1: # undrained
        dstrain = np.array([[-strain_inc*0.5],[strain_inc],[-strain_inc*0.5],[0.0],[0.0],[0.0]])
    elif analysis==2:
        dstrain = np.array([[0.0],[strain_inc],[0.0],[0.0],[0.0],[0.0]])

    dS = np.dot(Dep, dstrain)

    sig += dS

    strain += dstrain

    depsV = dstrain[0] + dstrain[1] + dstrain[2]
    depsD = (2.0 / 3.0) * (dstrain[0] - dstrain[1])

    i += 1

    p[i] = (sig[0] + sig[1] + sig[2]) / 3


    q[i] = np.sqrt((3.0/2.0)*((sig[0]-pdash)**2+(sig[1]-pdash)**2+ \
        (sig[2]-pdash)**2+2.0*(sig[3])**2+2.0*(sig[4])**2+2.0*(sig[5])**2))


    epsV[i] = epsV[i-1] + depsV
    epsD[i] = epsD[i-1] + depsD

    u[i] = ((sig0+sig1+sig2)/3.0)+(q[i]/3)-p[i]

    yield_s = ((q[i]-alpha0*p[i]/(M*M-alpha0*alpha0))+(p[i]-0.5*pm)**2-(0.5*pm)**2)

    print('yield_s: ', yield_s)

    if yield_s<0:
        ((q[i] - alpha0 * p[i] / (M * M - alpha0 * alpha0)) + (p[i] - 0.5 * pm) ** 2 - (0.5 * pm) ** 2)
    else:
        yield_s = 0




plt.figure(1)
plt.plot(p_trial,q_trial1,'-b')
plt.plot(p_trial,q_trial2,'-b')
plt.plot(p_triali,q_triali1,'-r')
plt.plot(p_triali,q_triali2,'-r')
plt.plot(pdash_given,q_given,'ro')
plt.plot(p,q,'-r')
plt.plot([0,pdash+5],[0,(pdash+5)*M],'--m')
plt.plot([0,pdash+5],[0,-(pdash+5)*M],'--g')
plt.xlabel('Mean effective stress (kPa)')
plt.ylabel('Deviator stress (kPa)')
plt.title('Initial yield surface of SCLAY1S')
plt.grid(True)
plt.show()
