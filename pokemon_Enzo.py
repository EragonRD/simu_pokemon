from math import sqrt
import random

class pokemon:
    def __init__(self, nom, hp, atk_n, atk_spe, def_n , def_spe, vit, xp = 0):
        self.nom = nom
        #Generer les Niveau d'Effort pour chaque stats du pokemon
        self.hp_NE = random.randint(0,10)
        self.atk_n_NE = random.randint(0,10)
        self.atk_spe_NE = random.randint(0,10)
        self.def_n_NE = random.randint(0,10)
        self.def_spe_NE = random.randint(0,10)
        self.vit_NE = random.randint(0,10)
        #Definir les stats de base du pokemon
        self.hp_base = hp
        self.atk_n_base = atk_n
        self.atk_spe_base = atk_spe
        self.def_n_base = def_n
        self.def_spe_base = def_spe
        self.vit_base = vit
        self.xp = xp
        #Definir le niveau du pokemon
        self.niveau = self.fonction_pour_calculer_niveau()
        #Met a jour les stats et l'hp
        self.Update_stat_and_hp()
    
    def Update_stat_and_hp(self):
        #Lance la fonction de calcul pour chaque stats et hp
        self.hp = self.calcul_pv(self.hp_NE, self.hp_base)
        self.atk_n = self.calcul_stat(self.atk_n_NE, self.atk_n_base)
        self.atk_spe = self.calcul_stat(self.atk_spe_NE, self.atk_spe_base)
        self.def_n = self.calcul_stat(self.def_n_NE, self.def_n_base)
        self.def_spe = self.calcul_stat(self.def_spe_NE, self.def_spe_base)
        self.vit = self.calcul_stat(self.vit_NE, self.vit_base)

    def calcul_pv(self, NE, base):
        #Formule de calcul pour les pv
        return (((self.niveau / 100) + 1) * base) + self.niveau + (((sqrt(base)*f(NE))+self.niveau)/2.5)

    def calcul_stat(self, NE, base):
        #Formule de calcul pour les stats
        return ((((self.niveau/50)+1)*base)/1.5) + (((sqrt(base)*f(NE))+self.niveau)/2.5)
    
    def level_up(self):
        #Methode d'augmentation de niveau
        self.niveau += 1
        self.Update_stat_and_hp()
    
    def fonction_pour_calculer_niveau(self):
        #Fonction a voir pour l'implementation
        pass



def f(NE):
    values = {
        0: 0,
        1: 2,
        2: 3,
        3: 4,
        4: 7,
        5: 8,
        6: 9,
        7: 14,
        8: 15,
        9: 16,
        10: 25
    }
    return values.get(NE)

