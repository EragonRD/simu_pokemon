import Combat 
from Pokemon import Pokemon
import Get_ability
import json

picka = Pokemon("pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)

#charge les données des pokemon nom et stats lvl 1
with open('pokemon_stats_level_1.json', "r") as poke: 
    print(json.load(poke))

print(poke)

nom_pokemon = input("choose your pokemon")


Combat.lanceAttack(picka,salam)
Get_ability.get_ability(nom_pokemon)
picka.apprendreCapacite()