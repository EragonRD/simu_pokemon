from math import sqrt
import random
import numpy as np
from Capacite import Capacite

class Pokemon:
    def __init__(self, nom, elem, hp, atk_n, atk_spe, def_n , def_spe, vit, niveau,xp = 0):
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
        self.elem = elem
        self.atk_n_base = atk_n
        self.atk_spe_base = atk_spe
        self.def_n_base = def_n
        self.def_spe_base = def_spe
        self.vit_base = vit
        self.xp = xp
        self.capacites = np.empty([4], dtype=Capacite) 
        #Definir le niveau du pokemon
        self.niveau = niveau   #self.fonction_pour_calculer_niveau()
        #Met a jour les stats et l'hp
        self.Update_stat_and_hp()

    #descirption du Pokemon
    def __str__(self):
        return f'\nThe pokemon is a {self.nom} as for element {self.elem} and it stat are  : \n life {self.hp} \n attack {self.atk_n} \n defense {self.def_n} \n attaque Spé {self.atk_spe} \n defense Spé {self.def_spe} \n vitesse {self.vit} \n LVL {self.niveau}'

    #affichage des capacites avec leur indices 
    def __repr__(self):
        return f'0 : {self.capacites[0]}\t 1 : {self.capacites[1]}\t 2 : {self.capacites[2]}\t 3: {self.capacites[3]}'
    
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
        return int((((self.niveau / 100) + 1) * base) + self.niveau + (((sqrt(base)*f(NE))+self.niveau)/2.5))

    def calcul_stat(self, NE, base):
        #Formule de calcul pour les stats
        return int(((((self.niveau/50)+1)*base)/1.5) + (((sqrt(base)*f(NE))+self.niveau)/2.5))
    
    def level_up(self):
        #Methode d'augmentation de niveau
        self.niveau += 1
        self.Update_stat_and_hp()
    
    def get_level_from_experience(self, levels_experience):
        # Parcourir les niveaux et les expériences associées
        for level_data in levels_experience:
            if self.xp < level_data['experience']:
                # Si l'expérience est inférieure à celle requise pour ce niveau,
                # on retourne le niveau précédent.
                while self.niveau < (level_data['level'] - 1) :
                    self.level_up()
    
    #Getters
    def get_nom(self):
        return self.nom
    
    def get_elem(self):
        return self.elem

    def get_hp(self):
        return self.hp

    def get_atk_n(self):
        return self.atk_n

    def get_atk_spe(self):
        return self.atk_spe

    def get_def_n(self):
        return self.def_n

    def get_def_spe(self):
        return self.def_spe

    def get_vit(self):
        return self.vit

    def get_niveau(self):
        return self.niveau

    def get_xp(self):
        return self.xp
    
    def get_capacites(self):
        return self.capacites
    
    #1 setter hp
    def set_hp(self, value):
        self.hp = value
               



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

