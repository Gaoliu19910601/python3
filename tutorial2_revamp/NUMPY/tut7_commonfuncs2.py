import numpy as np


A = np.random.randint(3, 8, (6))
B = np.random.randint(4, 9, (6))
mult = A*B

print()
print(A)
print(np.diff(A)) # Consequent difference of A
print(B)
print()
print(A.nonzero()) # gives the indices of nonzero values
print()
print(np.vdot(A, B))
print(mult)

print(np.average(A, weights=B)) # weighted average function
print(np.sum(mult)/np.sum(B)) # Weighted average direct
print()
print(np.average(A)) # Average of matrix
print(np.mean(A)) # Mean of matrix
print(np.median(A)) # Gives the median value of MATRIX
print()
print(np.inner(A, B)) # inner product
C = np.outer(A, B)
print(C) # Outer product
print(C.T) # transpose
print(C.trace()) # trace of matrix
print()



