name:str = input("name: ")
email:str = input("email: ")

if len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif not email.endswith("@gmail.com"):
    print("the email is not valid, please provide a valid email .")
else:
    print(f"Welcome {name}, you registered with the email {email}")



