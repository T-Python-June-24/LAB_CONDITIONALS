weight:float = float(input("weight: "))
height:float = float(input("height: "))
height = height/100

bmi:float = weight/(height ** 2)
print(bmi)


if bmi >= 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi >= 18.5 and bmi < 25:
    print("You are fit & healthy.")
else: #below 18.5
    print("You are underweight. Watch your health.")

