      Subroutine MZEROR(R,K)
C
C***********************************************************************
C
C     Function: To make a real array R with dimension K to zero
C
C***********************************************************************
C
      Implicit Double Precision (A-H,O-Z)
      Dimension R(*)

      Do J=1,K
        R(J) = 0.0D0
      End Do

      Return
      End


      Subroutine MZEROI(I,K)
C
C***********************************************************************
C
C     Function: To make an integre array I with Dimension K to zero
C
C***********************************************************************
C
      Dimension I(*)

      Do J=1,K
        I(J)=0
      End Do

      Return
      End

      Subroutine SETRVAL(R,K,V)
C
C***********************************************************************
C
C     Function: To fill a real array R with Dimension K with value V
C
C***********************************************************************
C
      Implicit Double Precision (A-H,O-Z)
      Dimension R(*)

      Do J=1,K
        R(J)=V
      End Do

      Return
      End

      Subroutine SETIVAL(I,K,IV)
C
C***********************************************************************
C
C     Function: To fill an integer array I with Dimension K with value IV
C
C***********************************************************************
C
      Implicit Double Precision (A-H,O-Z)
      Dimension I(*)

      Do J=1,K
        I(J)=IV
      End Do

      Return
      End

      Subroutine COPYIVEC(I1,I2,K)
C
C***********************************************************************
C
C     Function: To copy an integer array I1 with Dimension K to I2
C
C***********************************************************************
C
      Implicit Double Precision (A-H,O-Z)
      Dimension I1(*),I2(*)

      Do  J=1,K
        I2(J)=I1(J)
      End Do

      Return
      End

      Subroutine COPYRVEC(R1,R2,K)
C
C***********************************************************************
C
C     Function: To copy a Double array R1 with Dimension K to R2
C
C***********************************************************************
C
      Implicit Double Precision (A-H,O-Z)
      Dimension R1(*),R2(*)

      Do J=1,K
        R2(J)=R1(J)
      End Do

      Return
      End


      Logical Function IS0ARR(A,N)
C
C***********************************************************************
C    Function :  To check whether a real array contains only zero values.
C                When an array contains only zero's is might not need to be
C                written to the XXX file.
C                exit Function when first non-zero value occured or when
C                all elements are checked and are zero.
C
C    Input:  A : array to be checked
C            N : number of elements in array that should be checked
C
C    Output : .TRUE.  when all elements are 0
C             .FALSE. when at least one element is not zero
C
C    Called by :  Subroutine TOBXX
C
C***********************************************************************
C
      Implicit Double Precision (A-H,O-Z)
      Dimension A(*)
      Is0Arr=.False.
      Do I=1,N
        If ( A(I) .Ne. 0 ) Return
      End Do
      Is0Arr=.True.
      Return
      End

      Logical Function IS0IARR(IARR,N)
C
C***********************************************************************
C    Function :  To check whether a integer array contains only zero values.
C                Similar to IS0ARR
C
C    Input:  IARR : array to be checked
C            N    : number of elements in array that should be checked
C
C    Output : .TRUE.  when all elements are 0
C             .FALSE. when at least one element is not zero
C
C    Called by :  Subroutine TOBXX
C
C***********************************************************************
C
      Implicit Double Precision (A-H,O-Z)
      Dimension IARR(*)

      Is0IArr=.False.
      Do I=1,N
        If ( IARR(I) .Ne. 0 ) Return
      End Do
      Is0IArr=.True.
      Return
      End
C***********************************************************************
      Subroutine MulVec(V,F,K)
C***********************************************************************
C
C     Function: To multiply a real vector V with dimension K by F
C
C***********************************************************************
C
      IMPLICIT DOUBLE PRECISION (A-H,O-Z)
      DIMENSION V(*)

      Do J=1,K
        V(J)=F*V(J)
      End Do

      Return
      End     ! Subroutine Mulvec
C***********************************************************************
      Subroutine MatVec(xMat,IM,Vec,N,VecR)
