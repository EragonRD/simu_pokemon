from Combat import Combat
from Pokemon import Pokemon
from Get_abilities import get_ability 
import json

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


#recupere les donnees json dans data et cree la lsite des nom de pokemons
with open('pokemon_stats_level_1.json', "r") as poke: 
    data = json.load(poke)
    pokemon_names = [pokemon["name"] for key,pokemon in data.items()]

#choose pokemon 1
while True:
        nom_pokemon_1 = input("Choose your First Pokémon: ").strip().lower()  # On met en minuscule pour faciliter la comparaison
        if nom_pokemon_1 in pokemon_names :  # On compare avec les noms 
            print(f"Vous avez choisi {nom_pokemon_1.capitalize()}!")
            break
        else:
            print(pokemon_names)
            print("Nom invalide, veuillez choisir un Pokémon valide.")

#choose pokemon 2
while True:
        nom_pokemon_2 = input("Choose your Second Pokémon: ").strip().lower()  # On met en minuscule pour faciliter la comparaison
        if nom_pokemon_2 in pokemon_names :  # On compare avec les noms 
            print(f"Vous avez choisi {nom_pokemon_2.capitalize()}!")
            break
        else:
            print(pokemon_names)
            print("Nom invalide, veuillez choisir un Pokémon valide.")

#lance la commande pour initiliser les pokemon et print les stats
poke_1 = creer_pokemon_depuis_json(nom_pokemon_1, data)
print("your First Pokemon is : \n"+str(poke_1))
poke_2 = creer_pokemon_depuis_json(nom_pokemon_2, data)
print("your Second Pokemon is : \n"+str(poke_2))

"""
# choose ability         
print("downloading pokemon data")
get_ability(nom_pokemon_1)
print("done data")
"""

cb = Combat(poke_1,poke_2)
flag=True
while (flag):
    cb.lance_combat()
    flag = (int(poke_1.get_hp())>0 and int(poke_2.get_hp())>0)

if(int(poke_1.get_hp())>0):
     print("\n NOTRE GRAND GAGANT EST "+poke_1.get_nom())
else : 
     print("\n NOTRE GRAND GAGANT EST "+poke_2.get_nom())
     


"""

picka = Pokemon("pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)
Combat.lanceAttack(picka,salam)
picka.apprendreCapacite()
"""