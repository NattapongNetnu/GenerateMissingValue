import pandas as pd
import numpy as np
import random
data = pd.read_csv("./datasets/e-commerce/data.csv", encoding="utf-8", index_col=[0])

random.seed(6)

columns = random.sample(population=list(data.columns), k=4)
count = data.shape[0]
countMissing = int(count / 10)

for index in columns:
    data[index].iloc[random.sample(range(count), countMissing)] = np.nan

print(columns)
print(data)


data.to_csv("./datasets/e-commerce/data_missing.csv", index=False, encoding='utf-8')