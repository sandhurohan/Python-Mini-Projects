# ---------------------------- Email Validation Using Regex -------------------

import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

email=input("Enter Email Address     :   ")

if (re.search(regex, email)):
    print("Valid Email")
else:
    print("Invalid Email")
