from pyzbar.pyzbar import decode

from PIL  import Image

img = Image.open('c:/Users/lenovo/Music/qr_code.png')
result = decode(img)
print(result)