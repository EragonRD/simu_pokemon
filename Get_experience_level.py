import requests
import json
 
 
def get_experience_to_level(pokemon_name):
    # Requête pour récupérer les détails du Pokémon
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
    response = requests.get(pokemon_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Requête pour récupérer le taux de croissance du Pokémon
        growth_rate_url = data['species']['url']
        growth_rate_response = requests.get(growth_rate_url)
        if growth_rate_response.status_code == 200:
            species_data = growth_rate_response.json()
            growth_rate_detail_url = species_data['growth_rate']['url']
            
            # Requête pour récupérer les détails du taux de croissance
            growth_rate_detail_response = requests.get(growth_rate_detail_url)
            if growth_rate_detail_response.status_code == 200:
                growth_data = growth_rate_detail_response.json()
                experience_levels = growth_data['levels']
                # Écrire les données dans un fichier JSON
                with open(f'{pokemon_name}_experience_to_level.json', 'w') as json_file:
                    json.dump(experience_levels, json_file, indent=4)
 
 
 
 