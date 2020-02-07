#Checking for positive/negative infinite values
#  
import numpy
p=numpy.array([0,1,2,numpy.nan,numpy.inf])
print(numpy.isinf(p))
# [False False False False  True]