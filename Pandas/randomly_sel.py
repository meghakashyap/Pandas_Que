import pandas as pd

# How to randomly select rows from Pandas DataFrame 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
        'Age':[27, 24, 22, 32, 15],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']}
df = pd.DataFrame(data)

# selecting row randomly
a = df.sample(n=1)
b = df.sample()
print(a)