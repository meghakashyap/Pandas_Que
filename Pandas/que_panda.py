# How to create a series from a list, numpy array and dict? 
import numpy as np
import pandas as pd
new_list=[1,91,67,51,45] 
x =pd.Series(new_list) 
print(x)

# uisng dic
import pandas as pd
d = {'name':'Bharti','class':'python'} 
s= pd.Series(d)
print(s) 

# loc
import pandas as pd 
import numpy as np 
arr = np.array([10,15,18,22,55,77])
s = pd.Series(arr) 
print(s.loc[2:4]) 

# iloc
import pandas as pd 
import numpy as np 
arr = np.array([10,15,18,22,55,77]) 
s = pd.Series(arr) 
print(s.iloc[2:4]) 


# slicing
import pandas as pd 
import numpy as np 
arr = np.array([10,15,18,22,55,77])
s = pd.Series(arr)
print(s[2:4]) 

arr = np.array([10,15,18,22,55,77,67])
s = pd.Series(arr)
print(s[0:6:3]) 