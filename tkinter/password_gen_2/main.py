#Depuis le generateur, creer un systeme de stockage des derniers mot de passe

from tkinter import *
from random import choice, randint
import string

def generate_password():
    password_min  = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    with open("history.txt", "a+") as file:
        password = "".join(choice(all_chars)   for x in range(randint(password_min, password_max))) # on choisi x des caractères
        file.write(password + '\n')
        password_entry.delete(0, END) # nettoyer le champs d'entrée
        password_entry.insert(0, password)

window = Tk()
window.title("Generateur de mot de passe")
window.geometry('720x480')
window.iconbitmap("logo.ico")
window.config(background='#000000')

frame = Frame(window, bg= '#000000')

width = 300
height = 300
image = PhotoImage(file="password.png").zoom(22).subsample(50)
canvas = Canvas(frame, width=width, height=height, bg = '#000000', bd = 0, highlightthickness = 0) # espace où l'on peu mettre des formes, des images...
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg = '#000000')

label_title = Label(right_frame, text = "Mot de passe", font=('Helvetica', 20), bg ='#000000', fg='#ff8100')
label_title.pack()

password_entry = Entry(right_frame, font=('Helvetica', 20), bg ='#ff8100', fg='#000000')
password_entry.pack()

password_generator_button = Button(right_frame, text='Générer', font=('Helvetica', 20), bg ='#ff8100', fg='white', command=generate_password)
password_generator_button.pack(pady=25, fill=X)

right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

window.mainloop()