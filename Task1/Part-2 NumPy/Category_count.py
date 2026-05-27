# Part-2 ---------- section 2


import numpy as np

f = open("Titanic-Dataset.csv", "r")

lines = f.readlines()

ages = []

for line in lines[1:]:
    data = line.strip().split(",")

    age = data[5]

    if age == "":
        ages.append(np.nan)

    else:
        ages.append(float(age))

ages = np.array(ages)

mean_age = np.nanmean(ages)

ages = np.where(np.isnan(ages), mean_age, ages)

groups = np.where(
    ages < 18,
    "Child",
    np.where(ages <= 60, "Adult", "Senior")
)

child_count = np.sum(groups == "Child")
adult_count = np.sum(groups == "Adult")
senior_count = np.sum(groups == "Senior")

print("Child:", child_count)
print("Adult:", adult_count)
print("Senior:", senior_count)

f.close()
