userWeight = float(input("Please enter your weight in kg:"))
userHeight = float(input("Please enter your height in cm:"))

#Calculaying the user BMI using this formula BMI = kg/m2
bmi = userWeight/((userHeight/100) ** 2)
print (f"Your BMI is: {round(bmi,2)} kg/m2")


if bmi >= 25:
    print("You are overwieght. You need to work out more and watch your diet!")
elif 25 > bmi >= 18.5:
    print("You are fit & healthy")
else:
    print("You are underweight. Watch your health.")
