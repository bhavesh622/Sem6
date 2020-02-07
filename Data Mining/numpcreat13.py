# Making an array with 10 zeroes 10 ones and 10 fives
import numpy
p=numpy.zeros(10)
print(p)
p=numpy.append(p,numpy.ones(10))
print(numpy.append(p, numpy.ones(10)*5))
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5.5. 5. 5. 5. 5. 5.]