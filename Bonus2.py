userName=input("Please Enter Your name: ")
ueserEmail=input("Please Enter Your Email: ")
stackMessages=[]
flage=True
if len(ueserEmail)<=2:
    message="you need to provide a name more than 2 charcters . Please provide real name"
    stackMessages.append(message)
    flage=False
print(ueserEmail.find("gmail.com"))
if  not ueserEmail.find("@gmail.com"):
    message="we only accept gmail emails. please try again"
    stackMessages.append(message)
    flage=False


if flage==True:
    print("Welcom to our website :)")
else:
    for i in stackMessages:
        print(i+"\n")
