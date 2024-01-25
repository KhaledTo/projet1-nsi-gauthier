# Créé par Elèves, le 23/11/2023 en Python 3.7
from PIL import Image, ImageTk
import tkinter as po

def Niv_gris():
    global image_a_modifier
    longueur,largeur=image_a_modifier.size
    image2=Image.new('RGB',(longueur,largeur))
    for y in range(largeur):
        for x in range(longueur):
            p=image_a_modifier.getpixel((x,y))
            rouge=p[0]
            vert=p[1]
            bleu=p[2]
            moyenne=0.2126*rouge+0.7152*vert+0.0722*bleu
            nbm = int(moyenne)
            image2.putpixel((x,y),(nbm,nbm,nbm))
    image2.save("image2.png")
    image_a_modifier=Image.open("image2.png")
    img = ImageTk.PhotoImage(Image.open("image2.png"))
    mon_label_noir = po.Label(fenetre, image=image_a_modifier)
    mon_label_noir.pack()
    mon_label_depart.destroy()
    fenetre.mainloop()


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
    mon_label_inver = po.Label(fenetre, image=image_a_modifier)
    mon_label_inver.pack()
    mon_label_depart.destroy()
    fenetre.mainloop()

fenetre = po.Tk()
global image_a_modifier
#image_a_modifier =Image.open('bebe-yoda.jpg')
fenetre.title("Pics-thon Gauthier_Roland")
fenetre.geometry("1080x700")
fenetre.minsize(1000, 800)
fenetre.config(background='#FF6133')
fenetre.iconbitmap("Pics-thon_logo.ico")
boite = po.Frame(fenetre, bg='#000000', bd=1, relief= po.SUNKEN)
label_title = po.Label(boite, text=" Outils d'édition", bg='#000000', fg='white', font=("Courier, 25"))
image_a_modifier = Image.open('bebe-yoda.jpg')


#image_a_modifier = po.Label(fenetre, image=image_a_modifier)
#image_a_modifier.pack()
b = po.Button(boite , text= "Tourner l'image", bg='#FF6133', fg='white', font=("Courier, 20"))
b1 = po.Button(boite , text= "Niveaux de gris", bg='#FF6133', fg='white', font=("Courier, 20"), command=Niv_gris)
b2 = po.Button(boite , text= "Eclaircir", bg='#FF6133', fg='white', font=("Courier, 20"))
b3 = po.Button(boite , text= "Inverser l'image", bg='#FF6133', fg='white', font=("Courier, 20"), command=Inverser)

boite.pack(anchor='ne')


label_title.pack()
b.pack()
b1.pack()
b2.pack()
b3.pack()
panel = po.Label(fenetre, image = image_a_modifier)
panel.pack()

fenetre.mainloop()


