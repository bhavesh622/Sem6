# to add vector to each row of a given matrix
import numpy
p=numpy.array([1,2,3])
q=numpy.arange(1,16).reshape(5,3)
print(p)
print(q)
q+=p
print(q)
# [1 2 3]
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]
#  [13 14 15]]
# [[ 2  4  6]
#  [ 5  7  9]
#  [ 8 10 12]
#  [11 13 15]
#  [14 16 18]]