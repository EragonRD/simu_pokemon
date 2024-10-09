from Combat import Combat
from Pokemon import Pokemon
from Get_ability import get_ability 
import json

picka = Pokemon("pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)


def creer_pokemon_depuis_json(pokemon_name, data):

    for key, pokemon_data in data.items():
        if pokemon_data['name'] == pokemon_name:
            nom = pokemon_data['name']
            types = pokemon_data['types']
            stats = pokemon_data['stats']
            
            # Créer une instance de la classe Pokemon
            new_pokemon = Pokemon(
                nom=nom,
                elem=types,  # Les types seront une liste (par exemple ["grass", "poison"])
                hp=stats['hp'],
                atk_n=stats['attack'],
                atk_spe=stats['special-attack'],
                def_n=stats['defense'],
                def_spe=stats['special-defense'],
                vit=stats['speed'],
                niveau=1
            )
            
            return new_pokemon
    
    # Si le Pokémon n'est pas trouvé, renvoyer None
    print("Pokémon non trouvé.")
    return None


#charge les données des pokemon nom et stats lvl 1
with open('pokemon_stats_level_1.json', "r") as poke: 
    data = json.load(poke)
    pokemon_names = [pokemon["name"] for key,pokemon in data.items()]
    print(pokemon_names)

#choose pokemon
while True:
        nom_pokemon = input("Choose your Pokémon: ").strip().lower()  # On met en minuscule pour faciliter la comparaison
        if nom_pokemon in pokemon_names :  # On compare avec les noms 
            print(f"Vous avez choisi {nom_pokemon.capitalize()}!")
            break
        else:
            print(pokemon_names)
            print("Nom invalide, veuillez choisir un Pokémon valide.")

#initilise the pokemon 
with open('pokemon_stats_level_1.json', "r") as poke: 
    poke_1 = creer_pokemon_depuis_json(nom_pokemon, json.load(poke))

# choose ability         
print("downloading pokemon data")
get_ability(nom_pokemon)
print("done")

#test
cb = Combat(picka,salam)


"""
Combat.lanceAttack(picka,salam)
picka.apprendreCapacite()
"""