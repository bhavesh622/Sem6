# Testing an array for finiteness

import numpy
p= numpy.array([[5,6],[numpy.inf,9]])
print(numpy.isfinite(p))
# [[ True  True]
#  [False  True]]