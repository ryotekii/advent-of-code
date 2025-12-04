import re
from pprint import pprint
import sys

def solve(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()

    max_couleurs_par_game = {}

    for ligne in texte.strip().split("\n"):
        
        game_part, tours_part = ligne.split(":", 1)
        game_name = game_part.strip()

        max_rouge = max([int(x) for x in re.findall(r'(\d+)\s+red', tours_part)] or [0])
        max_bleu  = max([int(x) for x in re.findall(r'(\d+)\s+blue', tours_part)] or [0])
        max_vert  = max([int(x) for x in re.findall(r'(\d+)\s+green', tours_part)] or [0])
        
        max_couleurs_par_game[game_name] = {
            "red": max_rouge,
            "blue": max_bleu,
            "green": max_vert
        }

    # pprint(max_couleurs_par_game)

    somme_games=0

    for game_name, couleurs in max_couleurs_par_game.items():
        somme_games+=couleurs["blue"]*couleurs["red"]*couleurs["green"]

    return (somme_games)

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
