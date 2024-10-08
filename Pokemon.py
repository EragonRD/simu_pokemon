import math

class Pokemon : 
    def __init__(self, element, vie, attack, defense, special, vitesse, lvl):
        self.element = element
        self.vie = vie
        self.attack = attack 
        self.defense = defense 
        self.special = special
        self.vitesse = vitesse
        self.lvl = lvl

    def attack(self,capacite,defenseur):
        """
        attack enleve la vie du defenseur selon la formule [([[[lvl*0,4+2]*Att*Pui/def]/50]+2)*CM]
        CM etant le bonus (element) soit type vs type 
        """
        cm = calcul_cm(self.element,defenseur.element)
        defenseur.vie = vie - math.floor((math.floor(math.floor((math.floor(self.lvl * 0.4 + 2) * self.attack * capacite.puissance)/50)) +2)*cm)

class Capacite :
    def __init__(self, element, categorie, puissance, precision, pp, cible):
        self.element = element
        self.categorie = categorie
        self.puissance = puissance
        self.precision = precision 
        self.pp = pp
        self.cible = cible

def calcul_cm (attackant, defenseur):
    """
    le type de l'attaque, puis le type du defenseur
    renvoie le cm soit 0.5, 1 ou 1.5 
    """
    tableau_element(attackant, defenseur)
    return int