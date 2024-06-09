special_chars = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|',
    '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c'
]
check1 = check2 = check3 = check4 = False

#Getting the user name and email.
name = input("Please enter your name:")
email = input("Please enter your email:")

#Getting email ID (i.e. the string before "@")
if "@" in email:
     emailID = email[:email.index("@")]
     #Firstly, check if emailID contains any special charachters
     for char in emailID:
      if char not in special_chars:
           check1 = True
     #Secondly, Check if first character of email ID is not "." or "_"
     if emailID[0] != "." and emailID[0] != "_":
        check2 = True

#Thirdly, Check if email ends with "@gmail.com"
if email[-10:] == "@gmail.com":
    check3= True

#Forthly, check if email has ONLY one "@"
if email.count("@") == 1:
      check4 = True

#Ckeck if name is more than 2 characters
if len(name) > 2:
        #check if email is valid
        if check1 and check2 and check3 and check4:
             print(f"welcome {name}, you registered with the email {email}")
        else:
             print("The email is not valid, please provide a valid email!")
else:
    print("The name length must be more than 2 characters, please provide a valid name!")