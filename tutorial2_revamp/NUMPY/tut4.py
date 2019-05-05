
import numpy as np


x = np.arange(-4.0, 5.0, 1)
y = np.arange(-5.0, 6.0, 1)

# print(x)
# print(y)

# This shows a 1-D struct but retains the 2D result
xx,  yy = np.meshgrid(x, y, sparse=True)
# xx1, yy1 = np.meshgrid(x, y, indexing='ij')# Transpose of each values of xx and yy


# print(xx)
# print(yy)

ellipse = xx**2+yy**2

# print(ellipse) # Proves the point that the result is 2D for sparse=True

# xx1, yy1 = np.mgrid[-5:5:1, -4:4:1] # gives integer values [arange operation]
# xx1, yy1 = np.mgrid[-5:5:1., -4:4:1.] # gives float values
xx1, yy1 = np.mgrid[-5:5:11j, -4:4:9j] # gives linspace operation


print(xx1)
print()
print(yy1)
print()
print(xx1.shape)
print(yy1.shape)

xx2, yy2 = np.ogrid[-5:5:11j, -4:4:9j] # gives sparse of mgrid


print(xx2)
print()
print(yy2)
print()

print(xx2.shape)
print(yy2.shape)


xx3, yy3 = np.broadcast_arrays(xx2, yy2) # Changes into nonsparsed form


print(xx3)
print()
print(yy3)
print()

print(xx3.shape)
print(yy3.shape)
