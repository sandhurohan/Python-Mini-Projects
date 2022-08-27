#------------------ Code To Genereate QR for Anything --------------------------------------

from PIL import Image
import qrcode

link=input("Enter URL/Text to Generate QR-Code of Same :    ")
name=input("Enter Name For QR-Code :    ")
name=name+".png"
ver=int(input("Enter Version of QR-Code :   "))
boxsize=int(input("Enter Box Size of QR-Code :  "))
border_size=int(input("Enter Border Size For QR-Code :  "))
color=input("Enter Color for QR-Code :  ")
bgcolor=input("Enter Background Color for QR-Code : ")

qr=qrcode.QRCode(version=ver,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=boxsize,border=border_size)
qr.add_data(link)
qr.make(fit=True)
qr_img=qr.make_image(fill_color=color,back_color=bgcolor)
qr_img.save(name)

#------------------- Showing Generated Image in Editor ------------------------------------

image=Image.open(name)
image.show(title=None)