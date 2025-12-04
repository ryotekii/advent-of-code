def solve(chemin):
    def ouvrir_fichier(chemin:str):
        with open(chemin) as f:
            resultat = [list(map(int, line.strip())) for line in f]
        return resultat

    tableau = ouvrir_fichier(chemin)

    resultat = 0
    for ligne in tableau:
        liste_max_ligne = []
        for i in range(11,-1,-1):
            if i == 0:
                maximum = max(ligne[:])
            else:
                maximum = max(ligne[:-i])
            
            liste_max_ligne.append(maximum)

            ligne = ligne[ligne.index(maximum)+1:]
            # print("[ligne]",ligne)
            # print("[memoire]",liste_max_ligne)
        temp=int(''.join(map(str, liste_max_ligne)))
        resultat+=temp
    return(resultat)

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