C***********************************************************************
C
C     Calculate VecR = xMat*Vec
C
C I   xMat  : (Square) Matrix (IM,*)
C I   Vec   : Vector
C I   N     : Number of rows/colums
C O   VecR  : Resulting vector
C
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension xMat(IM,*),Vec(*),VecR(*)
C***********************************************************************
      Do I=1,N
        X=0
        Do J=1,N
          X=X+xMat(I,J)*Vec(J)
        End Do
        VecR(I)=X
      End Do
      Return
      End    ! Subroutine MatVec

C***********************************************************************
      Subroutine AddVec(Vec1,Vec2,R1,R2,N,VecR)
C***********************************************************************
C
C     Calculate VecR() = R1*Vec1()+R2*Vec2()
C
C I   Vec1,
C I   Vec2  : Vectors
C I   R1,R2 : Multipliers
C I   N     : Number of rows
C O   VecR  : Resulting vector
C
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension Vec1(*),Vec2(*),VecR(*)
C***********************************************************************
      Do I=1,N
        X=R1*Vec1(I)+R2*Vec2(I)
        VecR(I)=X
      End Do
      Return
      End    ! Subroutine AddVec
C
C***********************************************************************
      Double Precision Function DInProd(A,B,N)
C***********************************************************************
C
C     Returns the Inproduct of two vectors
C
C I   A,B  : Two vectors
C I   N    : Used length of vectors
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension A(*),B(*)
C***********************************************************************

      X = 0
      Do I=1,N
        X = X + A(I)*B(I)
      End Do
      DInProd = X
      Return
      End     ! Function DInProd
C
C***********************************************************************
      Subroutine MatMat(xMat1,Id1,xMat2,Id2,nR1,nC2,nC1,xMatR,IdR)
C***********************************************************************
C
C     Calculate xMatR = xMat1*xMat2
C
C I   xMat1 : Matrix (Id1,*)
C I   xMat2 : Matrix (Id2,*)
C I   nR1   : Number of rows in resulting matrix    (= No rows in xMat1)
C I   nC2   : Number of columns in resulting matrix (= No cols in xMat2)
C I   nC1   : Number of columns in matrix xMat1
C             = Number  rows    in matrix xMat2
C O   xMatR : Resulting matrix (IdR,*)
C
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension xMat1(Id1,*),xMat2(Id2,*),xMatR(IdR,*)
C**********************************************************************

      Do I=1,nR1
        Do J=1,nC2
          X=0
          Do K=1,nC1
            X=X+xMat1(I,K)*xMat2(K,J)
          End Do
          xMatR(I,J)=X
        End Do
      End Do

      Return
      End     ! Subroutine MatMat

C***********************************************************************
      Subroutine MatMatSq(n, xMat1, xMat2, xMatR)
C***********************************************************************
C
C     Calculate xMatR = xMat1*xMat2 for square matrices, size n
C
C I   n     : Dimension of matrices
C I   xMat1 : Matrix (n,*)
C I   xMat2 : Matrix (n,*)
C O   xMatR : Resulting matrix (n,*)
C
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension xMat1(n,*),xMat2(n,*),xMatR(n,*)
C**********************************************************************

      Do I=1,n
        Do J=1,n
          X=0
          Do K=1,n
            X=X+xMat1(I,K)*xMat2(K,J)
          End Do
          xMatR(I,J)=X
        End Do
      End Do

      Return
      End     ! Subroutine MatMatSq

C***********************************************************************
      Subroutine WriVal ( io, C , V )
C***********************************************************************
C
C Write (Double) value to file unit io (when io>0)
C
C***********************************************************************
C
      Implicit Double Precision (A-H,O-Z)
      Character C*(*)

      If (io.Le.0) Return

      Write(io,*) C,V
    1 Format( A,3x, 1x,1p,e12.5)
      Return
      End
C***********************************************************************
      Subroutine WriIVl ( io, C , I )
