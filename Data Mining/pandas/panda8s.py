import pandas as pd 
a= pd.DataFrame({'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]})
print(a)
b=pd.Series(a.col1)
print(b)

#    col1  col2  col3
# 0     1     4     7
# 1     2     5     5
# 2     3     6     8
# 3     4     9    12
# 4     7     5     1
# 5    11     0    11
# 0     1
# 1     2
# 2     3
# 3     4
# 4     7
# 5    11