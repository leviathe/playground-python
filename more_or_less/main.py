
# Compter les clients
#for num_client in range(1,6):
#    print('Vous êtes le client n°', num_client)

# for each : pour chaque éléments d'une liste donnée. Exemple :

# Lister les emails
#emails=['ppazart@gmail.com', 'paezef@gmail.com', 'bioshock@outlook.com']

# Blacklist
#blacklist = [ 'paezef@gmail.com']

# Pour chacune des valeurs, j'affiche "Email envoyé à [insérer email]

#for email in emails :
#    if email in blacklist :
#        print('Email {} interdit ! Envoi impossible...'.format(email))
#        continue # Pour passer à l'itération suivante
        #break - cesse d'exécuter la boucle

#    print("Email envoyé à :", email)





# While : tant qu'une condition est vrai
# salarié 1500 $ / mois
#salary = 1500

# tant que salarié < 2000 $, +120 $

#while salary < 2000 :
#    salary += 120
#    print("Votre salaire actuel est de ", salary, '$')
#print("Fin du programme")



# Un youtuber "Gravinou", 2500 abonnés
#subscribers_count = 2500

# Il gagne 10% d'audience supplémentaire chaque mois
#months = 0

# On souhaite estimer, combien aura-t'il d'abonné, après 2 ans
#while months <= 24 :
#    subscribers_count *= 1.1
    # Afficher le nombre d'abonnés
#    print("Vous avez actuellement {} abonnés".format(subscribers_count))
    # On oublie pas de passer au mois suivant
#    months += 1

# ------ TP ------
# Le juste prix
# Choisir un nombre entre 1 et 1000
# Le joueur doit dire une valeur
# On doit lui répondre, c'est plus ou c'est moins ou c'est gagné
# Tant que le jeu n'est pas fini, demander à l'utilisateur de rentrée un prix

from random import randint

price = randint(1,1000)
estimation = 0
while estimation != price :
    if estimation < price :
        print("C'est plus")
        estimation = int(input("Quelle est le prix selon vous ? -> "))
    elif estimation > price :
        print("C'est moins")
        estimation = int(input("Quelle est le prix selon vous ? -> "))
print("Vous avez trouvé, le prix était : ", estimation, "$")