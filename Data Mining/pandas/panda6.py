import pandas as pd 
import numpy as np 
a= np.array([10,20,30,40,50])
b= pd.Series(a)
print(a)
print(b)

# [10 20 30 40 50]
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int32