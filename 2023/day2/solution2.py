import re
from pprint import pprint

with open("/home/etudiants/poirson48u/AOC-salome.poirson/2023/day2/input.txt", "r", encoding="utf-8") as f:
    texte = f.read()

max_couleurs_par_game = {}

for ligne in texte.strip().split("\n"):
    
    game_part, tours_part = ligne.split(":", 1)
    game_name = game_part.strip()
    
    # Pour chaque couleur, trouver toutes les occurrences et garder le max
    max_rouge = max([int(x) for x in re.findall(r'(\d+)\s+red', tours_part)] or [0])
    max_bleu  = max([int(x) for x in re.findall(r'(\d+)\s+blue', tours_part)] or [0])
    max_vert  = max([int(x) for x in re.findall(r'(\d+)\s+green', tours_part)] or [0])
    
    # Stocker dans le dictionnaire
    max_couleurs_par_game[game_name] = {
        "red": max_rouge,
        "blue": max_bleu,
        "green": max_vert
    }

# Affichage
pprint(max_couleurs_par_game)

somme_games=0

for game_name, couleurs in max_couleurs_par_game.items():
    somme_games+=couleurs["blue"]*couleurs["red"]*couleurs["green"]

print (somme_games)