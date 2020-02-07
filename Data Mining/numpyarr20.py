# to create a 3x4 array and iterate over it
import numpy
p=numpy.arange(2,14).reshape(3,4)
print(p)
for x in numpy.nditer(p):
    print(x)
# [[ 2  3  4  5]
#  [ 6  7  8  9]
#  [10 11 12 13]]
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13