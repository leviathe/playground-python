# Simulateur de ville
# Créer 3 classes :Immeuble(nb_balcon), Supermarché(nb_rayons) et Banque(nb_coffre)
# Superclass Batiment (addresses, nb_Etage)
# 4 immeubles, 2 supermarché et 1 banque

class Batiment:

    def __init__(self, addresse, etage):
        self.addresse = addresse
        self.nb_etage = etage

    def get_addresse(self):
        return self.addresse

    def get_etage(self):
        return self.nb_etage



class Immeuble (Batiment):
    def __init__(self, addresse, etage, nb_balcon):
        super().__init__(addresse, etage)
        self.nb_balcon = nb_balcon

    def get_nb_balcon(self):
        return self.nb_etage



class Supermarche (Batiment):
    def __init__(self, addresse, etage, nb_rayon):
        super().__init__(addresse, etage)
        self.nb_rayon = nb_rayon

    def get_nb_rayon(self):
        return self.nb_rayon



class Banque (Batiment):
    def __init__(self, addresse, etage, nb_coffre):
        super().__init__(addresse, etage)
        self.nb_coffre = nb_coffre

    def get_nb_balcon(self):
        return self.nb_coffre

EtherBank = Banque('17 Rue de la Suisse', 2, 4)
G20 = Supermarche('09 Rue des USA', 1,17)
Carrefour = Supermarche('106 Rue de Mercantile', 1,50)
Mt_Parnasse = Immeuble('23 Rue de la Gare', 45, 0)
Immeuble_1 = Immeuble('23 Rue de la Feuille', 4, 24)
Immeuble_2 = Immeuble('24 Rue de la Feuille', 10, 50)
Immeuble_3 = Immeuble('25 Rue de la Feuille', 6, 4)