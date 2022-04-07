import pandas as pd

# Select row with maximum and minimum value in Pandas dataframe  

dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}

df = pd.DataFrame(dict1)
# max
print(df.max())
# what is the maximum age ?
print(df.Age.max())
# who is the oldest driver ?
print(df[df.Age == df.Age.max()])

# min
print(df.min())
# Who scored less points ?
print(df[df.Points == df.Points.min()])