# To create  a 4x4 matrix in which 0 and 1 are staggered , with zeroes on the main diagonal
import numpy
p=numpy.zeros((4,4))
p[::2, 1::2] = 1
p[1::2, ::2] = 1
print(p)
# [[0. 1. 0. 1.]
#  [1. 0. 1. 0.]
#  [0. 1. 0. 1.]
#  [1. 0. 1. 0.]]