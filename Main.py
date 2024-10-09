import Combat 
from Pokemon import Pokemon
from Get_ability import get_ability 
import json

picka = Pokemon("pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)

#charge les données des pokemon nom et stats lvl 1
with open('pokemon_stats_level_1.json', "r") as poke: 
    pokemonsLvl1 = json.load(poke)
    

pokemon_names = [pokemon["name"] for pokemon in pokemonsLvl1.values()]
print(pokemon_names)

while True:
        nom_pokemon = input("Choose your Pokémon: ").strip().lower()  # On met en minuscule pour faciliter la comparaison
        if nom_pokemon in pokemon_names :  # On compare avec les noms 
            print(f"Vous avez choisi {nom_pokemon.capitalize()}!")
            break
        else:
            print("Nom invalide, veuillez choisir un Pokémon valide.")

print("downloading pokemon data")
get_ability(nom_pokemon)
print("done")

"""
Combat.lanceAttack(picka,salam)
picka.apprendreCapacite()
"""
