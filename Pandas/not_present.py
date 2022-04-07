import pandas as pd

# 6. How to get the items of series A not present in series B
a = pd.Series([1,2,3,4,5])
b = pd.Series([3,4,5,7,8])
df = a[~a.isin(b)]
print(df)

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
a=ser1[~ser1.isin(ser2)]
print(a)
