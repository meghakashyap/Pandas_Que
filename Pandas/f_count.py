import pandas as pd

# 9. How to get frequency counts of unique items of a series?
# 1st way
ser = pd.Series(["a","b","a","b","c","a","a","b","b","m","e"])
print(ser.value_counts())

# 2nd way
l=[]
for i in ser:
    c=0
    for x in ser:
        if i==x:
            c+=1
            v = i
    if v not in l:
        l.append(v)
        print(v,c)
    
    
