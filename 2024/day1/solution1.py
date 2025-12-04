import sys

def solve(chemin):
    col1 = []
    col2 = []

    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            a, b = ligne.split()
            col1.append(int(a))
            col2.append(int(b))


    col1.sort()
    col2.sort()

    somme = 0
    for i in range(len(col1)):
        somme+=abs(col1[i]-col2[i])
    return (somme)

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
