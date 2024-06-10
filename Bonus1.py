
wieght=float(input("Enter your wieght in kilograms "))
height=float(input("Enter your height In metres"))
BMI: float
BMI= wieght/height**2                             # kilograms /metres^2

if   BMI< 18.5 :
   print("You are underweight. Watch your health")
elif BMI >= 18.5 and BMI<= 24.9 :
   print("You are fit & healthy") 
elif BMI >= 25.0:
   print("You are overwieght you need to work out more and watch your diet")
