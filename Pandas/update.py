# Mapping external values to dataframe values in Pandas 
import pandas as pd
initial_data = {
                'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'], 
                'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'], 
                'Age': [42, 52, 36, 21, 23], 
                'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']
}

data = pd.DataFrame(initial_data)
data["Field"] = ["MBBS","ENGINEER","IAS","LLB","B.TECH"]
print(data)

# update 
new_data =  ["Megha","Sudha","Preeti"]
data["First_name"].update(pd.Series(new_data))
print(data)

# replace
new_data = { "Ram":"Shyam",
             "Tina":"Riya",
             "Jeetu":"Jitender" }
  
print(data, end ="\n\n")
  
# combine this new data with existing DataFrame
df = data.replace({"First_name":new_data})
print(df)