import pandas as pd

# Limited rows selection with given column in Pandas | Python 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 

df = pd.DataFrame(data)
# print(df.head(2))

# 2nd way
print(df.loc[0:3])

# 3rd way
print(df.iloc[0:4])

# iloc[row slicing, column slicing] 
print(df.iloc [0:2,1:3] )
