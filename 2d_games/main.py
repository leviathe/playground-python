#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((640, 480), RESIZABLE) # ou FULLSCREEN pou le plein écran

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert() # gestion pour adapter
fenetre.blit(fond, (0,0)) # "colle l'image fond en haut à gauche de l'image fenetre."

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha() #gestion de la transparence de l'image
position_perso = perso.get_rect() #l'objet Rect permet de manipuler des surfaces rectangulaires.
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

pygame.key.set_repeat(400, 30)  # Le délai avant de continuer les déplacements quand la touche reste enfoncée (en millisecondes)
                                # Le temps entre chaque déplacement. (en millisecondes)

#Boucle infinie
while continuer == 1:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT or event.type == K_x:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
        if event.type == KEYDOWN and event.key == K_DOWN: #Si flèche du bas
            position_perso = position_perso.move(0,3) # On descend le perso
        if event.type == KEYDOWN and event.key == K_UP: #Si flèche du bas
            position_perso = position_perso.move(0,-3)
        if event.type == KEYDOWN and event.key == K_RIGHT: #Si flèche du bas
            position_perso = position_perso.move(3,0)
        if event.type == KEYDOWN and event.key == K_LEFT: #Si flèche du bas
            position_perso = position_perso.move(-3,0)
    #Re-collage
    fenetre.blit(fond, (0,0))   
    fenetre.blit(perso, position_perso)
    #Rafraichissement
    pygame.display.flip()
    
    # Affiche "Zone dangereuse" lorsque l'on clique avec le bouton droit dans la bande de 100px de hauteur
    # d'en haut.
    if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
    print("Zone dangereuse")



#--------- COMMANDE SUPPLEMENTAIRE ---------

# pygame.display.flip() --> Ligne pour rafraichissement de la fenêtre.
# image.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent

