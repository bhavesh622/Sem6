# Comparing two arrays for equality, and within a tolerance

import numpy
p= numpy.array([5.000004,7,9])
q=numpy.array([5.0000001,7,9])
print(numpy.equal(p,q))
print(numpy.isclose(p,q))
# [False  True  True]
# [ True  True  True]