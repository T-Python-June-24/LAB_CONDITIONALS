
    #!################################
#! Asks the user to provide his name

name = input("Please enter your name: ")

#! Check that the name length is more than 2 characters
if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
else:
    #! Asks the user to provide his email
    email = input("Please enter your email: ")


    if  email.endswith("@gmail.com"):
        print(f"Welcome {name}, you registered with the email {email}!")
    else:
        print("The email is not valid, please provide a valid email!")
        


# Ask the user to provide his name
name = input("Please enter your name: ")

# Check that the name length is more than 2 characters
if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
else:
    # Ask the user to provide his email
    email = input("Please enter your email: ")

    # Check that the email is valid (using string operations and conditionals)
    if "@" in email and ".com" in email and email.index("@") < email.index(".com") and email.endswith("@gmail.com"):
        print(f"Welcome {name}, you registered with the email {email}!")
    else:
        print("The email is not valid, please provide a valid email.")