import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

df["FamilySize"] = df["SibSp"] + df["Parch"]

result = df.groupby("FamilySize")["Survived"].mean()

result = result.sort_values(ascending=False)

print(result)