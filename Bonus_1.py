weight:float = float(input("Please enter your weight in kilograms: "))
height:float = float(input("Please enter your height in meters: "))
bmi:float = weight / (height ** 2)
if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi >= 25:
    print("You are overwieght you need to work out more and watch your diet.")
else:
    print("You are fit & healthy.")