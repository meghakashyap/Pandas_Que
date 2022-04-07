import pandas as pd

# Python | Change column names and row indexes in Pandas DataFrame 

data = {
    "A":["Neha","Savita","Rani"],
    "B":[29,45,66]
}
df = pd.DataFrame(data)
df.columns=["Name","Age"]
df.index=["Row1","Row2","Row3"]
print(df)