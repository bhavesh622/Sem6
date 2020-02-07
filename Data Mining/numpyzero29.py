# Creating a zero matrix with elements on the main diagonal equal to 1, 2, 3, 4 ,5
import numpy
p=numpy.zeros((5,5))
print(p)
numpy.fill_diagonal(p,[1,2,3,4,5])
print(p)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
# [[1. 0. 0. 0. 0.]
#  [0. 2. 0. 0. 0.]
#  [0. 0. 3. 0. 0.]
#  [0. 0. 0. 4. 0.]
#  [0. 0. 0. 0. 5.]]