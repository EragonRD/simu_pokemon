import math
import numpy as np
from Capacite import Capacite

class Pokemon : 
    def __init__(self, name : str ,element: str, vie: int, attack: int, defense: int, attSpecial :int, defSpecial :int, vitesse :int, lvl :int):
        self.name = name
        self.element = element
        self.vie = vie
        self.attack = attack 
        self.defense = defense 
        self.attSpecial = attSpecial
        self.defSpecial = defSpecial
        self.vitesse = vitesse
        self.lvl = lvl
        self.capacites = np.empty([4], dtype=Capacite) 

    #descirption du Pokemon
    def __str__(self):
        return f'\nThe pokemon is a {self.name} as for element {self.element} and it stat are  : \n life {self.vie} \n attack {self.attack} \n defense {self.defense} \n attaque Spé {self.attSpecial} \n defense Spé {self.defSpecial} \n vitesse {self.vitesse} \n LVL {self.lvl}'

    #affichage des capacites avec leur indices 
    def __repr__(self):
        return f'0 : {self.capacites[0]}\t 1 : {self.capacites[1]}\t 2 : {self.capacites[2]}\t 3: {self.capacites[3]}'
    
    def apprendreCapacite():
        for i in range(4):
            if(self.capacites[i]!=None):
                continue
            else : 


        print("")
        self.capacites[]



# Test en dur ! 

picka = Pokemon("Pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)
