# Getting input from the user
wieght = float(input("Please inter your wieght in kg: "))
height = float(input("Please inter you height in cm: "))

'''
The BMI Formula is BMI = kg/m^2
'''

# Converting height from cm to m
height_in_meter = height / 100

# Calculating the BMI
BMI = wieght / (height_in_meter**2)
print(f"your BMI is: {round(BMI, 2)}")

# printing health advice to the user
if BMI >= 25:
  print("You are overwieght you need to work out more and watch your diet.")
elif BMI >= 18.5:
  print("You are fit & healthy.")
else:
  print("You are underweight. Watch your health.")
