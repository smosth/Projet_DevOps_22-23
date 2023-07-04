from pyzbar.pyzbar import decode
from PIL  import Image
from tkinter import filedialog
import tkinter as tk

print('Veuillez choisir le code qr que vous voulez decoder...')
root = tk.Tk()
root.withdraw()  
selected_path = filedialog.askopenfilename()  
root.destroy()

img = Image.open(selected_path)
result = decode(img)
print(result)
