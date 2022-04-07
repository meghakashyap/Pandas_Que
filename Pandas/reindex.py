import pandas as pd
# Reindexing in Pandas DataFrame 
index_ = ["r1","r2","r3"]
column = ["Name","Age","City"]
data = [["Megha",20,"Delhi"],
        ["Sneha",21,"Delhi"],
        ["Sudha",22,"Bihar"]]
df = pd.DataFrame(data,columns=column,index=index_)


a=df.reindex(["r2","r1","r3"])
print(a)
# reindex will work on existing index

