userName = input("please insert your name: ")
eMail = input("please insert your Gmail account:")

while len(userName) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
    userName = input("please insert your name again: ")
else:
    print("Welcome on board, ", userName)

while eMail.endswith("@gmail.com") is False:
    print("the email is not valid , please provide a valid email")
    eMail = input("please insert your Gmail account again:")
else:
    print("Welcome", userName , "you registered with the email" , eMail)

