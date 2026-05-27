# Part-1 ------ section 2

f = open("Titanic-Dataset.csv", "r")

lines = f.readlines()

header = lines[0]

newfile = open("survivors.csv", "w")

newfile.write(header)

for line in lines[1:]:
    data = line.strip().split(",")

    if data[1] == "1":
        newfile.write(line)

f.close()
newfile.close()
