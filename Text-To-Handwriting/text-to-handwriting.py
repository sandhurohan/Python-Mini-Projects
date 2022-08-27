#------------------------------ TEXT TO HANDWRITTEN -----------------------------------------

import pywhatkit as pw

text=input("Enter text To Covert to Handwritten     :   ")
print()
name=input("Enter Name of File  :   ")
name=name+'.png'

pw.text_to_handwriting(text,name,[0,0,138])
print()
print("File Made successfully, Please Check The Directory")
