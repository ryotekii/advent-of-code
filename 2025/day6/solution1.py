import sys

def solve(chemin:str):
    tableau = []
    with open(chemin, "r") as f:
        lignes = f.readlines()
        for ligne in lignes[:-1]:
            ligne = ligne.strip()
            tableau.append([int(x) for x in ligne.split()])
        ligne = lignes[-1]
        tableau.append([x for x in ligne.split()])
    # print(tableau)
    
    total = 0
    for i in range (len(tableau[0])):
        operation = tableau[-1][i]
        if operation == "*":
            provisoire = 1
        else :
            provisoire = 0
        for j in range (len(tableau)-1):
            if operation == "*":
                provisoire *= tableau[j][i]
            else :
                provisoire += tableau[j][i]
        total += provisoire
    return(total)
        
if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
