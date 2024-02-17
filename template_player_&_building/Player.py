class Player:    # Moule pour avoir concepte de joueur

    def __init__(self, pseudo, health, attack): # C'est le constructeur. Permet d'attribuer les caractéristiques de chaque personne
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", self.pseudo , "/ Points de vie :", self.health, "/ Attack :", self.attack)

    def get_pseudo(self): # Methode (== fonction dans classe) getter / assesseur : pour récupérer infos
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
        print("Aïe... vous venez de subir", damage, "dégats !")

    def attack_player(self, target_player):
        target_player.damage(self.attack)




class Warrior (Player): # Warrior va hériter de caractéristique de Player

    def __init__(self, pseudo, health, attack): # C'est le constructeur. Permet d'attribuer les caractéristiques de chaque personne
        super().__init__(pseudo, health, attack) # On appelle la classe supérieur Player pour recevoir les attributs
        self.armor = 3
        print("Bienvenue au guerrier", self.pseudo, "/ Points de vie :", self.health, "/ Attack :", self.attack)

    def get_armor_point(self):
        return self.armor

    def damage(self, damage):
        if self.armor > 0 :
            self.armor -= 1
            damage = 0
        super().damage(damage)


    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargés")


player = Player("Paul", 20, 2)
player.damage(3)

warrior = Warrior("DarkWarrior", 30, 4)
warrior.damage(4)
print("vie :", warrior.get_health(), '/ armure :', warrior.get_armor_point())

# Pour vérifier l'héritage entre deux classe, on peut faire :

if issubclass(Warrior, Player) :
    print("Le guerrier est bien une  spécialisation de player")