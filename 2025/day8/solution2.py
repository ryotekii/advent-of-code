from math import sqrt, dist
from itertools import combinations
import sys

def solve(chemin):
    liste_points = []
    with open(chemin, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(",")
            line = tuple(int(x) for x in line)
            liste_points.append(line)
    # print(liste_points)

    circuits = {}
    
    for point in liste_points:
        circuits[point]=[point]
        
    # print(circuits)
        
    possibilites = sorted(combinations(circuits, 2),
               key=lambda x: dist(*x))
    
    def uniq(liste_circuits_doubles):
        for liste in liste_circuits_doubles:
            liste.sort()
        
        liste_bis = []
        for i in range (len(liste_circuits_doubles)):
            if liste_circuits_doubles[i] not in liste_circuits_doubles[i+1:]:
                liste_bis.append(liste_circuits_doubles[i])
        return liste_bis
    
    for point1, point2 in possibilites:
        if set(circuits[point1]) == set(circuits[point2]):
            pass
        elif len(uniq(list(circuits.values()))) > 2:
                nv_circuit = list(set(circuits[point1] + circuits[point2]))
                for b in nv_circuit:
                    circuits[b] = nv_circuit
        elif len(uniq(list(circuits.values()))) == 2:
            return (point1[0]*point2[0])
          
if __name__ == "__main__":
    result = solve("2025/day8/input.txt")
    print(result)