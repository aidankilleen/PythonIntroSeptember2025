# pandas_pivot.py

import pandas as pd


df_sales = pd.read_csv("sales.csv")

df_pivot = pd.pivot_table(df_sales, index="product", columns="colour", values="quantity", aggfunc="sum", fill_value=0)
df_pivot['totals'] = df_pivot.sum(axis=1)

totals_row = df_pivot.sum(axis=0).to_frame().T
totals_row.index = ["Totals"]

pivot_with_totals = pd.concat([df_pivot, totals_row])

print (pivot_with_totals)

