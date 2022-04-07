import  pandas as pd

# 4. How to combine many series to form a dataframe?

ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series(["a","b","c","d","e"])
df = pd.DataFrame({"Serial":ser1,"Alpha":ser2})
print(df)

# using concat function
df1 = pd.concat([ser1,ser2],axis=1)
print(df1)

a =[[1,2,3,4],['A','B',"c",'D']]
d =pd.DataFrame(a,columns=["No","Name",'Age','Sum'])
print(d)
