import numpy as np 
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(type(a))
print(a.shape)
b =np.array(a[:2, 1:3])
b[0,0]=77
print(a)
print(b)