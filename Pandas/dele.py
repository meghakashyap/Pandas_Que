import pandas as pd
import numpy as np 
matrix = [("Ankur", "Cat", "Ball"), 
        (np.NaN, 23, 11),
        ("Sheetal", 36, 55), 
        ("Deepa", np.NaN, 34),
        ("Shehnaz", 21, 44) 
] 
x = pd.DataFrame(matrix,columns=list('xyz'))
# print(x) 
# y = x.max()
# print(y) 

# deleting data columnvise
y = x.drop(index=[2,3],axis=1) 
# print(y)

# To add column 
x['new_col']=10 
print(x)

# deleting column
# x.pop('x') 
# print(x)

# del x['x']
# print(x)

# deleting the y
# y = x.drop('y',axis=1) 
# print(y)

# deleting row 
# y = x.drop(index=[2,3],axis=1) 
# print(y)

# multiple column delete
a=x.drop(["x","y"],axis=1)
# print(a)