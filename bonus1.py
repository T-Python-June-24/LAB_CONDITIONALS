
#! user provide his weight by using the input function
weight = float(input("Please enter your weight in kilograms: "))

# ! user to provide his height
height = float(input("Please enter your height in meters: "))

# ! Calculate the BMI 
bmi = weight / (height ** 2)#!Weight in kilograms/height in square metres thx google

print("Your BMI is: ", bmi)

if bmi > 25:#! if the BMI is greater than 25, the user is overweight
    print("You are overweight. You need to work out more and watch your diet.")
elif bmi >= 18.5:#! if the BMI is greater than 18.5, the user is fit and healthy
    print("You are fit & healthy.")
else:#! if the BMI is less than 18.5, the user is underweight 
    print("You are underweight. Watch your health.")

    