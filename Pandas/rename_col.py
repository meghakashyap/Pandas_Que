import pandas as pd

# How to rename columns in Pandas DataFrame 
data = {'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]}
df = pd.DataFrame(data)

# 1st way
df.rename(columns = {"Event":"Program"},inplace = True)
print(df.columns)
print(df)

# 2nd way
df.columns = ["Date","Program","Cost"]
print(df)