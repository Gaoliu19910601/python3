! ----------------------------------------------------------------------------------------
! 'S-Clay1S': user-defined soil model for PLAXIS, Wiltafsky (2003)
!  modifications: to LAhey Fortran, Vogler (2006)
!  change subincrementing procedure for Plaxis 8.5, Vogler (2007)
!  Changed to automatic sup-stepping MNR algorithm by Siva (2010)
! ----------------------------------------------------------------------------------------

  Subroutine My_SCLAY	( IDTask, iMod, IsUndr, &
	                      iStep, iTer, iEl, Intp, &
		                  X, Y, Z, &
			              Time0, dTime, &
						  Props, Sig0, Swp0, StVar0, &
		                  dEps, D, BulkW, &
	                      Sig, Swp, StVar, ipl, &
		                  nStat, &
			              NonSym, iStrsDep, iTimeDep, iTang, &
				          iPrjDir, iPrjLen, &						
					      iAbort )
        
  IMPLICIT DOUBLE PRECISION (A-H,O-Z)
  common / SOAbort / iAbortSO
  common / iounit / iou
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
  
  

  Integer			iPrjDir(iPrjLen)
  Double Precision	StVar(nStat)
  Double Precision	Sig(6),Sig_(6)
  Double Precision	Sig0(6),Sig0_(6)
  Double Precision	StVar0(nStat)
  Double Precision	dEps(6),dEps_(6)
  Double Precision	D(6,6)
  Double Precision	Props(50)

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
! Initialize state variables
! ----------------------------------------------------------------------------------------
    If (IDTask .Eq. 1) Then 