C***********************************************************************
C
C Write (integer) value to file unit io (when io>0)
C
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Character C*(*)

      If (io.Le.0) Return

      Write(io,*) C,I
    1 Format( A,3x, 1x,I6)
      Return
      End
C***********************************************************************
      Subroutine WriIVc ( io, C , iV , n )
C***********************************************************************
C
C Write (integer) vector to file unit io (when io>0)
C
C***********************************************************************
      Character C*(*)
      Dimension iV(*)

      If (io.Le.0) Return

      Write(io,*) C
      Write(io,1) (iv(i),i=1,n)
    1 Format( ( 2(3x,5i4) ) )
      Return
      End
C***********************************************************************
      Subroutine WriVec ( io, C , V , n )
C***********************************************************************
C
C Write (Double) vector to file unit io (when io>0)
C 6 values per line
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Character C*(*)
      Dimension V(*)

      If (io.Le.0) Return

      If (Len_Trim(C).Le.6) Then
        Write(io,2) C,( V(i),i=1,n)
      Else
        Write(io,*) C
        Write(io,1) ( V(i),i=1,n)
      End If
    1 Format( ( 2(1x, 3(1x,1p,e10.3) ) ) )
    2 Format( A, ( T7, 2(1x, 3(1x,1p,e10.3) ) ) )
      Return
      End
C***********************************************************************
      Subroutine WriVec5( io, C , V , n )
C***********************************************************************
C
C Write (Double) vector to file unit io (when io>0)
C 5 values per line
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Character C*(*)
      Dimension V(*)

      If (io.Le.0) Return

      Write(io,*) C
      Write(io,1) ( V(i),i=1,n)
    1 Format( 5(1x,1p,e12.5) )
      Return
      End
C***********************************************************************
      Subroutine WriMat ( io, C , V , nd, nr, nc )
C***********************************************************************
C
C Write (Double) matrix to file unit io (when io>0)
C 6 values per line
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Character C*(*)
      Dimension V(nd,*)

      If (io.Le.0) Return

      Write(io,*) C
      Do j=1,nr
        Write(io,1) j,( V(j,i),i=1,nc)
      End Do
    1 Format(i4, (  T7,2(1x, 3(1x,1p,e10.3) ) ) )
      Return
      End
C***********************************************************************

      Subroutine MatInvPiv(Aorig,B,N)
      Implicit Double Precision (A-H,O-Z)
      Dimension Aorig(n,*), B(n,*),A(:,:)
      Allocatable :: A
      Allocate ( A(n,n) ) ! No error checking !!
      Call CopyRVec(AOrig, A, n*n )
      Call MZeroR(B,n*n)
      Do i=1,n
        B(i,i) = 1d0
      End Do
      Do I=1,n
        T=A(I,I)
        iPiv=i
        Do j=i+1,n
          If ( Abs(A(j,i)) .Gt. Abs(A(iPiv,i))  ) iPiv=j
        End Do
        If (iPiv.Ne.i) Then
          Do j=1,n
            x         = A( i  ,j)
            A( i  ,j) = A(iPiv,j)
            A(iPiv,j) = x
            x         = B( i  ,j)
            B( i  ,j) = B(iPiv,j)
            B(iPiv,j) = x
          End Do
          T=A(I,I)
        End If
        Do J=1,n
          A(I,J)=A(I,J)/T
          B(I,J)=B(I,J)/T
        End Do
        Do K=1,n
          If (K.Ne.I) Then
            T=A(K,I)
            Do J=1,n
              A(K,J)=A(K,J)-T*A(I,J)
              B(K,J)=B(K,J)-T*B(I,J)
            End Do
          End If
        End Do
      End Do
      DeAllocate ( A  )
      Return
      End ! MatinvPiv

C***********************************************************************
      Subroutine PrnSig(iOpt,S,xN1,xN2,xN3,S1,S2,S3,P,Q)
