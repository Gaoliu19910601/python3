! ----------------------------------------------------------------------------------------
! 'S-Clay1S': user-defined soil model for PLAXIS, Wiltafsky (2003)
! ----------------------------------------------------------------------------------------

  Subroutine S_CLAY1S	( IsUndr, &
	                      Props, Sig0, Swp0, StVar0, &
		                  dEps, D, BulkW, &
	                      Sig, Swp, StVar, ipl, &
		                  nStat, xNewStep )

! ----------------------------------------------------------------------------------------
! User-defined soil model: S-Clay1S (iMod=1)
!
!  Depending on IDTask, 1 : Initialize state variables
!                       2 : calculate stresses
!                       3 : calculate material stiffness matrix
!                       4 : return number of state variables
!                       5 : inquire matrix properties
!                       6 : calculate elastic material stiffness matrix
!
!  Argument	I/O Type
!  -------- --- ----
!  IDTask   I   I    : see above
!  iMod     I   I    : model number (1..10)
!  IsUndr   I   I    : =1 for undrained, 0 otherwise
!  iStep    I   I    : Global step number
!  iter     I   I    : Global iteration number
!  iel      I   I    : Global element number
!  Intp     I   I    : Global integration point number
!  X        I   R    : X-Position of integration point
!  Y        I   R    : Y-Position of integration point
!  Z        I   R    : Z-Position of integration point
!  Time0    I   R    : Time at start of step
!  dTime    I   R    : Time increment
!  Props    I   R()  : List with model parameters
!  Sig0     I   R()  : Stresses at start of step
!  Swp0     I   R    : Excess pore pressure start of step
!  StVar0   I   R()  : State variable at start of step
!  dEps     I   R()  : Strain increment
!  D       I/O  R(,) : Material stiffness matrix
!  BulkW   I/O  R    : Bulkmodulus for water (undrained only)
!  Sig      O   R()  : Resulting stresses
!  Swp      O   R    : Resulting excess pore pressure
!  StVar    O   R()  : Resulting values state variables
!  ipl      O   I    : Plasticity indicator
!  nStat    O   I    : Number of state variables
!  NonSym   O   I    : Non-Symmetric D-matrix ?
!  iStrsDep O   I    : =1 for stress dependent D-matrix
!  iTimeDep O   I    : =1 for time dependent D-matrix
!  iPrjDir  I   I    : Project directory (ASCII numbers)
!  iPrjLen  I   I	 : Length of project directory name		
!  iAbort   O   I    : =1 to force stopping of calculation
! ----------------------------------------------------------------------------------------
  
  Implicit Double Precision (A-H, O-Z)
  common / iounit / iou
  !Integer			iPrjDir(iPrjLen)
  !Integer           intp
  Double Precision	StVar(nStat)
  Double Precision	Sig(6)
  Double Precision	Sig0(6)
  Double Precision	StVar0(nStat)
  Double Precision	dEps(6)
  Double Precision	D(6,6)
  Double Precision	Props(50)
  Double Precision	DMat(6,6)
  

! ----------------------------------------------------------------------------------------
! Expected contents of Props(1..50)
! 
!  1 : kappa		slope of post yield compression line from e-ln_p'-diagram
!  2 : ny			Poisson's ratio
!  3 : lambda		slope of swelling line from e-ln_p'-diagram
!  4 : M			critical state M value (in triaxial compression)
!  5 : my			absolute effectiveness of rotational hardening
!  6 : beta			relative effectiveness of rotational hardening	
!  7 : a			absolute effectiveness of destructurational hardening
!  8 : b			relative effectiveness of destructurational hardening
!  9 : OCR			overconsolidation ratio
! 10 : POP			pre-overburden pressure like in PLAXIS
! 11 : e0			initial voil ratio
! 12 : alpha0		initial inclination of the yield surface
! 13 : x0			initial bonding effect	
! 14 : StepSize		for controlling the increment size	
! ----------------------------------------------------------------------------------------

  Double Precision	::	kappa	
  Double Precision	::	ny			
  Double Precision	::	lambda	
  Double Precision	::	M	
  Double Precision	::	my		
  Double Precision	::	beta		
  Double Precision	::	a		
  Double Precision	::	b			
  Double Precision	::	OCR
  Double Precision	::	POP
  Double Precision	::	e0	
  Double Precision	::	alpha0			
  Double Precision	::	x0	
  Double Precision  ::  StepSize			

  Double Precision	::	K0nc			! K0 value calculated from M
  Double Precision	::	phi				! phi calculated from M
  Double Precision	::	pm				! p'm = (1+x) * p'mi
  Double Precision	::	pmi				! p'mi = p'm / (1+x)
  Double Precision	::	Kdash			! compression modulus
  Double Precision	::	pdash			! mean effective stress
  Double Precision	::	q				! deviatoric stress
  Double Precision	::	alpha_scalar	! current alpha 
  Double Precision	::	alpha(6)		! current alpha 
  Double Precision	::	alpha_d(6)		! deviatoric fabric tensor
  Double Precision	::	sig_d(6)		! deviatoric stress vector
  Double Precision	::	term(6)			! auxilary vector for evaluation
  Double Precision	::  dGdSig(6)		! auxilary vector of derivatives
  Double Precision	::  dFdSig(6)		! auxilary vector of derivatives
  Double Precision	::  dSigdLam(6)		! auxilary vector of derivatives
  Double Precision	::  dFdad(6)		! auxilary vector of derivatives
  Double Precision	::  daddEpsV(6)		! auxilary vector of derivatives
  Double Precision	::  daddEpsD(6)		! auxilary vector of derivatives
  Double Precision	::  dGdSigD(6)		! auxilary vector of derivatives
  Double Precision	::	xx				! current x 
  Double Precision	::	ee				! current void ratio
  Double Precision	::	alpha_K0		! alpha calculated from K0 and M
  Double Precision	::	eta_K0			! stress ratio for oedometric conditions

  Double Precision	::	dsig(6)			! stress increment
  Double Precision	::	Sig0_mod(6)		! modified initial stress state due to POP/OCR
  Double Precision	::	Sig_trial(6)	! trial stress state
  Double Precision	::	dSig_trial(6)	! trial stress increment

  Double Precision	::	dEps_trial(6)	! target strain increment 
  Double Precision	::	dEps_plastic(6)	! plastic strain increment 
  Double Precision	::	dEpsVol			! plastic volumetric strain increment
  Double Precision	::	dEpsDev(6)		! plastic deviatoric strain increment vector

  Double Precision	::	dpmi			! change of pmi
  Double Precision	::	dad(6)			! change of alpha_d
  Double Precision	::	dxx				! change of xx

  Integer			::	n_sub			! number of subincrements
  Double Precision	::	dEps_sub(6)		! strain increment for subincrementing
  Double Precision	::	dEps_norm		! norm of dEps for subincementing
  Double Precision	::	Sig0_sub(6)		! stress state at start of respective subincr.

  Logical			::	converged		! convergence for iteration
  Integer			::	ipl				! state of plasticity

  Character			::	fname*255		! file name for debugging
  Logical			::	IsOpen			! file status
  
  ! new parameters for NR algorithm
  Double Precision	::  dEpsE(6)
  Double Precision	::  ddEpsE(6)
  Double Precision	::  r1(6)
  Double Precision	::  r1nrm
  Double Precision	::  d2fds2(6,6)
  Double Precision	::  HMat(6,6)
  Double Precision	::  xM77(7,7)
  Double Precision	::  rhs7(7)
  Double Precision	::  xSol(7)
  Double Precision	::  tmp(6)
  Double Precision	::  DdFdS(6)
  Double Precision	::  StVar_tmp(nStat)
  Double Precision	::  xNewStep
  Double Precision	::  pmi_tmp
  Double Precision	::  xx_tmp
  Double Precision	::  FE, Fprev
  
	kappa		= Props(1)		
	ny			= Props(2)		
	lambda		= Props(3)
	M			= Props(4)	
	my			= Props(5)			
	beta		= Props(6)
	a			= Props(7)
	b			= Props(8)	
	OCR			= Props(9)		
	POP			= Props(10)
	e0			= Props(11)			
	alpha0		= Props(12)
	x0			= Props(13)



