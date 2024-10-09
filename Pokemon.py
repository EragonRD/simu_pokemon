import math
import numpy as np

class Pokemon : 
    def __init__(self, element: str, vie: int, attack: int, defense: int, attSpecial :int, defSpecial :int, vitesse :int, lvl :int):
        self.element = element
        self.vie = vie
        self.attack = attack 
        self.defense = defense 
        self.attSpecial = attSpecial
        self.defSpecial = defSpecial
        self.vitesse = vitesse
        self.lvl = lvl
        self.capacites = np.empty(4, dtype=Capacite) 

    def lanceAttack(self,defenseur: type[Pokemon]):
        """
        attack enleve la vie du defenseur selon la formule [([[[lvl*0,4+2]*Att*Pui/def]/50]+2)*CM]
        CM etant le bonus (element) soit type vs type 
        """
        print(self.capacites)
        try :
            chose = int(input ("Chose a capacity"))
        except ValueError:
            print(f"la velur entrée n'est pas valide")
        
        cm = calcul_cm(self.element,defenseur.element)
        # attaque physique
        if capacite.categorie == 0 and capacite.cible == 1 :
            defenseur.vie = defenseur.vie - math.floor((math.floor(math.floor(((math.floor(self.lvl * 0.4 + 2) * self.attack * capacite.puissance)/self.defense)/50)) +2)*cm)
        # attaque spéciale
        if capacite.categorie == 1 and capacite.cible == 1 : 
            defenseur.vie = defenseur.vie - math.floor((math.floor(math.floor(((math.floor(self.lvl * 0.4 + 2) * self.attSpecial * capacite.puissance)/self.defSpecial)/50)) +2)*cm)


    """def apprendreCapacite(c :Capacite):
        for i in range(4):
            if(capacites[i]):

        print("")
        self.capacites[]  """
    
    


class Capacite :
    def __init__(self, element, categorie, puissance, precision, pp, cible):
        self.element = element
        self.categorie = categorie
        self.puissance = puissance
        self.precision = precision 
        self.pp = pp
        self.cible = cible

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

def calcul_cm(attack, defense):
    """
    l'element de l'attaque, puis l'element du defenseur
    renvoie le cm soit 0, 0.5, 1 ou 2 
    """
    if (attack not in list_element) or (defense not in list_element):
        return "frerot fait un effort sur la syntaxe, majuscule accent etc" 
    if (attack in element_chart) and (defense in element_chart[attack]):
        return element_chart[attack][defense]
    else :
        return 1




# Test en dur ! 

picka = Pokemon("Electrique",154,91,115,113,93,50)
salameche = Pokemon("Feu",154,91,115,113,93,50)
charge = Capacite("Normal",)


print(calcul_cm("Feu","Eau"))