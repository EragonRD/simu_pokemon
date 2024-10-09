import Combat  as Combat
from Pokemon import Pokemon
<<<<<<< HEAD
from Get_ability import get_ability

#picka = Pokemon("Pickachu","Electrique",154,91,115,113,113,93,50)
#salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)
=======
import Get_ability
import json

picka = Pokemon("pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)
>>>>>>> 1c6f9a10cc7919fad37a3f30325e8660d75e269b

#charge les données des pokemon nom et stats lvl 1
with open('pokemon_stats_level_1.json', "r") as poke: 
    print(json.load(poke))

print(poke)

nom_pokemon = input("choose your pokemon")

<<<<<<< HEAD
#Combat.lanceAttack(picka,salam)
get_ability(nom_pokemon)
=======

Combat.lanceAttack(picka,salam)
Get_ability.get_ability(nom_pokemon)
picka.apprendreCapacite()
>>>>>>> 1c6f9a10cc7919fad37a3f30325e8660d75e269b
