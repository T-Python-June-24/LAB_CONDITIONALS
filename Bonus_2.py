name:str = input("Please enter your name: ")
email:str = input("Please enter your email address: ")
name_valid:bool = False
email_valid:bool = False
at_index = name.find("@")  # index of @ if found, -1 if not

# Check if the name has more than 2 characters
if len(name) > 2:
    # Name is valid
    name_valid = True

# Check if @ is present and preceeded by at least 1 character
if at_index >= 1:
    # Check if mail provider is gmail
    if email.count("@gmail") == 1:
        # Check if at least 1 . is present
        if email.find("."):
            # Email is valid
            email_valid = True

# When both are valid
if name_valid and email_valid:
    print(f"Welcome {name}, you registered with the email {email}!")
# When name is valid but not the email
elif name_valid:
    print("The email is not valid, please provide a valid email.")
# When the name is not valid
else:
    print("The name length must be more than 2 characters, please provide a valid name")