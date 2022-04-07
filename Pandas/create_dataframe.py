import pandas as pd

# create dataframes from dic array
data={
    "calories":[500,300,450],
    "duration":[49,35,28]
}
df = pd.DataFrame(data)
print(df)

# Creating Pandas dataframe using list of lists 
user={
    "Name":["Megha","Sudha","somi"],
    "Age":[20,34,21]
}
a = pd.DataFrame(user)
print(a)

# Create a Pandas DataFrame from List of Dicts 
info=[
    {"A","B","C"},
      {91,92,93}
]
df1 = pd.DataFrame(info)
print(df1)
 
# Creating a list of nested dictionary.
list = [
        {
        "Student": [{"Exam": 90, "Grade": "a"},
                    {"Exam": 99, "Grade": "b"},
                    {"Exam": 97, "Grade": "c"},
                   ],
        "Name": "Paras Jain"
        },
        {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                   ],
        "Name": "Chunky Pandey"
        }
]
df2 = pd.DataFrame(list)
print(df2.to_string())

# Replace values in Pandas dataframe using regex
city={
    'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
    'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
    'Cost':[10000, 5000, 15000, 2000, 12000]
}
c_df = pd.DataFrame(city)
replace = c_df.replace(to_replace = "[Nn]ew",value = "New_",regex = True)
print(replace)

# Creating a dataframe from Pandas series 
n_list = ["a","b","c"]
s1 = pd.Series(n_list)
df3 = pd.DataFrame(s1,columns = ["Alpha"])
print(df3)

# Construct a DataFrame in Pandas using string data 

# {left}




df_ = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':[' UMbreLla', '  maTress', 'BaDmintoN ', 'Shuttle'],
                   'Updated_Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 8, 15, 10]})
  
# Print the dataframe
print(df_)
# Using the df.apply() function on product column
df_['Product'] = df_['Product'].apply(lambda x : x.strip().capitalize())
# Print the Dataframe
print(df_)