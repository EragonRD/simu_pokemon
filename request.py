import requests

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
                return experience_levels  # Retourner tous les niveaux d'expérience
            else:
                return f"Erreur lors de la récupération des détails du taux de croissance: {growth_rate_detail_response.status_code}"
        else:
            return f"Erreur lors de la récupération des informations de l'espèce: {growth_rate_response.status_code}"
    else:
        return f"Erreur lors de la récupération des informations du Pokémon: {response.status_code}"


def get_level_from_experience(experience, levels_experience):
    # Parcourir les niveaux et les expériences associées
    for level_data in levels_experience:
        if experience < level_data['experience']:
            # Si l'expérience est inférieure à celle requise pour ce niveau,
            # on retourne le niveau précédent.
            return level_data['level'] - 1
    # Si l'expérience est supérieure ou égale à l'expérience nécessaire pour le dernier niveau, retourner le dernier niveau.
    return levels_experience[-1]['level']

def get_base_experience(pokemon_name):
    # Requête pour récupérer les détails du Pokémon
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
    response = requests.get(pokemon_url)
    
    if response.status_code == 200:
        data = response.json()
        base_experience = data.get('base_experience', "Donnée indisponible")
        return base_experience
    else:
        return f"Erreur lors de la récupération des informations du Pokémon: {response.status_code}"

# Exemple d'utilisation pour Pikachu
levels_experience = get_level_from_experience(5000, get_experience_to_level("pikachu"))
print(levels_experience)