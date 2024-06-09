movie = "Moana"

#rating out of 5
rating:int = 3

#popularity score
popularity:float = 72.65

if rating >= 4 and popularity > 80:
    print("Highly recomended")
elif rating >= 3 and popularity > 70:
    print("I recommend it, it is good.")
elif rating <= 2 and popularity > 60:
    print("You should check it out!")
else:
    print("Don't watch it, it is a waste of time.")