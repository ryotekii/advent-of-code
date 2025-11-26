import csv

col1 = []
col2 = []


with open("/home/etudiants/poirson48u/AOC-salome.poirson/2024/day1/input.csv", "r", newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:     # s'assurer qu'il y a au moins deux colonnes
            col1.append(int(row[0]))
            col2.append(int(row[1]))

col1.sort()
col2.sort()

somme = 0
for i in range(len(col1)):
    somme+=abs(col1[i]-col2[i])

print (somme)
