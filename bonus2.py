
username = input("Enter username : ") 

user_email = input("Enter your Email :")

at_index = user_email.find("@")

valid_email = "@gmail.com"
if len(username) < 3 : # first check if the username is more than 2 characters.
    print("the name length must be more than 2 characters, please provide a valid name.")
elif user_email.count("@") == 1 and user_email[at_index:] == valid_email :

    print(f"welcome {username}, you registered with the email {user_email} !")

else:
    
    print("the email is not valid , please provide a valid email .")
