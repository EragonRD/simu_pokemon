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

    
    """def apprendreCapacite(c :Capacite):
        for i in range(4):
            if(capacites[i]):

        print("")
        self.capacites[]  """



# Test en dur ! 

picka = Pokemon("Electrique",154,91,115,113,93,50)
salameche = Pokemon("Feu",154,91,115,113,93,50)
