wieght:float = float(input("enter your wieght in kg:"))

height:int = float(input("enter your height in cm :"))

height_in_meter:float = height/100 # for calculate bmi height should be in meter  

bmi:float = wieght/ (height_in_meter ** 2) # formula for calculating BMI (Body Mass Index) 

if bmi < 18.5 :
    
    print("You are underweight. Watch your health.")

elif bmi >= 18.5 and bmi < 25 :
    
    print("You are fit & healthy.")

elif bmi >= 25 and bmi < 30:
    
    print("You are overwieght you need to work out more and watch your diet.")

else :
    
    print("You are obese. You should lose weight safely")