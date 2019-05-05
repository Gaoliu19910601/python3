
#================================================================
#
#             MODIFIED CAM CLAY (MCC) MODEL FOR PYTHON3
#
#  [BY Amardeep A]
#
# Created on June 7-2018 (Inspired from Octave code by
# Krishna Kumar, University of Cambridge)
#================================================================


import numpy as np
import matplotlib.pyplot as plt

analysis = 0 # only values 0-Tri Dr, 1-Tri Undr, 2-Oedo

#--------------- Input parameters---------------------
kappa = 0.05          # Swelling index
lambda1 = 0.25        # Compression index
nu = 0.15             # poisson ratio
M = 1.5               # critical state slope
N = 3.426             # isotropic normal
pc = 300.0            # Preconsolidation pressure (kPa)
p0 = 250.0            # Consolidation pressure (kPa)


#---------------- Initial calculations-----------------
v = N-lambda1*np.log(pc)\
    -kappa*np.log(pc/p0)            # Specific volume
e0 = v-1                            # Initial void ratio
OCR = pc/p0                         # Isotropic preconsolidation pressure

K0_nc = (6.0-2.0*M)/(6.0+M)         # Following Jaky's formula
eta_K0nc = 3.0*(1.0-K0_nc)/(1.0+2.0*K0_nc) # K0 stress ratio


#------------------ Iteration input details------------
itr = 100000                  # Number of iterations
strain_inc = 0.0001/1000      # Strain increment

#------------------ Initialization ---------------------

# Updating at each iteration
p = np.zeros((itr,1))    # Mean effective stress (kPa)
q = np.zeros((itr,1))    # Deviatoric stress (kPa)
u = np.zeros((itr,1))    # Pore pressure (kPa)
void = np.zeros((itr,1)) # Void ratio
epsV = np.zeros((itr,1)) # Volumetric strain
epsD = np.zeros((itr,1)) # Deviatoric strain


# Not updating for each iteration
D = np.zeros((6,6))      # Stiffness matrix
dfds = np.zeros((6,1))   # Yield surface derivative w.r.t stresses
dfdep = np.zeros((6,1))  # Yield surface derivative w.r.t volumetric strain


#------------------ Initial Yield Surface ------------------------

p_ys = np.linspace(0,pc,500)

q_ys_c = ((M**2)*p_ys*pc-(M**2)*p_ys*p_ys)**0.5
q_ys_e = -((M**2)*p_ys*pc-(M**2)*p_ys*p_ys)**0.5

#------------- Initialization before Iteration --------------------

i = 0

stress = np.array([[p0],[p0],[p0],[0.0],[0.0],[0.0]])
strain = np.array([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0]])

p[i] = (stress[0]+stress[1]+stress[2])/3.0
q[i] = (stress[0] - stress[1])


yield_s = q[i]**2- (M**2)*p[i]*pc+(M**2)*(p[i]**2) # Define the yield surface

void[i] = e0

# ------------------- Start the Iteration ------------------


