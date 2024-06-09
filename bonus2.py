# Ask the user to provide his name
name = input("Please enter your name: ")

# Check that the name length is more than 2 characters
if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
else:
    # Ask the user to provide his email
    email = input("Please enter your email: ")

    # Split the email at "@" and ".com" and check if there are exactly two parts for each
    at_parts = email.split("@")
    part = email.split(".com")
    part2 = email.split("@")
    dotcom_parts = email.split(".com")

    if len(at_parts) == 2 and len(dotcom_parts) == 2 and at_parts[1].startswith("gmail"):
        print(f"Welcome {name}, you registered with the email {email}!")
    else:
        print("The email is not valid, please provide a valid email.")