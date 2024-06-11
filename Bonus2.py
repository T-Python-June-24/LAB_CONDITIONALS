userName=input("Please Enter Your name: ")
userEmail=input("Please Enter Your Email: ")
stackMessages=[]
flage=True
if len(userName)<=2:
    message="you need to provide a name more than 2 charcters ."
    print(message)
    
if not userEmail.endswith("@gmail.com"):
    print("incorrect email strcure")

if not len(userName)<=2 and  userEmail.endswith("@gmail.com"):
    print("welcom to our website")

