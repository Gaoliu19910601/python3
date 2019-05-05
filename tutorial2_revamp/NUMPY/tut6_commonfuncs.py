import numpy as np

A = np.random.randint(2, 15, (3, 3))

print(A)

print(A.max(), A.min())

print(A.argmax()) # Gives the index for the maximum value

print(A.max(axis=1), A.max(axis=0)) # Axis=1 searches the row and Axis=0 searches the column for maximum value and reurns an array

B = A.flatten()

print()
print(B) # Flattens the matrix A
print(A.cumsum()) # Cumulative sum of A - check with B
print(np.sort(B)) # Sorts the values in B in ascending order
print(np.argsort(B)) # Sorts the indices in B  w.r.t.  np.sort(B)

print()
print(A.mean()) # for total matrix
print(A.sum()/9)
print()
print(A.mean(axis=1)) # for each row
print(A.mean(axis=0)) # for each column
print()
print(A.sum(axis=1)/3) # for each row
print(A.sum(axis=0)/3) # for each column
print()
print(A.var()) # Variance of matrix A
print(A.std()) # Standard deviation of matrix A

