movie = "Monk"
rate = 3 
popularity_score = 72.65

if rate >= 4 and popularity_score > 80:
    print( "Highly recommended")
elif rate >= 3 and popularity_score > 70:
    print( "I Recommended it")
elif rate <= 2 and popularity_score > 60:
    print( "You should check it out!")
else:
    print( "Don't watch it. It is a waste of time")
    
    