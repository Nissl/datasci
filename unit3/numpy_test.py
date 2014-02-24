import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2])

print np.dot(b, a)
# seems to be [9, 12, 15], from the class example, but this doesn't work here! Why?

print a
print b