import pandas as pd

x=pd.read_csv("mycsv.csv")

# df2 =pd.read_josn("details.json")
# print(df2)
# reading Json file

pd.DataFrame(x)
# this will work in  browser and data will come in readable form
# print(x)

df = pd.read_csv("test.csv") 
df1=df["Exit_date"].fillna("MYVALUE") 
print(df1) 

x=df["id"].mean()
print(x)
# here finding average

a=df[["id","age"]].mean()
print(a)
# Here we are finding average from more than one column

df["Exit_date"].fillna("MYVALUE",inplace=True) 
print(df) 
# replacing nan value using column

df.replace(to_replace="Bharti",value="Bhagya",inplace=True) 
print(df)
# replacing bharti to bhagya

df.fillna("Blank",inplace=True) 
print(df)
# filling empty space with Blank

df["state"] = ['Delhi','Bangalore','Chennai']
print(df)
# creating in column


