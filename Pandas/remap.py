import pandas as pd

# Using dictionary to remap values in Pandas DataFrame columns 
data = {'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                    'Event':['M', 'P', 'T', 'C'],
                    'Cost':[10000, 5000, 15000, 2000]}
df = pd.DataFrame(data)

dic = {"M":"Music","P":'Poetry',"T":'Theatre',"C":'Comedy'}
a = df.replace({"Event":dic})
print(a)
