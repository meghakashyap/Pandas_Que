import pandas as pd

# Select any row from a Dataframe using iloc[] and iat[] in Pandas 
data = {
    "Name":["Megha","Somi","Ridhi","Vaibhav"],
    "Class":[12,11,12,12],
    "Subject":["Science","Arts","Science","Commerce"],
    "Marks":[90,76,56,69]
}

df = pd.DataFrame(data)
#  used to get a single value from a dataframe based on the row and column index
print(df.iat[1,2])
print(df.iloc[0:1])