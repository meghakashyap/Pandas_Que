import pandas as pd
import numpy as np

arr = np.array([1,23,5,6,7,6])
series = pd.Series(arr)
print(series)

# series with numpy linspace()
ser2 = pd.Series(np.linspace(1, 100, 10))
print("\n", ser2)
  