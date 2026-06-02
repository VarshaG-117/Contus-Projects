import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("loan_approval_dataset.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

df.columns = df.columns.str.strip()

df["education"] = df["education"].str.strip()
df["self_employed"] = df["self_employed"].str.strip()
df["loan_status"] = df["loan_status"].str.strip()

le_education = LabelEncoder()
le_self_employed = LabelEncoder()
le_status = LabelEncoder()

df["education"] = le_education.fit_transform(df["education"])
df["self_employed"] = le_self_employed.fit_transform(df["self_employed"])
df["loan_status"] = le_status.fit_transform(df["loan_status"])

X = df.drop(["loan_id", "loan_status"], axis=1)
y = df["loan_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

sample = X.iloc[[0]]

prediction = model.predict(sample)

print("\nSample Prediction:")

if prediction[0] == 0:
    print("Approved")
else:
    print("Rejected")