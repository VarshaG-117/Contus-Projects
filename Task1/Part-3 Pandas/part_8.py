import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df.groupby("Pclass").agg({
    "Survived": "mean",
    "Age": "mean",
    "Fare": "mean"
})

print(result)