C  -- intermediate part: scale maximum stress to 1 unit
C  -- prevent errors for very high/low stresses
      Implicit Double Precision (A-H,O-Z)
      Dimension S(*),St(6),xN1(*),xN2(*),xN3(*)
      ! detemine maximum stress component
      X = 0
      Do j=1,6
        St(j) = S(j)  ! Copy S() to St(), leave S() original
        X = Max ( X, Abs( St(j) ) )
      End Do
      If (X.Eq.0) X = 1 ! Prevent devision by zero
      ! scale stresses such that maximum stress component = +/- 1
      Do j=1,6
        St(j) = St(j) / X
      End Do
      IntGlo = 0
      Call Prn_Sig(IOpt,IntGlo,St,xN1,xN2,xN3,S1,S2,S3,P,Q)
      ! scale stresses back; also Si and P, Q
!      Do j=1,6
!        St(j) = St(j) * X ! not needed as St() is local only,
!                          ! original S() is still intact
!      End Do
      S1 = S1*X
      S2 = S2*X
      S3 = S3*X
      P  = P *X
      Q  = Q *X

      Return
      End ! PrnSig

      Subroutine Prn_Sig(IOpt,IntGlo,S,xN1,xN2,xN3,S1,S2,S3,P,Q)
C***********************************************************************
C
C    Function:  To calculate the principal stresses from the cartesian
C               values. At the same time the princial stress directions
C               are calculated. As a by-product also P and Q are
C               calculated (Note that P is positive for tension !!).
C
C I   IOpt   :   0 : Principal directions not needed
C              <>0 : Also get principal directions
C I   S(i)   : Cartesian stresses (1..6=xx,yy,zz,xy,yz,zx)
C O   xN1,
C O   xN2,
C O   xN3    : Principal directions
C O   S1..S3 : Principal stresses (S1óS2óS3)
C O   P      : Isotropic stress, positive for tension
C O   Q      : Deviatoric stress
C
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension S(*),xN1(*),xN2(*),xN3(*),xNt(3)
      Parameter (Pi23 = 2.09439510239319549230842892d0 ) ! 2*Pi/3
      Parameter (Eps  = 1D-10 )
      Parameter (IP   = -43   )
      Logical LEqual
      Double Precision ArcSin,DInProd
C***********************************************************************
      xnt(1)=0
      xnt(2)=0
      xnt(3)=0
      xx = S(1)
      yy = S(2)
      zz = S(3)
      xy = S(4)
      yz = S(5)
      zx = S(6)
      Sm = (xx+yy+zz)/3
      ASum = (Abs(xx) + Abs(yy) + Abs(zz))/3d0
      P  = Sm
      Q  = 0
      sx = xx-sm
      sy = yy-sm
      sz = zz-sm
      S1 = xx
      S2 = yy
      S3 = zz
      Theta=0
      T  = DSQRT ( (    (xx-yy)**2 +(yy-zz)**2 +(zz-xx)**2
     *               +6*(xy*xy+yz*yz+zx*zx)                 )/3d0 )
      If (T.Gt.1e-10*ASum*ASum) Then
        SBar = t * DSQRT ( 2d0/3d0 )
        xJ3  = sx*sy*sz - sx*yz*yz - sy*zx*zx - sz*xy*xy + 2*xy*yz*zx
        If (dabs(xJ3).Gt.1e-10*dabs(t)*ASum) Then
          Theta= ArcSin(-DSQRT(54d0)*xJ3/(t*t*t),ie)/3d0
!          if (ie.ne.0) then
!            write(4,910) xx,yy,zz,xy,yz,zx
!  910       format('xx,yy..zx :',6(1x,1p,e10.3))
!            write(4,911) sbar,xJ3,t
!  911       format('SBar,xJ3,T:',3(1x,1p,e10.3))
!          end if
        End If ! xJ3> ... *T
c       Pi23 = 2d0*Pi/3d0
        S1 = Sm + SBar * Sin (Theta - Pi23 )
        S2 = Sm + SBar * Sin (Theta        )
        S3 = Sm + SBar * Sin (Theta + Pi23 )
        Q  = 1.5d0*SBar
      Else
