Informations:

Third parameter: Lambda

On the initiliazition one change, we replace Stvar0 by Stvar, see the code

change the position and number of debug files

Change the calculus of void ratio
      !StVar(11)= StVar0(11)	 !dEpsV*(1.+StVar0(11))+StVar0(11)	
      !change by jpgras
      StVar(11) = dEpsV*(1.+StVar0(11))+StVar0(11)
	  ! calculate pore water pressure
