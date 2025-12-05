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
    liste_intervalles.sort()
    intervalles_simplifies=[]
    inf_actuel, sup_actuel = liste_intervalles[0]
    for inf, sup in liste_intervalles:
        if inf<=sup_actuel+1:
            sup_actuel = max(sup_actuel, sup)
        else:
            intervalles_simplifies.append((inf_actuel,sup_actuel))
            inf_actuel, sup_actuel = inf, sup
    intervalles_simplifies.append((inf_actuel,sup_actuel))
    # print(intervalles_simplifies)
    return sum(sup - inf + 1 for inf, sup in intervalles_simplifies)
    
    
if __name__ == "__main__":
    result = solve("2025/day5/input.txt")
    print(result)