!        IF (T.Lt.0) write(4,*)'T<0 ?',T
      End If

c      Prs(1) = S1
c      Prs(2) = S2
c      Prs(3) = S3
!      If (IntGlo.Eq.Ip) write(4,901)'S123',S1,S2,S3

      If (IOpt.Eq.0) Return


      Call MZeroR(xN1,3)
      Call MZeroR(xN2,3)
      Call MZeroR(xN3,3)

      xN1(1) = 1
      xN2(2) = 1
      xN3(3) = 1
      If (LEqual(S1,S2,Eps) .And. LEqual(S2,S3,Eps)) Then
c       write(4,*)'A ',LEqual(S1,S2,Eps),' ',LEqual(S2,S3,Eps)
        Return
      EndIf

      if (1.eq.0) then
        If (LEqual(S1,S2,Eps) .Or. LEqual(S2,S3,Eps)) Then
          If (IntGlo.Eq.IP)
     *      write(4,*)'B ',LEqual(S1,S2,Eps),' ',LEqual(S2,S3,Eps)
          Call PrnDir(IntGlo,S,S1,xN1,1,xNt)
          Call PrnDir(IntGlo,S,S3,xN3,2,xNt)
          Call CrossProd(xN3,xN1,xN2)
        Else
          Call PrnDir(IntGlo,S,S1,xN1,1,xNt)
          Call PrnDir(IntGlo,S,S2,xN2,2,xNt)
          Call CrossProd(xN1,xN2,xN3)
        End If

      else
        If (LEqual(S1,S2,Eps) ) Then
          If (IntGlo.Eq.IP) write(4,*)'S1=S2 ',LEqual(S1,S2,Eps)
          Call PrnDir(IntGlo,S,S3,xN3,1,xNt)
          If (IntGlo.Eq.IP) write(4,901)'xN3',(xN3(J),J=1,3)
          xn2(1)=0
          xn2(2)=0
          xn2(3)=0
          if (abs(xn3(1)).lt.0.5) then
            xn2(1)=1
          else
            xn2(2)=1
          end if
          Call CrossProd(xN3,xN2,xN1)
          call setveclen(xn1,3,1d0)
          If (IntGlo.Eq.IP) write(4,901)'xN1',(xN1(J),J=1,3)
          Call CrossProd(xN3,xN1,xN2)
          If (IntGlo.Eq.IP) write(4,901)'xN2',(xN2(J),J=1,3)
        Else If (LEqual(S2,S3,Eps) ) Then
          If (IntGlo.Eq.IP) write(4,*)'S2=S3 ',LEqual(S2,S3,Eps)
          Call PrnDir(IntGlo,S,S1,xN1,1,xNt)
          If (IntGlo.Eq.IP) write(4,901)'xN1',(xN1(J),J=1,3)
          xn2(1)=0
          xn2(2)=0
          xn2(3)=0
          if (abs(xn1(1)).lt.0.5) then
            xn2(1)=1
          else
            xn2(2)=1
          end if
          Call CrossProd(xN1,xN2,xN3)
          call setveclen(xn3,3,1d0)
          If (IntGlo.Eq.IP) write(4,901)'xN3',(xN3(J),J=1,3)
          Call CrossProd(xN3,xN1,xN2)
          If (IntGlo.Eq.IP) write(4,901)'xN2',(xN2(J),J=1,3)
        Else ! all different
          Call PrnDir(IntGlo,S,S1,xN1,1,xNt)
          Call PrnDir(IntGlo,S,S2,xN2,2,xNt)
          Call CrossProd(xN1,xN2,xN3)
        End If
        xL1 = DInProd(xN1,xN1,3)
        xL2 = DInProd(xN2,xN2,3)
        xL3 = DInProd(xN3,xN3,3)
        xIP1 = DInProd(xN1,xN2,3)
        xIP2 = DInProd(xN2,xN3,3)
        xIP3 = DInProd(xN3,xN1,3)
        xIP  =abs(xIP1)+abs(xIP2)+abs(xIP3)
        if (abs(xl1+xl2+xl3-3+xIP).Gt.0.001) Then
