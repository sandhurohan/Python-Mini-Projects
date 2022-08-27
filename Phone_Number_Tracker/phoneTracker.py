#------------------------------ PHONE NUMBER TRACKER --------------------------------

import phonenumbers
from phonenumbers import timezone,geocoder,carrier

#-------------------------------- Getting Detaols ----------------------------------------

number=input("Please Enter Number to Be Traced with Country Code    :   ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
reg=geocoder.description_for_number(phone,'en')
car=carrier.name_for_number(phone,'en')

#-------------------------------- Printing Details ----------------------------------------

print("Details of Given Number Are  :")
print(phone)
print(time)
print(reg)
print(car)
