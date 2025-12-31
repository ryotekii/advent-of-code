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
    
    largeur = max(x for x, _ in rouge) + 1
    hauteur = max(y for _, y in rouge) + 1
    
    def creer_contour(rouge):
        tri_colonnes = sorted(list(rouge), key=lambda p: (p[0], p[1]))
        tri_lignes = sorted(list(rouge), key=lambda p: (p[1], p[0]))
        segments_contour_horizontaux = {}
        segments_contour_verticaux = {}
        i = 0
        while i < len(tri_lignes):
            y = tri_lignes[i][1]
            if i + 1 < len(tri_lignes) and tri_lignes[i + 1][1] == y:
                x1 = tri_lignes[i][0]
                x2 = tri_lignes[i + 1][0]
                segments_contour_horizontaux[y] = (min(x1, x2), max(x1, x2))
                i += 2 
            else:
                i += 1
                
        i = 0
        while i < len(tri_colonnes):
            x = tri_colonnes[i][0]
            if i + 1 < len(tri_colonnes) and tri_colonnes[i + 1][0] == x:
                y1 = tri_colonnes[i][1]
                y2 = tri_colonnes[i + 1][1]
                segments_contour_verticaux[x] = (min(y1, y2), max(y1, y2))
                i += 2 
            else:
                i += 1
        return segments_contour_horizontaux, segments_contour_verticaux

    segments_contour_horizontaux,segments_contour_vertiaux = creer_contour(rouge)
    
    def croise_verticalement()->bool:
        pass
        
    def croise_horizontalement()->bool:
        pass

if __name__ == "__main__":
    result = solve("2025/day9/input.txt")
    print(result)