import sys

def solve(chemin):
    rows = []
    with open(chemin, "r") as f:
        for line in f:
            line = line.strip()
            rows.append([line[0], int(line[1:])])
    

    def modifier_compteur(row:list[str,int],cpt)->int:
        if row[0] == "R":
            return (cpt+row[1])%100
        else :
            return (cpt-row[1])%100
    
    def calculer():
        ocurrences = 0
        compteur = 50
        for row in rows:
            compteur = modifier_compteur(row,compteur)
            if compteur == 0:
                ocurrences+=1
        return (ocurrences)
    return calculer()

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)