!          write(4,*)'Wrong length or inproduct, intglo=',intglo
!          write(4,901)'xN1',(xN1(J),J=1,3),xL1,xIP1
!          write(4,901)'xN2',(xN2(J),J=1,3),xL2,xIP2
!          write(4,901)'xN3',(xN3(J),J=1,3),xL3,xIP3
        End If
      end if


      xIP1 = DInProd(xN1,xN2,3)
      xIP2 = DInProd(xN2,xN3,3)
      xIP3 = DInProd(xN3,xN1,3)

      IF (xIP1 .Gt. 0.1) Call CrossProd(xN3,xN1,xN2)
      IF (xIP2 .Gt. 0.1) Call CrossProd(xN3,xN1,xN2)
      IF (xIP3 .Gt. 0.1) Call CrossProd(xN3,xN1,xN2)


      If (IntGlo.Eq.Ip) Then
  901   Format(A,6(1x,1p,e12.5))
        xIP1 = DInProd(xN1,xN2,3)
        xIP2 = DInProd(xN2,xN3,3)
        xIP3 = DInProd(xN3,xN1,3)
        write(4,901)'xN1',(xN1(J),J=1,3),xIP1
        write(4,901)'xN2',(xN2(J),J=1,3),xIP2
        write(4,901)'xN3',(xN3(J),J=1,3),xIP3
      EndIf

      Return
      End     ! Subroutine PrnSig
C
C***********************************************************************
      Subroutine PrnDir( IntGlo, S , Si , xN ,it,xNt)
C***********************************************************************
C
C Function : Calculate principal direction (XN) for a given stress (S)
C            and given principal stress (Si)
C
C I   S    : Cartesian stresses (1..6=xx,yy,zz,xy,yz,zx)
C I   Si   : Principal stress
C O   xN   : Principal direction for Si
C                                            | xx  xy  zx |
C Method: Put stresses in stress matrix SM = | xy  yy  yz |
C                                            | zx  yz  zz |
C         Subtract I*Si (SM=SM-I*Si)
C                    | a  b  c |
C               SM = | d  e  f |
C                    | g  h  i |
C         Normalise: one element a..i becomes 1 for row=IRow, col=ICol
C                    | a' 1  c' |  <- IRow
C         i.e.  SM = | d' e' f' |
C                    | g' h' i' |   h'=h/b
C                         ^- ICol
C         Wipe matrix: column ICol contain zeros except at row IRow
C                    | p  1  q |  <- IRow
C         i.e.  SM = | r  0  s |
C                    | t  0  u |
C                         ^- ICol
C         Determine which other row has absolute largest values -> Row J
C         The cross product of rows IRow and J gives the normal vector
C         There is one exception: r, s, t and u are (nearly) zero. In
C         that case we can choose one value (other than ICol) to be 1
C         and the other values 0 i.e. nT = {1,0,0}
C         Finally normalise the normal vector
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension S(*),xN(*),xNt(*)
      Dimension SM(3,3)
      Parameter (Eps = 1D-5 )
      Parameter (Ip  = -43 )
C***********************************************************************

C
C**** Put components of stressvector in matrix and subtract eigenvalue
C
!      If (IntGlo.eq.Ip) write(4,901)'Pr.Sig',Si
      Call MZeroR(SM,9)
      SM(1,1) = S(1) - Si
      SM(2,2) = S(2) - Si
      SM(3,3) = S(3) - Si
      SM(1,2) = S(4)
      SM(2,1) = S(4)
      SM(2,3) = S(5)
      SM(3,2) = S(5)
      SM(1,3) = S(6)
      SM(3,1) = S(6)
