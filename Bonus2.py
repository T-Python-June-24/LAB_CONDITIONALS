name = input("Enter your name: ")
email = input("Enter your email: ")

if len(name) > 2:
    N=True
else:
    N=False

if email.__contains__("@gmail"):
    E=True
else:
    E=False


if N== True and E==True:
    print("welcome "+name+", you registered with the email "+email+" !")
elif N== False and E==True:
    print("the name length must be more than 2 characters, please provide a valid name")
elif E==False and N==True:
    print("the email is not valid , please provide a valid email")
else:
    print("the email and name are not valid, please try again!")