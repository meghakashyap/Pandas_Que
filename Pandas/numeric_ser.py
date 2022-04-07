import pandas as pd
import numpy as np

# 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
state = np.random.RandomState(100)
ser = pd.Series(state.normal(10, 5, 25))
df = np.percentile(ser, q=[0, 25, 50, 75, 100])
print(df)