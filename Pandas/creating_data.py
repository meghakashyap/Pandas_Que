import pandas as pd 
import numpy as np 
matrix = [("Ankur", "Cat", "Ball"),
          (np.NaN, 23, 11), 
          ("Sheetal", 36, 55), 
          ("Deepa", np.NaN, 34), 
          ("Shehnaz", 21, 44) ] 
x = pd.DataFrame(matrix,columns=list('xyz'))
print(x) 
# y = x.max() # print(y) 


import pandas as pd 
dic = {"A":[1,1,11,9,2],"B":[21,90,81,71,4]} 
df = pd.DataFrame(dic) 
print(df) 


import pandas as pd 
dic = [{'name':'Bharti','sirname':'kumari'}, {'name':"Deepa",'sirname':'deepa'}] 
df = pd.DataFrame(dic) 
print(df) 


import pandas as pd 
import numpy as np 
matrix = [("Ankur", "Cat", "Ball"), 
          (np.NaN, 23, 11), 
          ("Sheetal", 36, 55), 
          ("Deepa", np.NaN, 34), 
          ("Shehnaz", 21, 44) ] 
x = pd.DataFrame(matrix,columns=list('xyz'))
print(x) # y = x.max() # print(y) 