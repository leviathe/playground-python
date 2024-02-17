from main import Player
from Weapon import Weapon

# TP
# Créer une méthode set_weapon() pour changer l'arme du joueur
# Modifier attack_player pour prendre en compte les dégât de l'arme si équipé. Dégât en +

knife = Weapon('Couteau', 7)

player_1 = Player("Paul", 20, 3)
player_2 = Player("Luap", 20, 5)

player_1.set_weapon(knife)
print(player_1.get_weapon())

print(player_1.get_pseudo(), "attaque", player_2.get_pseudo())
player_1.attack_player(player_2)


print("Bienvenue au joueur", player_1.pseudo , "/ Points de vie :", player_1.health, "/ Attaque :", player_1.attack)
print("Bienvenue au joueur", player_2.pseudo , "/ Points de vie :", player_2.health, "/ Attaque :", player_2.attack)