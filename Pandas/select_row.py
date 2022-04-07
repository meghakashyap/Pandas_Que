import pandas as pd


# Selecting rows in pandas DataFrame based on conditions
record = {
 'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
 'Age': [21, 19, 20, 18, 17, 21],
 'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
 'Percentage': [88, 92, 95, 70, 65, 78] }
  
# create a dataframe
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
result = dataframe[dataframe["Percentage"]>70]
print(result)

# 2nd  selecting rows based on condition
rslt_df = dataframe.loc[dataframe['Percentage'] > 80]
print('\nResult dataframe :\n', rslt_df)


# 3rd
options = ['Math', 'Commerce']
rslt_df = dataframe[dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)