# To test if arrays elements are nan or not

import numpy
p=numpy.array([1,2,numpy.nan])
print(numpy.isnan(p))
# [False False  True]