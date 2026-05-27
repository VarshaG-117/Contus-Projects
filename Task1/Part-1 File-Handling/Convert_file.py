# Part-1 --------- section 3


import json

f = open("Titanic-Dataset.csv", "r")

lines = f.readlines()

columns = lines[0].strip().split(",")

mylist = []

for line in lines[1:]:
    values = line.strip().split(",")

    row = {}

    for i in range(len(columns)):
        row[columns[i]] = values[i]

    mylist.append(row)

jsonfile = open("titanic.json", "w")

json.dump(mylist, jsonfile, indent=4)

f.close()
jsonfile.close()
