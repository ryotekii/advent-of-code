import sys

def solve(chemin):
    tableau = []
    with open(chemin, "r") as f:
        for line in f:
            line = line.strip()
            tableau.append(list(line))
    # print (tableau)

    tableau_alternatif = [[False for _ in range (len(tableau[0]))] for _ in range (len(tableau))]
    
    compteur = 0
    for ligne in range(len(tableau)):
        for colonne in range (len(tableau[0])):
            if tableau[ligne][colonne]=="S":
                tableau_alternatif[ligne][colonne]=True
                # print("init")
            else:
                if tableau_alternatif[ligne-1][colonne]:
                    # print("continuer")
                    if tableau[ligne][colonne] == ".":
                        tableau_alternatif[ligne][colonne]=True
                        # print("suite",tableau_alternatif)
                    if tableau[ligne][colonne] == "^":
                        tableau_alternatif[ligne][colonne-1]=True
                        tableau_alternatif[ligne][colonne+1]=True
                        compteur+=1
    return compteur
            
if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)