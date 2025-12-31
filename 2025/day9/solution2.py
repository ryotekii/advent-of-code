import sys
from itertools import combinations

def solve(chemin):
    
    rouge = set()
    with open(chemin,"r") as f:
        for line in f:
            line = line.strip()
            line = line.split(",")
            rouge.add((int(line[0]),int(line[1])))
    # print(rouge)

    contours = set()
    
    
    largeur = max(x for x, _ in rouge) + 1
    hauteur = max(y for _, y in rouge) + 1
    
    """
    def afficher_grille(rouge,sans_couleur,taille):
        res = ""
        for ligne in range (taille):
            affichage_ligne = ""
            for colonne in range (taille):
                if ((colonne,ligne)) in sans_couleur:
                    affichage_ligne+="O"
                elif ((colonne,ligne)) in rouge:
                    affichage_ligne+="#"
                else:
                    affichage_ligne+="."
            res+=affichage_ligne+"\n"
        print(res)
    """
    
    def definir_contours(rouge,contours,hauteur,largeur):
        for ligne in range (hauteur):
            mur = False
            for colonne in range(largeur):
                if (colonne,ligne) in rouge:
                    contours.add((colonne,ligne))
                    mur = not mur
                if mur:
                    contours.add((colonne,ligne))
        
        for colonne in range (largeur):
            mur = False
            for ligne in range(hauteur):
                if (colonne,ligne) in rouge:
                    contours.add((colonne,ligne))
                    mur = not mur
                if mur:
                    contours.add((colonne,ligne))
    
    sans_couleur = set()
    
    def faire_exterieur(contours,taille):
        for ligne in range (taille):
            for colonne in range(taille):
                if (colonne,ligne) in contours:
                    break
                sans_couleur.add((colonne,ligne))
        
        for colonne in range (taille):
            for ligne in range(taille):
                if (colonne,ligne) in contours:
                    break
                sans_couleur.add((colonne,ligne))
                    
        for ligne in range (taille):
            for colonne in range(taille,-1,-1):
                if (colonne,ligne) in contours:
                    break
                sans_couleur.add((colonne,ligne))
        
        for colonne in range (taille,-1,-1):
            for ligne in range(taille,-1,-1):
                if (colonne,ligne) in contours:
                    break
                sans_couleur.add((colonne,ligne))
                    
    definir_contours(rouge,contours,largeur,hauteur)
    print("contours ok")
    # faire_exterieur(contours,100000)
    print("extérieur ok")
    # print("finito")
    # afficher_grille(rouge,sans_couleur,15)
    
    def taille(point1,point2):
        return (abs(point1[0]-point2[0])+1)*(abs(point1[1]-point2[1])+1)
    
    def points_intermediaires(point1,point2):
        xmin, xmax, ymin, ymax = min(point1[0],point1[0])+1, max(point1[0],point2[0])-1, min(point1[1],point2[1])+1,max(point1[1],point2[1])-1
        a_verif = {(x,y) for x in range (xmin,xmax+1) for y in range(ymin,ymax+1)}
        for point in a_verif:
            if point in contours:
                return False
        return True
    
    aire_max = float("-inf")
    for point1, point2 in combinations(rouge, 2):
        aire = taille(point1,point2)
        # print(point1,point2,aire)
        if aire > aire_max :
            if points_intermediaires(point1,point2):
                aire_max = aire
            
    return aire_max

if __name__ == "__main__":
    result = solve("2025/day9/input.txt")
    print(result)