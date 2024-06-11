'''
# loops 
phrase:str= " i like you"
for char in phrase:
    print(char.upper()) # يحسب حتى المسافات يكتب كل حرف لحال 
print("----")

# using range to generate a sequence of number
some_numbers=range(1,10 , 2)
for number in some_numbers:
    print(number)
    print(f"{number} sequard is {number**2}")

# while loop 
# الفرق بين ال for و while   استخدم فور لو كنت عارفه  البدايه والنهايه تكون محدده 
# استخدم while لو ماكنت عارف كم عملية دوران احتاج انفذها 
i=5
while i>0:
    print(i)
    i=i-1 # increamnt(+) decremnt (_)
else:
    print("loop ended")

# while loop and for whth else
# break لانهاء عملية الدوران continue يتخطى عمليات معينه ويروح للي بعده
i=5
while i>0:
    print(i)
    i=i-1 # increamnt(+) decremnt (_)
    if i ==2:
        break # لما طلعنا مانفذنا ما بداخل else 
else:
    print("loop ended")

print("---")
phrase:str= " i like you"
for char in phrase:
    if char =="k" or char ==" ":
        continue # بعدها يتخطى اي اوامر 
    print(char.upper()) # يحسب حتى المسافات يكتب كل حرف لحال 
print("----")
some_numbers=range(1,10)
for number in some_numbers:
    print(number)

'''

print("welcome to our puzzles programm")
print("-"*20)

puzzle = "the more it gets bigger"

while input(puzzle) != "fog":
    print("your number is wrong.")
else:
    print("your answer is correct")