! ----------------------------------------------------------------------------------------
! calculate stresses
! ----------------------------------------------------------------------------------------
  
   
	  ! initialize StVar for non changing values (others have to be overwritten)
	  
	  Call CopyRVec( StVar0, StVar, nStat ) !StVar = StVar0
	  

	  ipl = 0				! reset plasticity indicator

	  ! subincrementing
	  dEps_norm=sqrt(dEps(1)**2+dEps(2)**2+dEps(3)**2+dEps(4)**2+dEps(5)**2+dEps(6)**2)
	  n_sub=1 ! at least one subincrement
	  !if (StepSize.lt.0.) n_sub=ceiling(dEps_norm/abs(StepSize/1000.)) ! number of subinc. 
	  !if (StepSize.gt.0.) n_sub=StepSize ! number of subincrements by direct input
	  n_sub=ceiling(dEps_norm/abs(1/1000.))
	  n_sub = Max(1,n_sub)
	  dEps_sub=dEps/n_sub ! subincrement
	  Sig0_sub=Sig0 ! stress state at start of subincrementing
	  
	  CALL DStiff(Sig0, kappa,ny,StVar0,nStat,IsUndr, BulkW, DMat)
      D = DMat
      
      
	  Do ii=1,n_sub
	
	  ! first trial for each subincrement (elastic)
	  dEps_trial=dEps_sub

	  ! reset 
	  dEps_plastic=0.		! reset plastic strain increment
	  converged=.false.		! do at least one iteration for each subincrement

			
		converged=.true. ! gets false again during iteration when plasticity occurs
        
		! new trial strain increment
		dEps_trial=dEps_trial - dEps_plastic
        
	    dEps_plastic=0.

		! calculate new trial stress increment dSig_trial=dEps_trial*D
		Call MatVec( DMat, 6, dEps_trial, 6, dSig_trial)
        
      
		! get new trial stress state
		Sig_trial=Sig0_sub+dSig_trial

	    ! get state variables
		alpha_scalar	= StVar(7)
	    xx				= StVar(9)
	    ee				= StVar0(11)	
		pmi				= StVar(8)
		alpha(1:6)		= StVar(1:6)
		
		pmi_tmp = pmi
		xx_tmp  = xx
		
		pm = (1.+xx) * pmi

		! calculate generalized alpha
		alpha_d(1)=	alpha(1) - 1.
		alpha_d(2)=	alpha(2) - 1.
		alpha_d(3)=	alpha(3) - 1.
		alpha_d(4)=	alpha(4) * Sqrt(2.)
		alpha_d(5)=	alpha(5) * Sqrt(2.)
		alpha_d(6)=	alpha(6) * Sqrt(2.)

	    ! calculate stress invariants
	    pdash	= ( Sig_trial(1) + Sig_trial(2) + Sig_trial(3) ) /3

		! calculate generalized deviatoric stress vector sig_d
		sig_d(1)=	Sig_trial(1) - pdash
		sig_d(2)=	Sig_trial(2) - pdash
		sig_d(3)=	Sig_trial(3) - pdash
		sig_d(4)=	Sqrt(2.) * Sig_trial(4)
		sig_d(5)=	Sqrt(2.) * Sig_trial(5)
		sig_d(6)=	Sqrt(2.) * Sig_trial(6)

		! check yield criterion
		!term= sig_d - pdash*alpha_d ! calculating auxilary vector
		!F= 3./2.*(DInProd(term,term,6)) - (M**2.-alpha_scalar**2)*(pm-pdash)*pdash		
		CAll SCLAY_Yield( Sig_trial, alpha,alpha_scalar, M, pm, F)
 If (iounit.Eq.2)	write(4,*) 'F ',F	

		IF (F.Gt.1d-7) Then ! plastic stress correction: associated flow
            
             FE = F
             dEpsE = dEps_sub
		    ! g = f (associated flow)
		    ! sig is positive for compression 
		    
           	
           	s1 = Sig_trial(1)
			s2 = Sig_trial(2)
			s3 = Sig_trial(3)
			s4 = Sig_trial(4)
			s5 = Sig_trial(5)
			s6 = Sig_trial(6)
			
			a1 = alpha(1)
			a2 = alpha(2)
			a3 = alpha(3)
			a4 = alpha(4)
			a5 = alpha(5)
			a6 = alpha(6) 
           
            CALL Get_dFdS( Sig_trial, alpha, M, pm, dFdSig)
 If (iounit.Eq.2)	write(4,*) 'dFdSig ',dFdSig            
			dFdSigX		= dFdSig(1)
			dFdSigY		= dFdSig(2)
			dFdSigZ		= dFdSig(3)
			dFdTauXY	= dFdSig(4)
			dFdTauYZ	= dFdSig(5)
			dFdTauZX	= dFdSig(6)

			dGdSigX		= dFdSigX
			dGdSigY		= dFdSigY
			dGdSigZ		= dFdSigZ
			dGdTauXY	= dFdTauXY
			dGdTauYZ	= dFdTauYZ
			dGdTauZX	= dFdTauZX

			dGdSig(1)	= dGdSigX
			dGdSig(2)	= dGdSigY
			dGdSig(3)	= dGdSigZ
			dGdSig(4)	= dGdTauXY
			dGdSig(5)	= dGdTauYZ
			dGdSig(6)	= dGdTauZX
			
			Call MatVec( D, 6, dGdSig, 6, dSigdLam)
 If (iounit.Eq.2)	write(4,*) 'dSigdLam ',dSigdLam			
			dSigXdLam	= (-1.)*dSigdLam(1)
			dSigYdLam	= (-1.)*dSigdLam(2)
			dSigZdLam	= (-1.)*dSigdLam(3)
			dTauXYdLam	= (-1.)*dSigdLam(4)
			dTauYZdLam	= (-1.)*dSigdLam(5)
			dTauZXdLam	= (-1.)*dSigdLam(6)

			dd = dFdSigX*dSigXdLam + dFdSigY*dSigYdLam + dFdSigZ*dSigZdLam &
				  + dFdTauXY*dTauXYdLam + dFdTauYZ*dTauYZdLam + dFdTauZX*dTauZXdLam
			
			ad1 = alpha_d(1)
			ad2 = alpha_d(2)
			ad3 = alpha_d(3)
			ad4 = alpha_d(4)
			ad5 = alpha_d(5)
			ad6 = alpha_d(6)

			dFdpmi = ((3*ad1**2 + 3*ad2**2 + 3*ad3**2 + 3*ad4**2 + 3*ad5**2 + 3*ad6**2 &
					   - 2*M**2)*(s1 + s2 + s3)*(1 + xx))/6.
			
			dFdad(1)	= ((3*ad1*pm - 2*s1 + s2 + s3)*(s1 + s2 + s3))/3.
			dFdad(2)	= ((3*ad2*pm + s1 - 2*s2 + s3)*(s1 + s2 + s3))/3.
			dFdad(3)	= ((3*ad3*pm + s1 + s2 - 2*s3)*(s1 + s2 + s3))/3.
			dFdad(4)	= (s1 + s2 + s3)*(ad4*pm - Sqrt(2.)*s4)
			dFdad(5)	= (s1 + s2 + s3)*(ad5*pm - Sqrt(2.)*s5)
			dFdad(6)	= (s1 + s2 + s3)*(ad6*pm - Sqrt(2.)*s6)
			
			dFdxx  = ((3*ad1**2 + 3*ad2**2 + 3*ad3**2 + 3*ad4**2 + 3*ad5**2 + 3*ad6**2 &
					   - 2*M**2) *pmi*(s1 + s2 + s3))/6.
			
			dpmidEpsV	= ((1+ee)*pmi)/(lambda-kappa)

			daddEpsV(1)	= my*(-ad1 + (9*(s1 + (-s1 - s2 - s3)/3.))/(4.*(s1 + s2 + s3)))
			daddEpsV(2)	= my*(-ad2 + (9*(s2 + (-s1 - s2 - s3)/3.))/(4.*(s1 + s2 + s3)))
			daddEpsV(3)	= my*(-ad3 + (9*((-s1 - s2 - s3)/3. + s3))/(4.*(s1 + s2 + s3)))
			daddEpsV(4)	= my*(-ad4 + (9*s4)/(2.*Sqrt(2.)*(s1 + s2 + s3)))
			daddEpsV(5)	= my*(-ad5 + (9*s5)/(2.*Sqrt(2.)*(s1 + s2 + s3)))
			daddEpsV(6)	= my*(-ad6 + (9*s6)/(2.*Sqrt(2.)*(s1 + s2 + s3)))

			daddEpsD(1)	= beta*my*(-ad1 + (s1 + (-s1 - s2 - s3)/3.)/(s1 + s2 + s3))
			daddEpsD(2)	= beta*my*(-ad2 + (s2 + (-s1 - s2 - s3)/3.)/(s1 + s2 + s3))
			daddEpsD(3)	= beta*my*(-ad3 + (s3 + (-s1 - s2 - s3)/3.)/(s1 + s2 + s3))
			daddEpsD(4)	= beta*my*(-ad4 + (Sqrt(2.)*s4)/(s1 + s2 + s3))
			daddEpsD(5)	= beta*my*(-ad5 + (Sqrt(2.)*s5)/(s1 + s2 + s3))
			daddEpsD(6)	= beta*my*(-ad6 + (Sqrt(2.)*s6)/(s1 + s2 + s3))

			dxxdEpsV	= -(a*xx)
			dxxdEpsD	= -(a*b*xx)
			
			sd1	= sig_d(1)
			sd2 = sig_d(2)
			sd3 = sig_d(3)
			sd4 = sig_d(4)
			sd5 = sig_d(5)
			sd6 = sig_d(6)

			dGdpdash	= (M**2*(4*pdash - 2*pm) + 3*(ad1**2*pm + ad2**2*pm + ad3**2*pm &
							+ ad4**2*pm + ad5**2*pm + ad6**2*pm - 2*ad1*sd1 - 2*ad2*sd2 &
							- 2*ad3*sd3 - 2*ad4*sd4 - 2*ad5*sd5 - 2*ad6*sd6))/2.
			
			dGdSigD(1)	= 3.*(-(ad1*pdash) + sd1)
			dGdSigD(2)	= 3.*(-(ad2*pdash) + sd2)
			dGdSigD(3)	= 3.*(-(ad3*pdash) + sd3)
			dGdSigD(4)	= 3.*(-(ad4*pdash) + sd4)
			dGdSigD(5)	= 3.*(-(ad5*pdash) + sd5)
			dGdSigD(6)	= 3.*(-(ad6*pdash) + sd6)
						
			aux = Sqrt(2./3.*(DInProd(dGdSigD,dGdSigD,6))) !auxilary scalar
			dGdpdashMac = dGdpdash
			if (dGdpdashMac.lt.0.) dGdpdashMac = 0. !Macauley brackets
			
			hh1 = dFdpmi * dpmidEpsV * dGdpdash
			hh2 = DInProd(dFdad, ((daddEpsV*dGdpdashMac) + (daddEpsD*aux)), 6)	  
			hh3 = dFdxx * ((dxxdEpsV*Abs(dGdpdash)) + (dxxdEpsD*aux))

			hh = hh1 + hh2 + hh3

			dFdLam	= dd + hh

			xLam = -F/dFdLam
 
			! calculate plastic strains
			dEps_plastic = xLam * dGdSig

		    dEpsVol	= dEps_plastic(1) + dEps_plastic(2) + dEps_plastic(3)
			dEpsVolMac = dEpsVol
          
			if (dEpsVolMac.lt.0.) dEpsVolMac = 0. !Macauley brackets

			dEpsDev(1) = (2.*dEps_plastic(1) - dEps_plastic(2) - dEps_plastic(3))/3.
			dEpsDev(2) = (2.*dEps_plastic(2) - dEps_plastic(1) - dEps_plastic(3))/3.
			dEpsDev(3) = (2.*dEps_plastic(3) - dEps_plastic(2) - dEps_plastic(1))/3.
			dEpsDev(4) = Sqrt(2.)*dEps_plastic(4)
			dEpsDev(5) = Sqrt(2.)*dEps_plastic(5)
			dEpsDev(6) = Sqrt(2.)*dEps_plastic(6)

			dEpsDevScalar = Sqrt(2./3.*(DInProd(dEpsDev,dEpsDev,6)))
			
			dEpsE = dEpsE - dEps_plastic
			
			        ! Stress updates Should be before StVar or after StVar?????????????????????????
		            Call MatVec(DMat, 6, dEpsE, 6, dSig )            
                    Call AddVec( Sig0_sub, dSig, 1d0, 1d0, 6, Sig_trial )
                    pdash	 = ( Sig_trial(1) + Sig_trial(2) + Sig_trial(3) ) /3
            
                    ! calculate generalized deviatoric stress vector sig_d
		            sig_d(1) =	Sig_trial(1) - pdash
		            sig_d(2) =	Sig_trial(2) - pdash
		            sig_d(3) =	Sig_trial(3) - pdash
		            sig_d(4) =	Sqrt(2.) * Sig_trial(4)
		            sig_d(5) =	Sqrt(2.) * Sig_trial(5)
		            sig_d(6) =	Sqrt(2.) * Sig_trial(6)
             
			! update state variables
		    dpmi = ((1.+ee)*pmi*dEpsVol)/(lambda-kappa)
			dad = my*(((3.*sig_d)/(4.*pdash)-alpha_d)*dEpsVolMac &
						+ beta*(sig_d/(3.*pdash)-alpha_d)*dEpsDevScalar)
			dxx = -(a*xx*( Abs(dEpsVol) + b*Abs(dEpsDevScalar) ))
              
			StVar(1)	= (alpha_d(1)+dad(1)) + 1.
			StVar(2)	= (alpha_d(2)+dad(2)) + 1.
			StVar(3)	= (alpha_d(3)+dad(3)) + 1.
			StVar(4)	= (alpha_d(4)+dad(4)) / Sqrt(2.)
			StVar(5)	= (alpha_d(5)+dad(5)) / Sqrt(2.)
			StVar(6)	= (alpha_d(6)+dad(6)) / Sqrt(2.)
			StVar(7)	= Sqrt(3./2.*(DInProd((alpha_d+dad),(alpha_d+dad),6)))
			StVar(8)	= pmi + dpmi 
			StVar(9)	= xx + dxx
      		StVar(10)	= (pmi + dpmi) * (1. + (xx+dxx))

			! set convergence criterion
			converged=.false.

			! increase plasticity indicator
			ipl= ipl+1
		  
                ! Newton Rapshon iteration procedures starts    
                IF ( 1 .eq. 1) then
      
                    !write(*,*)'dSig_trial', dSig_trial
            
                    pdash	 = ( Sig_trial(1) + Sig_trial(2) + Sig_trial(3) ) /3
            
                    ! calculate generalized deviatoric stress vector sig_d
		            sig_d(1) =	Sig_trial(1) - pdash
		            sig_d(2) =	Sig_trial(2) - pdash
		            sig_d(3) =	Sig_trial(3) - pdash
		            sig_d(4) =	Sqrt(2.) * Sig_trial(4)
		            sig_d(5) =	Sqrt(2.) * Sig_trial(5)
		            sig_d(6) =	Sqrt(2.) * Sig_trial(6)
            
                    ! get state variables
		            alpha_scalar	= StVar(7)
	                xx				= StVar(9)
	                ee				= StVar0(11)	
		            pmi				= StVar(8)
		            alpha(1:6)		= StVar(1:6)
		  		    
		            pm = (1.+xx) * pmi
		   
                    CAll SCLAY_Yield( Sig_trial, alpha,alpha_scalar, M, pm, F)
 If (iounit.Eq.2)	write(4,*) 'F ',F                    
         
                    CALL Get_dFdS( Sig_trial, alpha, M, pm, dFdSig)
                    
                    ! calculating residual errors
                    r1 = dEps_sub - dEpsE - xLam*dFdSig            
                    
            
                    r1nrm=Sqrt(xDot(r1,r1))    
                               
                    iConv = 0        
                    maxit = 2*25      
                    r1nrm0=  Sqrt(xDot(dEps,dEps))            
                    FTOL = Max( 1D-10 * Abs(F)  , 1D-8 )
                    RTOL = Max( 1D-10 * r1nrm0  , 1D-8 )
                    
           
                        do it=2,maxit
                            
                                  Fprev = F
                            CALL  Get_dFdS( Sig_trial, alpha, M, pm, dFdSig)   
                                  r1 = dEps_sub - dEpsE - xLam*dFdSig
                                  r1nrm=Sqrt(xDot(r1,r1))
                      
                            CALL  MatVec(DMat, 6, dFdSig, 6, DdFdS )                      
                      
                                  delt = 1d-7*pm
                            CALL  Second_dFdS( delt, Sig_trial, alpha,alpha_scalar, M, pm, d2fds2)
                                                        
                      
                            CALL  MatMatSq(6, d2fds2, DMat, HMat)
     
                            DO    i=1,6
                                  Do j=1,6
                                    xM77(i,j) = xLam*HMat(i,j)
                                  End Do
                                  xM77(i,i) = xM77(i,i) + 1
                                  xM77(7,i) = DdFdS(i)
                                  If (i.le.3) xM77(7,i) = xM77(7,i) 
                                  xM77(i,7) =  dFdSig(i)
                                  rhs7(i) =  1 *  r1(i)   !!!!
                            End  Do
          
                                  xM77(7,7) = 0d0
          
                                  rhs7(7) = - F
                      
                            CALL  PivSolv(xM77,7,7,rhs7,xSol,0,iErr)      
                                  
                     
                            IF    (iErr.Gt.0)  Then 
                                  xNewStep = 0.25
                                  Return
                            END   If
                
                                  xom = 1
                            IF    (it.Gt.1111) xom = 0.75
                            IF    (it.Gt.20)   xom = 0.5
                
                            Do    i=1,6
                                  ddEpsE(i) = xom * xSol(i)
                            End   Do
                
                                  dLam = xom * xSol(7)                                         
                                  xLam = xLam+dLam      
                                  !xLam = Max(xLam,0d0)      
                
                                  dEpsE = dEpsE + ddEpsE
                                  dEps_plastic = dEps_sub  - dEpsE  
                
             	                  dEpsVol	= dEps_plastic(1) + dEps_plastic(2) + dEps_plastic(3)
			                      dEpsVolMac = dEpsVol
			                IF    (dEpsVolMac.lt.0.) dEpsVolMac = 0. !Macauley brackets

			                      dEpsDev(1) = (2.*dEps_plastic(1) - dEps_plastic(2) - dEps_plastic(3))/3.
			                      dEpsDev(2) = (2.*dEps_plastic(2) - dEps_plastic(1) - dEps_plastic(3))/3.
			                      dEpsDev(3) = (2.*dEps_plastic(3) - dEps_plastic(2) - dEps_plastic(1))/3.
			                      dEpsDev(4) = Sqrt(2.)*dEps_plastic(4)
			                      dEpsDev(5) = Sqrt(2.)*dEps_plastic(5)
			                      dEpsDev(6) = Sqrt(2.)*dEps_plastic(6)

			                      dEpsDevScalar = Sqrt(2./3.*(DInProd(dEpsDev,dEpsDev,6)))
			                      
			                      ! Stress updates Should be before StVar or after StVar
			                Call  MatVec(DMat, 6, dEpsE, 6, dSig ) 
                            Call  AddVec( Sig0_sub, dSig, 1d0, 1d0, 6, Sig_trial ) 
                                  
                             
                                  pdash	= ( Sig_trial(1) + Sig_trial(2) + Sig_trial(3) ) /3.0
                                              
                                  ! calculate generalized deviatoric stress vector sig_d
		                          sig_d(1)=	Sig_trial(1) - pdash
		                          sig_d(2)=	Sig_trial(2) - pdash
		                          sig_d(3)=	Sig_trial(3) - pdash
		                          sig_d(4)=	Sqrt(2.) * Sig_trial(4)
		                          sig_d(5)=	Sqrt(2.) * Sig_trial(5)
		                          sig_d(6)=	Sqrt(2.) * Sig_trial(6)

			                      ! update state variables
		                          dpmi = ((1.+ee)*pmi_tmp*dEpsVol)/(lambda-kappa)
			                      dad = my*(((3.*sig_d)/(4.*pdash)-alpha_d)*dEpsVolMac &
						                + beta*(sig_d/(3.*pdash)-alpha_d)*dEpsDevScalar)
			                      dxx = -(a*xx_tmp*( Abs(dEpsVol) + b*Abs(dEpsDevScalar) ))
                                                     
			                      StVar(1)	= (alpha_d(1)+dad(1)) + 1.
			                      StVar(2)	= (alpha_d(2)+dad(2)) + 1.
			                      StVar(3)	= (alpha_d(3)+dad(3)) + 1.
			                      StVar(4)	= (alpha_d(4)+dad(4)) / Sqrt(2.)
			                      StVar(5)	= (alpha_d(5)+dad(5)) / Sqrt(2.)
			                      StVar(6)	= (alpha_d(6)+dad(6)) / Sqrt(2.)
			                      StVar(7)	= Sqrt(3./2.*(DInProd((alpha_d+dad),(alpha_d+dad),6)))
			                      StVar(8)	= pmi_tmp + dpmi 
			                      StVar(9)	= xx_tmp + dxx
      		                      StVar(10)	= (pmi_tmp + dpmi) * (1. + (xx_tmp+dxx))
                  		
      		                      ! get state variables
		                          alpha_scalar	= StVar(7)
	                              xx			= StVar(9)
	                              ee			= StVar0(11)	
		                          pmi			= StVar(8)
		                          alpha(1:6)	= StVar(1:6)
                  		        
      		                      pm = (1.+xx) * pmi
      		        
      		             
		
                            CAll  SCLAY_Yield( Sig_trial, alpha,alpha_scalar, M, pm, F)
  If (iounit.Eq.2)	write(4,*) 'F ',F                           
                            IF    (F/FE.Gt.1000) Then                                  
                                  xNewStep = 0.25
                                  Return
                            End If
                                                         
             
                            IF    ( Abs(F) .Lt. FTOL  .And.  r1nrm .Lt. RTOL ) Then                                    
                                  iConv = 1
                                  Goto 2
                            End   If   
            
                        END DO ! it=2..maxIt  N-R iteration
 2           Continue   
  If (iounit.Eq.2) write(4,*) 'dFdSig',dFdSig(1:4)           
                         
            
                    IF   (iConv.Eq.0) Then
                         xNewStep = 0.25  
                         Return
                    End If   
            
                End IF  ! Condition temporarly applied for NR mtd
  
         
        End If  ! F>0
   
 	  ! calculate new global stress state
	  Sig0_sub = Sig_trial
	
	  End Do ! Subincrementing

	  ! set plasticity indicator
	  if (ipl.gt.0) ipl=3     
 
 	  ! calculate new global stress state
	  sig = Sig_trial

	  ! calculate change of volumetric strains
	  dEpsV = (-1.)*(dEps(1) + dEps(2) + dEps(3))

      ! update state variables: current void ratio
      !StVar(11)= StVar0(11)	 !dEpsV*(1.+StVar0(11))+StVar0(11)	
      !change by jpgras
      StVar(11) = dEpsV*(1.+StVar0(11))+StVar0(11)
	  ! calculate pore water pressure
	  If (IsUndr.Eq.1) Then
        dSwp  = BulkW * dEpsV
        Swp   = Swp0 + dSwp
      Else
        Swp = Swp0
      End If

	
	
	 Return

  End Subroutine S_CLAY1S

