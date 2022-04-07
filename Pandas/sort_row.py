import pandas as pd

# Sorting rows in pandas DataFrame

data = {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'], 
        'Maths': [8, 5, 6, 9, 7], 
        'Science': [7, 9, 5, 4, 7],
        'English': [7, 4, 7, 6, 8]}
df = pd.DataFrame(data)

# 1st way
a = df.sort_values(by="name",ascending=1)
print(a)

# 2nd way
b = df.sort_values(by =['Maths', 'English'])
print(b)