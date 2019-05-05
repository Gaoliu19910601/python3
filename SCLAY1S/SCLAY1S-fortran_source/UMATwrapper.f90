!   ******************************************************************                                                              
!   *                                                                *                                                              
!   *                     U M A T  WRAPPER                           *                                                              
!   *                                                                *                                                              
!   *      A TOCHNOG USER MATERIAL MODEL FOR Creep S-CLAY1S          *
!   *                             *
!   *                                                                *                                                              
!   *  WRITTEN BY : N. SIVASITHAMPARAM - PLAXIS NGI                  *
!   *                    DATE : May 2012                             *
!   *  REVISED BY :                                                  *                                                              
!   *                    DATE :                                      *                                                              
!   *                                                                *                                                              
!   ******************************************************************                                                              

! include the following original files converted to F90 for gfortran
!  MY_CLAY (main SCLAY file)
!  Creep_UNITS (substepping)
!  Creep_SCLAY1S (constitutive model)
!  HANDYLIB (helper functions)

                                                              
       SUBROUTINE UMAT (STRESS,STATEV,DDSDDE,SSE,SPD,SCD, &                                                                          
                 RPL,DDSDDT,DRPLDE,DRPLDT, &                                                                                                   
                 STRAN,DSTRAN,TIME,DTIME,TEMP,DTEMP,PREDEF,DPRED,CMNAME, &                                                                      
                 NDI,NSHR,NTENS,NSTATV,PROPS,NPROPS,COORDS,DROT,PNEWDT, &                                                                      
                 CELENT,DFGRD0,DFGRD1,NOEL,NPT,LAYER,KSPT,KSTEP,KINC) 
       Implicit Double Precision (A-H,O-Z)           

!        Arguments     Type
!        ---------    ------------------------------------------------
!     1  STRESS     : Stress tensor
!     2  STATEV     : State variables  
!     3  DDSDDE     : Jacobian matrix of the Constitutive model
!     4  SSE        : Specific elastic strain energey
!     5  SPD        : Plastic dissipation
!     6  SCD        : Creep dissipation

!     --- Only in fully coupled thermal analysis --------------------- 
!     7  RPL        : Volumetric heat generation per unit time
!     8  DDSDDT     : Variation of the stress increment wrt temper..
!     9  DRPLDE     : Variation of RPL wrt strain increment
!     10 DRPLDT     : Variation of RPL wrt the temperature

!     11 STRAN      : Total strain at begineing
!     12 DSTRAN     : Strain increment
!     13 TIME       : (1) : Step time at the begining
!                   : (2) : Total time at the begining
!     14 DTIME      : Time increment
!     15 TEMP       : Temperature at the begineing
!     16 DTEMP      : Increment of temperature
!     17 PREDEF     : Predefined field variables
!     18 DPRED      : Increments of predefined field variables     
!     19 CMNAME     : User defiend material name
!     20 NDI        : Number of direct stress components
!     21 NSHR       : Number of engineering shear stress
!     22 NTENS      : Size of stress or strain component
!     23 NSTATV     : Number of solution dependant state variables
!     24 PROPS      : Material constants
!     25 NPROPS     : Number of matrial constants
!     26 COORDS     : Coordinates of a point
!     27 DROT       : Rotation increment matrix
!     28 PNEWDT     : Ratio of suggested new time increment
!                   : < 1 : 
!                   : > 1 :                                                                
!     29 CELENT     : Characteristic element length 
!     30 DFGRD0     : Deformation gradient at the begining of the incr.
!     31 DFGRD1     : Deformation gradient at the end of the increment
!     32 NOEL       : Element number
!     33 NPT        : Integration point number
!     34 LAYER      : Layer number
!     35 KSPT       : Section point number within current layer
!     36 KSTEP      : Step number
!     37 KINC       : Increment number

      Integer      ::  NDI
      Integer      ::  NSHR
      Integer      ::  NTENS
      Integer      ::  NSTATV
      Integer      ::  NPROPS
      Integer      ::  NPT
      Integer      ::  LAYER
      Integer      ::  KSPT
      Integer      ::  KSTEP
      Integer      ::  KINC                                                            
      Integer      ::  NOEL   
      
      Double Precision  ::  STRESS(NTENS)                                                  
      Double Precision  ::  STATEV(NSTATV)
      Double Precision  ::  DDSDDE(NTENS,NTENS)
      Double Precision  ::  DDSDDT(NTENS)
      Double Precision  ::  DRPLDE(NTENS)
      Double Precision  ::  STRAN(NTENS)
      Double Precision  ::  DSTRAN(NTENS)
      Double Precision  ::  TIME(2)
      Double Precision  ::  PREDEF(1)
      Double Precision  ::  DPRED(1)
      Double Precision  ::  PROPS(NPROPS)
      Double Precision  ::  COORDS(3)
      Double Precision  ::  DROT(3,3)
      Double Precision  ::  DFGRD0(3,3)
      Double Precision  ::  DFGRD1(3,3) 
      Double Precision  ::  DTIME
      Double Precision  ::  SSE 
      Double Precision  ::  SPD
      Double Precision  ::  SCD
      Double Precision  ::  DRPLDT
      Double Precision  ::  TEMP 
      Double Precision  ::  DTEMP
      Double Precision  ::  RPL
      Double Precision  ::  PNEWDT
      Double Precision  ::  CELENT
      
      CHARACTER*80 CMNAME 
      
                                                                                                                                   