while i<itr-1:
    K = v*p[i]/kappa                           # Bulk modulus
    G = (3.0*K*(1.0-2.0*nu))/(2.0*(1.0+nu))    # Shear modulus
    if yield_s == 0:
        pc = (q[i]**2/ M**2 + p[i]**2) / p[i]
    else:
        pc = pc

    print('Iteration nr: ',i, '|| Yield value: ',yield_s,'|| pc: ',pc)

    # Considering isotropic elasticity inside the yield surface

    D[0,0] = D[1,1] = D[2,2] = K+(4.0/3.0)*G
    D[0,1] = D[0,2] = D[1,0] = D[1,2] = D[2,0] = D[2,1] = K-(2.0/3.0)*G
    D[3,3] = D[4,4] = D[5,5] = G

    dfds[0,0] = (2.0*p[i]-pc)/3.0 + 3.0*(stress[0]-p[i])/M**2
    dfds[1,0] = (2.0*p[i]-pc)/3.0 + 3.0*(stress[1]-p[i])/M**2
    dfds[2,0] = (2.0*p[i]-pc)/3.0 + 3.0*(stress[2]-p[i])/M**2

    # dfds[0,0] = (2.0*stress[0]-stress[1]-stress[2])-((2*stress[0]+2*stress[1]+2*stress[2])*(M**2)/9)-((2*stress[0]+2*stress[1]+2*stress[2]-3*pc)*(M**2)/9)
    # dfds[1,0] = (2.0*stress[1]-stress[0]-stress[2])-((2*stress[0]+2*stress[1]+2*stress[2])*(M**2)/9)-((2*stress[0]+2*stress[1]+2*stress[2]-3*pc)*(M**2)/9)
    # dfds[2,0] = (2.0*stress[2]-stress[1]-stress[0])-((2*stress[0]+2*stress[1]+2*stress[2])*(M**2)/9)-((2*stress[0]+2*stress[1]+2*stress[2]-3*pc)*(M**2)/9)

    dfds[3,0] = dfds[4,0] = dfds[5,0] = 0.0


    # dfdep[0,0] = (-1.0)*(M**2)*(p[i]*pc*(1.0+e0))/(lambda1-kappa)
    # dfdep[1,0] = (-1.0)*(M**2)*(p[i]*pc*(1.0+e0))/(lambda1-kappa)
    # dfdep[2,0] = (-1.0)*(M**2)*(p[i]*pc*(1.0+e0))/(lambda1-kappa)

    # As given in the OCTAVE CODE
    dfdep[0,0] = (-1.0)*(1.0**2)*(p[i]*pc*(1.0+e0))/(lambda1-kappa)
    dfdep[1,0] = (-1.0)*(1.0**2)*(p[i]*pc*(1.0+e0))/(lambda1-kappa)
    dfdep[2,0] = (-1.0)*(1.0**2)*(p[i]*pc*(1.0+e0))/(lambda1-kappa)


    dfdep[3,0] = dfdep[4,0] = dfdep[5,0] = 0.0

    # if yield_s == 0:
    #     print(dfds)
    #     print(dfdep)
    #     print(D)



    if yield_s < 0:
        Dep = D
    else:
        Dep = D-(np.dot(np.dot(D,dfds),np.dot(np.transpose(dfds),D))/((-1.0*np.dot(np.transpose(dfdep),dfds))+
                                                                      (np.dot(np.transpose(dfds),np.dot(D,dfds)))))

        # print(i)
        # print(Dep)

    if analysis==0: # drained
        dstrain = np.array([[strain_inc],
                   [-Dep[1,0]/(Dep[1,1]+Dep[1,2])*strain_inc],
                   [-Dep[2,0]/(Dep[2,1]+Dep[2,2])*strain_inc],
                   [0.0],[0.0],[0.0]])

    elif analysis==1: # undrained
        dstrain = np.array([[strain_inc],[-strain_inc*0.5],[-strain_inc*0.5],[0.0],[0.0],[0.0]])
    elif analysis==2:
        dstrain = np.array([[strain_inc],[0.0],[0.0],[0.0],[0.0],[0.0]])

    dS = np.dot(Dep,dstrain)

    stress += dS

    strain += dstrain

    depsV = dstrain[0]+dstrain[1]+dstrain[2]
    depsD = (2.0/3.0)*(dstrain[0]-dstrain[1])

    V = N-(lambda1*np.log(pc))+(kappa*np.log(pc/p[i]))

    i += 1

    p[i] = (stress[0] + stress[1] + stress[2]) / 3
    q[i] = (stress[0] - stress[1])
    u[i] = p0+(q[i]/3)-p[i]


    yield_s = q[i] ** 2 - (M ** 2) * p[i] * pc + (M ** 2) * (p[i] ** 2)  # Define the yield surface

    print('yield_s: ',yield_s)

    void[i] = V-1.0

    epsV[i] = epsV[i-1] + depsV
    epsD[i] = epsD[i-1] + depsD

    if yield_s<0:
        yield_s = q[i]**2-(M**2)*p[i]*pc+(M**2)*p[i]**2
    else:
        yield_s = 0


p_ys_final = np.linspace(0,pc,500)
q_ys_c_final = ((M**2)*p_ys_final*pc-(M**2)*p_ys_final*p_ys_final)**0.5
q_ys_e_final = -((M**2)*p_ys_final*pc-(M**2)*p_ys_final*p_ys_final)**0.5


plt.figure(2)
plt.plot(p_ys_final,q_ys_c_final,'-b')
plt.plot(p,q,'-r',label='stress state')
plt.plot([p[0],p[-1]],[q[0],q[-1]],'ro')
plt.plot(p_ys_final,q_ys_e_final,'-b')
plt.plot([0,pc+20],[0,(pc+20)*M],'--r')
plt.plot([0,pc+20],[0,-(pc+20)*M],'--r')
plt.plot([0,(pc+20)],[0,(pc+20)*eta_K0nc],'--g')
plt.plot(p_ys,q_ys_c,'-b')
plt.plot(p_ys,q_ys_e,'-b')
plt.grid(True)
plt.xlabel("Mean effective stress,$p^{'}$ (kPa)")
plt.ylabel("Deviator Stress, q (kPa)")
plt.title("Modified Cam Clay - yield surface")
plt.legend()
# plt.show()




plt.figure(3)
plt.plot(epsD,q,'-r',label='with M')
plt.xlabel('Deviatoric strain, $\epsilon_{d}$')
plt.ylabel('Deviatoric stress, q (kPa)')
# plt.legend()
plt.grid(True)
# plt.show()

plt.figure(4)
plt.semilogx(p,epsV,'-r',label='with M')
plt.ylabel('Volumetric strain, $\epsilon_{v}$')
plt.gca().invert_yaxis()
plt.xlabel(" Mean effective stress, $p^{'}$ (kPa)")
plt.title('Compression Plane',fontweight='bold')
# plt.legend()
plt.grid(True)



# plt.figure(5)
# plt.plot(epsD,u,'-r')
# plt.xlabel('Deviatoric strain, $\epsilon_{d}$')
# plt.ylabel(" Excess pore pressure, $u$ (kPa)")
# plt.title('Excess Pore Pressure Development',fontweight='bold')
# plt.grid(True)
plt.show()