!      If (IntGlo.eq.Ip) Then
!        write(4,901)'SM 1j',(SM(1,JJ),JJ=1,3)
!        write(4,901)'SM 2j',(SM(2,JJ),JJ=1,3)
!        write(4,901)'SM 3j',(SM(3,JJ),JJ=1,3)
!        write(4,*)
!      End If

C
C**** Use 2 rows of matrix and determine vector N perpendicular to these
C     rows (cross product). Make sure that not all components of N are 0
C
      IRow= 1
      Piv = 0 ! Find maximum value in array
      Do I=1,3
        Do J=1,3
          If ( Abs(SM(I,J)) .GT. Abs(Piv)) Then
            IRow=I
            ICol=J
            Piv=SM(I,J)
          End If
        End Do
      End Do

c     I=IRow
c     J=1+Mod(IRow,3)
c     I=IRow
c     J1=1+Mod(IRow,3)
c     J2=1+Mod(IRow+1,3)
c     J=J1
c     P1 = DMax1( DAbs(SM(J1,J1)), DAbs(SM(J1,J2)) )
c     P2 = DMax1( DAbs(SM(J2,J2)), DAbs(SM(J2,J1)) )
c     If (P2.GT.P1) J=J2
!      If (IntGlo.eq.Ip) write(4,902)'IJPiv ',IRow,ICol,Piv
  902 Format(A,2I3,5(1x,1p,e12.5))
      Do II=1,3
        Do JJ=1,3
          SM(II,JJ)=SM(II,JJ)/Piv
        End Do
      End Do
!      If (IntGlo.eq.Ip) Then
!        write(4,901)'S" 1j',(SM(1,JJ),JJ=1,3)
!        write(4,901)'S" 2j',(SM(2,JJ),JJ=1,3)
!        write(4,901)'S" 3j',(SM(3,JJ),JJ=1,3)
!      End If
      I=IRow
      J1=1+Mod(IRow  ,3)
      J2=1+Mod(IRow+1,3)
      P=SM(J1,ICol)
      P1=0
      Do I=1,3
        SM(J1,I)=SM(J1,I)-P*SM(IRow,I)
        P1=P1+DAbs(SM(J1,I))
      End Do
      P=SM(J2,ICol)
      P2=0
      Do I=1,3
        SM(J2,I)=SM(J2,I)-P*SM(IRow,I)
        P2=P2+DAbs(SM(J2,I))
      End Do

      I=IRow
      J=J1
      If (P2.Gt.P1) J=J2
      Jmax=J

      xN1 = SM(I,2)*SM(J,3)-SM(I,3)*SM(J,2)
      xN2 = SM(I,3)*SM(J,1)-SM(I,1)*SM(J,3)
      xN3 = SM(I,1)*SM(J,2)-SM(I,2)*SM(J,1)


C
C**** Normalise vector
C
      xNL = DSQRT(xN1*xN1+xN2*xN2+xN3*xN3)
      If (xNL.LT.1E-12) Then
        Call MZeroR(xN,3)
        Jt=1 + Mod(IRow+1,3)
        Jt=JMax
        if (it.gt.1) Then
          if (dabs(xNt(1)).Lt.1e-10) Jt=1
          if (dabs(xNt(2)).Lt.1e-10) Jt=2
          if (dabs(xNt(3)).Lt.1e-10) Jt=3
        End If
        xN( Jt ) = 1
      Else
        xN(1) = xN1/xNL
        xN(2) = xN2/xNL
        xN(3) = xN3/xNL
      End If
      Return
      End     ! Subroutine PrnDir
C
C***********************************************************************
      Logical Function LEqual(A,B,Eps)
C***********************************************************************
C
C     Returns .TRUE.  when two real values are (almost) equal,
C             .FALSE. otherwise
C
C I   A,B  : Two real values to be compared
C I   Eps  : Toleration (Magnitude ~= 1E-5)
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
C***********************************************************************
      LEqual =.True.
      If (A .Eq. B) Return
      If (DAbs(A-B) .LT. 0.5D0*Eps*( DAbs(A) + DAbs(B) + Eps ) )Return
      LEqual =.False.
      Return
      End     ! function LEqual
