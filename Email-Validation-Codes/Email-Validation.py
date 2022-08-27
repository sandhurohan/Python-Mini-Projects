#------------------ Validating An Email Address ---------------------------

email=input("Please Enter an Email  :   ")
email=email.lower()
k,d=0,0
if(len(email)>=6):
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-4]=='.') ^ (email[-3] =='.'):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isdigit():
                        continue
                    elif i.isalpha():
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    else:
                        d=1
                if k==0 or d==0:
                    print("Valid Email")
                else:
                    print("Invalid Email, Error Code : 01 ")
            else:
                print("Invalid Email, Error Code : 04 ")
        else:
            print("Invalid Email, Error Code : 03 ")
    else:
        print("Invalid Email, Error Code : 02 ")
else:
    print("Invalid Email, Error Code : 01 ")