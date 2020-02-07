# creating vector with values from 0 to 20 and changing signs of numbers in the range of 9 to 15
import numpy
p=numpy.arange(0,21)
print(p)
p[9:16]=numpy.negative(p[9:16])
print(p)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
# [  0   1   2   3   4   5   6   7   8  -9 -10 -11 -12 -13 -14 -15  16  17
#   18  19  20]