!      ! create file name for debugging
!	  fname=' '
!      Do i=1,iPrjLen
!        fname(i:i) = Char( iPrjDir(i) )
!      End Do
!	  fname= fname(:iPrjLen)//'\DATA.usrdbg.RR0'
!
!	  ! open debugging file
!	  Inquire(Unit= 1, Opened= IsOpen)
!	  If (.not.IsOpen) Then
!        Open(Unit= 1, File= fname, Position= 'append')
!        write(3,*)'starting next phase'							
!      End If
!      
!      Open( Unit= 2, File= fname(:iPrjLen)//'DATA.debug.RR0')
!       
!	  ! do IDTask1 only once
!	  If (StVar0(12)==123.) Return
!     
!	  ! create debugging file
!	  If (iEl==1.and.intp==1) Then
!	    Close(Unit= 1, Status= 'delete')
!        Open(Unit= 1,File= fname)
!        write(3,*)'initialization'								
!        Call WriVec(3,' Props...',Props,14)
!	  End If

!change made by jpgras: the debug files are put on a file called Running_files
!their unit number is changed        
      fname= 'Running_files\DATA.usrdbg.txt'        
        
      Inquire(Unit= 3, Opened= IsOpen)
   	  If (.not.IsOpen) Then
        Open(Unit= 3, File= fname, Position= 'append')
        Write(3,*)'starting next phase'							
      End If

      Open( Unit= 4, File = 'Running_files\DATA.debug.RR0')
   	  ! do IDTask1 only once
   	  If (StVar0(12)==123.) Return
      
   	  If (iEl==1.and.inte==1) Then
   	    Close(Unit= 3, Status= 'delete')
         Open(Unit= 3,File= fname)
         Write(3,*)'initialization'								
         Call WriVec(3,' Props...',Props,25)
       End If      
      
      ! checking input variables
	  if ((OCR.ne.0.).and.(POP.ne.0.)) then	! using POP and OCR together is not possible
        write(3,*)'ERROR: using POP and OCR together is not possible'								
	    Stop
	  end if
	  if (POP.lt.0.) then ! POP has to be positive (Compression positive in DLL)
        write(3,*)'ERROR: POP has to be negative (compression=positive in DLL)'								
	    Stop
	  end if
	  if (OCR.lt.0.) then ! negative OCR values are not possible 
        write(3,*)'ERROR: negative OCR values are not possible'								
	    Stop
	  end if
	  if (lambda==kappa) then ! dpmidEpsV not calculable
        write(3,*)'ERROR: dpmidEpsV not calculable - division by zero'								
	    Stop
	  end if

	  ! get K0nc value 
	  phi=asin(3.*M/(6.+M))
	  K0nc=1-sin(phi)
	  
	       
      Sig0(1) = Min(Sig0(1), -1.0d-8 )
	  Sig0(2) = Min(Sig0(2), -1.0d-8 )
      Sig0(3) = Min(Sig0(3), -1.0d-8 )

	  ! provide modified Sig0(1:6) in case of no POP and no OCR
	  Sig0_mod(1)= Sig0(2)*K0nc
	  Sig0_mod(2)= Sig0(2)
	  Sig0_mod(3)= Sig0(2)*K0nc
	  Sig0_mod(4)= 0.
	  Sig0_mod(5)= 0.
	  Sig0_mod(6)= 0.

	  ! write to file
	  If (iEl==1.and.intp==1) Then
        Call WriVec(3,' Sig0....',Sig0_mod,6)
	  End If

	  ! adjust Sig0(1:3) due to POP
	  if (POP.ne.0.) then
	  
        POP = -1*POP ! Change sign of POP to PLAXIS formulation of compression	  
	    
	    Sig0_mod(1)= (Sig0(2)+POP)*K0nc	
	    Sig0_mod(2)= (Sig0(2)+POP)	
	    Sig0_mod(3)= (Sig0(2)+POP)*K0nc	
	  end if

	  ! adjust Sig0(1:3) due to OCR
	  if (OCR.ne.0.) then
	    Sig0_mod(1)= (Sig0(2)*OCR)*K0nc
	    Sig0_mod(2)= (Sig0(2)*OCR)
	    Sig0_mod(3)= (Sig0(2)*OCR)*K0nc
	  end if

      ! change sign due to SCLAY formulation (compression positive)
	  Sig0_mod=(-1.)*Sig0_mod	  
	 
	  
	  ! write to file
	  If (iEl==1.and.intp==1) Then
        Call WriVec(3,' Sig0_mod',Sig0_mod,6)
        write(3,*)' K0nc POP OCR'								
        write(3,'(3(f8.3,x))') K0nc, POP, OCR								
	  End If

	  ! calculate stress invariants
	  pdash	= ( Sig0_mod(1) + Sig0_mod(2) + Sig0_mod(3) ) /3
	  q = sqrt(3./2.*( (Sig0_mod(1)-pdash)**2. + (Sig0_mod(2)-pdash)**2. &
					+ (Sig0_mod(3)-pdash)**2. + 2.*(Sig0_mod(4))**2. &
					+ 2.*(Sig0_mod(5))**2. + 2.*(Sig0_mod(6))**2. ))
	  
      ! checking input variables
	  if ((pdash==0.).or.(M**2.==alpha0**2.)) then	! pm not calculable
        write(3,*)'ERROR: pm not calculable - division by zero'								
	    Stop
	  end if

	  ! determine size of the initial yield curve
	  pm = ( (q-alpha0*pdash)**2. / (pdash*(M**2.-alpha0**2.)) ) + pdash	  
	  pm = Max(2.0d0, pm)
	 
	  !Change made by jpgras, umatwrapper is sending Stvar to incremental driver
      !then we replace StVar0 by stVar
	  ! pre-set state variables
	  StVar(1)	= -(alpha0/3.)+1.		! alpha_x
	  StVar(2)	= (2.*alpha0/3.)+1.		! alpha_y
	  StVar(3)	= -(alpha0/3.)+1.		! alpha_z
	  StVar(4)	= 0.					! alpha_xy
	  StVar(5)	= 0.					! alpha_yz
	  StVar(6)	= 0.					! alpha_zx
	  StVar(7)	= alpha0				! alpha_scalar
	  StVar(8)	= pm/(1.+x0)			! pmi
	  StVar(9)	= x0					! x
	  StVar(10)= pm					! pm
	  StVar(11)= e0					! e_current (current void ratio)
	  StVar(12)= 123.					! initialization is done
	  
	  ! check alpha0 towards alpha_K0
	  eta_K0=3*(1-K0nc)/(1+2*K0nc)
	  alpha_K0=(eta_K0**2+3*eta_K0-M**2)/3
	  
	  ! write to file
	  If (iEl==1.and.intp==1) Then
        Call WriVec(3,' StVar0',StVar0,12)
        write(3,*)' pdash q pm'								
        write(3,'(2x,3(f8.3,x))') pdash, q, pm								
        write(3,*)' alpha0 alpha_K0' 								
        write(3,'(2(f10.5,x))') alpha0, alpha_K0								
	  End If

	  ! output
	  if (iEl==1.and.intp==1) then
	    write (1,*) 'starting first step'	
        write (2,*) 'starting first step'
	  end if
		
    End If  !IDTask = 1
    

! ----------------------------------------------------------------------------------------
! calculate stresses
! ----------------------------------------------------------------------------------------
    If (IDTask .Eq. 2) Then 
   
	   Do i=1,6
          Sig0_(i) = -Sig0(i)
          dEps_(i) = -dEps(i)
          Sig_ (i) = -Sig(i)
        End Do
                
        CALL  S_CLAY1S_Sub	(      IsUndr, &
                                   Props, Sig0_, Swp0, StVar0, &
                                   dEps_, D, BulkW, &
                                   Sig_, Swp, StVar, ipl, &
                                   nStat )
        
        
        
        Do i=1,6
          Sig(i) = -Sig_(i)
        End Do
        
!		write (1,*) 'alpha', StVar(7)	
		

	End If  ! IDTask = 2

! ----------------------------------------------------------------------------------------
! calculate material stiffness matrix (D-matrix)
! ----------------------------------------------------------------------------------------
    If ( IDTask .Eq. 3 .Or. IDTask .Eq. 6 ) Then 
 
      ! get ny value
	  xNu = ny

	  ! determine shear modulus from Youngs' modulus
	  pdash = + ( Sig0(1) + Sig0(2) + Sig0(3) ) /3		! global mean stress
	  if ((pdash.gt.-1.).and.(pdash.le.0.)) pdash=-1.			  
	  if ((pdash.lt.1.).and.(pdash.gt.0.)) pdash=1.			  
	  ee = StVar0(11)									! get current void ratio
	  Kdash= -(1.+ee)*pdash/kappa						! ...compression modulus	
	  !Kdash= -(1.+e0)*pdash/kappa						! ...compression modulus
	  E= 3.*(1.-(2.*xNu))*Kdash							! E (Young's) from kappa

	  G   = 0.5*E/(1.+xNu)

	  ! compose liner elastic material stiffness matrix
      F1  = 2.*G*(1.-xNu)/(1.-2.*xNu)
      F2  = 2.*G*( xNu )/(1.-2.*xNu)
      Call MZeroR(D,36)
      Do i=1,3
        Do j=1,3
          D(i,j) = F2
        End Do
        D(i,i) = F1
        D(i+3,i+3) = G
      End Do

      !calculate bulk modulus
	  BulkW = 0
      If (IsUndr.Eq.1) Then
        xNu_U = 0.495d0
        Fac=(1+xNu_U)/(1-2*xNu_U) - (1+xNu)/(1-2*xNu)
        Fac=2D0*G/3D0  * Fac
        BulkW = Fac
      End If
    
	End If  ! IDTask = 3, 6

! ----------------------------------------------------------------------------------------
! get number of state parameters
! ----------------------------------------------------------------------------------------
    If (IDTask .Eq. 4) Then

	  nStat = 12	! (1)	alpha_x
					! (2)	alpha_y
					! (3)	alpha_z
					! (4)	alpha_xy
					! (5)	alpha_yz
					! (6)	alpha_zx
					! (7)	alpha_scalar
					! (8)	pmi
					! (9)	x
					! (10)	pm
					! (11)	e_current
					! (12)	initialization index

   End If  ! IDTask = 4

! ----------------------------------------------------------------------------------------
! get matrix attributes
! ----------------------------------------------------------------------------------------
    If (IDTask .Eq. 5) Then 

      NonSym   = 0  ! 1 for non-symmetric D-matrix		
      iStrsDep = 1  ! 1 for stress dependent D-matrix	
      iTang    = 0  ! 1 for tangent D-matrix
      iTimeDep = 0  ! 1 for time dependent D-matrix

    End If  ! IDTask = 5

  Return

  End Subroutine My_SCLAY