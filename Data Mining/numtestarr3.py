# Checking if none of the elements are 0 in an array

import numpy
p= numpy.array([0,5,6,7])
print(p)
q= numpy.array([1,2,3,4])
print(q)
print(numpy.all(p))
print(numpy.all(q))

# [0 5 6 7]
# [1 2 3 4]
# False
# True