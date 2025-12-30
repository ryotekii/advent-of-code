from math import sqrt
from itertools import combinations
import sys

def solve(chemin):
    tableau = []
    with open(chemin, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(",")
            line = [int(x) for x in line]
            tableau.append(line)
    # print(tableau)
    
    def distance_euclidienne(point1:list[int],point2:list[int]):
        return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2)

    deja_pris = []
    
    """
    def appartient(point, deja_pris:list[list]):
        for ligne in deja_pris:
            for elem in ligne:
                if point==elem:
                    return True
        return False
    """
    def meme_circuit(point1,point2,deja_pris):
        for ligne in deja_pris:
            if point1 in ligne and point2 in ligne:
                return True
        return False
    
    def ajouter(point1, point2, deja_pris:list[list]):
        ajoute = False
        for ligne in deja_pris:
            if point1 in ligne:
                ligne.append(point2)
                ajoute = True
            elif point2 in ligne:
                ligne.append(point1)
                ajoute = True
        if not ajoute:
            deja_pris.append([point1,point2])
    
    def trouver_distance_mini(tableau:list, deja_pris:list[list], connexions):
        dist_min = float("inf")
        paire_min = None

        for p1, p2 in combinations(tableau, 2):
            e = frozenset({tuple(p1), tuple(p2)})
            if e not in connexions:
                if meme_circuit(p1,p2,deja_pris):
                    connexions.add(frozenset({tuple(p1),tuple(p2)}))
                    return False
                
                d = distance_euclidienne(p1, p2)
                if d < dist_min:
                    dist_min = d
                    paire_min = (p1,p2)
        # print("[PAIRE] ",paire_min,dist_min)
        ajouter(paire_min[0],paire_min[1],deja_pris)
        connexions.add(frozenset({tuple(paire_min[0]),tuple(paire_min[1])}))
        # print("[LISTE] ",deja_pris)
        return True

    connexions = set()
    i=0
    while i<10:
        if trouver_distance_mini(tableau,deja_pris,connexions):
            i+=1
    
    resultat = sorted(deja_pris, key=len, reverse=True)
    print(resultat)
    
    solution = 1
    
    for i in range (3):
        solution*=len(resultat[i])

    print(solution)
                
                
if __name__ == "__main__":
    result = solve("2025/day8/input.txt")
    print(result)