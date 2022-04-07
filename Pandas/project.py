import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/admin123/Downloads/archive/crime/01_District_wise_crimes_committed_IPC_2001_2012.csv")

df.plot()

plt.show()


