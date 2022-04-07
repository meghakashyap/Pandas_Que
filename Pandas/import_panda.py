import pandas as pd
print(pd.__version__)
# print(pd.show_versions(as_json=True))


# 1st
matrix = [["Bharti",22], 
          ["Sheetal", 21], 
          ["Deepa", 20], 
          ["Shehnaz", 19] ] 

x = pd.DataFrame(matrix,columns=["Name","Age"])
# print(x)



# 2nd way
l=[11,22,31,40]
s1=pd.Series(l)
y=pd.DataFrame(s1,columns=["Age"])

y["Name"]=["A","B","C","D"]
# print(y)


# Python | Creating DataFrame from dict of narray/list
dic={"A":["Bharti",22], 
    "B":["Sheetal", 21], 
    "C":["Deepa", 20], 
    "D":["Shehnaz", 19]}

a= pd.DataFrame(dic)
# print(a)

# creating dataframes using list ,tuple
mat = [("Bharti",22), 
          ("Sheetal", 21), 
          ("Deepa", 20), 
          ("Shehnaz", 19) ] 

b=pd.DataFrame(mat,columns=["Name","Token"])
# print(b)

# reset index
myarr=["a","b","c"]
s = pd.Series(myarr) 
# print(s)
df = pd.DataFrame(myarr,index=["a1","b1","c1"])
# df = s.to_frame().reset_index() 
# print(df)

# Change column name ane row indexes
df1=pd.DataFrame({"A":['Megha','Nidhi','Nisha','Rajjo'],
                 "B":[15,26,17,28]})

df1.columns=["Name","Age"]
# print(df1)

df1.index=["r_1","r_2","r_3","r_4"]
# print(df1)


# Selecting rows in pandas DataFrame based on conditions want percenatge <80
record = { 'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ], 'Age': [21, 19, 20, 18, 17, 21], 'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'], 'Percentage': [88, 92, 95, 70, 65, 78] } 
df2=pd.DataFrame(record)
# print(df2)

# 1st way
s=df2[df2.Percentage>80]
# print(s)

# 2nd way
# for i in df2["Percentage"]:
    # if i>80:
    #     print(i)

# select any row using iloc
print(df2.iloc[0:1])



# get the index of max value
m=df2["Percentage"].idxmax()
print(m)

# Get n-largest values from a particular column in Pandas DataFrame 

# 1st
n_l=df2.nlargest(2,["Percentage"])
print(n_l)

# 2nd
n=df2["Percentage"].nlargest(2)
print(n)

