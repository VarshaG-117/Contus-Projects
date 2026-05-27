# Part-2 ------------- section 3

import numpy as np

f = open("Titanic-Dataset.csv", "r")

lines = f.readlines()

fares = []

for line in lines[1:]:
    data = line.strip().split(",")

    fares.append(float(data[9]))

fares = np.array(fares)

min_value = np.min(fares)
max_value = np.max(fares)

normalised = (fares - min_value) / (max_value - min_value)

print(normalised[:10])

f.close()
