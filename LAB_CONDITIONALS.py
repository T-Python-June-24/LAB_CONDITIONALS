movie = "Monk"
rate = 3 
popularity_score = 72.65

if rate >= 4 and popularity_score > 80:
    print( "Highly recommended")
elif rate >= 3 and popularity_score > 70:
    print( "I Recommended")
elif rate <= 2 and popularity_score > 60:
    print( "You should check it out!")
else:
    print( "Don't watch it. It is a waste of time")
    
    
#! user provide his weight by using the input function
weight = float(input("Please enter your weight in kilograms: "))

#  user to provide his height
height = float(input("Please enter your height in meters: "))

# Calculate the BMI
bmi = weight / (height ** 2)

print("Your BMI is: ", bmi)

if bmi > 25:
    print("You are overweight. You need to work out more and watch your diet.")
elif bmi >= 18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")

    
    #!################################
#! Ask the user to provide his name

name = input("Please enter your name: ")

#! Check that the name length is more than 2 characters
if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
else:
    #! Ask the user to provide his email
    email = input("Please enter your email: ")


    if  email.endswith("@gmail.com"):
        print(f"Welcome {name}, you registered with the email {email}!")
    else:
        print("The email is not valid, please provide a valid email!")
        
