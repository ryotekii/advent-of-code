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

    solution = 0

                
    def diviseurs(n: int):
        res = []
        for i in range(1, n):
            if n % i == 0:
                res.append(i)
        return sorted(res)

    def valid(chaine:str)->bool:
        for diviseur in diviseurs(len(chaine)):
            base = chaine[:diviseur]
            all_same = True
            for i in range(len(chaine)//diviseur):
                if chaine[i*diviseur:(i+1)*diviseur]!=base:
                    all_same = False
            if all_same:
                return False
        return True



    for debut, fin in intervalles:
        for i in range (debut, fin+1):
            chaine = str(i)
            if not (valid(chaine)):
                solution+=i

    return (solution)

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
