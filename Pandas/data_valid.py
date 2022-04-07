import pandas as pd
import json
a= open("dirty.json")
data = json.load(a)

df = pd.read_csv("/home/admin123/Pandas/dirtydata.csv",error_bad_lines=False)
# print(df)

# df.dropna(inplace=True)

no_of_columns = len(df.columns)
print(no_of_columns)
for i in df.index:
    col_in_row = df.loc[i]
    print(col_in_row)
    if len(col_in_row) != no_of_columns:
        df.drop(i,inplace=True)

# # appending keysa and value of dic into list
# keys = []
# values = []
# for i in data:
#     keys.append(i)
#     values.append(data[i])

# # chceking data type of column and columns value 
# c = 0
# for value in df:
#     if value == keys[c]:
#         i = 0
#         for key in df[value]:
#             if type(values[c]) == int:
#                 if type(key) != type(values[c]):
#                     try:
#                         df[key].astype('i')
#                     except ValueError:
#                         df.drop(df.index[i],inplace = True)
                
#             if type(values[c]) == str:
#                 if type(key) != type(values[c]):
#                     try:
#                         df[key].astype('str')
#                         df.drop(df.index[i],inplace = True)
#                     except ValueError:
#                         df.drop(df.index[i],inplace = True)
#                 else:
#                     try:
#                         df[key].astype('i')
#                         df.drop(df.index[i],inplace = True)
#                     except ValueError:
#                         print("Relax")
                        
#             if type(values[c]) == float:
#                 if type(key) != type(values[c]):
#                     try:
#                         df[key].astype('float')
#                     except ValueError:
#                         df.drop(df.index[i],inplace = True)
                        
#             i+=1   
#     c+=1





















# print(df.loc[0],"ijyul8ij")


# a = df.select_dtypes(include = ['int64','float64'])

# df.drop(df.index[15],axis=0,inplace = True)
# print(df)
# print(df["Pulse"].dtypes)




# df.dropna(inplace=True)
# print(df)

# a = df.select_dtypes(include = ['int64','float64'])
# print(a)
# print(df["Maxpulse"].dtypes=="f")


# checking  datatype of column
# columns = {}
# for name, dtype in df.dtypes.iteritems():
#     columns[name] = dtype
# print(columns)
# for i in range(len(df)):
#     isdif = False
#     for c in columns:
#         print(c, " | ", type(df.loc[i, c]), " | ", columns[c])
#     print("----------------------\n")
    
    
    

    
        # print(type(df.loc[i, c])== columns[c], df.loc[i])
        # if type(df.loc[i, c])!= columns[c]:
        #     isdif = True


# for i in df:
#     col_type =  df[i].dtypes
#     clm=df[i].map(type)
#     c=0
#     for x in df[i]:
#         s=type(x)
#         if type(x) != clm.any():
#             print(type(x) == clm)
#             print(c,"its ajlkmiljiioumuoinyuoinu7obuo;9 x")
#         else:
#             df.drop(df.index[c],inplace = True)
#             print("fina")
#         c+=1



df.to_csv("/home/admin123/Pandas/dirtydata.csv",index=False)
# print(df)



# checking  datatype of column
# data = df.dtypes
# for i in df:
#     #  col_type =  df[i].dtypes
#     a=df[i].map(type)
#     # print(df[i])
#     for x in df[i]:
#         df[i].map(type) != str
#         s=type(x)
#         if type(x) != a:
#             df.drop(df[i],inplace = True)
#             print("fina")
#         else:
#             print("gfghfh")
#             pass
        
#         # print(i,"dhku")
#         # value_type = 
#         # if col_type != value_type:
#         #     df.drop(df[i],inplace = True)
#         # print(type(x)!=a)
     
# We know how to check column's datatype but the problem is:

# Supposed there is a column called ' age' which contains integer datatype and if any single row contains string datatype so all column data is converting automatically to string? 

# So how to get the original data type of the column?
        
# df['ABC'].map(type) != str
       
        # print("")
        # print(type(x))
        # print(type(x)==a,a,x,"kfj")
    # print("++++++++++++++++++++++")
    
    
    
    
    
    
    
    # def check_int(value):
    #     try:
    #     int(value)
    #     return np.NaN
    # except ValueError:
    #     return value


# no_of_row = 
# print(no_of_columns,"hy")
# cl=[]
# for i in a.columns:
#     for x in a.index:
#         if a.loc[x, i] < 0:
#             print(i,"its column")
#             df.drop(x, inplace = True)
#             print("Yes")
# print(df)

# for i,r in df.iterrows():
#     print(r)
# print(df.columns)
# no_of_columns = len(df.columns)
# for i in df.index:
#     col_in_row = df.loc[i]
#     print( col_in_row)
#     print(len(col_in_row) ,no_of_columns)
#     if len(col_in_row) != no_of_columns:
#         print("nu")
#         df.drop(i,inplace=True)
#     else:
#         print("yuo")

        

    
    
# for i,row in df.iterrows():
#     print(i)
#     a = df.loc[i]
#     if ( a < 0).int():
#         df.drop(row, inplace = True)
#         print("done")
        
    # print(df.dtypes,"typpe")
    # if df.dtypes == "int64":
    #     print(row,"hgbghgh")
    #    # if row < 0:
    #     #     df.drop(row, inplace = True)
    #     #     print("yes")
    
    
