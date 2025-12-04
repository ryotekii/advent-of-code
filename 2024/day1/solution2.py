import sys

def solve(chemin):
    col1 = []
    col2 = []


    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            a, b = ligne.split()
            col1.append(int(a))
            col2.append(int(b))

    count=0
    for elem in col1:
        count+=elem*col2.count(elem)

    return(count)

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
