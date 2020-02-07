# Testing if a number is complex, real, scalar
import numpy
p= numpy.array([0,1.2,2,complex(5,7)])
print(numpy.iscomplex(p))
print(numpy.isreal(p))
print(numpy.isscalar(p))
# [False False False  True]
# [ True  True  True False]
# False