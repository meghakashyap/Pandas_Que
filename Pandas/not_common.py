import pandas as pd
import numpy as np

# 7. How to get the items not common to both series A and series B?
# 1st way
ser1 = pd.Series([1, 2, 3, 4, 5]) 
ser2 = pd.Series([4, 5, 6, 7, 8]) 
combine = pd.Series(np.union1d(ser1,ser2)) 
print(combine)
common = pd.Series(np.intersect1d(ser1,ser2))
print(common) 

# 2nd way
df = pd.concat([ser1,ser2])
n_common = ser1[ser1.isin(ser2)]
common = df[~df.isin(n_common)]
print(common)

