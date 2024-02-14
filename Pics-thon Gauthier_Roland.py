# Créé par Elèves, le 23/11/2023 en Python 3.7
from PIL import Image, ImageTk
from pathlib import Path
import tkinter as tk

chemin = Path(__file__).parent.absolute()
chemin = str(chemin)

def Niv_gris():
    global image_a_modifier_pil
    longueur,largeur=image_a_modifier_pil.size
    for y in range(largeur):
        for x in range(longueur):
            p=image_a_modifier_pil.getpixel((x,y))
            rouge=p[0]
            vert=p[1]
            bleu=p[2]
            moyenne=0.2126*rouge+0.7152*vert+0.0722*bleu
            nbm = int(moyenne)
            image_a_modifier_pil.putpixel((x,y),(nbm,nbm,nbm))
    image_a_modifier_pil.save(f"{chemin}/image_gris.png")
    img = ImageTk.PhotoImage(Image.open(f"{chemin}/image_gris.png"))
    panel.configure(image=img)
    panel.image = img


def Inverser():
    global image_a_modifier_pil
    longueur, largeur=image_a_modifier_pil.size
    image_a_modifier_pil_inverse = Image.new('RGB', (512, 512))
    for x in range(longueur):
        for y in range(largeur):
            r,g,b=image_a_modifier_pil.getpixel((x,y))
            image_a_modifier_pil_inverse.putpixel((-x, y), (r, g, b))
    image_a_modifier_pil_inverse.save(f"{chemin}/image_inverse.png")
    img = ImageTk.PhotoImage(Image.open(f"{chemin}/image_inverse.png"))
    image_a_modifier_pil = image_a_modifier_pil_inverse
    panel.configure(image=img)
    panel.image = img

fenetre = tk.Tk()
global image_a_modifier

fenetre.title("Pics-thon Gauthier_Roland")
fenetre.geometry("1080x700")
fenetre.minsize(1000, 800)
fenetre.config(background='#FF6133')
icone = ImageTk.PhotoImage( Image.open(f"{chemin}/Pics-thon_logo.ico"))
fenetre.wm_iconphoto(True, icone)
boite = tk.Frame(fenetre, bg='#000000', bd=1, relief= tk.SUNKEN)
label_title = tk.Label(boite, text=" Outils d'édition", bg='#000000', fg='white', font=("Courier, 25"))
image_a_modifier_pil = Image.open(f'{chemin}/bebe-yoda.jpg')
image_a_modifier = ImageTk.PhotoImage(image_a_modifier_pil)

b = tk.Button(boite , text= "Tourner l'image", bg='#FF6133', fg='white', font=("Courier, 20"))
b1 = tk.Button(boite , text= "Niveaux de gris", bg='#FF6133', fg='white', font=("Courier, 20"), command=Niv_gris)
b2 = tk.Button(boite , text= "Eclaircir", bg='#FF6133', fg='white', font=("Courier, 20"))
b3 = tk.Button(boite , text= "Inverser l'image", bg='#FF6133', fg='white', font=("Courier, 20"), command=Inverser)

boite.pack(anchor='ne')

label_title.pack()
b.pack()
b1.pack()
b2.pack()
b3.pack()

panel = tk.Label(fenetre, image = image_a_modifier)
panel.pack()
fenetre.mainloop()