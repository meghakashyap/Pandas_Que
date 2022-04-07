import pandas as pd
  
# Create the dataframe
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})
  

print(df)

Row_list =[]
  
# Iterate over each row
for i in range((df.shape[0])):
    print(df.loc[i])
    Row_list.append(list(df.iloc[i, :]))
  
print(Row_list)