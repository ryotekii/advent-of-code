import sys

def solve(chemin):
    liste_intervalles = []
    liste_ids = []

    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            
            if "-" in ligne:
                a, b = ligne.split("-")
                liste_intervalles.append((int(a), int(b)))
            else:
                liste_ids.append(int(ligne))
    nb_id = 0
    for id in liste_ids:
        found = False
        for inf, sup in liste_intervalles:
            if id>=inf and id<=sup:
                found = True
        if found:
            nb_id+=1
    return nb_id
    
if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
