import pandas as pd

# Convert a column to row name/index in Pandas

data = {'Name':["Akash", "Geeku", "Pankaj", "Sumitra","Ramlal"],
       'Branch':["B.Tech", "MBA", "BCA", "B.Tech", "BCA"],
       'Score':["80","90","60", "30", "50"],
       'Result': ["Pass","Pass","Pass","Fail","Fail"]}

df = pd.DataFrame(data)
df.index.names = ["Index"]
print(df)