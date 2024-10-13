from Pokemon import Pokemon
from Capacite import Capacite
import math

class Combat:
    def __init__(self,poke_1: Pokemon, poke_2: Pokemon):
        self.poke_1 = poke_1
        self.poke_2 = poke_2
        self.tour = 0

    def get_pok_1(self):
        return self.poke_1
    
    def get_pok_2(self):
        return self.poke_2
    
    
    def lance_combat(self):
        """
        attack enleve la vie du defenseur selon la formule [([[[lvl*0,4+2]*Att*Pui/def]/50]+2)*CM]
        CM etant le bonus (element) soit type vs type 
        """
        #decide de l'attaquand en fonction de la vitesse
        print(self.poke_1.get_vit())
        if(self.poke_1.get_vit()<self.poke_2.get_vit()):
            p1 = self.poke_1
            p2 = self.poke_2
        else :
            p1 = self.poke_2
            p2 = self.poke_1 
        #chacun sont tour celon la boucle 1,0,1 
        if (self.tour):
            print(p1.get_nom()+" se prepare pour lancer une attaque")
            print(repr(p1))
            attaque = p1.get_capacites()[choix_de_la_capacite()]
            print(f"Vous attaquez avec {attaque} !")
            lance_attack(p1,p2,attaque)
        else :
            print(p2.get_nom()+" se prepare pour lancer une attaque")
            print(repr(p2))
            attaque = p2.get_capacites()[choix_de_la_capacite()]
            print(f"Vous attaquez avec {attaque} !")
            lance_attack(p2,p1,attaque)
    
        self.tour = 1 - self.tour
        print(str(self.poke_1))
        print(str(self.poke_2))




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




def lance_attack(p1:Pokemon,p2:Pokemon,attaque:Capacite):
    """
    prend un pokemon attaquant p1 attaquant et p2 defenseur, une capacite 
    enleve les hp du pokemon defenseur en fonction de la formule
    """
    if (attaque == None):
        print("ne pouvant pas lancez un sort notre pokemon s'elance a pleine vitesse tete la premiere")
        degat = math.floor((math.floor(math.floor(((math.floor(int(p1.get_niveau()) * 0.4 + 2) * p1.get_atk_n() * 150) / p2.get_def_n()) / 50)) + 2) * 1)
        p2.set_hp(p2.get_hp()- degat)
        p1.set_hp(p1.get_hp()- int(degat/4))
        print("une attaque de "+str(degat) +" degats")
    # attaque physique
    elif (attaque.get_categorie() == "normal" or attaque.get_categorie() == "physical"): #verifiez si les conditions sont correctent
        #transforme les hp du defenseur 
        p2.set_hp(p2.get_hp()-math.floor((math.floor(math.floor(((math.floor(p1.get_niveau() * 0.4 + 2) * p1.get_atk_n() * attaque.get_puissance())/p2.get_def_n)/50)) +2)*cm))
    # attaque special
    elif (attaque.get_categorie() == "special"): #verifiez si les conditions sont correctent
        #transforme les hp du defenseur 
        p2.set_hp(p2.get_hp() - math.floor((math.floor(math.floor(((math.floor(p1.get_niveau() * 0.4 + 2) * p1.get_atk_n() * attaque.get_puissance()) / p2.get_def_n()) / 50)) + 2) * cm))
    else :
        print("attaque echoué, better luck next time")



def lance_attack(p1: Pokemon, p2: Pokemon, attaque: Capacite):
    """
    Lance une attaque du Pokémon p1 (attaquant) sur p2 (défenseur) en utilisant une capacité.
    Modifie les HP du Pokémon défenseur selon la formule de dégâts Pokémon.
    """
    cm = calcul_cm(p1.get_elem(),p2.get_elem())
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
