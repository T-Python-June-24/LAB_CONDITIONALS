name:str= str(input("what your name"))
email:str= str(input("what your email"))

if len(name)<=2:
      print("the name length must be more than 2 characters, please provide a valid name."
)
elif not email.endswith("@gmail emails"):
      print( "the email is not valid , please provide a valid email ."
) 
else: 
     print(f" welcome {name}, you registered with the email{email}")













'''
Check that the name length is more than 2 characters.
- Check that the email is valid (using string operations and coditionals)
- You only accept @gmail emails . 
- if the email is valid, display a welcome message to the user . for example :
welcome Ahmed, you registered with the email ahmed@gmail.com !
- if the email or name is not valid, display the message : 
 the email is not valid , please provide a valid email .
or 
the name length must be more than 2 characters, please provide a valid name.
'''