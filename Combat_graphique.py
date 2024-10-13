from Pokemon import Pokemon
from Capacite import Capacite
import math

class Combat:
    def __init__(self,poke_1: Pokemon, poke_2: Pokemon):
        self.poke_1 = poke_1
        self.poke_2 = poke_2
        self.engagement()
        self.info = ""

    def get_pok_1(self):
        return self.poke_1
    
    def get_pok_2(self):
        return self.poke_2
    
    def get_capacites(self):
        if self.tour:
            return self.poke_2.get_capacites()
        else :
            return self.poke_1.get_capacites()
    
    def engagement(self):
        if(self.poke_1.get_vit()<self.poke_2.get_vit()):
            self.tour = 1
        else :
            self.tour = 0
    
    
    def lance_combat(self):
        """
        attack enleve la vie du defenseur selon la formule [([[[lvl*0,4+2]*Att*Pui/def]/50]+2)*CM]
        CM etant le bonus (element) soit type vs type 
        """
        #decide de l'attaquand en fonction de la vitesse
        # print(self.poke_1.get_vit())
        
        
        #chacun sont tour celon la boucle 1,0,1 
        if (self.tour):
            cm = calcul_cm(self.poke_2.get_elem(),self.poke_1.get_elem())
            self.info = self.poke_2.get_nom() + " se prepare pour lancer une attaque"
            
        else :
            cm = calcul_cm(self.poke_1.get_elem(),self.poke_2.get_elem())
            self.info = self.poke_1.get_nom() + " se prepare pour lancer une attaque"
            
    
    def lance_combat(self):
        """
        attack enleve la vie du defenseur selon la formule [([[[lvl*0,4+2]*Att*Pui/def]/50]+2)*CM]
        CM etant le bonus (element) soit type vs type 
        """
       
        if (self.tour):
            self.info = self.poke_2.get_nom() + " se prepare pour lancer une attaque"
        else :
            self.info = self.poke_1.get_nom() + " se prepare pour lancer une attaque"

    def attaque_tour(self, attaque):
        if (self.tour):
            self.info = self.poke_2.get_nom() + " attaque avec {attaque}"
            lance_attack(self.poke_2, self.poke_1, attaque)
        else :
            self.info = self.poke_1.get_nom() + " attaque avec {attaque}"
            lance_attack(self.poke_1, self.poke_2, attaque)
        self.tour = 1 - self.tour





list_element=["Normal", "Combat", "Vol", "Poison", "Sol", "Roche", "Insecte", "Spectre", "Acier", "Feu", "Eau", "Plante", "Electrique", "Psy", "Glace", "Dragon", "Ténèbres", "Fée"]

# Dictionnaire représentant les interactions des types
element_chart = {
    "Normal":     {"Roche": 0.5, "Spectre": 0, "Acier": 0.5},
    "Combat":     {"Normal": 2, "Vol": 0.5, "Poison": 0.5, "Roche": 2, "Insecte": 0.5, 
                   "Spectre": 0, "Acier": 2, "Glace": 2, "Ténèbres": 2, "Fée": 0.5},
    "Vol":        {"Combat": 2, "Roche": 0.5, "Insecte": 2, "Acier": 0.5, "Plante": 2, 
                   "Electrique": 0.5},
    "Poison":     {"Roche": 0.5, "Sol": 0.5, "Acier": 0, "Plante": 2, "Fée": 2},
    "Sol":        {"Vol": 0, "Roche": 2, "Insecte": 0.5, "Acier": 2, "Feu": 2, "Electrique": 2, 
                   "Plante": 0.5},
    "Roche":      {"Combat": 0.5, "Vol": 2, "Sol": 0.5, "Insecte": 2, "Acier": 0.5, 
                   "Feu": 2, "Glace": 2},
    "Insecte":    {"Combat": 0.5, "Vol": 0.5, "Poison": 0.5, "Spectre": 0.5, "Acier": 0.5, 
                   "Feu": 0.5, "Plante": 2, "Psy": 2, "Ténèbres": 2, "Fée": 0.5},
    "Spectre":    {"Normal": 0, "Spectre": 2, "Psy": 2, "Ténèbres": 0.5},
    "Acier":      {"Roche": 2, "Acier": 0.5, "Feu": 0.5, "Eau": 0.5, "Plante": 0.5, 
                   "Glace": 2, "Fée": 2},
    "Feu":        {"Roche": 0.5, "Insecte": 2, "Acier": 2, "Feu": 0.5, "Eau": 0.5, 
                   "Plante": 2, "Glace": 2, "Dragon": 0.5},
    "Eau":        {"Roche": 2, "Feu": 2, "Eau": 0.5, "Plante": 0.5, "Dragon": 0.5},
    "Plante":     {"Vol": 0.5, "Poison": 0.5, "Roche": 2, "Sol": 2, "Insecte": 0.5, 
                   "Acier": 0.5, "Feu": 0.5, "Eau": 2, "Plante": 0.5, "Dragon": 0.5},
    "Electrique":   {"Vol": 2, "Sol": 0, "Roche": 1, "Electrique": 0.5, "Eau": 2, "Plante": 0.5, 
                   "Dragon": 0.5},
    "Psy":        {"Combat": 2, "Poison": 2, "Spectre": 0.5, "Acier": 0.5, "Psy": 0.5, 
                   "Ténèbres": 0},
    "Glace":      {"Vol": 2, "Sol": 2, "Roche": 0.5, "Insecte": 1, "Acier": 0.5, 
                   "Feu": 0.5, "Eau": 0.5, "Plante": 2, "Dragon": 2},
    "Dragon":     {"Acier": 0.5, "Dragon": 2, "Fée": 0},
    "Ténèbres":   {"Combat": 0.5, "Spectre": 2, "Psy": 2, "Fée": 0.5},
    "Fée":        {"Combat": 2, "Dragon": 2, "Feu": 0.5, "Acier": 0.5, "Ténèbres": 2}
}

