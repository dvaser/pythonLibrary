import pandas as pd
import numpy as np

# data = pd.read_csv('Datasets/imdb.csv')

# data.dropna(inplace=True, thresh=4, how='all')

# data['Year of Release'] = data['Year of Release'].str.replace('(','').str.replace(')','')

# data = data[(data['Year of Release'] <= '2000') & (data['Movie Rating'] >= 8.0)]

# data[['FirstName','LastName']] = data['Movie Name'].loc[data['Movie Name'].str.split().str.len() == 2].str.split(expand=True)

# print(data.head(10))


# Customers = {
#     'CustomerId' : [1,2,3,4],
#     'FirstName' : ['Ahmet', 'Ali', 'Hasan', 'Canan'],
#     'LastName' : ['Yilmaz', 'Korkmaz', 'Celik', 'Toprak']
# }

# Orders = {
#     'OrderId' : [10,11,12,13],
#     'CustomerId' : [1,2,5,7],
#     'OrderDate' : ['2010-07-04', '2010-08-04', '2001-01-07', '2001-09-07']
# }

# df_customers = pd.DataFrame(Customers, columns=['CustomerId', 'FirstName', 'LastName']) 
# df_orders = pd.DataFrame(Orders, columns=['OrderId', 'CustomerId', 'OrderDate']) 

# df = pd.merge(df_customers, df_orders, how='left')

# df = df.dropna(subset=['FirstName', 'LastName'])

# print(df)


# data = pd.read_csv('Datasets/nba.csv')

# result = data.head(10)      #1
# result = len(data.index)    #2
# result = data[(25.0 >= data["age"]) & (data["age"] >= 20.0)][["player_name", "team_abbreviation"]]        #6
# result = data[data["player_name"]=="John Holland"][["player_name","team_abbreviation"]]   #7
# result = data["team_abbreviation"].unique()   #8-9
# result = data["team_abbreviation"].value_counts()   #10
# result = data[data["player_name"].str.contains("and")]

# print(result)