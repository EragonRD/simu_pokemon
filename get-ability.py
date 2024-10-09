import requests
import json

# URL de l'API pour obtenir les informations sur un Pokémon
pokemon_name = "pikachu"
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

# Faire une requête GET pour obtenir les informations sur le Pokémon
response = requests.get(pokemon_url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    pokemon_data = response.json()

    # Extraire les statistiques du Pokémon
    pokemon_stats = []
    for stat in pokemon_data['stats']:
        pokemon_stats.append({
            "nom": stat['stat']['name'],
            "valeur": stat['base_stat']
        })

    # Extraire les attaques que le Pokémon peut apprendre
    attaques = []
    for move in pokemon_data['moves']:
        move_url = move['move']['url']
        move_response = requests.get(move_url)
        if move_response.status_code == 200:
            move_data = move_response.json()
            attaque = {
                "nom": move_data['name'],
                "type": move_data['type']['name'],
                "puissance": move_data['power'],
                "precision": move_data['accuracy'],
                "pp": move_data['pp'],
                "effet": move_data['effect_entries'][0]['effect'] if move_data['effect_entries'] else "Aucun effet"
            }
            attaques.append(attaque)

    # Créer un dictionnaire pour les données à écrire dans le fichier JSON
    data_to_write = {
        "attaques": attaques
    }

    # Écrire les données dans un fichier JSON
    with open(f'{pokemon_name}_stats_attaques.json', 'w') as json_file:
        json.dump(data_to_write, json_file, indent=4)

    print(f"Les statistiques et les attaques de {pokemon_name} ont été écrites dans {pokemon_name}_stats_attaques.json")
else:
    print(f"Erreur lors de la requête API: {response.status_code}")


