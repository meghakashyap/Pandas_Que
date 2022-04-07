import pandas as pd


# Collapse multiple Columns in Pandas 
col_1 = ['Manan ', 'Raghav ', 'Sunny ','Megha']
col_2 = ['Goel', 'Sharma', 'Chawla','Kashyap']
col_3 = [12, 24, 56, 20]

mapping = {'First_Name': col_1,'Last_Name': col_2, "Age":col_3}
df = pd.DataFrame(mapping)
print(df)
  
  
# 2nd way
df = pd.DataFrame({'First': ['Manan ', 'Raghav ', 'Sunny '],
                   'Last': ['Goel', 'Sharma', 'Chawla'],
                   'Age':[12, 24, 56]})
  
mapping = {'First': 'Full Name', 'Last': 'Full Name'}
  
df = df.set_index('Age').groupby(mapping, axis = 1).sum()
print(df)
  
df.reset_index(level = 0)
print(df)