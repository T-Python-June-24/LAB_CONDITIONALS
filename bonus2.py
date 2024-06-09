user_name: str = input("Enter your name: ")
user_email: str = input("Enter your email: ")

is_name_more_than_2_char: bool = len(user_name) > 2

is_email_formula_valid: bool = user_email.endswith("@gmail.com")

# extra validation for the email
is_full_email_valid: bool = user_email.count("@") == 1 and user_email.count(".com") == 1 and user_email.count("-") == 0

if is_name_more_than_2_char and is_email_formula_valid and is_full_email_valid:
    print(f"Welcome {user_name}, you are registered with the email {user_email}")
else:
    if not is_name_more_than_2_char:
        print("the name length must be more than 2 characters, please provide a valid name.")
    if not is_full_email_valid or not is_email_formula_valid:
        print("the email is not valid , please provide a valid email .")
    