import pandas as pd

# Ranking Rows of Pandas DataFrame

movies = {'Name': ['The Godfather', 'Bird Box', 'Fight Club'],
         'Year': ['1972', '2018', '1999'],
         'Rating': ['9.2', '6.8', '8.8']}
  
df = pd.DataFrame(movies)


# Create a column Rating_Rank which contains
# the rank of each movie based on rating
df['Rating_Rank'] = df['Rating'].rank(ascending = 0)
  
# Set the index to newly created column, Rating_Rank
df = df.set_index('Rating_Rank')
print(df)