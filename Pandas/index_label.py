import pandas as pd
 
# Return the Index label if some condition is satisfied over a column in Pandas Dataframe
data = {'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':['Umbrella', 'Matress', 'Badminton', 'Shuttle'],
                   'Last_Price':[1200, 1500, 1600, 352],
                   'Updated_Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 10, 10, 10]} 
df = pd.DataFrame(data,index = ["Item1","Item2","Item3","Item5"])
index_label = df[df['Updated_Price']>1300].index.to_list()
print(index_label)

# 2nd  way
Index_label = df.query('Updated_Price > 1000').index.tolist()
print(Index_label)