!     INCLUDE 'ABA_PARAM.INC'  !This is for Abaqus                                                                                                   
                                                                                                                                    
                                                                                                         
                                                                                                                                    
      Double Precision  StVar(NSTATV)
      Double Precision  Sig(6)
      Double Precision  Sig0(6)
      Double Precision  StVar0(NSTATV)
      Double Precision  dEps(6)
      Double Precision  D(6,6)
!      Double Precision Props(50) ! Props already defined in UMAT
!      Double Precision DMat(6,6)
  
!      setting number of state variables
        nStat = NSTATV  
               
        Call CopyRVec( STATEV, StVar0, nStat ) !StVar0 = STATEV

!In incremental driver the axis are not defined in the same way than in Ms Clays.
!in ID, 1 is vertical while in MS Clays, 2 is vertical
!Moreover in ID,the stress vector is defined in this order Sigma_11, Sigma_22, Sigma_33, Sigma_12, Sigma_13, Sigma_23  
!While in MS Clays, it is defined in this order Sigma_11, Sigma_22, Sigma_33, Sigma_12, Sigma_23, Sigma_13
!For this reason we have to give the good values to MsClays for the calculations 
 
!!!!!Verifier la convention de signe dans incrémental driver pour savoir si il faut mettre négatif ou pas        
          Sig0(1) = STRESS(3)
          Sig0(2) = STRESS(1)
          Sig0(3) = STRESS(2)
          Sig0(4) = STRESS(6)
          Sig0(5) = STRESS(4)
          Sig0(6) = STRESS(5)
                       
          Sig(1) = STRESS(3)
          Sig(2) = STRESS(1)
          Sig(3) = STRESS(2)
          Sig(4) = STRESS(6)
          Sig(5) = STRESS(4)
          Sig(6) = STRESS(5)
            
          dEps(1) = DSTRAN(3)
          dEps(2) = DSTRAN(1)
          dEps(3) = DSTRAN(2)
          dEps(4) = DSTRAN(6)
          dEps(5) = DSTRAN(4)
          dEps(6) = DSTRAN(5)
          
        
! to avoid undrained calculation        
        IsUndr = 0
!        Swp0 = 0
        !write (*,*) IsUndr

        
      
!  dummy == do not use
!  Argument     I/O Type                                      Abaqus
!  -------- --- ----
!  IDTask   I   I    : see above                                only if StVar0)12 == 0
!  iMod     I   I    : model number (1..10)                     dummy
!  IsUndr   I   I    : =1 for undrained, 0 otherwise            0
!  iStep    I   I    : Global step number                       KSTEP
!  iter     I   I    : Global iteration number                  KINC
!  iel      I   I    : Global element number                    NOEL
!  Intp     I   I    : Global integration point number          NPT
!  X        I   R    : X-Position of integration point          COORDS(1)
!  Y        I   R    : Y-Position of integration point          COORDS(2)
!  Z        I   R    : Z-Position of integration point          COORDS(3)
!  Time0    I   R    : Time at start of step                    TIME(1)
!  dTime    I   R    : Time increment                           DTIME
!  Props    I   R()  : List with model parameters               PROPS
!  Sig0     I   R()  : Stresses at start of step                STRESS
!  Swp0     I   R    : Excess pore pressure start of step       dummy
!  StVar0   I   R()  : State variable at start of step          STATEV
!  dEps     I   R()  : Strain increment                         DSTRAN
!  D       I/O  R(,) : Material stiffness matrix                DDSDDE
!  BulkW   I/O  R    : Bulkmodulus for water (undrained only)   dummy
!  Sig      O   R()  : Resulting stresses                       STRESS
!  Swp      O   R    : Resulting excess pore pressure           dummy
!  StVar    O   R()  : Resulting values state variables         STATEV
!  ipl      O   I    : Plasticity indicator                     dummy
!  nStat    O   I    : Number of state variables                NSTATV
!  NonSym   O   I    : Non-Symmetric D-matrix ?                 dummy
!  iStrsDep O   I    : =1 for stress dependent D-matrix         dummy
!  iTimeDep O   I    : =1 for time dependent D-matrix           dummy
!  iPrjDir  I   I    : Project directory (ASCII numbers)        dummy
!  iPrjLen  I   I        : Length of project directory name     dummy        
!  iAbort   O   I    : =1 to force stopping of calculation      0
! ---------------------------------------------------------------------------------------- 

