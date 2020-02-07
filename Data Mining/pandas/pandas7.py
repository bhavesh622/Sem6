import pandas as pd 
a = pd.Series([100, 200,'python', 300.12, 400])
print(a)
b = pd.to_numeric(a,errors="coerce")
b = pd.to_numeric(a,errors="coerce")

# 0       100
# 1       200
# 2    python
# 3    300.12
# 4       400
# dtype: object
# 0    100.00
# 1    200.00
# 2       NaN
# 3    300.12
# 4    400.00
# dtype: float64