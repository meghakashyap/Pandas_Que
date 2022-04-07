import pandas as pd
import numpy as np

# 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
print("Top 2 Freq:", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
print(ser)
