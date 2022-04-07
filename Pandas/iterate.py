import pandas as pd

# How to iterate over rows in Pandas Dataframe 


data = {
    "Name":["Neha","Savita","Rani"],
    "Age":[29,45,66]
}
df = pd.DataFrame(data)
for x in df:
    for i in df[x]:
        print(i)
    print("")
    
    
# 2nd way
for index, row in df.iterrows():
    print(index,row['Name'], row['Age'])


 # 3rd way
for row in df.itertuples():
    print(getattr(row, 'Name'), getattr(row, 'Age'))
    
# 4 way
for ind in df.index:
    print(df['Name'][ind], df['Age'][ind])

# 5 way
for i in range(len(df)) :
  print(df.loc[i, "Name"], df.loc[i, "Age"])