C
C***********************************************************************
      Subroutine CrossProd(xN1,xN2,xN3)
C***********************************************************************
C
C     Returns cross product of xN1 and xN2
C
C I   xN1,xN2 : Two basic vectors
C O   xN3     : Resulting vector
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension xN1(*),xN2(*),xN3(*)
C***********************************************************************

      xN3(1) = xN1(2)*xN2(3) - xN1(3)*xN2(2)
      xN3(2) = xN1(3)*xN2(1) - xN1(1)*xN2(3)
      xN3(3) = xN1(1)*xN2(2) - xN1(2)*xN2(1)

      Return
      End     ! Subroutine CrossProd
C
C***********************************************************************
      Double Precision Function ArcSin(X,ie)
C***********************************************************************
C
C     Returns the Arc Sine of X
C
C I   X : Input value
C
C     Note : In stead of using default routine DASIN we use this one
C            because ³X³ can be slightly beyond 1 and this will give
C            a RTE using DASIN(X)
C
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
C***********************************************************************
      Ie=0
      S = (1-X*X)
!      If (S .Lt. -1E-10) Ie=1
!      If (S .Lt. -1E-10) Write(*,1) X,S
!      If (S .Lt. -1E-10) write(4,1) X,S
    1 Format(' ArcSin(',1x,1p,e13.5e3,') , S =',1x,1p,e13.5e3)
      If (S.LT.0) S = 0
      S = DSQRT(S)
      ArcSin = DATan2(X,S)
      Return
      End     ! function ArcSin
C
C***********************************************************************
      Subroutine CarSig(S1,S2,S3,xN1,xN2,xN3,SNew)
C***********************************************************************
C
C     Returns the Cartesian stresses using the principal stresses S1..S3
C     and the principal directions
C
C I   S1..S3   : Principal stresses
C I   xN1..xN3 : Principal directions (xNi for Si)
C
C***********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension xN1(*),xN2(*),xN3(*),SNew(*)
      Dimension SM(3,3),T(3,3),TT(3,3),STT(3,3)
C***********************************************************************
C
C**** Fill transformation (rotation) matrix
C
      Do I=1,3
        T(I,1) = xN1(I)
        T(I,2) = xN2(I)
        T(I,3) = xN3(I)
        TT(1,I) = T(I,1)
        TT(2,I) = T(I,2)
        TT(3,I) = T(I,3)
      End Do
!      Call MatTranspose(T,3,TT,3,3,3)

      Call MZeroR(SM,9)
      SM(1,1) = S1
      SM(2,2) = S2
      SM(3,3) = S3
C
C**** SMnew = T*SM*TT
C
      Call MatMat(SM ,3,  TT,3 , 3,3,3 ,STT,3)
      Call MatMat( T ,3, STT,3 , 3,3,3 ,SM ,3)
!     Call MatMatSq(3, SM,  TT, STT )   ! STT = SM*TT
!     Call MatMatSq(3,  T, STT, SM  )   ! SM  =  T*STT
C
C**** Extract cartesian stress vector from stress matrix
C
      Do I=1,3
        SNew(I) = SM(I,I)
      End Do
      SNew(4) = SM(2,1)
      SNew(5) = SM(3,2)
      SNew(6) = SM(3,1)

      Return
      End     ! Subroutine CarSig
C**********************************************************************
      subroutine setveclen(xn,n,xl)
C**********************************************************************
      Implicit Double Precision (A-H,O-Z)
      Dimension xN(*)
      x=0
      do i=1,n
        x=x+xn(i)**2
      end do
      if (x.Ne.0) Then
        f=xl/sqrt(x)
        do i=1,3
          xn(i)=xn(i)*f
        end do
      end if
      return
      end ! setveclen

C**********************************************************************
C End Of file
C**********************************************************************
