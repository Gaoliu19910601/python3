#!usr/bin/python3

import numpy as np


amar = []

F0 = 0

F1 = 1

amar.append(F0)

amar.append(F1)


n = int(input("Please enter the value of n: "))

amar2 = np.zeros(n+1,dtype=np.int32)
amar2[1] = F0
amar2[2] = F1

for i in range(2,n):

   a = amar[i-2]+amar[i-1]

   amar.append(a)

   amar2[i+1] = a

   
print(amar)
print(amar2)
   

