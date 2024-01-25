# Créé par Elèves, le 23/11/2023 en Python 3.7
from PIL import Image, ImageTk
import tkinter as tk

def Niv_gris():
    longueur,largeur=image_a_modifier_pil.size
    image_gris=Image.new('RGB',(longueur,largeur))
    for y in range(largeur):
        for x in range(longueur):
            p=image_a_modifier_pil.getpixel((x,y))
            rouge=p[0]
            vert=p[1]
            bleu=p[2]
            moyenne=0.2126*rouge+0.7152*vert+0.0722*bleu
            nbm = int(moyenne)
            image_gris.putpixel((x,y),(nbm,nbm,nbm))
    image_gris.save("image_gris.png")
    img = ImageTk.PhotoImage(Image.open("image_gris.png"))
    panel.configure(image=img)



def Inverser():
    global image_a_modifier
    L,H = image_a_modifier.size
    image2 = Image.new('RGB', (512, 512))
    for x in range(L):
        for y in range(H):
            r,g,b=image_a_modifier.getpixel((x,y))
            image2.putpixel((-x, y), (r, g, b))
    image2.save("image2.png")
    image_a_modifier=Image.open("image2.png")
    img = ImageTk.PhotoImage(Image.open("image2.png"))
    mon_label_inver = tk.Label(fenetre, image=image_a_modifier)
    mon_label_inver.pack()
    image_a_modifier.destroy()
    fenetre.mainloop()

fenetre = tk.Tk()
global image_a_modifier

fenetre.title("Pics-thon Gauthier_Roland")
fenetre.geometry("1080x700")
fenetre.minsize(1000, 800)
fenetre.config(background='#FF6133')
icone = ImageTk.PhotoImage( Image.open("Pics-thon_logo.ico"))
fenetre.wm_iconphoto(True, icone)
boite = tk.Frame(fenetre, bg='#000000', bd=1, relief= tk.SUNKEN)
label_title = tk.Label(boite, text=" Outils d'édition", bg='#000000', fg='white', font=("Courier, 25"))
image_a_modifier_pil = Image.open('bebe-yoda.jpg')
image_a_modifier = ImageTk.PhotoImage(image_a_modifier_pil)

#image_a_modifier = tk.Label(fenetre, image=image_a_modifier)
#image_a_modifier.pack()
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