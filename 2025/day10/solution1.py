import sys, re, ast

def solve(chemin):
    donnees = {}
    with open(chemin,"r") as f:
        i = 1
        for line in f:
            line = line.strip()
            ampoules = re.search(r"\[([.#]*)\]", line).group(1)
            # print(ampoules)
            objectif = [x=="#" for x in ampoules]
            # print(objectif)
            boutons_str = re.findall(r"\(([0-9,]*)\)",line)
            boutons=[]
            for x in boutons_str:
                interrupteurs = ast.literal_eval(x)
                if isinstance(interrupteurs,tuple):
                    boutons.append([x for x in interrupteurs])
                else:
                    boutons.append([interrupteurs])
            print(boutons)
            donnees[i]=(objectif,boutons_str)
            i+=1
            
    print(donnees)
    
if __name__ == "__main__":
    result = solve("2025/day10/input.txt")
    print(result)