import pandas as pd

# Drop rows from the dataframe based on certain condition applied on a column
df = pd.read_csv("mycsv.csv")
df.drop(df[df["Duration"]<60].index,inplace=True)
print(df)
