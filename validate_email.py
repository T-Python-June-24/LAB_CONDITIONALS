# Taking input from the user
name = input("Enter your name: ")
email = input("enter your email: ")

# Checking the user input 
# Validating the name
if len(name) <= 2:
  print("the name length must be more than 2 characters, please provide a valid name.")
elif '@' not in email or not email.endswith('@gmail.com'):
  # Validating the email
  print("the email is not valid , please provide a valid email .")
else: 
  # both name and email are valid, print welcome message
  print("welcome Ahmed, you registered with the email ahmed@gmail.com !")