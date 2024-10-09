import requests
import json
import os

# Fonction pour obtenir les informations sur un Pokémon
def get_ability(pokemon_name):
    # Nom du fichier JSON
    file_name = f'{pokemon_name}_stats_attaques.json'

    # Vérifier si le fichier existe déjà
    if os.path.exists(file_name):
        print(f"Le fichier {file_name} existe déjà. Les données ne seront pas réécrites.")
        return

    # URL de l'API pour obtenir les informations sur un Pokémon
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
            "nom": pokemon_data['name'],
            "statistiques": pokemon_stats,
            "attaques": attaques
        }

        # Écrire les données dans un fichier JSON
        with open(file_name, 'w') as json_file:
            json.dump(data_to_write, json_file, indent=4)

        print(f"Les statistiques et les attaques de {pokemon_name} ont été écrites dans {file_name}")
    else:
        print(f"Erreur lors de la requête API: {response.status_code}")
