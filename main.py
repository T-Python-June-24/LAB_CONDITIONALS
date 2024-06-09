# create a variable for the movie
movie: str = "Interstellar"

# rating of a movie
rating: int = 5

# popularity score of a movie
popularity: float = 90.0

# Evaluate and print recommendations based on rating and popularity
if rating >= 4 and popularity > 80:
    print("Highly Recommended")
elif rating >= 3 and popularity > 70:
    print("I recommend it. It is good.")
elif rating <= 2 and popularity > 60:
    print("You should check it out!")
elif rating <= 2 and popularity < 50:
    print("Don't watch it. It is a waste of time")