! ----------------------------------------------------------------------------------------
! calculate material stiffness matrix (D-matrix)
! ----------------------------------------------------------------------------------------

Subroutine DStiff(Sig0, kappa,ny,StVar0,nStat,IsUndr, BulkW, DMat)
    Implicit Double Precision (A-H,O-Z)
   
    Double Precision	StVar0(nStat)
    Double Precision    Sig0(6)
    Double Precision    DMat(6,6)
    Double Precision    ny, xNu
    Double Precision    kappa
    Double Precision    BulkW
    Double Precision    ee
    Double Precision    F1, F2
    Double Precision    E,G
    Double Precision    Fac
    Double Precision    pdash, Kdash
      ! get ny value
	  xNu = ny
   
	  ! determine shear modulus from Youngs' modulus
	  pdash = + ( Sig0(1) + Sig0(2) + Sig0(3) ) /3		! global mean stress
	  if ((pdash.gt.-1.).and.(pdash.le.0.)) pdash=-1.			  
	  if ((pdash.lt.1.).and.(pdash.gt.0.)) pdash=1.			  
	  ee = StVar0(11)									! get current void ratio
	  	  
	  Kdash= (1.+ee)*pdash/kappa						! ...compression modulus	
	  !Kdash= -(1.+e0)*pdash/kappa						! ...compression modulus
	  E= 3.*(1.-(2.*xNu))*Kdash							! E (Young's) from kappa

	  G   = 0.5*E/(1.+xNu)

	  ! compose liner elastic material stiffness matrix
      F1  = 2.*G*(1.-xNu)/(1.-2.*xNu)
      F2  = 2.*G*( xNu )/(1.-2.*xNu)
      Call MZeroR(DMat,36)
      Do i=1,3
        Do j=1,3
          DMat(i,j) = F2
        End Do
        DMat(i,i) = F1
        DMat(i+3,i+3) = G
      End Do

      !calculate bulk modulus
	  BulkW = 0
      If (IsUndr.Eq.1) Then
        xNu_U = 0.495d0
        Fac=(1+xNu_U)/(1-2*xNu_U) - (1+xNu)/(1-2*xNu)
        Fac=2D0*G/3D0  * Fac
        BulkW = Fac
      End If

  
    Return

    End Subroutine DStiff
    
! ----------------------------------------------------------------------------------------
! calculate derivetive of yield function (dFdSig)
! ----------------------------------------------------------------------------------------   
    
    Subroutine Get_dFdS( Sig_trial, alpha, M, pm, dFdSig)
     Implicit Double Precision (A-H,O-Z)
     
    Double Precision ::   Sig_trial(6)
    Double Precision ::   alpha(6)
    Double Precision ::   M
    Double Precision ::   pm
    Double Precision ::   a1,a2,a3,a4,a5,a6
    Double Precision ::   s1,s2,s3,s4,s5,s6
    Double Precision ::   dFdSig(6)
    
            s1 = Sig_trial(1)
			s2 = Sig_trial(2)
			s3 = Sig_trial(3)
			s4 = Sig_trial(4)
			s5 = Sig_trial(5)
			s6 = Sig_trial(6)
			
			a1 = alpha(1)
			a2 = alpha(2)
			a3 = alpha(3)
			a4 = alpha(4)
			a5 = alpha(5)
			a6 = alpha(6)
    
            dFdSig(1)	= (3*(9 - 6*a1 + 3*a1**2 - 6*a2 + 3*a2**2 - 6*a3 + 3*a3**2 &
							+ 6*a4**2 + 6*a5**2 + 6*a6**2 - 2*M**2)*pm - 2*(2*(-9 &
							+ 6*a1 - 3*a2 - 3*a3 - M**2)*s1 + (9 + 3*a1 + 3*a2 &
							- 6*a3 - 2*M**2)*s2 + 9*s3 + 3*a1*s3 - 6*a2*s3 + 3*a3*s3 &
							- 2*M**2*s3 + 18*a4*s4 + 18*a5*s5 + 18*a6*s6))/18.
			dFdSig(2)	= (3*(9 - 6*a1 + 3*a1**2 - 6*a2 + 3*a2**2 - 6*a3 + 3*a3**2 &
							+ 6*a4**2 + 6*a5**2 + 6*a6**2 - 2*M**2)*pm - 2*((9 + 3*a1 &
							+ 3*a2 - 6*a3 - 2*M**2)*s1 - 2*(9 + 3*a1 - 6*a2 + 3*a3 &
							+ M**2)*s2 + 9*s3 - 6*a1*s3 + 3*a2*s3 + 3*a3*s3 &
							- 2*M**2*s3 + 18*a4*s4 + 18*a5*s5 + 18*a6*s6))/18.
			dFdSig(3)	= (3*(9 - 6*a1 + 3*a1**2 - 6*a2 + 3*a2**2 - 6*a3 + 3*a3**2 &
							+ 6*a4**2 + 6*a5**2 + 6*a6**2 - 2*M**2)*pm - 2*((9 + 3*a1 &
							- 6*a2 + 3*a3 - 2*M**2)*s1 + (9 - 6*a1 + 3*a2 + 3*a3 &
							- 2*M**2)*s2 - 2*((9 + 3*a1 + 3*a2 - 6*a3 + M**2)*s3 &
							- 9*(a4*s4 + a5*s5 + a6*s6))))/18.
			dFdSig(4)	= -2*(a4*(s1 + s2 + s3) - 3*s4)
			dFdSig(5)	= -2*(a5*(s1 + s2 + s3) - 3*s5)
			dFdSig(6)	= -2*(a6*(s1 + s2 + s3) - 3*s6)
    
    Return
    
    End Subroutine Get_dFdS
    
! ----------------------------------------------------------------------------------------
! calculate  yield function value (F)
! ----------------------------------------------------------------------------------------   
    
    Subroutine SCLAY_Yield( Sig_trial, alpha,alpha_scalar, M, pm, F)
    Implicit Double Precision (A-H,O-Z)
    
    Double Precision ::   Sig_trial(6)
    Double Precision ::   alpha(6)
    Double Precision ::   M
    Double Precision ::   pm
    Double Precision ::   a1,a2,a3,a4,a5,a6
    Double Precision ::   s1,s2,s3,s4,s5,s6
    Double Precision ::   F
    Double Precision ::   pdash
    Double Precision ::   alpha_d(6)
    Double Precision ::   sig_d(6)
    Double Precision ::   term(6)
    Double Precision ::   alpha_scalar
    
        ! calculate generalized alpha
		alpha_d(1)=	alpha(1) - 1.
		alpha_d(2)=	alpha(2) - 1.
		alpha_d(3)=	alpha(3) - 1.
		alpha_d(4)=	alpha(4) * Sqrt(2.)
		alpha_d(5)=	alpha(5) * Sqrt(2.)
		alpha_d(6)=	alpha(6) * Sqrt(2.)

	    ! calculate stress invariants
	    pdash	= ( Sig_trial(1) + Sig_trial(2) + Sig_trial(3) ) /3
       
		! calculate generalized deviatoric stress vector sig_d
		sig_d(1)=	Sig_trial(1) - pdash
		sig_d(2)=	Sig_trial(2) - pdash
		sig_d(3)=	Sig_trial(3) - pdash
		sig_d(4)=	Sqrt(2.) * Sig_trial(4)
		sig_d(5)=	Sqrt(2.) * Sig_trial(5)
		sig_d(6)=	Sqrt(2.) * Sig_trial(6)

		! check yield criterion
		term= sig_d - pdash*alpha_d ! calculating auxilary vector
		F= 3./2.*(DInProd(term,term,6)) - (M**2.-alpha_scalar**2)*(pm-pdash)*pdash  
 
    
    Return
    
    End Subroutine SCLAY_Yield
    
    
! ----------------------------------------------------------------------------------------
! calculate  second derivatives of yield function (d2fds2)
! ----------------------------------------------------------------------------------------     
 Subroutine Second_dFdS( delta, Sig_trial, alpha,alpha_scalar, M, pm, d2fds2)
    Implicit Double Precision (A-H,O-Z)
    
    Double Precision ::   Sig_trial(6)
    Double Precision ::   SigT(6)
    Double Precision ::   alpha(6)
    Double Precision ::   M
    Double Precision ::   pm   
    Double Precision ::   Fa,Fb,Fc,Fd  
    Double Precision ::   alpha_scalar
    Double Precision ::   delta
    Double Precision ::   d2fds2(6,6)
    
        
     Do i=1,6
        Do j=1,6
          SigT = Sig_trial
          SigT(i)=SigT(i) + delta
          SigT(j)=SigT(j) + delta
          Call SCLAY_Yield( SigT, alpha,alpha_scalar, M, pm, Fa)
          
          SigT = Sig_trial
          SigT(i)=SigT(i) + delta
          SigT(j)=SigT(j) - delta
          Call SCLAY_Yield( SigT, alpha,alpha_scalar, M, pm, Fb)


          SigT = Sig_trial
          SigT(i)=SigT(i) - delta
          SigT(j)=SigT(j) + delta
          Call SCLAY_Yield( SigT, alpha,alpha_scalar, M, pm, Fc)
          
          SigT = Sig_trial
          SigT(i)=SigT(i) - delta
          SigT(j)=SigT(j) - delta
          Call SCLAY_Yield( SigT, alpha,alpha_scalar, M, pm, Fd)
          
          d2FdS2(i,j) = ( (fa-fb) - (fc-fd) ) / (4*delta*delta)
        End Do
      End Do
    
    
    
    Return
    
    End Subroutine Second_dFdS
    
!-----------------------------------------------------------------------+
      Subroutine PivSolv(A,ia,n,f,u,io,iErr)
!-----------------------------------------------------------------------+
! Purpose: Solve system of equations (A*u = f) using pivotting
! Arguments:
!  A    I  R(,)   : Matrix (destroyed on output)
!  ia   I  I      : First dimension of A
!  n    I  I      : Number of equations
!  f    I  R()    : Rhs-vector (unchanged)
!  u    O  R()    : Solution vector
!  iErr O  I      : non-zero gives column of zero pivot
!-----------------------------------------------------------------------+
   Implicit Double Precision (A-H,O-Z)
   Dimension A(ia,*), F(*), u(*), A0(n,n)
!     *          ,A0 (6,6) ,ft(6)
      Do i=1,n
        Do j=1,n
          A0(i,j) = A(i,j)
        End Do
      End Do

!      If (io.Eq.1) write(3,*)'PivSolv'
      Do i=1,n
        u(i) = f(i)
      End Do
      iErr=0
      PivMax=0
     ! If (io.Eq.1) Call Show(A,ia,u,n)
      Do i=1,n
        ! Determine largest absolute value of column i
        iPiv = i
        Do j=i+1,n
          If (Abs(A(j,i)) .Gt. Abs(A(iPiv,i)) ) iPiv = j
        End Do
        If (iPiv.Ne.i) Then ! swap rows/rhs i and iPiv
          Do j=i,n
            X         = A(i,j)
            A(i,j)    = A(iPiv,j)
            A(iPiv,j) = X
          End Do
          X         = u(i)
          u(i)    = u(iPiv)
          u(iPiv) = X
 !         If (io.Eq.1) Call Show(A,ia,u,n)
        End If
        X = A(i,i)
        If (Abs(X).Gt.Abs(PivMax) ) PivMax= X
        If (Abs(X).Lt.1d-10*PivMax) Then
          ! nearly zero pivot found : return with iErr=i
          iErr=i
 !         write(4,*)'ierr=',ierr,' n=',n, abs(x)/abs(pivmax)
          do ii=1,n
            do jj=1,n
 !             write(4,*)ii,jj,a0(ii,jj)
            end do
          end do
          do ii=1,n
 !           write(4,*)ii,f(ii)
          end do
          call flush(2)
!          If (io.Eq.1) write(3,*)'iErr=',iErr
          Return
        End If
        Do j=i,n
          A(i,j) = A(i,j) / X
        End Do
        u(i) = u(i) /X
!        If (io.Eq.1) Call Show(A,ia,u,n)

        ! Subtract row i from other rows such that zero's occur in column i
        Do j=1,n
          If (j.Ne.i) Then
            X = A(j,i)
            Do k=i,n
              A(j,k) = A(j,k) - X * A(i,k)
            End Do
            u(j) = u(j) - X * u(i)
          End If
        End Do
        !If (io.Eq.1) Call Show(A,ia,u,n)
      End Do ! i
     
      Return
      End ! PivSolv

      Subroutine Show(A,ia,u,n)
      Implicit Double Precision (A-H,O-Z)
      Dimension A(ia,*), u(*)
      fac=1
      !write(3,*)
      Do i=1,n
        write(3,901) (fac*a(i,j),j=1,n), fac*u(i)
  901   Format(6(1x,1p,g14.7))
      End Do
      Return
      End
      
      Double precision Function VecLen(A,n)
      Implicit Double Precision (a-h,o-z)
      Dimension A(n)
      x=0
      do i=1,n
        x=x+a(i)*a(i)
      end do
      VecLen=Sqrt(x)
      Return
      End
      
      
      Double Precision Function xDot(a,b)
      Implicit Double Precision (A-H,O-Z)
      Dimension A(6),B(6)

      X =        A(1)*B(1)  &
           +    A(2)*B(2)   &
           +    A(3)*B(3)   &
           +2*( A(4)*B(4)   &
               +A(5)*B(5)   &
               +A(6)*B(6)   &
                          )
      xDot = X
      Return
      End ! xDot

 