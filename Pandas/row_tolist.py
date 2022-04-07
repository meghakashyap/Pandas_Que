import pandas as pd

# Create a list from rows in Pandas dataframe
  
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})

rows = []
for index,row in df.iterrows():
    my_list =[row.Date,row.Event,row.Cost]
    rows.append(my_list)

print(rows)


# 2nd way
row_list = []
for  row in df.itertuples():
    my_list =[row.Date,row.Event,row.Cost]
    row_list.append(my_list)

print(row_list)
    