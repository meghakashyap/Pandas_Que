import pandas as pd

# l=list("abcdefghijklmnopqrstuvwxyz")
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# Solution
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)

print(ser3.head())

# agian
import pandas as pd
import numpy as np 
x = np.array([10,61,78,91]) 
s = pd.Series(x) 
print(s) 


# giving name to the index
import pandas as pd 
import numpy as np 
x = np.array([10,61,78,91]) 
s = pd.Series(x,index=['first','second','third','fourth'])
print(s)

# creating static series by defining the length  of index
import pandas as pd 
import numpy as np 
s = pd.Series(50,index=[0,1,2,3]) 
print(s) 

# using head printing top 2 rows(bydefault 5 rows of top will print)
import pandas as pd 
import numpy as np 
a = np.array([10,15,61,78,81,90,67,45,9,11,10,12,13,15,17,81,51]) 
s = pd.Series(a) 
print(s.head(2)) 

# using tail printing bottom rows 
import pandas as pd 
import numpy as np 
a = np.array([10,15,61,78,81,90,67,45,9,11,10,12,13,15,17,81,51]) 
s = pd.Series(a) 
print(s.tail(3)) 