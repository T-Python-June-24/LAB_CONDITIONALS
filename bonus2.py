# Ask the user to provide his name
name = input("Please enter your name: ")

#! Check that the name length is more than 2 characters by using the len build in function

if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
else:
    print("The name is unvalid.")
    
    #! Ask the user to provide his email
    
email = input("Please enter your email: ")

#! Split the email at "@" and ".com" and check if there are exactly two parts for each

at_parts = email.split("@")
dotcom_parts = email.split(".com")



'''
#!  the first condition is to check if the email has two @ signs if has two @ signs then the email is invalid 
#?  the same thing gose for the .com part
#*  startswitch is to check if the first word after the @ sign is gmail 
'''


if len(at_parts) == 2 and len(dotcom_parts) == 2 and at_parts[1].startswith("gmail"):
        print(f"Welcome {name}, you registered with the email {email} !")    
#! if the condition is true print the welcome message that contains the user name (var name) and the email (var email)

else:
    print("The email is not valid, please provide a valid email.")
        
