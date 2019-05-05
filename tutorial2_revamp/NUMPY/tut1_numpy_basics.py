
import numpy as np


list = [1., 2., 3., 4., 5., 6.]

array = np.array(list, dtype='float64')

print(array)

list2 = [[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]

array2 = np.array(list2)

print()
print(array2)
print(array2.itemsize)
print(array2.ndim)
print(array2.shape)
print(array2.size)
print(array2.dtype.name)
print(type(array2))

print()
array3 = np.zeros((5, 3), dtype='float64')
array4 = np.ones((5, 3), dtype='float64')
array5 = np.empty((5, 3), dtype='float64')

print(array3)
print()
print(array4)
print()
print(array5)

ind = np.indices((5, 3), dtype='float32')

print(ind)
print()

iden = np.eye(5)

print(iden)
print()

iden2 = np.identity(5, dtype='int64')

print(iden2)
print()

