# Element wise comparison of two arrays
import numpy
p= numpy.array([5,7,9])
q=numpy.array([7,4,9])
print(numpy.greater(p,q))
print(numpy.greater_equal(p,q))
print(numpy.equal(p,q))
print(numpy.less(p,q))
print(numpy.less_equal(p,q))
# [False  True False]
# [False  True  True]
# [False False  True]
# [ True False False]
# [ True False  True]