def calcul_cm(attack:str, defense:str):
    """
    l'element de l'attaque, puis l'element du defenseur
    renvoie le cm soit 0, 0.5, 1 ou 2 
    """
    if (attack not in list_element) or (defense not in list_element):
        return "Erreur de calcul du cm !" 
    if (attack in element_chart) and (defense in element_chart[attack]):
        return element_chart[attack][defense]
    else :
        return 1


def choix_de_la_capacite():
    """
    attend l'input du user un int entre 0 et 3 
    """
    while True:
        choix = input("Choose a capacity (0-3): ")
        try:
            # Conversion de l'entrée en entier
            choix = int(choix)
            # Vérification si l'entier est entre 0 et 3
            if 0 <= choix <= 3:
                return choix
            else:
                print("donnée invalide, veuillez choisir une capacité, un entier entre 0 et 3.")
        except ValueError:
            print("donnée invalide, veuillez entrer un nombre entier.")


def lance_attack(p1: Pokemon, p2: Pokemon, attaque: Capacite):
    """
    Lance une attaque du Pokémon p1 (attaquant) sur p2 (défenseur) en utilisant une capacité.
    Modifie les HP du Pokémon défenseur selon la formule de dégâts Pokémon.
    """
    cm = 1.5
    if attaque is None:
        print("Ne pouvant pas lancer un sort, notre Pokémon s'élance à pleine vitesse tête la première !")
        # Attaque de base sans capacité 
        degat = math.floor((math.floor(math.floor(((math.floor(int(p1.get_niveau()) * 0.4 + 2) * int(p1.get_atk_n()) * 150) / int(p2.get_def_n())) / 50)) + 2) * 1)
        p2.set_hp(p2.get_hp() - degat)
        # Le Pokémon perd un quart des dégâts infligés 
        p1.set_hp(p1.get_hp() - int(degat / 4))
        print(f"Une attaque physique inflige {degat} dégâts à l'adversaire.")

    # Attaque physique
    elif attaque.get_categorie() == "normal" or attaque.get_categorie() == "physical":
        # Dégâts pour une attaque physique
        degat = math.floor((math.floor(math.floor(((math.floor(int(p1.get_niveau()) * 0.4 + 2) * int(p1.get_atk_n()) * int(attaque.get_puissance())) / int(p2.get_def_n())) / 50)) + 2) * cm)
        p2.set_hp(p2.get_hp() - degat)
        print(f"{p1.get_nom()} utilise {attaque.get_nom()} et inflige {degat} dégâts à {p2.get_nom()}.")

    # Attaque spéciale
    elif attaque.get_categorie() == "special":
        # Dégâts pour une attaque spéciale
        degat = math.floor((math.floor(math.floor(((math.floor(int(p1.get_niveau()) * 0.4 + 2) * int(p1.get_atk_spe()) * int(attaque.get_puissance())) / int(p2.get_def_spe())) / 50)) + 2) * cm)
        p2.set_hp(p2.get_hp() - degat)
        print(f"{p1.get_nom()} utilise {attaque.get_nom()} et inflige {degat} dégâts à {p2.get_nom()}.")

    else:
        # Catégorie inconnue, échec de l'attaque
        print(f"L'attaque {attaque.get_nom()} a échoué, meilleure chance la prochaine fois !")
