import sys

def solve(chemin):
    tableau = []

    with open(chemin, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            tableau.append(list(line))

    # print(tableau)
    # print(len(tableau[0]))
    # print(len(tableau))

    def next_direction(coord_y:int,coord_x:int,direction:tuple[int,int]):
        if tableau[coord_y][coord_x]==".":
            return [(coord_y+direction[0],coord_x+direction[1],direction)]    
        if tableau[coord_y][coord_x]=="-":
            if abs(direction[1])==1:
                return [(coord_y+direction[0],coord_x+direction[1],direction)]   
            return[(coord_y,coord_x+1,(0,1)),(coord_y,coord_x-1,(0,-1))]
        if tableau[coord_y][coord_x]=="|":
            if abs(direction[0])==1 :
                return [(coord_y+direction[0],coord_x+direction[1],direction)]
            return [(coord_y+1,coord_x,(1,0)),(coord_y-1,coord_x,(-1,0))]
        if tableau[coord_y][coord_x]=="/":
            if direction[0]==0:
                if direction[1]==1:
                    return [(coord_y-1,coord_x,(-1,0))]
                else:
                    return [(coord_y+1,coord_x,(1,0))]
            elif direction[0]==1:
                return [(coord_y,coord_x-1,(0,-1))]
            else:
                return [(coord_y,coord_x+1,(0,1))]
        if tableau[coord_y][coord_x]=="\\":
            if direction[0]==0:
                if direction[1]==1:
                    return [(coord_y+1,coord_x,(1,0))]
                else:
                    return [(coord_y-1,coord_x,(-1,0))]
            elif direction[0]==1:
                return [(coord_y,coord_x+1,(0,1))]
            else:
                return [(coord_y,coord_x-1,(0,-1))]
        # print("erreur")
        
    def parcourir():
        chemin = [[0 for i in range (110)] for i in range(110)] 
        a_explorer=[(0,0,(0,1))]
        deja_fait=[]

        while a_explorer:
            actuel = a_explorer[0]
            if -1<=actuel[0]+actuel[2][0]<=110 and -1<=actuel[1]+actuel[2][1]<=110 and not (actuel in deja_fait):
                a_explorer.extend(next_direction(actuel[0],actuel[1],actuel[2]))
                chemin[actuel[0]][actuel[1]]=1
                deja_fait.append(actuel)
            a_explorer.remove(actuel)
        return chemin

    resultat = parcourir()

    # for ligne in resultat:
    #     print("".join(map(str, ligne)))

    somme = 0
    for ligne in resultat:
        for x in ligne:
            somme += x

    return(somme)

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
