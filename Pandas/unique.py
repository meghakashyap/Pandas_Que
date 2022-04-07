import pandas as pd

# Get unique values from a column in Pandas DataFrame
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] }

df = pd.DataFrame(data)
# unique value
a = df.B.unique()
print(a)