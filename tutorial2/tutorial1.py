import numpy as np

F0 = 0

F1 = 1

n = 50

amar = []

amar.append(F0)
amar.append(F1)

amar2 = np.zeros(n+1,dtype=np.int32)
amar2[1] = F0
amar2[2] = F1

for i in range(2,n):
    a = amar[i-1]+amar[i-2]
    amar.append(a)
    amar2[i+1] = a




print(amar)
print(amar2)
