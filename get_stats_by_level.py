import requests
import json

# URL de base de l'API Pokéapi
base_url = "https://pokeapi.co/api/v2/pokemon/"

# Fonction pour obtenir les statistiques d'un Pokémon
def get_pokemon_stats(pokemon_id):
    url = f"{base_url}{pokemon_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        stats = {}
        for stat in pokemon_data['stats']:
            stats[stat['stat']['name']] = stat['base_stat']

        # Extraire les types du Pokémon
        types = [type_info['type']['name'] for type_info in pokemon_data['types']]

        return {
            "name": pokemon_data['name'],
            "stats": stats,
            "types": types
        }
    else:
        print(f"Erreur lors de la requête API pour le Pokémon {pokemon_id}: {response.status_code}")
        return None

# Récupérer les statistiques des 151 premiers Pokémon
pokemon_stats = {}
for pokemon_id in range(1, 152):
    pokemon_data = get_pokemon_stats(pokemon_id)
    if pokemon_data:
        pokemon_stats[pokemon_id] = pokemon_data

# Écrire les données dans un fichier JSON
with open('pokemon_stats_level_1.json', 'w') as json_file:
    json.dump(pokemon_stats, json_file, indent=4)

print("Les statistiques des 151 premiers Pokémon au niveau 1 ont été écrites dans pokemon_stats_level_1.json")
