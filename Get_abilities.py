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

    try:
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
                    puissance = move_data.get('power', None)
                    if puissance is not None:  # Ignorer les attaques avec une puissance nulle
                        attaque = {
                            "nom": move_data['name'],
                            "type": move_data['type']['name'],
                            "category":move_data['damage_class']['name'],
                            "puissance": puissance,
                            "precision": move_data.get('accuracy', 'donnée indisponible'),
                            "pp": move_data['pp'],
                            "effet": move_data['effect_entries'][0]['effect'] if move_data['effect_entries'] else "Aucun effet"
                        }
                        attaques.append(attaque)

            # Extraire le type du Pokémon
            pokemon_types = [type_info['type']['name'] for type_info in pokemon_data['types']]

            # Créer un dictionnaire pour les données à écrire dans le fichier JSON
            data_to_write = {
                "nom": pokemon_data['name'],
                "statistiques": pokemon_stats,
                "attaques": attaques,
                "types": pokemon_types,
                "xp_base": pokemon_data.get('base_experience', 'donnée indisponible')
            }

            # Écrire les données dans un fichier JSON
            with open(file_name, 'w') as json_file:
                json.dump(data_to_write, json_file, indent=4)

            print(f"Les statistiques et les attaques de {pokemon_name} ont été écrites dans {file_name}")
        else:
            print(f"Erreur lors de la requête API: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête API: {e}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier JSON: {e}")
