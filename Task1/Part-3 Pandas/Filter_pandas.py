# Part-3 ---------- section 4


import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

filtered = df[
    (df["Sex"] == "female") &
    (df["Age"] >= 18) &
    (df["Age"] <= 35) &
    (df["Pclass"] == 1)
]

filtered.to_csv("first_class_women.csv", index=False)

print(filtered)
