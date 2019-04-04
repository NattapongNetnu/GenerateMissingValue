import pandas as pd
import numpy as np
import random
data = pd.read_csv("./datasets/e-commerce/data.csv", encoding='utf-8')


# print(random.sample(range(800), 321))

columns = data.columns
count = data.shape[0]
countMissing = int(count / 10)

for index in columns:
    data[index].iloc[random.sample(range(count), countMissing)] = np.nan

print(data)
# print(count)
# print(columns)

# data['month'].iloc[random.sample(range(500), 100)] = np.nan
# data['date_of_month'].iloc[random.sample(range(500), 100)] = np.nan
# data['day_of_week'].iloc[random.sample(range(500), 100)] = np.nan
# data['births'].iloc[random.sample(range(500), 100)] = np.nan

# data.to_csv("./Exercise7_edit.csv", index=False)

# data['year'] = data['year'].fillna(1994)
# data['month'] = data['month'].fillna(1)
# data['date_of_month'] = data['date_of_month'].fillna(4)
# data['day_of_week'] = data['day_of_week'].fillna(7)
# data['births'] = data['births'].fillna(123)
# print(data.head(10))
# data['date_of_month'].iloc[random.sample(range(500), 100)] = np.nan
# data['day_of_week'].iloc[random.sample(range(500), 100)] = np.nan
# data['births'].iloc[random.sample(range(500), 100)] = np.na

# data.to_csv("./pokemon_missing.csv", index=False)