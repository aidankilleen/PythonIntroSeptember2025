# pandas_pivot.py

import pandas as pd


df_sales = pd.read_csv("sales.csv")

print (df_sales.head())


df_pivot = pd.pivot_table(df_sales, index="product", columns="colour", values="quantity", aggfunc="sum", fill_value=0)

df_pivot['totals'] = df_pivot.sum(axis=1)
print (df_pivot)

