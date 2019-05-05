
import numpy as np

A = np.ones((5, 3), dtype='float64')

B = 5.0*np.ones((5, 3), dtype='float64')

C = np.random.randint(-5, 5, (3, 3))

print(A+B)
print(A*B)
print(A/B)
print(A-B)
print(1.5*A)

print((1.5*A)**B)
print(1.5**5)

print(np.dot(A, B.T))

print(C)
print()
print(np.linalg.inv(C))
print()
print(np.dot(C, np.linalg.inv(C)))

eigval, eigvec = np.linalg.eig(C)
print()
print(eigval)
print()
print(eigvec)
