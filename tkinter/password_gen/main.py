import string
from random import randint, choice
from tkinter import *


def generate_password():
    password_min  = 6
    password_max = 12
    all_chars = string.ascii_letters+string.punctuation+string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max))) # on choisi x des caractères
    password_entry.delete(0, END) # nettoyer le champs d'entrée
    password_entry.insert(0, password)

# creer la fenetre
window = Tk()
window.title("Generateur de mot de passe")
window.geometry('720x480')
window.iconbitmap("Half-Life_PNG76.ico")
window.config(background='#AFEEEE')

# creer la frame principale
frame = Frame(window, bg= '#AFEEEE')

# creation d'image
width = 300
height = 300
image = PhotoImage(file="cake.png").zoom(22).subsample(50)
canvas = Canvas(frame, width=width, height=height, bg = '#AFEEEE', bd = 0, highlightthickness = 0) # espace où l'on peu mettre des formes, des images...
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous boite
right_frame = Frame(frame, bg = '#AFEEEE')

# creer un titre
label_title = Label(right_frame, text = "Mot de passe", font=('Helvetica', 20), bg ='#AFEEEE', fg='white')
label_title.pack()

# creer un champs d'entrée
password_entry = Entry(right_frame, font=('Helvetica', 20), bg ='#AFEEEE', fg='white')
password_entry.pack()

# creer un bouton
password_generator_button = Button(right_frame, text='Générer', font=('Helvetica', 20), bg ='#b12e50', fg='white', command=generate_password)
password_generator_button.pack(pady=25, fill=X)

# on place la sous boite à droite de la boite principale
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# creation de la barre de menu
menu_bar = Menu(window)
# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password())
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer notre fenetre pour ajouter cette menu barre
window.config(menu=menu_bar)

# afficher la fenetre
window.mainloop()
