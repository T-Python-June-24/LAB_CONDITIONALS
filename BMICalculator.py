# Bonus 1
userWeight= float(input("Enter your weight: "))
userHeight= float(input("Enter your height: "))

convertTo_meter= (userHeight / 100) ** 2
bmiFormula = userWeight / convertTo_meter

if bmiFormula < 18.5:
    print("You are underweight. Watch your health.")
elif 18.5 <= bmiFormula < 24.9:
    print( "You are fit & healthy.")
elif 25 <= bmiFormula < 29.9:
    print( "You are overweight you need to work out more and watch your diet.")
else:
    print ("Obesity")

print("="*20)

# Bonus 2

userName:str=input("Enter your name :")
userEmail:str=input("Enter your email: ")

Length:int= len(userName)

if userEmail.endswith("@gmail.com") and Length >2:
    print(f"welcome {userName}, you registered with the email {userEmail} !")
else:
    print ("The email is not valid , please provide a valid email .")
