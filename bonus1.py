weight: int = int(input("Enter your weight in kg: "))
height: int = int(input("Enter your height in cm: "))

bmi:float = weight / ((height/100) ** 2)

print(f"Your BMI is {bmi}")
if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi > 25:
    print("You are overwieght you need to work out more and watch your diet.")
else:
    print("You are fit & healthy.")



