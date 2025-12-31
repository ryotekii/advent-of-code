import sys
from itertools import combinations

def solve(chemin):
    
    coordonnees = set()
    with open(chemin,"r") as f:
        for line in f:
            line = line.strip()
            line = line.split(",")
            coordonnees.add((int(line[0]),int(line[1])))
    # print(coordonnees)
    
    def taille(point1,point2):
        return (abs(point1[0]-point2[0])+1)*(abs(point1[1]-point2[1])+1)
    
    aire_max = float("-inf")
    for point1, point2 in combinations(coordonnees, 2):
        aire = taille(point1,point2)
        # print(point1,point2,aire)
        if aire > aire_max :
            aire_max = aire
            
    return aire_max

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)