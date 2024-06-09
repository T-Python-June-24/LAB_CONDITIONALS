
move:str = "Prison Break"
rating:int = 3
score:float= 72.65

if rating >= 4 and score > 80 :
    print("Highly recommended")
elif rating >= 3 and score > 70:
    print ("I recommended it . It is good")
elif rating <= 2 and score >60:
    print("You should check it out!")
    
elif rating <=2 and score <50:
    print("Don't watch it. It is a waste of time")
######################################################



print("-"*15)

wieght=int(input("wieght: "))
height= int(input("height :"))
meter:float= (height /100) **2
BMI:float= wieght / meter
if BMI >=30:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI >=15.5 and BMI <= 24.9:
    print("You are fit & healthy")
else:
    print("You are underweight. Watch your health.")
##############################################################


print("-"*15)
name:str=input("name :")
email:str=input("email: ")
verification=email[-10:]

Length:int= len(name)
verif:int=verification.count("@gmail.com")


if verif == 1 and Length >2:
    print("welcome "+name+", you registered with the email "+ email)
else:
    print ("Please check your email and name")
