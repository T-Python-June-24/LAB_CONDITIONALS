wieght=float(input("Please Enter you wieght in Kg: "))
height=float(input("Please Enter you height in m: "))
BMI=float(wieght/height**2)
print(BMI)
if BMI <18.5:
    print("You are underweight. Watch your health.")
elif BMI>=18.5 and BMI<=24.99:
    print("You are fit & healthy.")
else:
    print("You are overwieght you need to work out more and watch your diet.")

