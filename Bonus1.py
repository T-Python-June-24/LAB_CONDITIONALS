Weight = eval(input("Enter Your Weight: "))

Height = eval(input("Enter Your Height: "))

Height_m= Height / 100

BMI = Weight / (Height_m**2)

if BMI <= 18.5:
    print("You are underweight. Watch your health")
elif BMI >= 25:
    print("You are overwieght you need to work out more and watch your diet")
else:
    print("You are fit & healthy")

