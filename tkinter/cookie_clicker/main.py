# TP : cookie clicker
# Creer une fenetre avec un cookie au centre de l'ecran
# Creer un compteur
# Une boutique ( changer l'image )
# /!\ Regarder code video car Tkinter + Objet

from tkinter import *

cookie_count = 0

def add_cookie():
    global cookie_count # variable dans code globale pour eviter le rénitialisation
    cookie_count += 1
    label_counter.config(text=cookie_count)


# creer la fenetre
window = Tk()
window.title("Cookie Clicker")
window.geometry("720x480")
window.iconbitmap("Half-Life_PNG76.ico")
window.config(background='#dee5dc')

# ajout du compteur
label_counter = Label(window, text="0", font=("Courrier", 30), bg="#dee5dc")
label_counter.pack()

# creer la frame principale
frame = Frame(window, bg='#dee5dc')

# creation d'image
width = 300
height = 300
image = PhotoImage(file="cookie.png").zoom(32).subsample(64)

# ajout du bouton/image
button = Button(frame, image=image, bg='#dee5dc', bd=0, relief=SUNKEN, command=add_cookie) # les boutons peuvent devenir des images grâce à image=...
button.pack()

# ajout de la frame au centre
frame.pack(expand=YES)

# affichage
window.mainloop()