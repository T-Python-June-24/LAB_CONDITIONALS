name:str=input("Enter your name : ")
email:str=input("Enter your email  : ")
if len(name)<2 :
    print("the name length must be more than 2 characters, please provide a valid name.")
if email.count("@gmail")>1 or email.count("@gmail")==0 or not email.endswith("@gmail.com") or email.count(" ")!=0 :
   print("the email is not valid , please provide a valid email")
else :
    print(f"welcome {name}  , you registered with the email{email} !")