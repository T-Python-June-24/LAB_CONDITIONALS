name, email = input("enter your name :") , input("enter your email : ")
if len(name)<=2:
     print("chek your name")
elif not email.endswith("@gmail.com"):
    print("email is not valid")
else:
     print(f"welcome{name} , your register with email{email }")