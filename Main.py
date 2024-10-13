import random
from Combat import Combat
from Pokemon import Pokemon
from Capacite import Capacite
from Get_abilities import get_ability 
import json

# Fonction pour charger les données du fichier Json des Attaques d'un seul pokemon
def charger_donnees_pokemon(pokemon_name):
    file_name = f'{pokemon_name}_stats_attaques.json'
    
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Le fichier {file_name} n'existe pas.")
        return None

# Fonction pour sélectionner 4 capacités aléatoires parmi les attaques disponibles
def choisir_capacites_aleatoires(pokemon_data,pokemon: Pokemon):
    attaques_disponibles = pokemon_data['attaques']
    
    # S'il y a moins de 4 attaques, on les prend toutes, sinon on choisit 4 au hasard
    capacites_choisies = random.sample(attaques_disponibles, min(4, len(attaques_disponibles)))

    print(f"\nLes 4 capacités aléatoires choisies pour {pokemon_data['nom']} sont :")
    for capacite in capacites_choisies:
        print(f"- {capacite['nom']} (Type: {capacite['type']}, Puissance: {capacite['puissance']})")
        new_capacite = Capacite(
            nom = capacite['nom'],
            element = capacite['type'],
            categorie= capacite['category'],
            puissance= capacite['puissance'],
            precision= capacite['precision'],
            pp = capacite['pp']
        )
        pokemon.apprend_capacite(new_capacite)
    
    return capacites_choisies

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

# Récupère les données JSON dans data et crée la liste des noms de Pokémon
with open('pokemon_stats_level_1.json', "r") as poke: 
    data = json.load(poke)
    pokemon_names = [pokemon["name"] for key,pokemon in data.items()]

# Choix du premier Pokémon
while True:
    nom_pokemon_1 = input("Choose your First Pokémon: ").strip().lower()  # On met en minuscule pour faciliter la comparaison
    if nom_pokemon_1 in pokemon_names:  # On compare avec les noms 
        print(f"Vous avez choisi {nom_pokemon_1.capitalize()}!")
        get_ability(nom_pokemon_1)  # Génère le fichier JSON correspondant
        break
    else:
        print(pokemon_names)
        print("Nom invalide, veuillez choisir un Pokémon valide.")

# Choix du second Pokémon
while True:
    nom_pokemon_2 = input("Choose your Second Pokémon: ").strip().lower()  # On met en minuscule pour faciliter la comparaison
    if nom_pokemon_2 in pokemon_names:  # On compare avec les noms 
        print(f"Vous avez choisi {nom_pokemon_2.capitalize()}!")
        get_ability(nom_pokemon_2)  # Génère le fichier JSON correspondant
        break
    else:
        print(pokemon_names)
        print("Nom invalide, veuillez choisir un Pokémon valide.")

# Lance la commande pour initialiser les Pokémon et affiche leurs statistiques
poke_1 = creer_pokemon_depuis_json(nom_pokemon_1, data)
print("Your First Pokemon is : \n" + str(poke_1))
poke_2 = creer_pokemon_depuis_json(nom_pokemon_2, data)
print("Your Second Pokemon is : \n" + str(poke_2))

# Sélection des capacités aléatoires pour chaque Pokémon
pokemon_1_data = charger_donnees_pokemon(nom_pokemon_1)
pokemon_2_data = charger_donnees_pokemon(nom_pokemon_2)
capacites_poke_1 = choisir_capacites_aleatoires(pokemon_1_data,poke_1)
capacites_poke_2 = choisir_capacites_aleatoires(pokemon_2_data,poke_2)

# Combat entre les deux Pokémons
cb = Combat(poke_1, poke_2)
flag = True
while flag:
    cb.lance_combat()
    flag = (int(poke_1.get_hp()) > 0 and int(poke_2.get_hp()) > 0)

if int(poke_1.get_hp()) > 0:
     print("\nNOTRE GRAND GAGANT EST " + poke_1.get_nom())
else: 
     print("\nNOTRE GRAND GAGANT EST " + poke_2.get_nom())
