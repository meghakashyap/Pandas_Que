import pandas as pd
import numpy as np

# # converting index  series into column
# mylist = list('abcedfghijklmnopqrstuvwxyz')
# myarr = np.arange(26)
# mydict = dict(zip(mylist, myarr))
# ser = pd.Series(mydict)

# # Solution
# df = ser.to_frame().reset_index()
# print(df)


# 2.converting series
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

s1= pd.Series(mylist)
s2=pd.Series(myarr)
s3=pd.Series(mydict)
print(s1)
print(s2)
print(s3)

# 3.converting index  series into column
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mylist)

x=pd.DataFrame(ser,columns=index)# Input mylist = list('a# Input 
mylist = list('abcedfghijklmnopqrstuvwxyz') 
print(mylist) 
myarr = np.arange(26) 
x = dict(zip())
print(x)

s = pd.Series(x) 
print(s) 
df = s.to_frame().reset_index() 
print(df) 

# Input mylist = list('abcedfghijklmnopqrstuvwxyz') print(mylist) myarr = np.arange(26) x = dict(zip()) print(x) s = pd.Series(x) print(s) df = s.to_frame().reset_index() print(df) # Input mylist = list('abcedfghijklmnopqrstuvwxyz') print(mylist) myarr = np.arange(26) x = dict(zip()) print(x) s = pd.Series(x) print(s) df = s.to_frame().reset_index() print(df) bcedfghijklmnopqrstuvwxyz') print(mylist) myarr = np.arange(26) x = dict(zip()) print(x) s = pd.Series(x) print(s) df = s.to_frame().reset_index() print(df) 
print(x)

# Input
mylist = list('abcedfghijklmnopqrstuvwxyz') 
print(mylist) 
myarr = np.arange(26) 
x = dict(zip()) 
print(x) 
s = pd.Series(x) 
print(s)
df = s.to_frame().reset_index() 
print(df) 

# not present in ser1
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# 7. How to get the items not common to both series A and series B?
import numpy as np 
import pandas as pd 
ser1 = pd.Series([1, 2, 3, 4, 5]) 
ser2 = pd.Series([4, 5, 6, 7, 8]) 
combine=pd.Series(np.union1d(ser1,ser2)) 
print(combine)
common = pd.Series(np.intersect1d(ser1,ser2))
print(common) 