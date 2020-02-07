# to compute sum of all elements, sum of each column and sum of each row in an array
import numpy
p=numpy.arange(1,21).reshape(4,5)
print(p)
print(numpy.sum(p))
print(numpy.sum(p,0))
print(numpy.sum(p,1))
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]
# 210
# [34 38 42 46 50]
# [15 40 65 90]