import Combat 
from Pokemon import Pokemon
import Get_ability
import json

picka = Pokemon("pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)

import json

# Opening JSON file
f = open('pokemon_stats_level_1.json')

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data:
    print(i)

# Closing file
f.close()
nom_pokemon = input("choose your pokemon")


Combat.lanceAttack(picka,salam)
Get_ability.get_ability(nom_pokemon)
picka.apprendreCapacite()