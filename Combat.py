from Pokemon import Pokemon
import math

class Combat:
    def __init__(self,poke_1: Pokemon, poke_2: Pokemon, tour: int):
        self.poke_1 = poke_1
        self.poke_2 = poke_2
        self.tour = 0

    def get_pok_1(self):
        return self.poke_1
    
    def get_pok_2(self):
        return self.poke_2
    
    
    def lanceAttack(self):
        """
        attack enleve la vie du defenseur selon la formule [([[[lvl*0,4+2]*Att*Pui/def]/50]+2)*CM]
        CM etant le bonus (element) soit type vs type 
        """
        #decide de l'attaquand en fonction de la vitesse
        if(self.get_pok_1.get_vit>self.get_pok_2.get_vit):
            p1 = self.get_pok_1
            p2 = self.get_pok_2
        else :
            p1 = self.get_pok_2
            p2 = self.get_pok_1 
        
        #tour etant 0 de base attaquant ne sera pas lui au commencement
        if (self.tour):
            print(p1.__repr__)
            while True:
                chose = input("Choose a capacity ")
                if (chose<0 and chose>=4):
                    print("donnée invalide, veuillez choisir une capacite, un int entre 0 et 3.")
                else:
                    attaque = p1.get_capacites()[chose]
                    print(f"Vous attaquez avec {attaque} !")
                    break
            cm = calcul_cm(p1.get_elem,p2.elem)
            # attaque physique
            if (attaque.get_categorie == 0 and attaque.get_cible == 1): #verifiez si les conditions sont correctent
                #transforme les hp du defenseur 
                p2.set_hp(p2.get_hp-math.floor((math.floor(math.floor(((math.floor(p1.get_lvl * 0.4 + 2) * p1.get_atk_n * attaque.puissance)/p2.get_def_n)/50)) +2)*cm))
            # attaque special
            if (attaque.get_categorie == 0 and attaque.get_cible == 1): #verifiez si les conditions sont correctent
                #transforme les hp du defenseur 
                p2.set_hp(p2.get_hp-math.floor((math.floor(math.floor(((math.floor(p1.get_lvl * 0.4 + 2) * p1.get_atk_spe * attaque.puissance)/p2.get_def_spe)/50)) +2)*cm))
            else :
                print("attaque non conforme, à verifier")
        
        #
        else :
            print(p.__repr__)
            while True:
                chose = input("Choose a capacity ")
                if (chose<0 and chose>=4):
                    print("donnée invalide, veuillez choisir une capacite, un int entre 0 et 3.")
                else:
                    attaque = p.get_capacites()[chose]
                    print(f"Vous attaquez avec {attaque} !")
                    break
            cm = calcul_cm(p.get_elem,p1.elem)
            # attaque physique
            if (attaque.get_categorie == 0 and attaque.get_cible == 1): #verifiez si les conditions sont correctent
                #transforme les hp du defenseur 
                p1.set_hp(p1.get_hp-math.floor((math.floor(math.floor(((math.floor(p.get_lvl * 0.4 + 2) * p.get_atk_n * attaque.puissance)/p1.get_def_n)/50)) +2)*cm))
            # attaque special
            if (attaque.get_categorie == 0 and attaque.get_cible == 1): #verifiez si les conditions sont correctent
                #transforme les hp du defenseur 
                p1.set_hp(p1.get_hp-math.floor((math.floor(math.floor(((math.floor(p.get_lvl * 0.4 + 2) * p.get_atk_spe * attaque.puissance)/p1.get_def_spe)/50)) +2)*cm))
            else :
                print("attaque non conforme, à verifier")




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

"""

def lanceAttack(attaquant :type[Pokemon],defenseur: type[Pokemon]):
        print(attaquant.capacites)
        try :
            print(str(attaquant))
            print(repr(attaquant))
            chose = int(input ("Chose a capacity : "))
            print(str(i) + " :" + "\n".join(str(attaquant.capacites[i])) for i in range(4))
            
        except ValueError:
            print(f"la velur entrée n'est pas valide")
        cm = calcul_cm(attaquant.element,defenseur.element)
        capacite = attaquant.capacites[chose]
        if(capacite==None):
            print("cant attack sorry next turn")
            return "non non non"
        # attaque physique
        if capacite.categorie == 0 and capacite.cible == 1 :
            defenseur.vie = defenseur.vie - math.floor((math.floor(math.floor(((math.floor(attaquant.lvl * 0.4 + 2) * attaquant.attack * capacite.puissance)/attaquant.defense)/50)) +2)*cm)
        # attaque spéciale
        if capacite.categorie == 1 and capacite.cible == 1 : 
            defenseur.vie = defenseur.vie - math.floor((math.floor(math.floor(((math.floor(attaquant.lvl * 0.4 + 2) * attaquant.attSpecial * capacite.puissance)/attaquant.defSpecial)/50)) +2)*cm)



"""