!write (*,*) StVar0(12)
! check for IDTASK       
        If (StVar0(12) == 0) Then        
            IDTask = 1 !(initialisation)
        Else
            IDTask = 2 !(calc stress)
        End if

! iMod = 1 (creep), IsUndr = 0)
        Call My_SCLAY(   IDtask, 1, IsUndr, iStep, iTer, iEl, Intp, &
                         X, Y, Z, Time0, dTime, &
                         Props, Sig0, Swp0, StVar0, &
                         dEps, D, BulkW, Sig, Swp, StVar, ipl, &
                         nStat, NonSym, iStrsDep, iTimeDep, iTang, &
                         iPrjDir, iPrjLen,&
                         iAbort &
                         ) 
        
        !write (*,*)  IsUndr

                         
!       UPDATE STATE VARIABLES, STRESS AND STRAIN
                                       
        Call CopyRVec( StVar, STATEV, nStat ) !STATEV = StVar   

!        write (*,*) StVar0(12),StVar(12), STATEV(12) 
      
        STRESS(1) = Sig(2)
        STRESS(2) = Sig(3)
        STRESS(3) = Sig(1)
        STRESS(4) = Sig(5)
        STRESS(5) = Sig(6)
        STRESS(6) = Sig(4)
        
        DSTRAN(1) = dEps(2)
        DSTRAN(2) = dEps(3)
        DSTRAN(3) = dEps(1)
        DSTRAN(4) = dEps(5)
        DSTRAN(5) = dEps(6)
        DSTRAN(6) = dEps(4)
        
        !Do i=1,6
        !    STRAN(i) = STRAN(i) + DSTRAN(i)
        !End Do 
        
        
        DDSDDE(1,1) = D(2,2)
        DDSDDE(1,2) = D(2,3)
        DDSDDE(1,3) = D(2,1)
        DDSDDE(1,4) = D(2,5)
        DDSDDE(1,5) = D(2,6)
        DDSDDE(1,6) = D(2,4)
        
        DDSDDE(2,1) = D(3,2)
        DDSDDE(2,2) = D(3,3)
        DDSDDE(2,3) = D(3,1)
        DDSDDE(2,4) = D(3,5)
        DDSDDE(2,5) = D(3,6)
        DDSDDE(2,6) = D(3,4)
        
        DDSDDE(3,1) = D(1,2)
        DDSDDE(3,2) = D(1,3)
        DDSDDE(3,3) = D(1,1)
        DDSDDE(3,4) = D(1,5)
        DDSDDE(3,5) = D(1,6)
        DDSDDE(3,6) = D(1,4)
        
        DDSDDE(4,1) = D(5,2)
        DDSDDE(4,2) = D(5,3)
        DDSDDE(4,3) = D(5,1)
        DDSDDE(4,4) = D(5,5)
        DDSDDE(4,5) = D(5,6)
        DDSDDE(4,6) = D(5,4)
        
        DDSDDE(5,1) = D(6,2)
        DDSDDE(5,2) = D(6,3)
        DDSDDE(5,3) = D(6,1)
        DDSDDE(5,4) = D(6,5)
        DDSDDE(5,5) = D(6,6)
        DDSDDE(5,6) = D(6,4)
        
        DDSDDE(6,1) = D(4,2)
        DDSDDE(6,2) = D(4,3)
        DDSDDE(6,3) = D(4,1)
        DDSDDE(6,4) = D(4,5)
        DDSDDE(6,5) = D(4,6)
        DDSDDE(6,6) = D(4,4)

        
       !Open(Unit= 1, File= "dummy", Position= 'append')
       !write(3,*) StVar
   
!      print*, "sig =",STRESS(1),STRESS(2),STRESS(3)
     
                                                                                                                         
!      parsed State quantities, this works as well after copying stvar0 to stvar in IDTask 1
!      print*, "alphax =",STATEV(1), "alphay =", STATEV(2), "alphaz =", STATEV(3), &
!          "alphaxy =", STATEV(4)
!      print*, "alphayz =",STATEV(5), "alphazx =", STATEV(6), "alphascal =", STATEV(7), &
!          "pmi =", STATEV(8), "x =", STATEV(9)
!      print*, "pm =",STATEV(10), "ecurr =", STATEV(11), "inidone =", STATEV(12)
        
        
        
       RETURN                                                                                                                       
       END  SUBROUTINE UMAT  


