import sys

def solve(chemin:str):
    tableau = []
    with open(chemin, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            tableau.append(list(line))
    print(tableau)
    
    def verifier_voisins(y:int,x:int)->bool:
        voisins = {(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)}
        if y==0:
            voisins = {v for v in voisins if v[0] != -1}
        if x==0:
            voisins = {v for v in voisins if v[1] != -1}
        if y==len(tableau[0])-1:
            voisins = {v for v in voisins if v[0] != 1}
        if x==len(tableau)-1:
            voisins = {v for v in voisins if v[1] != 1}
        nb = 0
        for y_shift,x_shift in voisins :
            if tableau[y+y_shift][x+x_shift] == "@":
                nb += 1
        # print(y,x,nb)
        return (nb<4)
    
    res = 0
    for y in range(len(tableau)) :
        for x in range(len(tableau[0])) :
            if tableau[y][x]=="@" and verifier_voisins(y,x):
                res+=1
    
    return res
            
if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
