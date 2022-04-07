import pandas as pd


  
data = {'Voter_name': ['Rekha', 'Geeta', 'Radha', 'Sudha', 
                           'Raghav', 'Megha', 'Muskan', 'Sandhya'], 
            'Voter_age': [15, 23, 25, 9, 22, 20, 42,56]}

df = pd.DataFrame(data)

eligible = []
for i in data["Voter_age"]:
    if i >= 18:
        eligible.append("Yes")
    else:
         eligible.append("No")

df["Eligiblity"] = eligible
print(df)