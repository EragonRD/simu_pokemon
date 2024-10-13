
class Capacite :
    def __init__(self,nom, element, categorie, puissance, precision, pp, cible):
        self.nom = nom
        self.element = element
        self.categorie = categorie
        self.puissance = puissance
        self.precision = precision 
        self.pp = pp
        
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