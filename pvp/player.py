
class Player:    # Moule pour avoir concepte de joueur

    def __init__(self, pseudo, health, attack): # C'est le constructeur. Permet d'attribuer les caractéristiques de chaque personne
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        self.weapon_damage = None
        print("Bienvenue au joueur", self.pseudo , "/ Points de vie :", self.health, "/ Attack :", self.attack)

    def get_pseudo(self): # Methode (== fonction dans classe) getter / assesseur : pour récupérer infos
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def get_weapon(self):
        return self.weapon_damage

    def damage(self, damage):
        self.health -= damage
        print("Aïe... vous venez de subir", damage, "dégats !")

    def attack_player(self, target_player):
        target_player.damage((self.attack + self.weapon_damage))

    def set_weapon(self, recovered_weapon):
        self.weapon = recovered_weapon.name
        self.weapon_damage = recovered_weapon.damage