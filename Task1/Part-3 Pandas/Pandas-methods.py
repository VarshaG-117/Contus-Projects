# Part-3 ---------- section 1

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.isnull().sum())
