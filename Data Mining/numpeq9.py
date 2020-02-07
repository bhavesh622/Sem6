# Checking if two arrays are equal within a certain limit
import numpy
p= numpy.array([5.000004,7,9])
q=numpy.array([5.0000001,7,9])
print(numpy.isclose(p,q))
# [ True  True  True]