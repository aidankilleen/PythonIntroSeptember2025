# pandas_introduction

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Carol', 'Dan'], 
    'Email': ['alice@gmail.com', 'bob@gmail.com', 'carol@gmail.com', 'dan@gmail.com'],
    'Active': [True, False, True, True]
}

df = pd.DataFrame(data)

print (df)

print (df[['Name', 'Email']])


# filtering

active_users = df[df['Active'] == True]

print (active_users)

# importing data
df = pd.read_json("https://jsonplaceholder.typicode.com/users/1/todos")

print (df.head())







