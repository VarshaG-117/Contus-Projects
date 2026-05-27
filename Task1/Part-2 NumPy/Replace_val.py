# Part-2 ---------- section 1

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

print("Mean:", np.mean(ages))
print("Median:", np.median(ages))
print("Standard Deviation:", np.std(ages))

f.close()
