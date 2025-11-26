import csv

col1 = []
col2 = []


with open("/home/etudiants/poirson48u/AOC-salome.poirson/2024/day1/input.csv", "r", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:     # s'assurer qu'il y a au moins deux colonnes
            col1.append(int(row[0]))
            col2.append(int(row[1]))

count=0
for elem in col1:
    count+=elem*col2.count(elem)

print(count)