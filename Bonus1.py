weight = float(input("Insert you weight in KG: "))
height = float(input("Insert Your Height in m: "))

BMI = weight/(height**2)

print("your body mass is: ", BMI)

if BMI >= 30:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI >=25:
    print("You are fit & healthy.")
elif BMI >= 18:
    print("You are underweight. Watch your health")
else:
    print("You're probably so thin")