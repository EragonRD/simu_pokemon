
class Capacite :
    def __init__(self,nom, element, categorie, puissance, precision, pp):
        self.nom = nom
        self.element = element
        self.categorie = categorie
        self.puissance = puissance
        self.precision = precision 
        self.pp = pp
        

    def get_nom(self):
        return self.nom
        
    def get_element(self):
        return self.element

    def get_categorie(self):
        return self.categorie

    def get_puissance(self):
        return self.puissance

    def get_precision(self):
        return self.precision

    def get_pp(self):
        return self.pp
    
    def __str__(self):
        return f'{self.nom}'