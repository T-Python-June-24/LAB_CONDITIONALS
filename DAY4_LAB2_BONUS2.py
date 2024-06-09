# write a program that asks the user to provide his name and his email using input , then do the following:

# Check that the name length is more than 2 characters.
# Check that the email is valid (using string operations and coditionals)
# You only accept @gmail emails .
# if the email is valid, display a welcome message to the user . for example :
# welcome Ahmed, you registered with the email ahmed@gmail.com !

# if the email or name is not valid, display the message :
#  the email is not valid , please provide a valid email .
# or

# the name length must be more than 2 characters, please provide a valid name.
# Note: don't use regular expressions or a library yet.


name = input("Your name: ")

while True:
    if len(name) > 2:
        email = input("Your email (gmail only): ")
        if email.endswith('@gmail.com'):
            print(f"welcome {name}, you registered with the email ({email})")
            break
        else:
            print("Invalid email! (email must ended with '@gmail.com')")
    else:
        print("name must be longer than 2 characters")
        name = input("Your name: ")
    
