# write a program that Calculates the BMI (body mass index) of the user:

# Ask the user to provide his wieght.
# Ask the user to provide hi height.
# print the BMI for the user.
# using conditionals tell the user that either :
# You are overwieght you need to work out more and watch your diet.
# You are fit & healthy.
# You are underweight. Watch your health.
# Note
# for formula , search the web.


weight = float(input("Enter your weight (kg): "))

height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)


if bmi >= 25:
    print("You are overwieght you need to work out more and watch your diet")
elif bmi >= 18.5 or bmi <= 24.9:
    print("You are fit & healthy")
elif bmi < 18.5:
    print("You are underweight. Watch your health")
else:
    print("Something went wrong!")