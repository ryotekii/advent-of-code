import sys

def solve(chemin):
    tableau = []
    with open(chemin, "r") as f:
        taille_ligne = len(f.readline())-1
        for i in range (taille_ligne):
            colonne = []
            f.seek(0)
            for line in f:
                colonne.append(line[i])
            tableau.append(colonne)
    # print(tableau)
    
    tableau.append([" " for _ in range(len(tableau))])
        
    
    def sous_listes(liste):
        def est_vide(ligne):
            for elem in ligne:
                if elem !=" ":
                    return False
            return True
        
        operateur = ""
        liste_operations = []
        nb_provisoire = 0
        liste_nb = []
        
        for colonne in liste:
            if est_vide(colonne):
                liste_operations.append((liste_nb,operateur))
                liste_nb = []
                nb_provisoire = 0
            else :
                nb_provisoire = 0
                for elem in colonne:
                    if elem.isdigit():
                        nb_provisoire = nb_provisoire*10 + int(elem)
                    if elem == "*":
                        operateur = "*"
                    if elem == "+":
                        operateur = "+"
                liste_nb.append(nb_provisoire)
        return(liste_operations)
            
    sous_l = sous_listes(tableau)
    # print(sous_l)

    def somme(tuples:list):
        resultat = 0
        for liste_nb, operateur in tuples:
            if operateur == "*":
                provisoire = 1
                for nb in liste_nb:
                    provisoire*=nb
            else :
                provisoire = 0
                for nb in liste_nb:
                    provisoire+=nb
            resultat += provisoire
        return(resultat)
    
    return(somme(sous_l))
                
                
                
if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)