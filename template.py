import sys

def solve(chemin):
    tableau = []
    with open(chemin, "r") as f:
        for line in f:
            line = line.strip()
            tableau.append(list(line))
    print (tableau)
    

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)