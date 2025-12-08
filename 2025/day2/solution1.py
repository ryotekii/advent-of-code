import sys

def solve(chemin):
    def lire_intervalles(path: str) -> list[tuple[int, int]]:
        with open(path, "r", encoding="utf-8") as f:
            contenu = f.read().strip()

        intervalles = []
        for bloc in contenu.split(","):
            a, b = bloc.split("-")
            intervalles.append((int(a), int(b)))

        return intervalles

    intervalles = lire_intervalles(chemin)
    # print(intervalles)

    solution = 0

    for debut, fin in intervalles:
        for i in range (debut, fin+1):
            chaine = str(i)
            compare1 = chaine[:(len(chaine)//2)]
            compare2 = chaine[(len(chaine)//2):]
            if compare1 == compare2:
                solution+=i

    return(solution)

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
