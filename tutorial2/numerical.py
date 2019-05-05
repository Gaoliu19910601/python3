import numpy as np

A = np.array([[5,  6,  2,  3,  3],
              [8,  9,  8,  8,-45],
              [8,  2,  8,  6,  5],
              [4,  1,-12,  1,  2],
              [8,  2, -4, -5,  5]])

b = np.array( [19,-12,29, -4,  6])

Ainv = np.linalg.inv(A)

x = np.linalg.solve(A,b)

print(x)

print(np.allclose(np.dot(A,x),b)) # Checks whether the solution is correct

print(np.dot(A,Ainv)) # This gives an identity matrix I

Eigval,Eigvec = np.linalg.eig(A)

print('The Eigen value of A:',Eigval)

print('The Eigen Vector of A is:',Eigvec)

print('The Determinant of A is:',np.linalg.det(A))