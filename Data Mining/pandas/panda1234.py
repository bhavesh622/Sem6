import pandas as pd 
a= pd.Series([4,5,6,7,8])
print(a)
print(type(a))
print(a.tolist())
print(type(a.tolist()))
b=pd.Series([2,4,6,8,10])
ds=a+b
print(ds)
ds1=a-b
print(ds1)
ds2=a*b
print(ds2)
ds3=a/b
print(ds3)

# 0    4
# 1    5
# 2    6
# 3    7
# 4    8
# dtype: int64
# <class 'pandas.core.series.Series'>
# [4, 5, 6, 7, 8]
# <class 'list'>
# 0     6
# 1     9
# 2    12
# 3    15
# 4    18
# dtype: int64
# 0    2
# 2    0
# 3   -1
# 4   -2
# dtype: int64
# 0     8
# 1    20
# 2    36
# 3    56
# 4    80
# dtype: int64
# 0    2.000
# 1    1.250
# 2    1.000
# 3    0.875
# 4    0.800
# dtype: float64