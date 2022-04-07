import pandas as pd
import numpy as np

# 13. How to find the positions of numbers that are multiples of 3 from a series

ser = pd.Series(np.random.randint(1, 10, 7))
print(ser)
np.argwhere(ser % 3==0)
print(np)


# left