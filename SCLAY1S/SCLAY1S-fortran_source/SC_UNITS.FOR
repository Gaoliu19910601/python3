      Subroutine S_CLAY1S_Sub	(   IsUndr, 
     *                          Props, Sig0, Swp0, StVar0, 
     *                          dEps, D, BulkW, 
     *                          Sig, Swp, StVar, ipl, 
     *                          nStat )
      Implicit Double Precision (A-H, O-Z)
     
        Double Precision	StVar(nStat)
        Double Precision	Sig(6)
        Double Precision	Sig0(6)
        Double Precision	StVar0(nStat)
        Double Precision	StVarT(nStat)
        Double Precision	dEps(6)
        Double Precision	D(6,6)
        Double Precision	Props(50)
        Double Precision	DMat(6,6)
  
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
        Double Precision    ::  StepSize			

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

        Integer			    ::	n_sub			! number of subincrements
        Double Precision	::	dEps_sub(6)		! strain increment for subincrementing
        Double Precision	::	dEps_norm		! norm of dEps for subincementing
        Double Precision	::	Sig0_sub(6)		! stress state at start of respective subincr.

        Logical			    ::	converged		! convergence for iteration
        Integer			    ::	ipl				! state of plasticity

        Character			::	fname*255		! file name for debugging
        Logical			    ::	IsOpen			! file status
     
       common / iounit / iou 
      ! Local variables
      Dimension 
     *          DInv(6,6),              ! elastic flexibility matrix
     *          SigE(6),                ! elastic trial stress
     *          Sig_C(6),               ! preconsolidation stress
     *          Eta_C(6),               ! normalised preconsolidation
     *          Sdev(6),
     *          dEpsE(6),               ! unknown elastic strain inc.
     *          dEpsT(6),
     *          SigT(6),
     *          SigET(6),
     *          ddEpsE(6),
     *          dFdS(6),                ! dF_dSig, deriv yield function
     *          DdFdS(6),               ! = D_e * dFdS
     *          s_bn(6),
     *          dEpsP(6),               ! Plastic strain increment
     *          r1(6),                  ! 'unbalance'
     *          d2fds2(6,6),
     *          HMat(6,6),
     *          xM77(7,7),
     *          rhs7(7),
     *          xSol(7),
     *          tmp(6)
     
      
      iAllowSubStepping = 1
      If (iAllowSubStepping.Eq.1) Then
        T0 = 0
        dT = 1

        SigT = Sig0
        dEpsT = dT * dEps
        StVarT = StVar0
        Sig=Sig0
        iCalls=0
   1    Continue
        !write(*,*)'T, dT', T0, dT
        !if (iou.gt.0) write(iou,*)'SO_get_Sig1 ',dT
        xNewStep = 1
        if (dt.lt.-0.999) stop
          
          !SigET = SigT + MatMul(DMat,dEpsT)
          iCalls=iCalls+1
     
          CALL S_CLAY1S	( IsUndr, 
     *                    Props, SigT, Swp0, StVarT, 
     *                    dEpsT, D, BulkW, 
     *                    Sig, Swp, StVar, ipl, 
     *                    nStat,xNewStep )
       

        If (xNewStep.Lt. 0.999) Then

          dT    = xNewStep * dT
          dEpsT = dT       * dEps
          If (dT.Gt.0.0001) Then
            goto 1
          Else
           

            CALL S_CLAY1S	( IsUndr, 
     *                    Props, SigT, Swp0, StVarT, 
     *                    dEpsT, D, BulkW, 
     *                    Sig, Swp, StVar, ipl, 
     *                    nStat,xNewStep )

            iAbortSO=29
            if (iou.gt.0) then
              
              call flush(iou)
            Else
              !write(3,*)'too small step ??'
              call flush(1)
            end if
            return
            !write(iou,*)'too small step ??'
            stop

          End If
        Else
          if (dt.lt.-0.9999) Then
            !call check_sosig(eta0,eta_c)
!            SigE = Sig0 + MatMul(DMat,dEps)
!            iCalls=iCalls+1

            CALL S_CLAY1S	( IsUndr, 
     *                    Props, SigT, Swp0, StVarT, 
     *                    dEpsT, D, BulkW, 
     *                    Sig, Swp, StVar, ipl, 
     *                    nStat,xNewStep )
     
          end if
        End If
        T0   = T0 + dT
        If (T0.Lt. 0.99999) Then
          dT       = 1-T0
          dEpsT    = dT * dEps
          SigT     = Sig
          StVarT   = StVar
          Goto 1
        End If
     
        Return
      End If


      Return
      End  ! SO_Get_Sig


      


      
