def solve(chemin):
    def ouvrir_fichier(chemin:str):
        with open(chemin) as f:
            resultat = [list(map(int, line.strip())) for line in f]
        return resultat

    tableau = ouvrir_fichier(chemin)

    resultat = 0
    for ligne in tableau:
        max_1 = max(ligne)
        index_1 = ligne.index(max_1)
        is_after = False
        copie = []
        if index_1<len(ligne)-1:
            copie = ligne[index_1:]
            copie.remove(max_1)
            is_after = True
        else:
            copie = ligne.copy()
            copie.remove(max_1)
        max_2 = max(copie)
        
        if is_after:
            index_2 = index_1 + copie.index(max_2)
        else:
            index_2 = ligne.index(max_2)
            
        if index_1 <= index_2:
            resultat+=max_1*10 + max_2
        else:
            resultat+=max_2*10 + max_1

    return(resultat)

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)