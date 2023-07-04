import qrcode

from tkinter import filedialog
import tkinter as tk

data = str(input('Veuillez saisir les informations à encoder dans le QR code: '))
name = str(input('Veuillez saisir le nom sous lequel vous voulez enregistrer  votre QR code(sans les côtes): '))
size = int(input('Veuillez saisir la taille de votre QR code: '))
color = str(input('Veuillez saisir la couleur de votre QR code(sans les côtes): '))
fcolor = str(input('Veuillez saisir la couleur de fond de votre QR code(sans les côtes): '))
print('Veuillez choisir le chemin du dossier où vous voulez enregistrer le qrcode...')


root = tk.Tk()
root.withdraw()  
selected_path = filedialog.askdirectory()  
root.destroy()


qr = qrcode.QRCode(version=1, box_size= size, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = color, back_color = fcolor)
img.save(selected_path + '/' + name + '.png')
