import pandas as pd

# How to get column names in Pandas dataframe 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 

df = pd.DataFrame(data)

# 1st way
for i in df.columns:
    print(i)
    
# 2nd way
print(list(df.columns))

# 3rd way
print(list(df.columns.values.tolist()))