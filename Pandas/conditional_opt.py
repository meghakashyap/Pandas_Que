import pandas as pd

# Conditional operation on Pandas DataFrame columns
data = {'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':['Umbrella', 'Matress', 'Badminton', 'Shuttle'],
                   'Last Price':[1200, 1500, 1600, 352],
                   'Updated Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 10, 10, 10]}
df = pd.DataFrame(data)
# print(df['Updated Price']*0.1)

if 'Updated Price' in df.columns:
    df['Final cost'] = df['Updated Price'] - (df['Updated Price']*0.1)
  
else :
    df['Final cost'] = df['Last Price'] - (df['Last Price']*0.1)

print(df)