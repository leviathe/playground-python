import numpy as np
import random


print("Bienvenue sur la machine à sous GravenFruitiiii")

fruit = ["ananas.png", "cerise.png", "orange.png", "pasteque.png", "pomme_dore.png"]

resultat = random.choices(fruit, k=3)

print(resultat)