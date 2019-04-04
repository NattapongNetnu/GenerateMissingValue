import pandas as pd
import numpy as np

df = pd.read_csv('./googleplaystore_missing.csv')


df['Price'] = df['Price'].fillna('0')

df.loc[df['Price'] != '0', 'Type'] = 'Paid'
df.loc[df['Price'] == '0', 'Type'] = 'Free'

print(df)

df.to_csv("./pokemon_missing_1.csv", index=False)
