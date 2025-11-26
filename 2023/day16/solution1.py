tableau = []

with open("/home/etudiants/poirson48u/AOC-salome.poirson/2023/day16/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        tableau.append(list(line))

print(tableau)
print(len(tableau[0]))
print(len(tableau))

chemin = [[0 for i in range (110)] for i in range(110)]
print(chemin)

a_explorer=[(0,0,(0,1))]

while a_explorer:
    pass

def next_direction(coord_x:int,coord_y:int,direction:tuple[int,int])->list[tuple[int,int]]:
    if tableau[coord_y][coord_x]==".":
        return [direction]    
    if tableau[coord_y][coord_x]=="-":
        if direction[1]==0:
            return [direction]
        return[(coord_y,coord_x+1),(coord_y,coord_x-1)]
    if tableau[coord_y][coord_x]=="|":
        if direction[0]==0:
            return [direction]
        return [(coord_y+1,coord_x),(coord_y-1,coord_x)]
    if tableau[coord_y][coord_x]=="/":
        if direction[0]==0:
            if direction[1]==1:
                return [(-1,0)]
            else:
                return [(1,0)]
        elif direction[0]==1:
            return [(0,-1)]
        else:
            return [(0,1)]
    if tableau[coord_y][coord_x]=="\\":
        if direction[0]==0:
            if direction[1]==1:
                return [(1,0)]
            else:
                return [(-1,0)]
        elif direction[0]==1:
            return [(0,1)]
        else:
            return [(0,-1)]